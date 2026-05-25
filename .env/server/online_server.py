from flask import Flask, request, jsonify, send_from_directory
import os
import json

app = Flask(__name__)

BASE_DIR = "../app/src/main/assets"

DATABASE_FILE = "cloud_saves.json"

if not os.path.exists(DATABASE_FILE):
    with open(DATABASE_FILE, "w") as f:
        json.dump({}, f)

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(BASE_DIR, path)

@app.route("/api/save", methods=["POST"])
def save_art():
    data = request.json

    with open(DATABASE_FILE, "r") as f:
        db = json.load(f)

    name = data.get("name", "sem_nome")

    db[name] = data

    with open(DATABASE_FILE, "w") as f:
        json.dump(db, f)

    return jsonify({
        "status": "ok",
        "message": "Arte salva na nuvem"
    })

@app.route("/api/load/<name>")
def load_art(name):
    with open(DATABASE_FILE, "r") as f:
        db = json.load(f)

    if name not in db:
        return jsonify({
            "error": "Arte não encontrada"
        }), 404

    return jsonify(db[name])

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )