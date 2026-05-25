function recoverLastSession() {

    const autosave =
        localStorage.getItem(
            "pixelart_autosave"
        );

    if (!autosave) return null;

    return JSON.parse(autosave);
}