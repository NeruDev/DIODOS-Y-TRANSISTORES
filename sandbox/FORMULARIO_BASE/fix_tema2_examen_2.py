import re

filepath = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2-examen.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add missing DC topologies
topologies_old = r"### 3.4 Análisis Rápido sin $\beta$ (Aproximación Práctica)"
topologies_new = r"""### 3.4 Polarización por Realimentación de Colector
Proporciona estabilidad contra variaciones de $\beta$ al conectar $R_B$ directamente al colector.
* **Corriente de Base:**
  $$ I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)} $$
* **Voltaje Colector-Emisor:**
  $$ V_{CE} = V_{CC} - I_C(R_C + R_E) $$

### 3.5 Base Común en DC
Normalmente utiliza dos fuentes de alimentación ($V_{EE}$ y $V_{CC}$).
* **Corriente de Emisor (Malla de entrada):**
  $$ I_E = \frac{V_{EE} - V_{BE}}{R_E} $$
* **Voltaje Colector-Base (Malla de salida):**
  $$ V_{CB} = V_{CC} - I_C R_C $$

### 3.6 Colector Común en DC / Seguidor de Emisor
No lleva resistencia de colector ($R_C = 0$). El colector va directo a $V_{CC}$.
* **Corriente de Base:**
  $$ I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1) R_E} $$
* **Voltaje Colector-Emisor:**
  $$ V_{CE} = V_{CC} - I_E R_E $$

### 3.7 Análisis Rápido sin $\beta$ (Aproximación Práctica)"""

text = text.replace(topologies_old, topologies_new)

# 2. Renumber Diseño Óptimo
optimo_old = r"### 3.5 Diseño Óptimo"
optimo_new = r"### 3.8 Diseño Óptimo"
text = text.replace(optimo_old, optimo_new)

# 3. Add Stability section before Section 5
metodo_old = r"## 5. Método de Análisis Rápido y Examen"

estabilidad_new = r"""## 5. Estabilidad Térmica ($S$)

> Mide la sensibilidad de la corriente de colector ($I_C$) ante variaciones de temperatura (específicamente por cambios en la corriente de fuga $I_{CBO}$). Un $S$ menor indica un circuito más estable.

* **Fórmula General de Estabilidad:**
  $$ S = \frac{\beta + 1}{1 - \beta \left( \frac{\partial I_B}{\partial I_C} \right)} $$

* **Comparativa de Estabilidad por Topología:**
| Topología | Factor $S$ (Aproximado) | Nivel de Estabilidad |
| --- | --- | --- |
| **Polarización Fija** | $S \approx \beta + 1$ | **Pésima** (Altamente inestable) |
| **Realimentación de Colector** | $S \approx \frac{\beta + 1}{1 + \beta \left( \frac{R_C}{R_C + R_B} \right)}$ | **Media** |
| **Divisor de Tensión (Thévenin)** | $S \approx \frac{\beta + 1}{1 + \beta \frac{R_E}{R_{TH} + R_E}} \approx 1 + \frac{R_{TH}}{R_E}$ | **Excelente** (Si $R_{TH} \ll R_E$) |

---

## 6. Método de Análisis Rápido y Examen"""

text = text.replace(metodo_old, estabilidad_new)

# 4. Renumber subsections of the old section 5 to section 6
text = text.replace(r"### 5.1 Método Universal", r"### 6.1 Método Universal")
text = text.replace(r"### 5.2 Trazado Rápido", r"### 6.2 Trazado Rápido")
text = text.replace(r"### 5.3 Tabla Visual", r"### 6.3 Tabla Visual")

# 5. Remove BV_{CEO} from glossary
glossary_item = r"| **$BV_{CEO}$** | Voltaje de ruptura colector-emisor con base en circuito abierto (V). |\n"
text = text.replace(glossary_item, "")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Tema 2 Exam Form updated successfully.")
