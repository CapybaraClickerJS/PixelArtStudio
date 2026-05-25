function saveProject() {
    const data = {
        width: gridWidth,
        height: gridHeight,
        pixels: pixels,
        color: currentColor
    };

    localStorage.setItem(
        "pixelart_autosave",
        JSON.stringify(data)
    );
}

function loadProject() {
    const save = localStorage.getItem("pixelart_autosave");

    if (!save) return;

    try {
        const data = JSON.parse(save);

        gridWidth = data.width;
        gridHeight = data.height;
        pixels = data.pixels;
        currentColor = data.color || "#ff0000";

        applyZoom();
        drawGrid();

    } catch(e) {
        console.log("Erro ao carregar save");
    }
}