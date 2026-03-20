"""
audit_report.py
───────────────
Script para generar reportes de auditoría del repositorio.

Genera:
- Reporte de estado general
- Snapshot estructural en JSON

Ejecutar desde la raíz del repositorio:
  python 00-meta/tools/audit_report.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configuración
REPO_ROOT = Path(__file__).parent.parent.parent
TOPICS_DIR = REPO_ROOT / "topics"
AUDITS_DIR = REPO_ROOT / "audits"


def count_files(directory: Path, pattern: str = "*") -> int:
    """Cuenta archivos que coinciden con un patrón."""
    if not directory.exists():
        return 0
    return len(list(directory.glob(pattern)))


def get_module_stats(module_path: Path) -> dict:
    """Obtiene estadísticas de un módulo."""
    stats = {
        "name": module_path.name,
        "theory_files": count_files(module_path / "theory", "*.md"),
        "problem_files": count_files(module_path / "problems", "*.md"),
        "solution_files": count_files(module_path / "solutions", "*.md"),
        "assets": count_files(module_path / "assets", "*.png"),
        "notes_files": count_files(module_path / "Notas", "*.md"),
        "status": "unknown"
    }

    # Leer estado desde manifest.json
    manifest_path = module_path / "manifest.json"
    if manifest_path.exists():
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            stats["status"] = manifest.get("status", "unknown")
            stats["title"] = manifest.get("title", module_path.name)

    return stats


def generate_snapshot() -> dict:
    """Genera un snapshot del estado del repositorio."""
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "modules": [],
        "totals": defaultdict(int)
    }

    for module_dir in sorted(TOPICS_DIR.iterdir()):
        if not module_dir.is_dir():
            continue

        stats = get_module_stats(module_dir)
        snapshot["modules"].append(stats)

        # Acumular totales
        for key in ["theory_files", "problem_files", "solution_files", "assets", "notes_files"]:
            snapshot["totals"][key] += stats.get(key, 0)

    snapshot["totals"] = dict(snapshot["totals"])
    return snapshot


def generate_report(snapshot: dict) -> str:
    """Genera un reporte en formato Markdown."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""# Reporte de Auditoría del Repositorio

> Generado: {timestamp}

---

## Estado General

| Métrica | Total |
|---------|-------|
| Archivos de teoría | {snapshot['totals'].get('theory_files', 0)} |
| Problemas | {snapshot['totals'].get('problem_files', 0)} |
| Soluciones | {snapshot['totals'].get('solution_files', 0)} |
| Imágenes generadas | {snapshot['totals'].get('assets', 0)} |
| Notas pendientes | {snapshot['totals'].get('notes_files', 0)} |

---

## Estado por Módulo

| Módulo | Estado | Teoría | Problemas | Soluciones | Assets | Notas |
|--------|--------|--------|-----------|------------|--------|-------|
"""

    for module in snapshot["modules"]:
        status_emoji = {
            "draft": "📝",
            "review": "🔄",
            "stable": "✅",
            "deprecated": "⚠️"
        }.get(module["status"], "❓")

        report += f"| {module.get('title', module['name'])} | {status_emoji} {module['status']} | {module['theory_files']} | {module['problem_files']} | {module['solution_files']} | {module['assets']} | {module['notes_files']} |\n"

    # Análisis de completitud
    report += """

---

## Análisis de Completitud

"""

    for module in snapshot["modules"]:
        if module["status"] == "draft":
            report += f"- **{module.get('title', module['name'])}:** En desarrollo\n"
            if module["notes_files"] > 0:
                report += f"  - {module['notes_files']} notas pendientes de migrar a theory/\n"

    report += """

---

## Próximos Pasos Sugeridos

1. Migrar contenido de `Notas/` a `theory/` en módulos con notas pendientes
2. Completar archivos stub en módulos en estado `draft`
3. Generar imágenes faltantes con scripts Python
4. Actualizar estado a `review` cuando la estructura esté completa
"""

    return report


def main():
    """Función principal."""
    print("📊 Generando reporte de auditoría...")

    if not TOPICS_DIR.exists():
        print("❌ Error: No se encontró el directorio topics/")
        return

    # Generar snapshot
    snapshot = generate_snapshot()

    # Guardar snapshot JSON
    snapshots_dir = AUDITS_DIR / "snapshots"
    snapshots_dir.mkdir(parents=True, exist_ok=True)

    date_str = datetime.now().strftime("%Y-%m-%d")
    snapshot_path = snapshots_dir / f"{date_str}.json"

    with open(snapshot_path, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, indent=2, ensure_ascii=False)

    print(f"📸 Snapshot guardado: {snapshot_path}")

    # Generar reporte Markdown
    report = generate_report(snapshot)

    reports_dir = AUDITS_DIR / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_path = reports_dir / f"{date_str}-audit.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"📄 Reporte guardado: {report_path}")

    # Mostrar resumen
    print(f"\n📈 Resumen:")
    print(f"   - Módulos: {len(snapshot['modules'])}")
    print(f"   - Archivos de teoría: {snapshot['totals'].get('theory_files', 0)}")
    print(f"   - Imágenes generadas: {snapshot['totals'].get('assets', 0)}")


if __name__ == "__main__":
    main()
