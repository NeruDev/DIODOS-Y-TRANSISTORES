# 🛠️ Herramientas de Generación de Gráficos

> Carpeta centralizada para scripts de Python que generan las imágenes del repositorio.

## Convención de Nombres

### Scripts

```
[PREFIJO]-gen-[descripción].py
```

| Prefijo | Módulo |
|---------|--------|
| `DIO` | 01 — Circuitos con Diodos |
| `BJT` | 02 — Transistor Bipolar |
| `FET` | 03 — Transistor FET/MOSFET |
| `AMP` | 04 — Amplificadores |
| `PRO` | 05 — Proyecto Final |

### Imágenes Generadas

```
{PREFIJO}-{tema}-{NN}-{descriptor}.png
```

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `PREFIJO` | Módulo (3 letras) | `DIO`, `BJT` |
| `tema` | Concepto físico (del script) | `curva-iv`, `curva-temp` |
| `NN` | Secuencia global (2 dígitos) | `01`, `02`, `03` |
| `descriptor` | Región o contenido | `general`, `directa`, `zoom-inversa` |

**Trazabilidad script → imagen:** el campo `{tema}` de la imagen corresponde al descriptor del script `{PREFIJO}-gen-{tema-raíz}.py`. Así, todas las imágenes `DIO-curva-temp-*` provienen de scripts `DIO-gen-curva-temperatura*.py`.

**Metadatos:** Cada carpeta `media/generated/` contiene un archivo `image-metadata.json` con parámetros, notas de uso y contexto de cada imagen.

## Scripts Disponibles

| Script | Genera | Imágenes |
|--------|--------|----------|
| `DIO-gen-curva-iv.py` | Curva I-V del diodo + zoom inversa | `DIO-curva-iv-01-general.png`, `DIO-curva-iv-02-zoom-inversa.png` |
| `DIO-gen-curva-temperatura.py` | Efecto temperatura (combinada) | `DIO-curva-temp-01-combinada.png` |
| `DIO-gen-curva-temperatura-split.py` | Temperatura split (directa/inversa/ruptura) | `DIO-curva-temp-02-directa.png`, `DIO-curva-temp-03-inversa.png`, `DIO-curva-temp-04-ruptura.png` |
| `BJT-gen-curvas-caracteristicas.py` | Familia IC-VCE, recta de carga, regiones | `02-Transistor-BJT/media/generated/` |
| `FET-gen-curva-transferencia.py` | Transferencia, salida, autopolarización | `03-Transistor-FET/media/generated/` |
| `AMP-gen-respuesta-frecuencia.py` | Bode, comparativa EC/BC/CC, efecto RL | `04-Amplificadores/media/generated/` |
| `PRO-gen-fuente-alimentacion.py` | Rectificación, filtrado, LM317 | `05-Proyecto-Final/media/generated/` |

## Ejecución

Todos los scripts deben ejecutarse **desde la raíz del repositorio**:

```bash
python 00-META/tools/DIO-gen-curva-iv.py
python 00-META/tools/BJT-gen-curvas-caracteristicas.py
# ... etc.
```

O ejecutar todos de una vez:

```bash
for script in 00-META/tools/*.py; do python "$script"; done
```

## Dependencias

### Instaladas (requeridas)

```bash
pip install numpy matplotlib scipy
```

| Paquete | Uso actual |
|---------|-----------|
| **numpy** | Cálculos numéricos, vectorización |
| **matplotlib** | Generación de gráficas 2D |
| **scipy** | Optimización (fsolve para punto Q), filtros |

### Recomendadas para gráficos avanzados

| Paquete | Uso potencial | Instalación |
|---------|--------------|-------------|
| **plotly** | Gráficas interactivas HTML (curvas con hover, zoom dinámico) | `pip install plotly` |
| **schemdraw** | Dibujo de esquemáticos de circuitos electrónicos profesionales | `pip install schemdraw` |
| **sympy** | Cálculo simbólico (simplificación de ecuaciones, LaTeX) | `pip install sympy` |
| **lcapy** | Análisis simbólico de circuitos lineales (impedancias, transferencias) | `pip install lcapy` |
| **PySpice** | Simulación SPICE desde Python (análisis DC, AC, transitorios) | `pip install PySpice` |
| **control** | Diagramas de Bode/Nyquist precisos, análisis de estabilidad | `pip install control` |
| **SciencePlots** | Estilos matplotlib para publicaciones científicas (IEEE, Nature) | `pip install SciencePlots` |

### Ejemplo rápido — schemdraw (circuito rectificador)

```python
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    d += elm.SourceSin().label('$V_{sec}$')
    d += elm.Diode().right().label('D1')
    d += elm.Resistor().down().label('$R_L$')
    d += elm.Line().left()
    d += elm.Capacitor().up().label('C')
```

### Ejemplo rápido — plotly (curva interactiva)

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=V, y=I, name='Curva I-V'))
fig.update_layout(title='Curva del Diodo', xaxis_title='V', yaxis_title='I')
fig.write_html('curva_interactiva.html')
```

## Organización de archivos

```
00-META/tools/
├── README.md              ← Este archivo
├── DIO-gen-curva-iv.py
├── DIO-gen-curva-temperatura.py
├── DIO-gen-curva-temperatura-split.py
├── BJT-gen-curvas-caracteristicas.py
├── FET-gen-curva-transferencia.py
├── AMP-gen-respuesta-frecuencia.py
└── PRO-gen-fuente-alimentacion.py

XX-Modulo/media/generated/
├── image-metadata.json         ← Metadatos de cada imagen (parámetros, notas, contexto)
├── {PREFIJO}-{tema}-NN-*.png   ← Imágenes con nomenclatura trazable
└── ...
```

> **Regla:** Los scripts viven en `00-META/tools/`. Las imágenes generadas se guardan en el `media/generated/` de cada módulo correspondiente. Nunca mezclar scripts con imágenes. Cada carpeta `generated/` debe incluir un `image-metadata.json`.
