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
  - Validado contra PROCEDIMIENTO_PRACTICA_1.md: 21/21 checks OK
  - L_H default = 1.5H, RL_Ohm = 40Ω (primario 120/12V@2A típico)
  - Bug crítico corregido: impedancia PASO 8 usaba 2×n×w_out (debía ser n×w_out)
  - Vr(pp) PASO 9 usa Vm_red (no Vo_dc); C_min exacto ≈5229µF para FR≤5%
  - FRi con C=2200µF = 13.4% (documento); Vo_dc_C = 12.63V; RT=50Ω

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

## Estándar H3 para esquemáticos de circuitos complejos
- **Parámetros:** unit=3.5, comp_length=3.5, separation=2.0, fontsize=13, dpi=300
- **Layout horizontal (L→R):** línea superior = positivos, línea inferior = GND
- **Paleta didáctica:** azul=fuente, rojo=diodo, verde=capacitor, naranja=resistor, gris=conexión, violeta=voltaje
- **Regla crítica de etiquetas:** NUNCA solapar con líneas de conexión ni componentes
  - Línea superior: `loc='top'` con `ofst=0.3`
  - Línea inferior: coordenadas absolutas desplazadas `(x - 0.5, y)`
- **Referencia:** `DIO-gen-duplicador-voltaje-horizontal.py`

## Preferencias de usuario
- Comentarios técnicos didácticos en cada sección del código
- GUIs con paleta oscura (tipo editor), tkinter estándar
- Resumen tabular de resultados + formas de onda embebidas
