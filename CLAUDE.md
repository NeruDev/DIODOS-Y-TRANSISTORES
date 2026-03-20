# CLAUDE.md — Contexto para Claude (Anthropic)

> **Hereda de:** [AGENTS.md](AGENTS.md) — Fuente de verdad centralizada
> **Última sincronización:** 2026-03-20

---

## Instrucciones para Claude

1. **Leer** [AGENTS.md](AGENTS.md) como primera acción obligatoria.
2. **Consultar** `manifest.json` del módulo objetivo.
3. **Seguir** las directivas específicas en `directives.md` del módulo.

---

## Referencias Rápidas

| Documento | Propósito |
|-----------|-----------|
| [AGENTS.md](AGENTS.md) | Directiva general completa |
| [00-meta/repo-map.md](00-meta/repo-map.md) | Mapa estructural del repositorio |
| [00-meta/naming-conventions.md](00-meta/naming-conventions.md) | Estándares de nomenclatura |
| [00-meta/standards.md](00-meta/standards.md) | Directivas técnicas (schemdraw, LaTeX) |
| [00-meta/tools/Control_Scripts.md](00-meta/tools/Control_Scripts.md) | Registro de scripts e imágenes |
| [glossary.md](glossary.md) | Glosario de términos técnicos |
| [WIKI_INDEX.md](WIKI_INDEX.md) | Mapa de navegación |

---

## Extensiones Específicas para Claude

### Entorno de ejecución preferido

```bash
# Activar entorno Python
source .venv/bin/activate  # Linux/Codespaces
& ".venv\Scripts\Activate.ps1"  # Windows PowerShell

# Para GUI en Codespaces
export DISPLAY=:1
```

### Ejecución de scripts

```bash
# Desde la raíz del repositorio
python 00-meta/tools/DIO-gen-curva-iv.py
```

```powershell
# PowerShell (Windows)
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
& ".venv\Scripts\python.exe" "00-meta/tools/SCRIPT.py"
```

### Precaución LaTeX en heredocs bash

Usar `<<'EOF'` (comillas simples) para evitar expansión de `$`:

```bash
cat >> archivo.md <<'EOF'
El voltaje térmico es $V_T$
EOF
```

---

## Arquitectura (Resumen)

```
topics/
├── 01-circuitos-diodos/  (DIO)
├── 02-transistor-bjt/    (BJT)
├── 03-transistor-fet/    (FET)
├── 04-amplificadores/    (AMP)
└── 05-proyecto-final/    (PRO)
```

Cada módulo contiene: `README.md`, `manifest.json`, `directives.md`, `theory/`, `methods/`, `problems/`, `solutions/`, `assets/`, `Notas/`.

---

## Sincronización

Este archivo hereda de `AGENTS.md`. Ante cambios estructurales, actualizar primero `AGENTS.md` y luego propagar a este archivo.
