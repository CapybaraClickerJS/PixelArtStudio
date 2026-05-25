window.addEventListener("offline", () => {
    console.log("Sem internet");
});

window.addEventListener("online", () => {
    console.log("Internet voltou");
});