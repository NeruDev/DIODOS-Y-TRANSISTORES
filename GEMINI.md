# Contexto del Repositorio: DIODOS-Y-TRANSISTORES

Este repositorio está dedicado al estudio de dispositivos electrónicos fundamentales: diodos y transistores. El contenido está diseñado para estudiantes de ingeniería electrónica y carreras afines.

## Metadatos

- **Título:** Curso de Diodos y Transistores
- **Audiencia:** Estudiantes de Ingeniería Electrónica
- **Idioma:** Español
- **Materia:** Electrónica Analógica
- **Palabras Clave:** Diodos, Transistores, BJT, FET, Amplificadores, Circuitos Electrónicos

## Generación de Contenido Gráfico

Todas las imágenes, gráficas y visualizaciones utilizadas para ilustrar los conceptos teóricos en este repositorio deben ser generadas a través de los scripts de Python que se encuentran en el directorio `00-META/tools/`.

Esto asegura la consistencia, precisión y reproducibilidad del material gráfico. Queda prohibido añadir imágenes de fuentes externas o creadas con herramientas de edición gráfica manual. Si se requiere una nueva ilustración, se debe crear o modificar un script de Python para generarla.

## Herramientas Python Instaladas

El repositorio cuenta con las siguientes librerías Python para generación de contenido gráfico y cálculo:

### Dependencias base (requeridas)

| Paquete | Uso |
|---------|-----|
| **numpy** | Cálculos numéricos, vectorización de ecuaciones |
| **matplotlib** | Generación de gráficas 2D (curvas I-V, Bode, etc.), exportación a PNG |
| **scipy** | Optimización (`fsolve` para punto Q), filtros |

### Herramientas de esquemáticos y cálculo (instaladas)

| Paquete | Uso | Elementos semiconductores |
|---------|-----|---------------------------|
| **schemdraw** | Dibujo programático de esquemáticos de circuitos. Genera PNG directamente vía matplotlib | 46 elementos: `Diode`, `Zener`, `Schottky`, `Varactor`, `LED`, `BjtNpn`, `BjtPnp`, `JFetN`, `JFetP`, `NFet`, `PFet`, `NMos`, `PMos`, `IgbtN`, `IgbtP`, `SCR`, `Triac`, `Diac`, etc. |
| **lcapy** | Análisis simbólico de circuitos lineales (impedancias, Laplace, Fourier). Esquemáticos vía circuitikz (requiere LaTeX) | Diodos, BJT (NPN/PNP), JFET, MOSFET |
| **sympy** | Cálculo simbólico: simplificación de ecuaciones, derivadas, la ecuación de Shockley en forma simbólica | N/A (matemáticas puras) |
| **SciencePlots** | Estilos matplotlib para publicaciones científicas (`science`, `ieee`, `nature`) | N/A (estilos visuales) |

### Uso de schemdraw (herramienta principal para esquemáticos)

```python
import schemdraw
import schemdraw.elements as elm

# Circuito básico con diodo
with schemdraw.Drawing(file='salida.png', show=False) as d:
    d += elm.SourceV().up().label('$V_{in}$')
    d += elm.Resistor().right().label('$R$')
    d += elm.Diode().down().label('$D$')
    d += elm.Line().left()

# Circuito con BJT
with schemdraw.Drawing(file='bjt.png', show=False) as d:
    d += (Q := elm.BjtNpn().label('$Q_1$'))
    d += elm.Resistor().at(Q.collector).up().label('$R_C$')
    d += elm.Resistor().at(Q.base).left().label('$R_B$')
    d += elm.Resistor().at(Q.emitter).down().label('$R_E$')
    d += elm.Ground()
```

### Al generar esquemáticos

- Crear script en `00-META/tools/` con convención `[PREFIJO]-gen-[descripción].py`.
- Guardar PNGs en `media/generated/` del módulo correspondiente.
- Usar `show=False` en `schemdraw.Drawing()` para entorno sin GUI.
- Usar `dpi=150` mínimo para calidad legible.
- Documentar los parámetros del circuito en el docstring del script.
