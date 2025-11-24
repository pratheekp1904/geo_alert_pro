import time
import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation
from geopy.geocoders import Nominatim

from components.custom_ui import apply_custom_theme
from components.geofence import haversine_distance, trigger_alert_if_needed

apply_custom_theme()

st.markdown('<div class="main-block">', unsafe_allow_html=True)

# --------- TITLE AREA ----------
st.markdown('<div class="app-title">Geo Alert Pro – Tracking</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Set a destination, choose your alert radius, and track your movement in real time.</div>',
    unsafe_allow_html=True,
)

# --------- SESSION STATE ----------
if "destination" not in st.session_state:
    st.session_state["destination"] = None
if "tracking" not in st.session_state:
    st.session_state["tracking"] = False
if "radius_m" not in st.session_state:
    st.session_state["radius_m"] = 250

geolocator = Nominatim(user_agent="geo_alert_app")

# --------- TOP CONTROLS CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card-header">
        <span>🎛 Live Controls</span>
        <span class="card-header-pill">Realtime</span>
    </div>
    """,
    unsafe_allow_html=True,
)

c_top_left, c_top_right = st.columns([1.3, 1])

with c_top_left:
    st.write("**Alert Radius (meters)**")
    st.session_state["radius_m"] = st.slider(
        "Alert Radius", 50, 2000, st.session_state["radius_m"], step=50, label_visibility="collapsed"
    )
    st.caption(f"Current geofence radius: **{st.session_state['radius_m']} m**")

with c_top_right:
    st.write("**Tracking Controls**")
    cc1, cc2 = st.columns(2)
    with cc1:
        if st.button("▶ Start"):
            st.session_state["tracking"] = True
    with cc2:
        if st.button("⏹ Stop"):
            st.session_state["tracking"] = False
    st.caption("Use on mobile (HTTPS) for accurate GPS.")

st.markdown('</div>', unsafe_allow_html=True)  # close card

# --------- DESTINATION CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card-header">
        <span>📍 Destination</span>
        <span class="card-header-pill">Search & Tap</span>
    </div>
    """,
    unsafe_allow_html=True,
)

c_dest_left, c_dest_right = st.columns([1.1, 1.4])

with c_dest_left:
    place_name = st.text_input("Search by place / address")
    if st.button("🔍 Search Location"):
        if place_name.strip():
            try:
                loc = geolocator.geocode(place_name)
                if loc:
                    st.session_state["destination"] = (loc.latitude, loc.longitude)
                    st.success("Destination updated from search.")
                    st.caption(loc.address)
                else:
                    st.error("Place not found. Try being more specific.")
            except Exception as e:
                st.error(f"Error while searching: {e}")
        else:
            st.warning("Type something before searching.")

    if st.session_state["destination"]:
        dlat, dlon = st.session_state["destination"]
        st.markdown(
            f'<div class="pill-muted">Current dest: <code>{dlat:.5f}, {dlon:.5f}</code></div>',
            unsafe_allow_html=True,
        )
    else:
        st.caption("No destination set yet. Use search or tap on the map.")

with c_dest_right:
    st.write("**Tap on the map to set destination**")
    if st.session_state["destination"]:
        center = st.session_state["destination"]
        zoom = 14
    else:
        center = [20.5937, 78.9629]  # India
        zoom = 5

    dest_map = folium.Map(location=center, zoom_start=zoom)
    if st.session_state["destination"]:
        folium.Marker(
            st.session_state["destination"],
            tooltip="🎯 Destination",
            icon=folium.Icon(color="red"),
        ).add_to(dest_map)

    dest_map_state = st_folium(dest_map, height=320, key="dest_map")
    if dest_map_state and dest_map_state.get("last_clicked"):
        lat = dest_map_state["last_clicked"]["lat"]
        lon = dest_map_state["last_clicked"]["lng"]
        st.session_state["destination"] = (lat, lon)
        st.session_state["alert_triggered"] = False
        st.success(f"Destination set: {lat:.5f}, {lon:.5f}")

st.markdown('</div>', unsafe_allow_html=True)  # close card

# --------- LIVE TRACKING CARD ----------
st.markdown('<div class="card map-wrapper">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card-header">
        <span>🛰 Live Tracking</span>
        <span class="card-header-pill">GPS & Geofence</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if st.session_state["tracking"] and st.session_state["destination"]:

    loc = get_geolocation()
    if not loc or "coords" not in loc:
        st.warning("Waiting for GPS permission... Ensure you're on HTTPS and allow location access.")
        st.markdown('</div></div>', unsafe_allow_html=True)  # close card + main-block
        time.sleep(2)
        st.rerun()

    user_lat = loc["coords"]["latitude"]
    user_lon = loc["coords"]["longitude"]
    dest_lat, dest_lon = st.session_state["destination"]

    dist_m = haversine_distance(user_lat, user_lon, dest_lat, dest_lon)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("📍 You", f"{user_lat:.5f}, {user_lon:.5f}")
    with m2:
        st.metric("🎯 Destination", f"{dest_lat:.5f}, {dest_lon:.5f}")
    with m3:
        st.metric("📏 Distance", f"{dist_m:.1f} m")

    live_map = folium.Map(location=[user_lat, user_lon], zoom_start=17)
    folium.Marker(
        [user_lat, user_lon],
        tooltip="You",
        icon=folium.Icon(color="blue"),
    ).add_to(live_map)
    folium.Marker(
        [dest_lat, dest_lon],
        tooltip="Destination",
        icon=folium.Icon(color="red"),
    ).add_to(live_map)
    folium.PolyLine(
        [[user_lat, user_lon], [dest_lat, dest_lon]],
        color="lime",
        weight=3,
    ).add_to(live_map)

    st_folium(live_map, height=360, key="live_map")

    inside = trigger_alert_if_needed(dist_m, st.session_state["radius_m"])
    if inside:
        st.error(f"🚨 Inside {st.session_state['radius_m']} m radius!")
    else:
        st.info("🧭 You are outside the radius. Move closer to the destination...")

    time.sleep(2)
    st.rerun()

else:
    if not st.session_state["destination"]:
        st.info("Set a destination to start tracking.")
    elif not st.session_state["tracking"]:
        st.info("Click **Start** in the controls above to begin tracking.")

st.markdown('</div>', unsafe_allow_html=True)  # close live card
st.markdown('</div>', unsafe_allow_html=True)  # close main-block
