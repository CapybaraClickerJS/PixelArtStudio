const DB_NAME = "PixelArtStudioDB";

function openDatabase() {

    return indexedDB.open(
        DB_NAME,
        1
    );
}