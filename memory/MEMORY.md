# MEMORY.md — DIODOS Y TRANSISTORES repo

## Scripts de herramientas del repo (00-META/tools/)
- Todos los scripts de generación de gráficos se ubican en `00-META/tools/`
- Patrón: `[PREFIJO]-gen-[descripcion].py` (ej. `DIO-gen-curva-iv.py`)
- Salida siempre en `XX-Modulo/media/generated/` (PNG, dpi≥100)
- Ejecutar siempre desde la raíz del repo con `.venv/Scripts/python.exe`
- Usar `matplotlib.use('Agg')` al inicio para scripts no interactivos
- Para scripts interactivos GUI: `matplotlib.use('TkAgg')`

## Scripts standalone / interactivos (Notas/)
- `01-Circuitos-Diodos/Notas/PRACTICA 1/practica1_calculadora.py`
  - GUI completa con tkinter + matplotlib (TkAgg)
  - 4 tabs: Cálculos por Pasos | Formas de Onda | Fourier | Diseño Filtros
  - 9 pasos de cálculo alineados con incisos a)-m) de PRACTICA_1.md
  - Validado: todos los valores teóricos nominales correctos (10/10 checks)
  - FRi con C=2200µF = 7.92% → advertencia visible; C_min = 2406 µF para FR≤5%

## Entorno de ejecución
- Python: `.venv/Scripts/python.exe` (desde raíz del repo)
- Shell en Claude Code: bash (no PowerShell) → no usar `&` ni `Set-Location`
- Windows: rutas con forward slash en bash, sin `&` antes del ejecutable
- Dependencias instaladas: numpy, matplotlib, scipy, schemdraw, sympy, SciencePlots

## Convenciones del repo
- Idioma: español
- Zona Notas/: sandbox libre, sin validación de formato
- Imágenes: solo desde scripts Python, nunca manuales
- Metadatos `::SCRIPT_METADATA::` obligatorios en cada script
- Registro centralizado: `00-META/tools/Control_Scripts.md`

## Preferencias de usuario
- Comentarios técnicos didácticos en cada sección del código
- GUIs con paleta oscura (tipo editor), tkinter estándar
- Resumen tabular de resultados + formas de onda embebidas
