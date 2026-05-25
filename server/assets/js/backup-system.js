function createBackup(data) {

    localStorage.setItem(
        "backup_" + Date.now(),
        JSON.stringify(data)
    );
}