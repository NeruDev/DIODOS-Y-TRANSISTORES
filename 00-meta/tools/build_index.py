"""
build_index.py
──────────────
Script para generar índices automáticos del repositorio.

Genera:
- WIKI_INDEX.md actualizado
- Índices por módulo

Ejecutar desde la raíz del repositorio:
  python 00-meta/tools/build_index.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configuración
REPO_ROOT = Path(__file__).parent.parent.parent
TOPICS_DIR = REPO_ROOT / "topics"


def get_module_info(module_path: Path) -> dict:
    """Extrae información de un módulo desde su manifest.json."""
    manifest_path = module_path / "manifest.json"

    if not manifest_path.exists():
        return None

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    return {
        "name": module_path.name,
        "title": manifest.get("title", module_path.name),
        "status": manifest.get("status", "draft"),
        "prerequisites": manifest.get("prerequisites", []),
        "tags": manifest.get("tags", [])
    }


def get_theory_files(module_path: Path) -> list:
    """Lista los archivos de teoría de un módulo."""
    theory_dir = module_path / "theory"
    files = []

    if theory_dir.exists():
        for file in sorted(theory_dir.glob("*.md")):
            # Extraer información del nombre
            name = file.stem
            files.append({
                "name": file.name,
                "path": f"topics/{module_path.name}/theory/{file.name}",
                "id": name
            })

    return files


def generate_wiki_index() -> str:
    """Genera el contenido de WIKI_INDEX.md."""
    timestamp = datetime.now().strftime("%Y-%m-%d")

    content = f"""<!--
::METADATA::
type: index
topic_id: wiki-index
file_id: WIKI_INDEX
status: active
audience: both
last_updated: {timestamp}
-->

# Índice Wiki — Diodos y Transistores

> **Mapa de navegación centralizado.** Generado automáticamente.

---

"""

    # Procesar cada módulo
    for module_dir in sorted(TOPICS_DIR.iterdir()):
        if not module_dir.is_dir():
            continue

        info = get_module_info(module_dir)
        if not info:
            continue

        module_name = module_dir.name
        prefix = module_name.split("-")[0]  # ej: "01"

        content += f"""## {info['title']}

- [README](topics/{module_name}/README.md) | [Índice](topics/{module_name}/00-Index.md)
- **Estado:** {info['status']}
- **Tags:** {', '.join(info['tags'][:5])}

| Archivo de Teoría |
|-------------------|
"""

        # Listar archivos de teoría
        theory_files = get_theory_files(module_dir)
        for tf in theory_files:
            content += f"| [{tf['id']}]({tf['path']}) |\n"

        content += "\n---\n\n"

    # Recursos globales
    content += """## Recursos Globales

| Recurso | Ubicación |
|---------|-----------|
| Temario | [00-meta/temario.md](00-meta/temario.md) |
| Glosario | [glossary.md](glossary.md) |
| Directiva para IAs | [AGENTS.md](AGENTS.md) |
| Nomenclatura | [00-meta/naming-conventions.md](00-meta/naming-conventions.md) |
| Mapa del Repo | [00-meta/repo-map.md](00-meta/repo-map.md) |
"""

    return content


def main():
    """Función principal."""
    print("🔨 Generando índices...")

    if not TOPICS_DIR.exists():
        print("❌ Error: No se encontró el directorio topics/")
        return

    # Generar WIKI_INDEX.md
    wiki_content = generate_wiki_index()
    wiki_path = REPO_ROOT / "WIKI_INDEX.md"

    with open(wiki_path, 'w', encoding='utf-8') as f:
        f.write(wiki_content)

    print(f"✅ Generado: {wiki_path}")
    print("📝 Nota: Revisa y ajusta el índice generado según sea necesario.")


if __name__ == "__main__":
    main()
