import math
from streamlit_js_eval import streamlit_js_eval

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

def send_push_notification(msg):
    streamlit_js_eval(js_expressions=f"""
        if (navigator.serviceWorker) {{
            navigator.serviceWorker.ready.then(reg => {{
                reg.showNotification("Geo Alert Pro 🚨", {{
                    body: "{msg}",
                    icon: "/static/icon-192.png",
                    vibrate: [200,100,200]
                }});
            }});
        }}
    """, key=f"push_{msg}")

def trigger_alert_if_needed(dist_m, radius_m):
    """Triggers alert once when inside radius; resets when outside"""
    import streamlit as st

    if "alert_triggered" not in st.session_state:
        st.session_state["alert_triggered"] = False

    if dist_m <= radius_m:
        if not st.session_state["alert_triggered"]:
            send_push_notification(f"You are within {radius_m} meters!")
            st.session_state["alert_triggered"] = True
        return True
    else:
        st.session_state["alert_triggered"] = False
        return False
