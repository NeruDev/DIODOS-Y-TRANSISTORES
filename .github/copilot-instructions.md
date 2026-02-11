# Instrucciones de Contexto para GitHub Copilot

> **Repositorio:** DIODOS-Y-TRANSISTORES  
> **Propósito:** Repositorio de conocimiento estructurado ("Jardín Digital") para la materia de Diodos y Transistores a nivel universitario (Ingeniería Electrónica).  
> **Idioma del contenido:** Español.

---

## 1. Metadatos del Proyecto

| Campo | Valor |
|-------|-------|
| Materia | Electrónica Analógica — Diodos y Transistores |
| Audiencia | Estudiantes de Ingeniería Electrónica |
| Nivel académico | Universitario |
| Idioma | Español |
| Tono | Técnico pero accesible, con analogías cuando sean útiles |
| Bibliografía principal | Boylestad & Nashelsky (11ª ed.), Sedra & Smith (7ª ed.), Malvino & Bates (7ª ed.) |

---

## 2. Arquitectura del Repositorio

```
DIODOS-Y-TRANSISTORES/
├── README.md                       → Punto de entrada del repo
├── WIKI_INDEX.md                   → Mapa de navegación centralizado
├── glossary.md                     → Glosario de ~45 términos técnicos
├── Temario.md                      → Temario oficial de la materia
├── GEMINI.md                       → Contexto para Gemini
├── .github/copilot-instructions.md → Este archivo (contexto para Copilot)
├── AUDITORIA_ESTADO_REPO.md        → Estado actual de completitud
│
├── 00-META/                        → Centro de control
│   ├── ia-contract.md              → Contrato obligatorio para IAs
│   ├── ai-directives.md            → Directivas técnicas complementarias
│   ├── nomenclatura-estandar.md    → Estándares de nomenclatura
│   ├── bibliografia-general.md     → Fuentes bibliográficas
│   ├── study-guide.md              → Guía de estudio para alumnos
│   └── tools/                      → Scripts de generación de gráficos (Python)
│
├── 01-Circuitos-Diodos/  (DIO)     → Módulo 1
├── 02-Transistor-BJT/    (BJT)     → Módulo 2
├── 03-Transistor-FET/    (FET)     → Módulo 3
├── 04-Amplificadores/    (AMP)     → Módulo 4
└── 05-Proyecto-Final/    (PRO)     → Módulo 5
```

### Estructura interna de cada módulo

```
XX-Nombre-Modulo/
├── manifest.json            → Metadatos y mapa de recursos (JSON)
├── _directives.md           → Instrucciones específicas del módulo para IA
├── [PREFIX]-00-Intro.md     → Punto de entrada del módulo
├── 00-Index.md              → Índice del módulo
├── formularios/             → Formularios de fórmulas clave
├── theory/                  → Desarrollo teórico por subtema
├── methods/                 → Procedimientos paso a paso
├── problems/                → Ejercicios
├── solutions/               → Soluciones desarrolladas
├── media/generated/         → Imágenes PNG generadas por scripts Python
└── Notas/                   → Zona sandbox (sin validación de formato)
```

---

## 3. Módulos y Prefijos

| # | Prefijo | Módulo | Carpeta | Subtemas |
|---|---------|--------|---------|----------|
| 01 | `DIO` | Circuitos con Diodos | `01-Circuitos-Diodos/` | Polarización, rectificación, recortadores, sujetadores, multiplicadores, Zener, otros diodos |
| 02 | `BJT` | Transistor Bipolar | `02-Transistor-BJT/` | Características, polarización (EC, BC, CC), conmutación, estabilidad |
| 03 | `FET` | Transistor Unipolar | `03-Transistor-FET/` | Polarización (fija, auto, divisor), MOSFET, redes combinadas |
| 04 | `AMP` | Amplificadores | `04-Amplificadores/` | Pequeña señal, amplificador BJT, amplificador JFET |
| 05 | `PRO` | Proyecto Final | `05-Proyecto-Final/` | Fuente con regulador transistorizado, fuente con regulador CI |

### Dependencias entre módulos

```
01-Diodos ──► 02-BJT ──► 04-Amplificadores ──► 05-Proyecto Final
01-Diodos ──► 03-FET ──► 04-Amplificadores ──► 05-Proyecto Final
```

---

## 4. Nomenclatura de Archivos

**Patrón:** `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `PREFIJO` | 3 letras del módulo | `DIO`, `BJT`, `FET`, `AMP`, `PRO` |
| `XX` | Número del subtema (2 dígitos) | `01`, `02`, ..., `08` |
| `Contenido` | Nombre descriptivo (PascalCase) | `Polarizacion`, `Rectificacion`, `EmComun` |
| `Tipo` | Clasificación | `Intro`, `Teoria`, `Metodos`, `Problemas`, `Respuestas`, `Soluciones`, `Resumen` |

**Ejemplos válidos:**
```
DIO-01-Teoria-Diodo.md
DIO-03-Teoria-Rectificacion-Filtrado.md
BJT-02-Teoria-Polarizacion-Emisor-Comun.md
FET-05-Teoria-Polarizacion-MOSFET.md
AMP-02-Teoria-Amplificador-BJT.md
```

---

## 5. Bloque de Metadatos Obligatorio

Todo archivo `.md` debe comenzar con un bloque HTML de metadatos:

```markdown
<!--
::METADATA::
type: [theory|method|problem|solution|reference|index|cheatsheet|answer-key]
topic_id: [id-del-tema]
file_id: [nombre-archivo-sin-extension]
status: [draft|review|stable|active]
audience: [student|ai_context|both]
last_updated: YYYY-MM-DD
-->
```

---

## 6. Formato Matemático (LaTeX)

- **Inline:** `$ expresión $` → $ V_T $
- **Bloque centrado:** `$$ expresión $$`
- Usar notación estándar de ingeniería eléctrica.

### Símbolos estándar del repositorio

| Símbolo | Notación | Descripción |
|---------|----------|-------------|
| $V_T$ | `$V_T$` | Voltaje térmico |
| $I_S$ | `$I_S$` | Corriente de saturación inversa |
| $V_{BR}$ | `$V_{BR}$` | Voltaje de ruptura |
| $V_K$ | `$V_K$` | Voltaje de umbral/rodilla |
| $V_Z$ | `$V_Z$` | Voltaje Zener |
| $\beta$ | `$\beta$` | Ganancia de corriente (BJT) |
| $g_m$ | `$g_m$` | Transconductancia |
| $r_e$ | `$r_e$` | Resistencia dinámica de emisor |
| $V_{GS}$ | `$V_{GS}$` | Voltaje compuerta-fuente (FET) |
| $I_{DSS}$ | `$I_{DSS}$` | Corriente de drenador en saturación |

### ⚠️ Precaución con LaTeX en terminal/bash

Al generar contenación automáticamente con comandos como `cat >> archivo <<EOF`, usar **comillas simples** en el delimitador heredoc (`'EOF'`) para evitar que bash interprete `$` como variables de entorno y destruya las fórmulas LaTeX.

```bash
# CORRECTO:
cat >> archivo.md <<'EOF'
El voltaje térmico es $V_T$
EOF

# INCORRECTO (destruye LaTeX):
cat >> archivo.md <<EOF
El voltaje térmico es $V_T$
EOF
```

---

## 7. Herramientas de Generación de Gráficos (Python)

### Ubicación y convención

Los scripts de Python viven en `00-META/tools/` y siguen el patrón:

```
[PREFIJO]-gen-[descripción].py
```

Las imágenes generadas (formato **PNG**) se guardan en el directorio `media/generated/` del módulo correspondiente. **Nunca** mezclar scripts con imágenes.

### Scripts disponibles

| Script | Qué genera | Directorio de salida |
|--------|-----------|---------------------|
| `DIO-gen-curva-iv.py` | Curva I-V del diodo + zoom región inversa | `01-Circuitos-Diodos/media/generated/` |
| `DIO-gen-curva-temperatura.py` | Efecto de temperatura en el diodo (combinada) | `01-Circuitos-Diodos/media/generated/` |
| `DIO-gen-curva-temperatura-split.py` | Temperatura split (directa/inversa/ruptura) | `01-Circuitos-Diodos/media/generated/` |
| `BJT-gen-curvas-caracteristicas.py` | Familia IC-VCE, recta de carga, regiones | `02-Transistor-BJT/media/generated/` |
| `FET-gen-curva-transferencia.py` | Transferencia, salida, autopolarización | `03-Transistor-FET/media/generated/` |
| `AMP-gen-respuesta-frecuencia.py` | Bode, comparativa EC/BC/CC, efecto RL | `04-Amplificadores/media/generated/` |
| `PRO-gen-fuente-alimentacion.py` | Rectificación, filtrado, regulador LM317 | `05-Proyecto-Final/media/generated/` |
| `DIO-gen-esquematico-pequena-senal.py` | Esquemáticos de circuitos (DC, AC, pequeña señal) con schemdraw + gráfica de linealización | `01-Circuitos-Diodos/media/generated/` |

### Ejecución

Todos los scripts **deben ejecutarse desde la raíz del repositorio**:

```bash
# Un script individual:
python 00-META/tools/DIO-gen-curva-iv.py

# Todos los scripts:
for script in 00-META/tools/*.py; do python "$script"; done
```

### Dependencias Python (requeridas)

```bash
pip install numpy matplotlib scipy schemdraw lcapy sympy SciencePlots
```

| Paquete | Uso |
|---------|-----|
| **numpy** | Cálculos numéricos, vectorización de ecuaciones |
| **matplotlib** | Generación de gráficas 2D, exportación a PNG |
| **scipy** | Optimización (`fsolve` para punto Q), filtros |
| **schemdraw** | Dibujo programático de esquemáticos de circuitos electrónicos. Genera PNG directamente vía matplotlib. Soporta 46 elementos semiconductores: `Diode`, `Zener`, `Schottky`, `Varactor`, `LED`, `BjtNpn`, `BjtPnp`, `JFetN`, `JFetP`, `NFet`, `PFet`, `NMos`, `PMos`, `IgbtN`, `SCR`, `Triac`, `Diac`, etc. |
| **lcapy** | Análisis simbólico de circuitos lineales (impedancias, Laplace, Fourier). Generación de esquemáticos vía circuitikz (requiere LaTeX para dibujos) |
| **sympy** | Cálculo simbólico, simplificación de ecuaciones, derivadas |
| **SciencePlots** | Estilos matplotlib para publicaciones científicas (`science`, `ieee`, `nature`). Usar con `plt.style.context(['science', 'no-latex'])` |

### Dependencias Python (recomendadas/opcionales)

| Paquete | Uso potencial |
|---------|--------------|
| **plotly** | Gráficas interactivas HTML |
| **PySpice** | Simulación SPICE desde Python |
| **control** | Diagramas de Bode/Nyquist precisos |

### Patrón estándar de un script de generación

```python
"""
[PREFIJO]-gen-[descripcion].py
───────────────────
Descripción breve de lo que genera.

Salida:
  - XX-Modulo/media/generated/nombre_imagen.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/[PREFIJO]-gen-[descripcion].py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Directorio de salida (relativo a la raíz del repo)
OUTPUT_DIR = os.path.join("XX-Modulo", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ... lógica de generación ...

plt.savefig(os.path.join(OUTPUT_DIR, 'nombre_imagen.png'), dpi=100)
print("Generada: nombre_imagen.png")
```

### Patrón para esquemáticos con schemdraw

```python
import schemdraw
import schemdraw.elements as elm
import os

OUTPUT_DIR = os.path.join("XX-Modulo", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Esquemático básico con diodo
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'nombre.png'),
                       show=False, dpi=150) as d:
    d += elm.SourceV().up().label('$V_{in}$')
    d += elm.Resistor().right().label('$R$')
    d += elm.Diode().down().label('$D$')
    d += elm.Line().left()

# Esquemático con BJT
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'bjt.png'),
                       show=False, dpi=150) as d:
    d += (Q := elm.BjtNpn().label('$Q_1$'))
    d += elm.Resistor().at(Q.collector).up().label('$R_C$')
    d += elm.Resistor().at(Q.base).left().label('$R_B$')
    d += elm.Resistor().at(Q.emitter).down().label('$R_E$')
    d += elm.Ground()
```

### Directivas técnicas para gráficos

- **Escalas dispares:** Componentes electrónicos tienen zonas con magnitudes extremadamente diferentes (ej. Amperios en directa vs. Nanoamperios en inversa). Usar gráficas separadas o insets (gráficas insertadas) para manejar esto; nunca una sola escala lineal.
- **Ecuación de Shockley:** Incluir el término de ruptura si se desea visualizar el diodo completo: `i_breakdown = -Is * np.exp(-(V - Vbr) / (n * Vt))`
- **Formato de salida:** PNG a 100 DPI como mínimo.
- **Estilo:** Incluir grid, etiquetas de ejes, título, leyenda y anotaciones de las regiones de operación.

---

## 8. Reglas de Generación de Contenido

### Reglas generales

1. **SIEMPRE** dar contexto antes de resolver un problema.
2. Usar notación estándar según `nomenclatura-estandar.md`.
3. Validar contra la bibliografía en `bibliografia-general.md`.
4. Formato de soluciones: paso a paso con explicación de cada operación y unidades.
5. Nunca inventar datos; solo usar valores realistas de componentes electrónicos.

### Al generar contenido Markdown

- Seguir el patrón de nomenclatura `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`.
- Incluir el bloque `::METADATA::` al inicio del archivo.
- Incluir header de navegación estándar:
  ```markdown
  > 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)
  ```

### Al generar gráficas

- Crear o modificar un script Python en `00-META/tools/`.
- Las imágenes se guardan en `media/generated/` del módulo correspondiente.
- **Prohibido** añadir imágenes de fuentes externas o creadas con editores gráficos manuales.
- Si se necesita una nueva ilustración, se debe crear un script Python para generarla.
- Documentar los parámetros usados en el script.

### Al generar esquemáticos de circuitos

- Usar **schemdraw** como herramienta principal para diagramas de circuitos.
- Usar `show=False` en `schemdraw.Drawing()` para entorno sin GUI.
- Usar `dpi=150` mínimo para calidad legible.
- Anclar elementos semiconductores con sus terminales: `Q.collector`, `Q.base`, `Q.emitter`, `J.gate`, `J.drain`, `J.source`.
- Para etiquetas LaTeX: `elm.Resistor().label('$R_C$')`.
- Incluir `elm.Ground()` para indicar referencia.

### Sintaxis de enlaces internos

| Tipo | Sintaxis |
|------|----------|
| Mismo directorio | `[Intro](DIO-01-Intro.md)` |
| Subdirectorio | `[Teoría](theory/DIO-01-Teoria.md)` |
| Al glosario | `[término](../../glossary.md#termino)` |
| Entre módulos | `[Tema](../02-Transistor-BJT/01-Caracteristicas/)` |

---

## 9. Zona Sandbox (Notas/)

Cada módulo contiene una carpeta `Notas/` que es **zona libre**:

- **NO** validar nomenclatura ni formato.
- **NO** sugerir correcciones de estilo.
- **LEER COMPLETO** si se solicita contexto.
- Cualquier archivo, cualquier formato.

---

## 10. Tareas Permitidas y Prohibidas

| Tarea | Estado | Notas |
|-------|--------|-------|
| Explicar conceptos | ✅ Permitida | Con contexto y ejemplos |
| Generar problemas | ✅ Permitida | Indicar dificultad |
| Verificar soluciones | ✅ Permitida | Paso a paso |
| Generar gráficas | ✅ Permitida | Python + matplotlib, guardar PNG |
| Crear resúmenes | ✅ Permitida | Con fórmulas clave |
| Modificar Notas/ | ⛔ Restringida | Zona sandbox exenta de validación |
| Inventar datos | ⛔ Prohibida | Solo valores realistas de componentes |

---

## 11. Flujo de Trabajo Recomendado

1. Consultar `manifest.json` del módulo objetivo para conocer el mapa de recursos.
2. Consultar `_directives.md` del módulo para instrucciones específicas.
3. Revisar el estado del contenido en `AUDITORIA_ESTADO_REPO.md`.
4. Generar contenido siguiendo las reglas de este documento.
5. Si se generan gráficas: crear/modificar script en `00-META/tools/`, ejecutar desde la raíz, verificar que las imágenes PNG se guarden en `media/generated/` del módulo correcto.

---

## 12. Documentos de Referencia Clave

| Documento | Propósito |
|-----------|-----------|
| [00-META/ia-contract.md](00-META/ia-contract.md) | Contrato obligatorio para toda IA |
| [00-META/ai-directives.md](00-META/ai-directives.md) | Directivas técnicas (escalas, LaTeX en bash) |
| [00-META/nomenclatura-estandar.md](00-META/nomenclatura-estandar.md) | Estándares de nomenclatura completos |
| [00-META/bibliografia-general.md](00-META/bibliografia-general.md) | Fuentes bibliográficas válidas |
| [00-META/tools/README.md](00-META/tools/README.md) | Documentación de los scripts Python |
| [glossary.md](glossary.md) | Glosario de términos técnicos |
| [Temario.md](Temario.md) | Temario oficial de la materia |
| [AUDITORIA_ESTADO_REPO.md](AUDITORIA_ESTADO_REPO.md) | Estado de completitud del repo |
