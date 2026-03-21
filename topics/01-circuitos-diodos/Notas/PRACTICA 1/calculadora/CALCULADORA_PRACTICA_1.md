# CALCULADORA PRÁCTICA 1 — Documentación Técnica

> **Análisis e Implementación de Rectificadores Monofásicos**
> Instituto Tecnológico de Toluca — Diodos y Transistores

---

## Índice

1. [Descripción General](#descripción-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Módulos y Funcionalidad](#módulos-y-funcionalidad)
4. [Flujo de Ejecución](#flujo-de-ejecución)
5. [Cálculos Implementados](#cálculos-implementados)
6. [Modos de Operación](#modos-de-operación)
7. [Salidas Generadas](#salidas-generadas)

---

## Descripción General

La calculadora es una herramienta modular para el análisis matemático y gráfico de circuitos rectificadores monofásicos tipo Puente Graetz (onda completa).

**Problema que resuelve:**
- El script original era monolítico (1260 líneas) con GUI hardcodeado
- No funcionaba en Codespaces/CI (requería display)
- Acoplamiento fuerte entre cálculos, GUI y matplotlib

**Solución implementada:**
- Separación de responsabilidades en módulos independientes
- Soporte para dual-mode: GUI (local) y headless (Codespaces/CI)
- Auto-detección de entorno para elegir modo apropiado

---

## Arquitectura del Sistema

```
calculadora/
│
├── core.py              ← Capa de cálculos matemáticos puros
│   • InputParams (dataclass)
│   • CalcResults (dataclass)
│   • calcular_todo() → 9 pasos de la práctica
│   • Funciones de generación de señales
│   • Validación de parámetros
│   • SIN dependencias de GUI o matplotlib backend
│
├── plotting.py          ← Capa de visualización (backend-agnostic)
│   • plot_waveforms()
│   • plot_fourier()
│   • plot_filter_design()
│   • save_all_figures()
│   • NO configura matplotlib backend
│
├── run_headless.py      ← Modo sin GUI (Codespaces/CI)
│   • Configura: matplotlib.use("Agg")
│   • CLI con argparse para parámetros
│   • Genera PNG + JSON
│
├── ui_tkinter.py        ← Modo con GUI (Windows/macOS/Linux)
│   • Configura: matplotlib.use("TkAgg")
│   • Interfaz Tkinter interactiva
│   • 4 tabs: Ondas, Fourier, Filtros, Resumen
│
├── main.py              ← Auto-detección de entorno
│   • detect_display() → verifica si hay X11/display
│   • run_gui() si hay display
│   • run_headless() si no hay display
│
├── __init__.py          ← Exports del paquete
├── __main__.py          ← python -m calculadora
└── README.md            ← Guía de uso rápido
```

### Principios de Diseño

1. **Separación de Capas**
   - `core.py` = lógica pura (matemáticas)
   - `plotting.py` = presentación (gráficas)
   - `ui_*.py` = interacción (GUI/CLI)

2. **Backend Agnostic**
   - `core.py` NO importa matplotlib
   - `plotting.py` NO configura backend
   - Cada modo elige su backend antes de importar

3. **Ejecutable Dual**
   - Como script directo: `python run_headless.py`
   - Como paquete: `from calculadora import calcular_todo`

---

## Módulos y Funcionalidad

### 1. `core.py` — Cálculos Matemáticos

**Responsabilidad:** Implementar los 9 pasos de la práctica sin dependencias externas de GUI.

**Clases principales:**

```python
@dataclass
class InputParams:
    """Parámetros de entrada del circuito"""
    Vs_rms: float = 12.0      # V RMS secundario
    f_red: float = 60.0       # Hz frecuencia
    Vd: float = 0.7           # V caída diodo
    R_carga: float = 10.0     # Ω resistencia
    L_H: float = 1.5          # H inductancia
    RL_Ohm: float = 40.0      # Ω R devanado
    C_uF: float = 2200.0      # µF capacitor
    FR_obj: float = 0.05      # Factor rizo objetivo
```

```python
@dataclass
class CalcResults:
    """Resultados de todos los pasos"""
    # PASO 1 - Transformador
    Vm: float
    Vm_red: float
    f_out: float
    T_out: float

    # PASO 2 - DC promedio
    Vo_dc: float
    Io_dc: float

    # ... (todos los pasos 1-9)
```

**Función principal:**

```python
def calcular_todo(params: InputParams) -> CalcResults:
    """
    Ejecuta los 9 pasos de cálculo de la práctica.

    PASO 1 — Parámetros del transformador
    PASO 2 — Voltaje y corriente DC promedio
    PASO 3 — Voltaje y corriente RMS sin filtro
    PASO 4 — Factor de forma y rizo sin filtro
    PASO 5 — Parámetros de los diodos
    PASO 6 — Potencias y rendimiento
    PASO 7 — Serie de Fourier (5 armónicos)
    PASO 8 — Filtro inductivo R-L
    PASO 9 — Diseño del filtro capacitivo
    """
```

**Funciones auxiliares:**

| Función | Propósito |
|---------|-----------|
| `generate_time_array()` | Array temporal para n ciclos |
| `generate_secondary_voltage()` | Señal vs(t) del secundario |
| `generate_rectified_voltage()` | Señal rectificada de onda completa |
| `generate_capacitor_filtered()` | Simulación RC muestra a muestra |
| `generate_inductor_filtered_current()` | Reconstrucción armónica con L |
| `generate_fourier_reconstruction()` | Serie de Fourier n armónicos |
| `generate_fr_vs_capacitance()` | Curva FR vs C para diseño |
| `generate_attenuation_vs_inductance()` | Curva atenuación vs L |

**Validación:**

```python
def validate_params(params: InputParams) -> tuple[bool, str]:
    """
    Valida parámetros de entrada.

    Returns:
        (is_valid, error_message)

    Reglas:
        • Vs_rms, R_carga, C_uF > 0
        • 0 ≤ Vd < Vs_rms
        • 0 < FR_obj < 1
    """
```

### 2. `plotting.py` — Visualización

**Responsabilidad:** Generar gráficas matplotlib sin asumir backend específico.

**Paleta de colores:**

```python
class ColorPalette:
    BG_MAIN = "#1e1e2e"    # Fondo principal oscuro
    VS = "#89b4fa"         # Azul - secundario
    RECT = "#f38ba8"       # Rosa - rectificada
    FILT = "#a6e3a1"       # Verde - filtrada
    ID = "#fab387"         # Naranja - corriente
    DC = "#6c7086"         # Gris - línea DC
```

**Funciones de graficación:**

```python
def plot_waveforms(fig: Figure, params: InputParams,
                   results: CalcResults) -> None:
    """
    Grafica 4 subplots de formas de onda:
    1. vs(t) - Secundario del transformador
    2. v_rect(t) - Salida rectificada sin filtro
    3. v_filt_C(t) - Con filtro capacitivo
    4. is(t) - Corriente: sin/con inductor
    """
```

```python
def plot_fourier(fig: Figure, params: InputParams,
                 results: CalcResults) -> None:
    """
    Grafica 2 subplots de serie de Fourier:
    1. Señal real vs reconstrucción
    2. Espectro de amplitudes (DC + 5 armónicos)
    """
```

```python
def plot_filter_design(fig: Figure, params: InputParams,
                        results: CalcResults) -> None:
    """
    Grafica 2 subplots de diseño de filtros:
    1. Factor de rizo FR vs capacitancia C
    2. Atenuación de armónicos vs inductancia L
    """
```

```python
def save_all_figures(params: InputParams, results: CalcResults,
                      output_dir: str = ".", prefix: str = "practica1",
                      dpi: int = 150) -> list[str]:
    """
    Genera y guarda todas las figuras en PNG.

    Returns:
        Lista de rutas de archivos generados
    """
```

**Características clave:**
- ✅ No configura `matplotlib.use()` (caller decide)
- ✅ Trabaja con objetos `Figure` ya creados
- ✅ Estilo oscuro consistente (paleta académica)
- ✅ Compatible con Agg (headless) y TkAgg (GUI)

### 3. `run_headless.py` — Modo Sin GUI

**Responsabilidad:** Ejecutar cálculos y generar salidas sin display.

**Configuración de backend:**

```python
import matplotlib
matplotlib.use("Agg")  # ← ANTES de cualquier otro import de matplotlib
```

**CLI (argparse):**

```bash
python run_headless.py \
    --Vs_rms 15 \
    --C_uF 4700 \
    --output-dir ./resultados \
    --json \
    --dpi 200
```

**Salidas generadas:**
- `practica1_formas_onda.png` (4 subplots)
- `practica1_fourier.png` (2 subplots)
- `practica1_filtros.png` (2 subplots)
- `practica1_results.json` (params + results)

**Ejemplo de JSON exportado:**

```json
{
  "params": {
    "Vs_rms": 12.0,
    "f_red": 60.0,
    "Vd": 0.7,
    "R_carga": 10.0,
    "C_uF": 2200.0
  },
  "results": {
    "Vm": 16.971,
    "Vo_dc": 9.913,
    "FRi": 13.49,
    "C_min_uF": 5228
  }
}
```

### 4. `ui_tkinter.py` — Modo Con GUI

**Responsabilidad:** Interfaz gráfica interactiva local.

**Configuración de backend:**

```python
import matplotlib
matplotlib.use("TkAgg")  # ← Backend embebible en Tkinter
```

**Estructura de la ventana:**

```
┌──────────────────────────────────────────────────────────────┐
│ PRÁCTICA 1 — ANÁLISIS DE RECTIFICADORES MONOFÁSICOS          │
├──────────────┬───────────────────────────────────────────────┤
│              │  ┌─ Formas de Onda ─────────────────────────┐ │
│  DATOS DE    │  │                                           │ │
│  ENTRADA     │  │  [Gráfica matplotlib embebida]            │ │
│              │  │                                           │ │
│ ┌──────────┐ │  └───────────────────────────────────────────┘ │
│ │Vs_rms  V │ │  ┌─ Serie de Fourier ────────────────────┐   │
│ │f_red  Hz │ │  │ [Tab seleccionable]                    │   │
│ │Vd      V │ │  └────────────────────────────────────────┘   │
│ │R_carga Ω │ │  ┌─ Diseño de Filtros ───────────────────┐   │
│ │L       H │ │  │ [Tab seleccionable]                    │   │
│ │C      µF │ │  └────────────────────────────────────────┘   │
│ └──────────┘ │  ┌─ Resumen ─────────────────────────────┐   │
│              │  │ [Tab seleccionable]                    │   │
│ [ CALCULAR ] │  └────────────────────────────────────────┘   │
└──────────────┴───────────────────────────────────────────────┘
```

**Tabs disponibles:**
1. **Formas de Onda** — vs(t), v_rect(t), v_filt(t), is(t)
2. **Serie de Fourier** — Reconstrucción + Espectro
3. **Diseño de Filtros** — FR vs C, Atenuación vs L
4. **Resumen** — Texto con todos los resultados

**Interacción:**
- Panel izquierdo: Campos de entrada editables
- Botón "CALCULAR": Recalcula y actualiza todas las gráficas
- Toolbar matplotlib: Zoom, Pan, Guardar
- Scroll vertical para parámetros largos

### 5. `main.py` — Auto-Detección

**Responsabilidad:** Detectar entorno y elegir modo apropiado.

**Lógica de detección:**

```python
def detect_display() -> bool:
    """Detecta si hay display disponible."""

    # Windows: siempre hay display
    if sys.platform == "win32":
        return True

    # macOS: verificar si no es SSH sin X11
    if sys.platform == "darwin":
        if os.environ.get("SSH_CONNECTION") and not os.environ.get("DISPLAY"):
            return False
        return True

    # Linux: verificar DISPLAY y xdpyinfo
    display = os.environ.get("DISPLAY", "")
    if display:
        try:
            result = subprocess.run(["xdpyinfo"], ...)
            return result.returncode == 0
        except:
            return bool(display)

    return False
```

**Decisión de modo:**

```python
if detect_display():
    run_gui()        # ui_tkinter.py
else:
    run_headless()   # run_headless.py
```

---

## Flujo de Ejecución

### Modo Headless (Típico en Codespaces)

```
1. Usuario ejecuta:
   $ python run_headless.py --json

2. Script configura:
   matplotlib.use("Agg")

3. Parsea argumentos:
   • Parámetros del circuito (Vs_rms, C_uF, etc.)
   • Opciones de salida (--output-dir, --dpi, --json)

4. Crea InputParams:
   params = InputParams(Vs_rms=12.0, ...)

5. Valida parámetros:
   is_valid, error = validate_params(params)

6. Ejecuta cálculos:
   results = calcular_todo(params)

7. Genera gráficas:
   files = save_all_figures(params, results, ...)
   → practica1_formas_onda.png
   → practica1_fourier.png
   → practica1_filtros.png

8. Exporta JSON (si --json):
   json.dump({"params": ..., "results": ...}, ...)
   → practica1_results.json

9. Muestra resumen en consola:
   Vo_dc = 9.913 V
   FRi = 13.49%
   C_min = 5228 µF
```

### Modo GUI (Típico en Local)

```
1. Usuario ejecuta:
   $ python ui_tkinter.py

2. Script configura:
   matplotlib.use("TkAgg")

3. Crea ventana Tkinter:
   app = App()

4. Inicializa con valores default:
   self._params = {k: StringVar(value=v) for ...}
   self._calcular()  # Auto-calcula al inicio

5. Usuario interactúa:
   • Modifica campos de entrada
   • Presiona botón "CALCULAR"

6. Evento click:
   def _calcular(self):
       params = self._get_params()
       results = calcular_todo(params)
       self._actualizar_ondas()
       self._actualizar_fourier()
       self._actualizar_filtros()
       self._actualizar_resumen()

7. Actualización de gráficas:
   • Limpia Figure: fig.clear()
   • Re-grafica: plotting.plot_waveforms(fig, ...)
   • Redibuja canvas: canvas.draw()

8. Loop principal:
   app.mainloop()  # Tkinter event loop
```

### Modo Auto-Detección

```
1. Usuario ejecuta:
   $ python main.py

2. Detecta entorno:
   has_display = detect_display()

3. Decide modo:
   if has_display:
       print("Display detectado, iniciando GUI...")
       from ui_tkinter import main
       main()
   else:
       print("No display, iniciando headless...")
       from run_headless import main
       main()
```

---

## Cálculos Implementados

### PASO 1 — Parámetros del Transformador

```python
Vm = Vs_rms × √2                    # Voltaje pico del secundario
Vm_red = Vm - 2·Vd                  # Pico disponible (2 diodos en serie)
f_out = 2·f_red                     # Frecuencia de salida (onda completa)
T_out = 1/f_out                     # Período de salida
```

**Ejemplo:** Vs_rms=12V, Vd=0.7V
- Vm = 12 × 1.414 = 16.97 V
- Vm_red = 16.97 - 2×0.7 = 15.57 V
- f_out = 2 × 60 = 120 Hz

### PASO 2 — Voltaje y Corriente DC

```python
Vo_dc = (2/π) × Vm_red              # Valor promedio onda completa
Io_dc = Vo_dc / R_carga             # Ley de Ohm
```

**Ejemplo:** Vm_red=15.57V, R=10Ω
- Vo_dc = 0.6366 × 15.57 = 9.91 V
- Io_dc = 9.91 / 10 = 0.991 A

### PASO 3 — Voltaje y Corriente RMS

```python
Vo_rms = Vm_red / √2                # RMS de onda rectificada
Io_rms = Vo_rms / R_carga
```

**Nota:** La señal rectificada |Vm·sin(ωt)| tiene el mismo RMS que la sinusoide original.

### PASO 4 — Factor de Forma y Rizo

```python
FF = Vo_rms / Vo_dc                       # Factor de forma
Vr_rms = √(Vo_rms² - Vo_dc²)             # Componente de rizo RMS
FR = Vr_rms / Vo_dc                       # Factor de rizo
```

**Teórico ideal:** FF = π/(2√2) ≈ 1.11, FR ≈ 0.483 (48.3%)

### PASO 5 — Parámetros de los Diodos

```python
ID_prom = Io_dc / 2                       # Cada diodo conduce 50%
ID_rms = Io_rms / √2
VPR = Vm                                  # Tensión inversa pico
P_diodo = Vd × ID_prom                    # Potencia disipada
```

### PASO 6 — Potencias y Rendimiento

```python
Po_dc = Vo_dc² / R_carga                  # Potencia DC útil
Po_ca = Vo_rms² / R_carga                 # Potencia AC total
η = (Po_dc / Po_ca) × 100%                # Rendimiento
```

**Teórico ideal:** η = 8/π² × 100 ≈ 81.1%

### PASO 7 — Serie de Fourier

```python
# Expansión: vo(t) = Vo_dc + Σ an·cos(2n·ω₀·t)
# donde ω₀ = 2πf_red

an = -4·Vm_red / [π·(4n² - 1)]           # Coeficiente armónico n

freq[n] = 2n·f_red                        # Frecuencias: 120, 240, 360, ...
```

**Ejemplo:** n=1, Vm_red=15.57V, f_red=60Hz
- a₁ = -4×15.57 / (π×3) = -6.61 V
- f₁ = 2×60 = 120 Hz (fundamental de salida)

### PASO 8 — Filtro Inductivo R-L

```python
RT = R_carga + RL_devanado                # Resistencia total
Io_dc_RL = Vo_dc / RT                     # DC atenuada por RL
V_carga_RL = Io_dc_RL × R_carga           # Solo sobre R

# Para cada armónico n:
Zn = √[RT² + (n·ω_out·L)²]                # Impedancia armónica
In = Vn / Zn                              # Corriente armónica
atenuación = (R / Zn) × 100%              # vs sin filtro
```

**Ejemplo:** RT=50Ω, L=1.5H, n=1 (120Hz)
- XL₁ = 2π×120×1.5 = 1131 Ω
- Z₁ = √(50² + 1131²) = 1132 Ω
- Atenuación = 10/1132 = 0.88% (muy efectivo)

### PASO 9 — Filtro Capacitivo

```python
Vr_pp = Vm_red / (f_out · C · R)          # Rizo pico a pico
Vo_dc_C = Vm_red - Vr_pp/2                # DC con filtro
Vr_rms_C = Vr_pp / (2√3)                  # RMS (onda triangular)
FR_C = Vr_rms_C / Vo_dc_C                 # Factor de rizo

# C mínimo para FR_obj:
x = 2√3·FR_obj / (1 + √3·FR_obj)
C_min = 1 / (x · f_out · R)
```

**Ejemplo:** Vm_red=15.57V, f=120Hz, R=10Ω, C=2200µF
- Vr_pp = 15.57/(120×2.2e-3×10) = 5.89 V
- Vo_dc_C = 15.57 - 5.89/2 = 12.63 V
- FRi = (5.89/(2√3)) / 12.63 × 100 = 13.49%

Para FRi ≤ 5%:
- C_min = 5228 µF → usar 5600 µF o 6800 µF comercial

---

## Modos de Operación

### Comparación de Modos

| Característica | GUI (TkAgg) | Headless (Agg) | Auto |
|----------------|-------------|----------------|------|
| **Display requerido** | ✅ Sí | ❌ No | 🔄 Detecta |
| **Interactividad** | ✅ High | ❌ None | 🔄 Depende |
| **Salidas** | Pantalla | PNG + JSON | 🔄 Depende |
| **Entorno ideal** | Windows, macOS, Linux+X11 | Codespaces, CI/CD | Cualquiera |
| **Entrada parámetros** | GUI forms | CLI args | 🔄 Depende |
| **Tiempo respuesta** | Inmediato | ~3-5 seg | 🔄 Depende |
| **Zoom/Pan** | ✅ Toolbar | ❌ No | 🔄 Depende |

### Casos de Uso Típicos

**1. Desarrollo Local (Windows/macOS)**
```bash
python calculadora/ui_tkinter.py
# → Ventana interactiva
# → Modificar parámetros en tiempo real
# → Ver resultados inmediatamente
```

**2. GitHub Codespaces**
```bash
python calculadora/run_headless.py --json
# → outputs/practica1_*.png
# → Abrir imágenes con "Open Preview"
```

**3. CI/CD Pipeline**
```yaml
- name: Generar figuras
  run: |
    python calculadora/run_headless.py \
      --output-dir ./artifacts \
      --json
- name: Upload artifacts
  uses: actions/upload-artifact@v3
  with:
    path: artifacts/
```

**4. Análisis Paramétrico**
```bash
for C in 1000 2200 4700 6800; do
  python calculadora/run_headless.py \
    --C_uF $C \
    --prefix "test_C${C}" \
    --json \
    --no-plots
done
# → Genera JSON para cada valor de C
# → Análisis posterior con scripts
```

**5. Uso Programático**
```python
from calculadora import InputParams, calcular_todo

params = InputParams(Vs_rms=15.0, C_uF=4700.0)
results = calcular_todo(params)

if results.FRi > 5.0:
    print(f"Aumentar C a >= {results.C_min_uF:.0f} uF")
```

---

## Salidas Generadas

### Gráficas PNG

#### 1. `practica1_formas_onda.png` (4 subplots)

```
┌─────────────────────────────────────────┐
│ vs(t) — Secundario transformador        │
│ [Senoidal 60 Hz, Vm marca]              │
├─────────────────────────────────────────┤
│ v_rect(t) — Rectificada sin filtro      │
│ [Onda completa 120 Hz, Vo_dc marca]     │
├─────────────────────────────────────────┤
│ v_filt_C(t) — Con filtro capacitivo     │
│ [Nivel DC + rizo triangular]            │
├─────────────────────────────────────────┤
│ is(t) — Corriente: sin/con inductor     │
│ [Púrpura sin L, Naranja con L]          │
└─────────────────────────────────────────┘
```

**Paleta:**
- Azul (#89b4fa): vs(t) secundario
- Rosa (#f38ba8): v_rect(t) rectificada
- Verde (#a6e3a1): v_filt_C(t) filtrada
- Naranja (#fab387): corriente con L
- Gris (#6c7086): líneas de DC promedio

#### 2. `practica1_fourier.png` (2 subplots)

```
┌────────────────────┬─────────────────────┐
│ Señal vs Fourier   │ Espectro de barras  │
│                    │                     │
│ [Línea discontinua │ [DC en gris]        │
│  señal real]       │ [120 Hz azul]       │
│ [Línea continua    │ [240 Hz verde]      │
│  reconstrucción]   │ [360 Hz naranja]    │
│                    │ [480 Hz rosa]       │
│                    │ [600 Hz púrpura]    │
└────────────────────┴─────────────────────┘
```

**Nota:** El espectro debe coincidir con FFT del osciloscopio.

#### 3. `practica1_filtros.png` (2 subplots)

```
┌─────────────────────┬──────────────────────┐
│ FR vs C (semilog-x) │ Atenuación vs L      │
│                     │                      │
│ [Curva azul]        │ [5 curvas colores]   │
│ [Línea roja: 5%]    │ arm. 2, 4, 6, 8, 10  │
│ [Línea naranja:     │                      │
│  C_min = 5228 µF]   │ [Línea blanca: L     │
│ [Línea verde:       │  actual = 1.5 H]     │
│  C_actual]          │                      │
└─────────────────────┴──────────────────────┘
```

### Archivo JSON

```json
{
  "params": {
    "Vs_rms": 12.0,
    "f_red": 60.0,
    "Vd": 0.7,
    "R_carga": 10.0,
    "L_H": 1.5,
    "RL_Ohm": 40.0,
    "C_uF": 2200.0,
    "FR_obj": 0.05
  },
  "results": {
    "Vm": 16.970562748477143,
    "Vm_red": 15.570562748477143,
    "f_out": 120.0,
    "T_out": 0.008333333333333333,
    "Vo_dc": 9.912646683080652,
    "Io_dc": 0.9912646683080652,
    "Vo_rms": 11.010281547311537,
    "Io_rms": 1.1010281547311537,
    "FF": 1.1107207345395915,
    "Vr_rms": 4.791046008095043,
    "FR": 0.4834265810306357,
    "ID_prom": 0.4956323341540326,
    "ID_rms": 0.7783174593052023,
    "VPR": 16.970562748477143,
    "P_diodo": 0.34694263390782284,
    "Po_dc": 9.826056693098334,
    "Po_ca": 12.122630035012084,
    "eta": 81.05574990409975,
    "fourier_freqs": [120.0, 240.0, 360.0, 480.0, 600.0],
    "fourier_amps": [6.607341165809906, 1.7700909775226148, 0.9019503058468274, 0.5577879935743726, 0.38317978672893635],
    "RT": 50.0,
    "Io_dc_RL": 0.19825293366161304,
    "V_carga_RL": 1.9825293366161304,
    "Z_RL_arms": [1131.9894154914817, 2263.9788309829634, 3395.968246474445, 4527.957661965927, 5659.947077457408],
    "IL_arms": [0.005835818458634804, 0.0007819176685318093, 0.0002654338912961859, 0.00012306197585847353, 6.77001395802423e-05],
    "aten_RL": [0.8836068824064766, 0.44180344120323827, 0.29453563080215886, 0.22090172060161914, 0.17672137648129532],
    "Ir_rms_RL": 0.004126221758891135,
    "FRi_RL": 2.08109475235886,
    "Vr_pp": 5.893007563852633,
    "Vo_dc_C": 12.624059466600826,
    "Vr_rms_C": 1.7022694699007245,
    "Ir_rms_C": 0.17022694699007246,
    "FR_C": 0.13487076868951084,
    "FRi": 13.487076868951084,
    "C_min_uF": 5228.379456483854
  }
}
```

**Uso del JSON:**
```python
import json

with open("practica1_results.json") as f:
    data = json.load(f)

print(f"FRi = {data['results']['FRi']:.2f}%")
print(f"C_min = {data['results']['C_min_uF']:.0f} µF")

# Comparar múltiples ejecuciones
if data['results']['FRi'] > 5.0:
    print("⚠️ Factor de rizo excede el objetivo")
```

---

## Troubleshooting

### Error: "No module named 'numpy'"

**Causa:** Entorno virtual no activado.

**Solución:**
```bash
cd /workspaces/DIODOS-Y-TRANSISTORES
source .venv/bin/activate
```

### Error: "ImportError: attempted relative import"

**Causa:** Ejecutar plotting.py directamente.

**Solución:** Los módulos internos no se ejecutan solos:
```bash
# ✅ Correcto
python main.py
python run_headless.py

# ❌ Incorrecto
python plotting.py
```

### Advertencia: "matplotlib backend"

Si ves:
```
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend
```

**Explicación:** Normal en modo headless. Las figuras se guardan en PNG, no se muestran.

### Error: "TclError: no display"

**Causa:** Intentando usar GUI sin display.

**Solución:**
```bash
# Forzar modo headless
python main.py --headless

# O directamente
python run_headless.py
```

### Figuras vacías o incorrectas

**Causa:** Parámetros fuera de rango.

**Solución:** Verificar validación:
```python
is_valid, error = validate_params(params)
if not is_valid:
    print(f"Error: {error}")
```

---

## Referencias

- Script original: `practica1_calculadora.py` (1260 líneas, monolítico)
- Práctica: `PRACTICA_1.md` — Enunciado completo
- Procedimiento: `PROCEDIMIENTO_PRACTICA_1.md` — Guía de laboratorio
- Explicación: `Explicacion_Practica_1.md` — Teoría de rectificadores

---

**Última actualización:** 2026-03-21
**Autor:** Refactorización ClaudeCode
**Versión:** 2.0.0 (arquitectura modular)
