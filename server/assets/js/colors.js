let palette = [];

async function loadPalette() {
    try {
        const response = await fetch("./data/palette.json");
        const data = await response.json();

        palette = data.defaultPalette;

        console.log("Paleta carregada:", palette);

    } catch (err) {
        console.error("Erro ao carregar paleta:", err);
    }
}

loadPalette();