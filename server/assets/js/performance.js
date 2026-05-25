function getDeviceMemory() {

    if (navigator.deviceMemory) {
        return navigator.deviceMemory;
    }

    return "unknown";
}