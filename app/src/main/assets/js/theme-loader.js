async function loadThemes() {

    const response =
        await fetch("./data/themes.json");

    return await response.json();
}