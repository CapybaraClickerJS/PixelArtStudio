# build.py
import os
import shutil
from pathlib import Path

SRC = Path("src")
DIST = Path("dist")

def build():
    if DIST.exists():
        shutil.rmtree(DIST)

    DIST.mkdir()

    # copia arquivos
    for file in SRC.rglob("*"):
        if file.is_file():
            target = DIST / file.relative_to(SRC)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(file, target)

    # "bundle" simples (remove comentários JS)
    js_file = DIST / "main.js"
    if js_file.exists():
        code = js_file.read_text()
        code = "\n".join(line for line in code.split("\n") if not line.strip().startswith("//"))
        js_file.write_text(code)

    print("🚀 Build finalizado em /dist")

if __name__ == "__main__":
    build()