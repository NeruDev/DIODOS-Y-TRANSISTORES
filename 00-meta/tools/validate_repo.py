"""
validate_repo.py
─────────────────
Script de validación estructural del repositorio.

Verifica:
- Carpetas requeridas
- Archivos faltantes
- Convenciones de nombres
- manifest.json vs estructura real

Ejecutar desde la raíz del repositorio:
  python 00-meta/tools/validate_repo.py
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
OUTPUT_DIR = REPO_ROOT / "audits" / "reports"

# Estructura esperada por módulo
EXPECTED_STRUCTURE = {
    "files": ["README.md", "manifest.json", "directives.md"],
    "dirs": ["theory", "methods", "problems", "solutions", "assets", "formularios"]
}

# Estados válidos
VALID_STATUSES = ["draft", "review", "stable", "deprecated"]


def validate_module(module_path: Path) -> dict:
    """Valida la estructura de un módulo individual."""
    issues = []
    module_name = module_path.name

    # Verificar archivos requeridos
    for file in EXPECTED_STRUCTURE["files"]:
        file_path = module_path / file
        if not file_path.exists():
            issues.append(f"Archivo faltante: {file}")

    # Verificar directorios requeridos
    for dir_name in EXPECTED_STRUCTURE["dirs"]:
        dir_path = module_path / dir_name
        if not dir_path.exists():
            issues.append(f"Directorio faltante: {dir_name}/")

    # Validar manifest.json si existe
    manifest_path = module_path / "manifest.json"
    if manifest_path.exists():
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)

            # Verificar campos requeridos
            required_fields = ["title", "status", "prerequisites", "tags", "last_updated", "modules"]
            for field in required_fields:
                if field not in manifest:
                    issues.append(f"manifest.json: campo faltante '{field}'")

            # Verificar estado válido
            if manifest.get("status") not in VALID_STATUSES:
                issues.append(f"manifest.json: estado inválido '{manifest.get('status')}'")

        except json.JSONDecodeError as e:
            issues.append(f"manifest.json: error de sintaxis JSON - {e}")

    return {
        "module": module_name,
        "path": str(module_path),
        "issues": issues,
        "valid": len(issues) == 0
    }


def validate_naming_conventions(module_path: Path) -> list:
    """Verifica convenciones de nomenclatura."""
    issues = []
    module_name = module_path.name

    # Verificar kebab-case en nombre del módulo
    if module_name != module_name.lower():
        issues.append(f"Nombre de módulo no está en kebab-case: {module_name}")

    # Verificar archivos de teoría
    theory_dir = module_path / "theory"
    if theory_dir.exists():
        for file in theory_dir.glob("*.md"):
            # Patrón esperado: PREFIX-XX-Tipo-Descripcion.md
            name = file.stem
            parts = name.split("-")
            if len(parts) < 3:
                issues.append(f"Nomenclatura incorrecta en theory/: {file.name}")

    return issues


def generate_report(results: list) -> str:
    """Genera un reporte en formato Markdown."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""# Reporte de Validación Estructural

> Generado: {timestamp}

---

## Resumen

| Módulo | Estado | Issues |
|--------|--------|--------|
"""

    total_issues = 0
    for result in results:
        status = "✅ OK" if result["valid"] else "❌ Errores"
        num_issues = len(result["issues"])
        total_issues += num_issues
        report += f"| {result['module']} | {status} | {num_issues} |\n"

    report += f"\n**Total de issues:** {total_issues}\n\n"

    # Detalles por módulo
    report += "---\n\n## Detalle por Módulo\n\n"

    for result in results:
        if not result["valid"]:
            report += f"### {result['module']}\n\n"
            for issue in result["issues"]:
                report += f"- ⚠️ {issue}\n"
            report += "\n"

    if total_issues == 0:
        report += "✅ **No se encontraron problemas estructurales.**\n"

    return report


def main():
    """Función principal."""
    print("🔍 Validando estructura del repositorio...")

    results = []

    # Validar cada módulo en topics/
    if TOPICS_DIR.exists():
        for module_dir in sorted(TOPICS_DIR.iterdir()):
            if module_dir.is_dir():
                print(f"  → Validando {module_dir.name}...")
                result = validate_module(module_dir)

                # Añadir validación de nomenclatura
                naming_issues = validate_naming_conventions(module_dir)
                result["issues"].extend(naming_issues)
                result["valid"] = len(result["issues"]) == 0

                results.append(result)
    else:
        print("❌ Error: No se encontró el directorio topics/")
        return

    # Generar reporte
    report = generate_report(results)

    # Guardar reporte
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    report_path = OUTPUT_DIR / f"{date_str}-validation.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n📄 Reporte guardado en: {report_path}")

    # Resumen
    valid_count = sum(1 for r in results if r["valid"])
    print(f"✅ {valid_count}/{len(results)} módulos válidos")


if __name__ == "__main__":
    main()
