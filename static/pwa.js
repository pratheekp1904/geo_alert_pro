console.log("PWA JS Loaded");

if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("static/service-worker.js")
    .then(reg => console.log("SW registered:", reg.scope))
    .catch(err => console.log("SW registration failed:", err));
}

if (window.Notification && Notification.permission !== "granted") {
    Notification.requestPermission().then(p => {
        console.log("Notification permission:", p);
    });
}
