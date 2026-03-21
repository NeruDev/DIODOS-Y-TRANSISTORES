# Calculadora de Rectificadores Monofasicos

Modulo refactorizado para analisis de rectificadores monofasicos (Puente Graetz).

## Arquitectura

```
calculadora/
├── __init__.py       # Paquete Python
├── __main__.py       # Permite: python -m calculadora
├── core.py           # Calculos matematicos puros (sin GUI)
├── plotting.py       # Generacion de graficas (backend-agnostico)
├── run_headless.py   # Modo sin GUI (Codespaces/CI)
├── ui_tkinter.py     # Interfaz grafica Tkinter
├── main.py           # Auto-deteccion de entorno
└── README.md         # Este archivo
```

## Modos de Ejecucion

### 1. Modo Automatico (Recomendado)

Detecta si hay display disponible y elige el modo apropiado:

```bash
# Desde la raiz del repositorio
source .venv/bin/activate
python topics/01-circuitos-diodos/Notas/PRACTICA\ 1/calculadora/main.py
```

O como modulo:

```bash
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1"
python -m calculadora
```

### 2. Modo GUI (Local)

Requiere display disponible (Windows, macOS, Linux con X11):

```bash
python calculadora/main.py --gui
# O directamente:
python calculadora/ui_tkinter.py
```

### 3. Modo Headless (Codespaces/CI)

No requiere display, genera archivos PNG y JSON:

```bash
# Uso basico
python calculadora/run_headless.py

# Con parametros personalizados
python calculadora/run_headless.py --Vs_rms 15 --C_uF 4700

# Exportar JSON
python calculadora/run_headless.py --json --output-dir ./resultados

# Solo calculos (sin graficas)
python calculadora/run_headless.py --json --no-plots --quiet
```

## Opciones de Linea de Comandos

### main.py

| Opcion       | Descripcion                         |
|--------------|-------------------------------------|
| `--gui`      | Forzar modo GUI                     |
| `--headless` | Forzar modo headless                |
| `--detect`   | Mostrar info del entorno detectado  |

### run_headless.py

| Opcion         | Default   | Descripcion                        |
|----------------|-----------|------------------------------------|
| `--Vs_rms`     | 12.0      | Voltaje RMS secundario [V]         |
| `--f_red`      | 60.0      | Frecuencia de red [Hz]             |
| `--Vd`         | 0.7       | Caida por diodo [V]                |
| `--R_carga`    | 10.0      | Resistencia de carga [Ohm]         |
| `--L_H`        | 1.5       | Inductancia del filtro [H]         |
| `--RL_Ohm`     | 40.0      | R del devanado [Ohm]               |
| `--C_uF`       | 2200.0    | Capacitancia del filtro [uF]       |
| `--FR_obj`     | 0.05      | Factor de rizo objetivo            |
| `--output-dir` | ./outputs | Directorio de salida               |
| `--prefix`     | practica1 | Prefijo para archivos              |
| `--dpi`        | 150       | Resolucion de imagenes             |
| `--json`       | false     | Exportar resultados a JSON         |
| `--no-plots`   | false     | No generar graficas                |
| `--quiet`      | false     | Modo silencioso                    |

## Uso Programatico

Puedes usar el modulo `core` directamente en otros scripts:

```python
from calculadora import InputParams, calcular_todo, validate_params

# Crear parametros
params = InputParams(
    Vs_rms=12.0,
    f_red=60.0,
    Vd=0.7,
    R_carga=10.0,
    C_uF=2200.0
)

# Validar
is_valid, error = validate_params(params)
if not is_valid:
    raise ValueError(error)

# Calcular
results = calcular_todo(params)

# Acceder a resultados
print(f"Vo_dc = {results.Vo_dc:.3f} V")
print(f"FR sin filtro = {results.FR * 100:.2f}%")
print(f"FR con C = {results.FRi:.2f}%")
print(f"C minimo requerido = {results.C_min_uF:.0f} uF")
```

## Archivos Generados (Modo Headless)

| Archivo                      | Contenido                                |
|------------------------------|------------------------------------------|
| `practica1_formas_onda.png`  | Senales vs(t), v_rect(t), v_filt(t), i(t)|
| `practica1_fourier.png`      | Reconstruccion Fourier + espectro        |
| `practica1_filtros.png`      | Curvas FR vs C y atenuacion vs L         |
| `practica1_results.json`     | Todos los parametros y resultados        |

## Compatibilidad

- **Python:** 3.10+
- **Dependencias:** numpy, matplotlib
- **Plataformas:** Windows, macOS, Linux (incluido Codespaces)

## Diferencias con el Script Original

| Caracteristica          | Original                    | Refactorizado              |
|-------------------------|-----------------------------|-----------------------------|
| Backend matplotlib      | TkAgg (hardcoded)           | Auto-detectado              |
| Entorno                 | Solo GUI local              | GUI + Headless              |
| Separacion de logica    | Monolitico                  | core/plotting/ui separados  |
| Uso programatico        | Dificil                     | Facil via imports           |
| CI/CD                   | No compatible               | Compatible                  |
| Codespaces              | Requiere VNC                | Funciona nativo             |
