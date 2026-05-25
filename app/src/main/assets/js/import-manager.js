function importJSON(file, callback) {

    const reader = new FileReader();

    reader.onload = () => {
        callback(
            JSON.parse(reader.result)
        );
    };

    reader.readAsText(file);
}