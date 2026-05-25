function saveCache(key, value) {
    localStorage.setItem(
        "cache_" + key,
        JSON.stringify(value)
    );
}

function loadCache(key) {
    const data = localStorage.getItem(
        "cache_" + key
    );

    return data
        ? JSON.parse(data)
        : null;
}