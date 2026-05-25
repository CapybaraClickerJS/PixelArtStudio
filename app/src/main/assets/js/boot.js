window.addEventListener("load", async () => {

    loadProject();

    if ("serviceWorker" in navigator) {
        try {
            await navigator.serviceWorker.register("./sw.js");
            console.log("SW ON");
        } catch(e) {
            console.log("SW ERROR");
        }
    }

});