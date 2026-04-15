# Herramientas de Generación

> Carpeta centralizada para scripts de Python que generan las imágenes del repositorio.

---

## Requisitos de Entorno (GUI)

Para ejecutar scripts que requieren interfaz gráfica (`tkinter`), es necesario configurar la redirección del Display hacia el servidor VNC.

**Comando obligatorio antes de ejecutar cualquier script GUI:**
```bash
export DISPLAY=:1
```

> Este comando configura la sesión actual de la terminal. Debe ejecutarse cada vez que se abre una terminal nueva si no se ha añadido globalmente al archivo `.bashrc`.

### Calculadoras Interactivas

| Script | Descripción | Comando |
|--------|-------------|---------|
| `practica1_calculadora.py` | Cálculo y validación gráfica para Práctica 1 (Diodos) | `python "topics/01-circuitos-diodos/Notas/PRACTICA 1/practica1_calculadora.py"` |

*Visualizar a través del puerto "Desktop" o "noVNC" en la pestaña "Puertos / Ports" de VS Code.*

---

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
| `DIO-gen-duplicador-voltaje.py` | Duplicador de voltaje (layout vertical) | `duplicador-voltaje.png` |
| `DIO-gen-duplicador-voltaje-horizontal.py` | Duplicador de voltaje (layout L→R, **estándar H3**) | `duplicador-voltaje-h1.png`, `duplicador-voltaje-h2.png`, `duplicador-voltaje-h3.png` |
| `DIO-gen-curva-zener.py` | Curva característica I-V del diodo Zener | `DIO-curva-zener-01-iv.png`, `DIO-curva-zener-02-zoom.png` |
| `DIO-gen-zener-regulador.py` | Esquema básico de regulador Zener | `DIO-esquema-zener-regulador.png` |
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
| **pygraphviz** | Diagramas de bloques con ruteo automatico (Graphviz) | `pip install pygraphviz` |
| **control** | Diagramas de Bode/Nyquist precisos, análisis de estabilidad | `pip install control` |
| **SciencePlots** | Estilos matplotlib para publicaciones científicas (IEEE, Nature) | `pip install SciencePlots` |

### Dependencias del sistema (para herramientas avanzadas)

- **Lcapy:** requiere `pdflatex` y utilidades de conversion (recomendado `texlive-latex-base`, `texlive-pictures`, `dvisvgm`, `ghostscript`).
- **PySpice:** requiere `ngspice`.
- **pygraphviz:** requiere `graphviz` y `libgraphviz-dev`.

Ejemplo en Debian/Codespaces:
```bash
sudo apt-get update
sudo apt-get install -y ngspice graphviz libgraphviz-dev texlive-latex-base texlive-pictures dvisvgm ghostscript
```

> Nota: `pdflatex` es una dependencia del sistema (no una extension de VS Code). Las extensiones solo mejoran la edicion y previsualizacion.

### Matriz de herramientas

| Herramienta | Estetica | Facilidad | Transistores | Uso ideal |
|-------------|----------|-----------|--------------|-----------|
| **schemdraw** | Media | Alta | Basicos | Diagramas rapidos en Markdown |
| **Lcapy** | Excelente | Media | Avanzados | Material tipo libro y teoria formal |
| **PySpice** | N/A | Baja | Reales | Validacion con modelos de fabricante |
| **Graphviz (pygraphviz)** | Alta | Media | N/A | Diagramas de bloques y ruteo automatico |

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

## Estándar H3 para Circuitos Complejos

Para esquemáticos de circuitos con múltiples componentes (multiplicadores, fuentes reguladas, amplificadores), se recomienda el **estándar H3**:

### Parámetros técnicos H3

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `unit_size` | 3.5 | Espaciado amplio entre componentes |
| `comp_length` | 3.5 | Longitud de componentes |
| `separation` | 2.0 | Separación entre secciones |
| `fontsize` | 13 | Tamaño de etiquetas |
| `dpi` | 300 | Resolución de imagen |

### Layout horizontal (flujo L→R)

- **Línea superior única:** conexiones de nodos positivos
- **Línea inferior única:** referencia a tierra (GND)

### Paleta de colores didácticos

```python
COLOR_FUENTE = '#2563EB'       # Azul - fuentes AC/DC y transformadores
COLOR_DIODO = '#DC2626'        # Rojo - diodos y semiconductores
COLOR_CAPACITOR = '#16A34A'    # Verde - capacitores
COLOR_RESISTOR = '#EA580C'     # Naranja - resistencias
COLOR_CONEXION = '#374151'     # Gris oscuro - líneas, nodos y tierra
COLOR_VOLTAJE = '#7C3AED'      # Violeta - indicadores de voltaje
COLOR_NODO = '#111827'         # Negro - puntos de nodo
```

### Reglas de posicionamiento de etiquetas

**CRÍTICO:** Las etiquetas **NUNCA** deben solaparse con líneas de conexión ni componentes.

| Ubicación | Técnica recomendada |
|-----------|---------------------|
| Línea superior | `loc='top'` con `ofst=0.3` |
| Línea inferior | Coordenadas absolutas `(x - 0.5, y)` |
| Voltajes | Espacio libre, nunca sobre componentes |

```python
# Ejemplo: etiqueta desplazada para evitar solapamiento con GND
d += elm.Label().at((nodo_B[0] - 0.5, nodo_B[1])).label('B')
```

> **Referencia:** Ver `DIO-gen-duplicador-voltaje-horizontal.py` como implementación de ejemplo del estándar H3.

### Ejemplo rápido — plotly (curva interactiva)

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=V, y=I, name='Curva I-V'))
fig.update_layout(title='Curva del Diodo', xaxis_title='V', yaxis_title='I')
fig.write_html('curva_interactiva.html')
```

## Organización de archivos

## Política de reemplazo y limpieza

- Si una imagen nueva reemplaza a otra existente, la imagen anterior debe eliminarse del repositorio cuando ya no tenga uso.
- Antes de eliminar, actualizar enlaces y referencias en `.md`, scripts y metadatos asociados.
- Después del reemplazo, verificar que `media/generated/` no conserve archivos huérfanos.

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
