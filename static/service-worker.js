self.addEventListener("install", () => {
  console.log("Service Worker Installed 🚀");
  self.skipWaiting();
});

self.addEventListener("activate", () => {
  console.log("Service Worker Activated 🛰️");
});

self.addEventListener("push", function (event) {
  const message = event.data?.text() || "You are near your destination!";
  self.registration.showNotification("Geo Alert Pro 🚨", {
    body: message,
    icon: "/static/icon-192.png",
    vibrate: [250, 100, 250]
  });
});
