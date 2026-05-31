import re

input_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2-completo.md'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2-examen.md'

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract Glossary
glossary_marker = '## Glosario de Variables'
parts = text.split(glossary_marker)

glossary_table = "## Glosario de Variables\n\n| Símbolo | Nombre y Descripción |\n|---------|----------------------|\n"

if len(parts) == 2:
    glossary_text = parts[1]
    lines = glossary_text.strip().split('\n')
    for line in lines:
        m = re.match(r'^\*\s*\*\*(.*?)\*\*:\s*(.*)', line)
        if m:
            symbol = m.group(1).replace('|', r'\|')
            desc = m.group(2).replace('|', r'\|')
            glossary_table += f"| **{symbol}** | {desc} |\n"
else:
    glossary_table += "| | |\n"

# Exam sheet content
exam_content = """# Formulario de Examen: Tema 2 (Transistores BJT)

> Documento simplificado para consulta rápida en exámenes. Contiene exclusivamente fórmulas, modelos ideales/prácticos y aproximaciones estandarizadas.

---

## 1. Relaciones Fundamentales del BJT

### 1.1 Corrientes y Ganancias (DC)
* **Ley de Nodos en Transistor:**
  $$ I_E = I_C + I_B $$
* **Relaciones de Corriente Directa (Aproximación $I_{CEO} \ll \beta I_B$):**
  $$ I_C \approx \\beta I_B \\quad ; \\quad I_C \\approx \\alpha I_E $$
* **Factores de Ganancia:**
  $$ \\alpha = \\frac{\\beta}{\\beta + 1} \\quad ; \\quad \\beta = \\frac{\\alpha}{1 - \\alpha} $$

### 1.2 Ecuaciones Exactas con Fuga (Alta Temp / Ge)
* **Emisor Común:**
  $$ I_C = \\beta I_B + I_{CEO} $$
* **Base Común:**
  $$ I_C = \\alpha I_E + I_{CBO} $$
* **Relación de Fugas:**
  $$ I_{CEO} = (\\beta + 1) I_{CBO} $$

---

## 2. Modelos Físicos y Pequeña Señal

### 2.1 Ecuación de Shockley y Efecto Early
* **Corriente de Colector (Básica):**
  $$ I_C = I_S e^{\\frac{V_{BE}}{V_T}} $$
* **Efecto Early (Dependencia de $V_{CE}$):**
  $$ I_C = \\beta I_B \\left( 1 + \\frac{V_{CE}}{V_A} \\right) $$
  *(Donde $V_A$ es el Voltaje Early)*

### 2.2 Parámetros de Pequeña Señal
* **Transconductancia ($g_m$):**
  $$ g_m = \\frac{I_C}{V_T} $$
* **Resistencia Dinámica de Emisor ($r_e$):**
  $$ r_e = \\frac{V_T}{I_E} \\approx \\frac{V_T}{I_C} \\approx \\frac{26\\text{ mV}}{I_{CQ}} $$

### 2.3 Desempeño por Configuraciones (Pequeña Señal)
| Parámetro | Emisor Común (E-com) | Base Común (B-com) | Colector Común (Seguidor) |
|-----------|----------------------|--------------------|---------------------------|
| **$A_v$** | Alta ($-R_C/r_e$) | Alta | $\\approx 1$ |
| **$A_i$** | Alta ($\\beta$) | $\\approx \\alpha < 1$ | Alta ($\\beta+1$) |
| **$Z_{in}$**| Media ($\\beta r_e$) | Muy Baja | Alta |
| **$Z_{out}$**| Alta | Muy Alta | Baja |

---

## 3. Topologías de Polarización DC

### 3.1 Polarización Simple (Malla Base-Emisor)
$$ I_B = \\frac{V_{CC} - V_{BE}}{R_B} $$

### 3.2 Polarización por Divisor de Tensión (Thévenin)
Es la topología más estable térmicamente y menos dependiente de $\\beta$.
1. **Voltaje y Resistencia Thévenin:**
   $$ V_{TH} = V_{CC} \\frac{R_2}{R_1 + R_2} \\quad ; \\quad R_{TH} = R_1 \\parallel R_2 = \\frac{R_1 R_2}{R_1 + R_2} $$
2. **Corriente de Base (Malla Entrada):**
   $$ I_B = \\frac{V_{TH} - V_{BE}}{R_{TH} + (\\beta + 1) R_E} $$
3. **Voltaje Colector-Emisor (Malla Salida Exacta):**
   $$ V_{CE} = V_{CC} - I_C R_C - I_E R_E \\approx V_{CC} - I_C (R_C + R_E) $$

### 3.3 Estabilidad Térmica
* **Factor de Estabilidad:** $S = \\frac{\\partial I_C}{\\partial I_{CBO}}$
* **Criterio de Rigidez del Divisor:** Para asegurar que $V_B$ no dependa de $I_B$:
  $$ R_{TH} \\approx \\frac{(\\beta_{\\min} + 1) R_E}{10} $$

---

## 4. BJT como Interruptor (Conmutación Digital)

### 4.1 Corrientes de Conmutación
* **Corriente Máxima de Saturación (Malla Salida):**
  $$ I_{C(\\text{sat})} = \\frac{V_{CC} - V_{CE(\\text{sat})}}{R_C} \\approx \\frac{V_{CC}}{R_C} $$
* **Corriente Mínima Teórica de Base:**
  $$ I_{B(\\text{sat},\\min)} = \\frac{I_{C(\\text{sat})}}{\\beta} $$

### 4.2 Criterio de Sobrediseño (Garantía de Saturación)
Para evitar que una caída de temperatura saque al BJT de saturación, se fuerza el estado ON asumiendo una ganancia degradada:
$$ I_B \\ge \\frac{I_{C(\\text{sat})}}{\\beta_{\\text{forzado}}} \\quad \\text{donde} \\quad \\beta_{\\text{forzado}} \\approx \\frac{\\beta}{5} \\text{ o } 10 $$

---

## 5. Método de Análisis Rápido y Examen

### 5.1 Método Universal (4 Pasos)
1. **Asume** $V_{BE} \\approx 0.7\\text{ V}$.
2. **Calcula** $I_B$ en la malla de entrada $\\implies$ **Calcula** $I_C = \\beta I_B$.
3. **Calcula** $V_{CE}$ en la malla de salida.
4. **Verifica Zona:**
   * $V_{BE} < 0.7\\text{ V} \\implies$ **CORTE** ($I_C = 0$).
   * $V_C > V_B \\implies$ **ACTIVA**.
   * $V_C \\le V_B \\implies$ **SATURACIÓN** (Recalcula con $V_{CE} = 0.2\\text{ V}$ y $V_{BE} = 0.8\\text{ V}$).

### 5.2 Trazado Rápido de Recta de Carga
* **Punto 1 (Eje Y):** Haz $V_{CE} = 0 \\implies I_C = \\frac{V_{CC}}{R_C + R_E}$ (Saturación)
* **Punto 2 (Eje X):** Haz $I_C = 0 \\implies V_{CE} = V_{CC}$ (Corte)
* **Punto Q:** Sitúa $(V_{CEQ}, I_{CQ})$ obtenido del método universal sobre la línea.

### 5.3 Tabla Visual de Conmutación
| Estado | $I_B$ | $I_C$ | $V_{CE}$ | Comportamiento |
|--------|-------|-------|----------|----------------|
| **Corte** | $0$ | $0$ | $V_{CC}$ | Switch ABIERTO |
| **Activa** | Media | $\\beta I_B$ | $V_{CC} - I_C R$ | Amplificador Lineal |
| **Sat.** | Alta | $I_{C(\\text{sat})}$ | $0.2\\text{ V}$ | Switch CERRADO |

---

"""

final_text = exam_content + glossary_table

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Exam cheat sheet generated.")
