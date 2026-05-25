function autoSave(data) {
    localStorage.setItem(
        "pixelart_autosave",
        JSON.stringify(data)
    );
}

function loadAutoSave() {
    const save = localStorage.getItem(
        "pixelart_autosave"
    );

    return save
        ? JSON.parse(save)
        : null;
}