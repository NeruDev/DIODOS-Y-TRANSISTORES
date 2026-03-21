# EJECUCIÓN EN TERMINAL — Guía Rápida

> **Calculadora de Rectificadores Monofásicos (Práctica 1)**
> Guía práctica para ejecutar desde la línea de comandos

---

## Índice Rápido

1. [Preparación del Entorno](#preparación-del-entorno)
2. [Ejecución Modo Headless](#ejecución-modo-headless)
3. [Ejecución Modo GUI](#ejecución-modo-gui)
4. [Ejecución Modo Auto](#ejecución-modo-auto)
5. [Ejemplos Prácticos](#ejemplos-prácticos)
6. [Solución de Problemas](#solución-de-problemas)

---

## Preparación del Entorno

### 1. Activar Entorno Virtual

**En Linux/macOS/Codespaces:**
```bash
cd /workspaces/DIODOS-Y-TRANSISTORES
source .venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
cd "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
& ".venv\Scripts\Activate.ps1"
```

**En Windows (CMD):**
```cmd
cd "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
.venv\Scripts\activate.bat
```

**Verificar activación:**
```bash
# Debe aparecer (.venv) al inicio del prompt
(.venv) user@host:~/DIODOS-Y-TRANSISTORES$
```

### 2. Navegar a la Carpeta de la Calculadora

```bash
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"
```

---

## Ejecución Modo Headless

**Uso:** Ambientes sin display (Codespaces, CI/CD, servidores)
**Salida:** Archivos PNG + JSON

### Comando Básico

```bash
python calculadora/run_headless.py
```

**Resultado:**
```
============================================================
CALCULADORA DE RECTIFICADORES - Modo Headless
============================================================

Parametros de entrada:
  Vs_rms = 12.0 V
  f_red  = 60.0 Hz
  Vd     = 0.7 V
  R      = 10.0 Ohm
  L      = 1.5 H
  RL     = 40.0 Ohm
  C      = 2200.0 uF
  FR_obj = 5.0%

Resultados principales:
----------------------------------------
  Vm     = 16.971 V
  Vm_red = 15.571 V
  f_out  = 120 Hz

  Vo_dc  = 9.913 V
  Io_dc  = 0.991 A

  FF     = 1.1107
  FR     = 48.34%

  eta    = 81.06%

  FRi (con C=2200uF) = 13.49%
  C_min  = 5228 uF

Generando graficas...
  -> ./outputs/practica1_formas_onda.png
  -> ./outputs/practica1_fourier.png
  -> ./outputs/practica1_filtros.png

Total: 3 archivos generados

Completado.
```

### Opciones CLI Completas

| Opción | Tipo | Default | Descripción |
|--------|------|---------|-------------|
| `--Vs_rms` | float | 12.0 | Voltaje RMS secundario [V] |
| `--f_red` | float | 60.0 | Frecuencia de red [Hz] |
| `--Vd` | float | 0.7 | Caída por diodo [V] |
| `--R_carga` | float | 10.0 | Resistencia de carga [Ω] |
| `--L_H` | float | 1.5 | Inductancia [H] |
| `--RL_Ohm` | float | 40.0 | R del devanado [Ω] |
| `--C_uF` | float | 2200.0 | Capacitancia [µF] |
| `--FR_obj` | float | 0.05 | Factor de rizo objetivo |
| `--output-dir` `-o` | str | ./outputs | Directorio de salida |
| `--prefix` | str | practica1 | Prefijo archivos |
| `--dpi` | int | 150 | Resolución imágenes |
| `--json` | flag | false | Exportar JSON |
| `--no-plots` | flag | false | No generar gráficas |
| `--quiet` `-q` | flag | false | Modo silencioso |

### Ver Ayuda Completa

```bash
python calculadora/run_headless.py --help
```

---

## Ejecución Modo GUI

**Uso:** Ambientes con display (Windows, macOS, Linux+X11)
**Salida:** Ventana interactiva

### Comando Directo

```bash
python calculadora/ui_tkinter.py
```

**O a través de main.py:**

```bash
python calculadora/main.py --gui
```

**Resultado:**
- Se abre ventana gráfica Tkinter
- Panel izquierdo: Campos de entrada
- Panel derecho: 4 tabs con gráficas
- Botón "CALCULAR" actualiza todo

### Interacción

1. **Modificar parámetros:**
   - Click en campos de entrada
   - Escribir nuevos valores
   - Presionar ENTER o click fuera

2. **Recalcular:**
   - Click en botón "CALCULAR"
   - Esperar ~1 segundo
   - Todas las gráficas se actualizan

3. **Navegar tabs:**
   - Click en "Formas de Onda"
   - Click en "Serie de Fourier"
   - Click en "Diseño de Filtros"
   - Click en "Resumen"

4. **Herramientas matplotlib:**
   - Zoom: Click en 🔍 y arrastrar
   - Pan: Click en ✋ y arrastrar
   - Home: Restablecer vista
   - Guardar: Exportar gráfica actual

---

## Ejecución Modo Auto

**Uso:** Detecta automáticamente el entorno y elige el modo apropiado

### Comando Auto-Detectar

```bash
python calculadora/main.py
```

**Comportamiento:**

| Plataforma | DISPLAY | Resultado |
|------------|---------|-----------|
| Windows | Siempre presente | → GUI |
| macOS Local | Siempre presente | → GUI |
| macOS SSH sin X11 | No presente | → Headless |
| Linux con X11 | :0, :1, etc. | → GUI |
| Linux Codespaces | :1 (sin xdpyinfo) | → Headless |
| Linux SSH sin X11 | No presente | → Headless |

### Solo Detectar (Sin Ejecutar)

```bash
python calculadora/main.py --detect
```

**Ejemplo de salida:**
```
Plataforma: linux
DISPLAY: :1
Display disponible: No
Modo recomendado: Headless
```

### Forzar Modo Específico

```bash
# Forzar GUI (falla si no hay display)
python calculadora/main.py --gui

# Forzar Headless (siempre funciona)
python calculadora/main.py --headless

# Pasar opciones al modo headless
python calculadora/main.py --headless --json --quiet
```

---

## Ejemplos Prácticos

### 1. Generar Gráficas con Parámetros Custom

```bash
python calculadora/run_headless.py \
  --Vs_rms 15 \
  --C_uF 4700 \
  --output-dir ./mis_resultados \
  --prefix "test1"
```

**Genera:**
- `mis_resultados/test1_formas_onda.png`
- `mis_resultados/test1_fourier.png`
- `mis_resultados/test1_filtros.png`

### 2. Solo Exportar JSON (Sin Gráficas)

```bash
python calculadora/run_headless.py \
  --json \
  --no-plots \
  --quiet
```

**Genera:**
- `outputs/practica1_results.json` (silencioso, sin PNG)

### 3. Barrido Paramétrico de Capacitancia

**Bash/Linux:**
```bash
mkdir -p resultados_barrido

for C in 1000 2200 3300 4700 6800; do
  echo "Calculando con C = $C uF..."
  python calculadora/run_headless.py \
    --C_uF $C \
    --output-dir resultados_barrido \
    --prefix "C_${C}uF" \
    --json \
    --quiet
done

echo "Barrido completado. Archivos generados:"
ls -lh resultados_barrido/
```

**PowerShell/Windows:**
```powershell
New-Item -ItemType Directory -Force -Path .\resultados_barrido

foreach ($C in @(1000, 2200, 3300, 4700, 6800)) {
    Write-Host "Calculando con C = $C uF..."
    python calculadora/run_headless.py `
        --C_uF $C `
        --output-dir .\resultados_barrido `
        --prefix "C_${C}uF" `
        --json `
        --quiet
}

Write-Host "Barrido completado. Archivos generados:"
Get-ChildItem .\resultados_barrido\ | Format-Table Name, Length
```

### 4. Alta Resolución para Reporte

```bash
python calculadora/run_headless.py \
  --dpi 300 \
  --output-dir ./figures_reporte \
  --prefix "reporte_final"
```

**Genera imágenes de 300 DPI** (apropiadas para impresión)

### 5. Comparar Diseños (con vs sin filtro L)

```bash
# Diseño 1: Solo capacitor
python calculadora/run_headless.py \
  --L_H 0 \
  --RL_Ohm 0 \
  --C_uF 4700 \
  --prefix "solo_C" \
  --json

# Diseño 2: Capacitor + inductor
python calculadora/run_headless.py \
  --L_H 1.5 \
  --RL_Ohm 40 \
  --C_uF 4700 \
  --prefix "L_y_C" \
  --json
```

**Comparar resultados:**
```bash
cat outputs/solo_C_results.json | grep -i "fri"
cat outputs/L_y_C_results.json | grep -i "fri"
```

### 6. Validar Diseño con Especificación FR ≤ 5%

```bash
python calculadora/run_headless.py \
  --FR_obj 0.05 \
  --C_uF 5600 \
  --json \
  --quiet > resultado.txt

# Verificar si cumple especificación
if grep -q "FRi.*[0-4]\." resultado.txt; then
  echo "✅ Diseño cumple con FR ≤ 5%"
else
  echo "❌ Diseño NO cumple, aumentar C"
fi
```

### 7. Ejecutar como Módulo Python

```bash
# Desde el directorio que contiene "calculadora/"
python -m calculadora --headless --json
```

### 8. Uso Programático en Script Custom

```python
#!/usr/bin/env python3
"""script_custom.py - Optimizar C para FR objetivo"""

import sys
sys.path.insert(0, "calculadora")

from calculadora import InputParams, calcular_todo

# Parámetros base
params = InputParams(
    Vs_rms=12.0,
    f_red=60.0,
    Vd=0.7,
    R_carga=10.0
)

# Buscar C óptimo
FR_objetivo = 5.0  # %

for C in range(1000, 10000, 500):
    params.C_uF = C
    results = calcular_todo(params)

    print(f"C = {C:5d} µF → FRi = {results.FRi:5.2f}%", end="")

    if results.FRi <= FR_objetivo:
        print(" ✅ CUMPLE")
        print(f"\nC óptimo encontrado: {C} µF")
        print(f"C_min teórico: {results.C_min_uF:.0f} µF")
        break
    else:
        print(" ❌ No cumple")
```

**Ejecutar:**
```bash
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"
python script_custom.py
```

---

## Solución de Problemas

### Problema 1: Comando no Encontrado

**Síntoma:**
```
bash: python: command not found
```

**Solución:**
```bash
# Verificar disponibilidad
which python3

# Si existe python3, usar ese:
python3 calculadora/run_headless.py

# O crear alias
alias python=python3
```

### Problema 2: Módulo numpy no Encontrado

**Síntoma:**
```
ModuleNotFoundError: No module named 'numpy'
```

**Solución:**
```bash
# 1. Verificar que .venv está activado
which python
# Debe mostrar: /workspaces/.../venv/bin/python

# 2. Si no está activado
source .venv/bin/activate

# 3. Si aún falla, reinstalar dependencias
pip install -r requirements.txt
```

### Problema 3: Permission Denied

**Síntoma:**
```
PermissionError: [Errno 13] Permission denied: './outputs'
```

**Solución:**
```bash
# Crear directorio con permisos
mkdir -p outputs
chmod 755 outputs

# O especificar directorio alternativo
python calculadora/run_headless.py --output-dir ~/mis_outputs
```

### Problema 4: TclError en Headless

**Síntoma:**
```
_tkinter.TclError: no display name and no $DISPLAY environment variable
```

**Causa:** Intentando ejecutar GUI sin display

**Solución:**
```bash
# Usar script headless en vez de GUI
python calculadora/run_headless.py  # ✅

# O forzar auto-detección
python calculadora/main.py  # ✅ Detecta y usa headless

# NO ejecutar
python calculadora/ui_tkinter.py  # ❌ Requiere display
```

### Problema 5: Figuras Vacías o Datos Incorrectos

**Síntoma:**
Gráficas en blanco o valores NaN

**Solución:**
```bash
# Verificar parámetros válidos
python calculadora/run_headless.py \
  --Vs_rms 12 \
  --Vd 0.7 \
  --R_carga 10 \
  --C_uF 2200

# Rango válido:
# Vs_rms > 0
# 0 ≤ Vd < Vs_rms
# R_carga > 0
# C_uF > 0
# 0 < FR_obj < 1
```

### Problema 6: Directorio No Existe

**Síntoma:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'calculadora/run_headless.py'
```

**Causa:** Ejecutando desde directorio incorrecto

**Solución:**
```bash
# 1. Verificar ubicación actual
pwd

# 2. Navegar a PRACTICA 1
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"

# 3. Verificar que calculadora/ existe
ls -d calculadora/
# Debe mostrar: calculadora/

# 4. Ejecutar
python calculadora/run_headless.py
```

### Problema 7: Warning sobre matplotlib backend

**Síntoma:**
```
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend
```

**Causa:** Normal en modo headless

**Solución:**
- ℹ️ Esto es **normal** y **esperado**
- Las figuras se guardan en PNG correctamente
- Para suprimir warning (opcional):
```bash
python calculadora/run_headless.py 2>/dev/null
```

### Problema 8: Gráficas no se Ven en Codespaces

**Causa:** Codespaces no muestra GUI

**Solución:**
```bash
# 1. Generar PNG
python calculadora/run_headless.py

# 2. Navegar en explorador de archivos
# calculadora/outputs/practica1_*.png

# 3. Click derecho → "Open Preview"
# O doble click para descargar
```

---

## Rutas de Ejecución Según Entorno

### Codespaces (GitHub)

```bash
# 1. Abrir terminal en Codespace
# 2. Activar entorno
source .venv/bin/activate

# 3. Navegar
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"

# 4. Ejecutar headless
python calculadora/run_headless.py --json

# 5. Ver resultados
ls -lh calculadora/outputs/
```

### Windows Local (PowerShell)

```powershell
# 1. Abrir PowerShell como Administrador
# 2. Navegar al repo
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"

# 3. Activar entorno
& ".venv\Scripts\Activate.ps1"

# 4. Navegar a práctica
Set-Location "topics\01-circuitos-diodos\Notas\PRACTICA 1"

# 5. Ejecutar GUI
python calculadora\ui_tkinter.py

# O headless
python calculadora\run_headless.py --json
```

### Linux/macOS Local

```bash
# 1. Abrir terminal
# 2. Navegar al repo
cd ~/Documentos/DIODOS-Y-TRANSISTORES

# 3. Activar entorno
source .venv/bin/activate

# 4. Navegar a práctica
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"

# 5. Auto-detectar modo
python calculadora/main.py

# O forzar GUI
python calculadora/main.py --gui
```

---

## Atajos y Tips

### Alias Útiles (Linux/macOS)

Agregar a `~/.bashrc` o `~/.zshrc`:

```bash
# Navegar rápido a la calculadora
alias goto-calc='cd ~/DIODOS-Y-TRANSISTORES/topics/01-circuitos-diodos/Notas/PRACTICA\ 1'

# Activar y ejecutar
alias calc-run='source ~/DIODOS-Y-TRANSISTORES/.venv/bin/activate && goto-calc && python calculadora/run_headless.py'

# Generar con timestamp
alias calc-now='calc-run --prefix "run_$(date +%Y%m%d_%H%M%S)"'
```

**Uso:**
```bash
calc-now --json --C_uF 4700
```

### Script Wrapper (Windows)

`calc.bat`:
```batch
@echo off
cd "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES\topics\01-circuitos-diodos\Notas\PRACTICA 1"
call "..\..\..\..\..\.venv\Scripts\activate.bat"
python calculadora\run_headless.py %*
```

**Uso:**
```cmd
calc.bat --json --C_uF 4700
```

### Makefile (Opcional)

`Makefile`:
```makefile
.PHONY: run gui headless clean

CALC_DIR = calculadora
VENV = ../../../../.venv/bin/activate

run:
	@source $(VENV) && python $(CALC_DIR)/main.py

gui:
	@source $(VENV) && python $(CALC_DIR)/ui_tkinter.py

headless:
	@source $(VENV) && python $(CALC_DIR)/run_headless.py --json

clean:
	@rm -rf $(CALC_DIR)/outputs/*
	@rm -rf $(CALC_DIR)/__pycache__

test:
	@source $(VENV) && python $(CALC_DIR)/core.py
```

**Uso:**
```bash
make headless
make gui
make clean
```

---

## Integración CI/CD

### GitHub Actions

`.github/workflows/generate-figures.yml`:
```yaml
name: Generar Figuras Práctica 1

on:
  push:
    paths:
      - 'topics/01-circuitos-diodos/Notas/PRACTICA 1/calculadora/**'

jobs:
  generate:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m venv .venv
          source .venv/bin/activate
          pip install -r requirements.txt

      - name: Generate figures
        run: |
          source .venv/bin/activate
          cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"
          python calculadora/run_headless.py \
            --output-dir artifacts \
            --json \
            --dpi 200

      - name: Upload artifacts
        uses: actions/upload-artifact@v3
        with:
          name: practica1-figures
          path: topics/01-circuitos-diodos/Notas/PRACTICA 1/artifacts/
```

---

## Referencias Rápidas

| Documento | Descripción |
|-----------|-------------|
| `README.md` | Guía de uso general |
| `CALCULADORA_PRACTICA_1.md` | Documentación técnica completa |
| `EJECUCION_TERMINAL.md` | Esta guía (ejecutar en terminal) |
| `PRACTICA_1.md` | Enunciado de la práctica |
| `PROCEDIMIENTO_PRACTICA_1.md` | Procedimiento de laboratorio |

---

**Última actualización:** 2026-03-21
**Para soporte:** Revisar `CALCULADORA_PRACTICA_1.md` sección Troubleshooting
