function createProject(name, width, height) {

    const project = {
        name,
        width,
        height,
        pixels: [],
        createdAt: Date.now()
    };

    saveProject(name, project);

    return project;
}