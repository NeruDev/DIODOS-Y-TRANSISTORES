import re

input_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1-completo.md'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1-examen.md'

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
exam_content = """# Formulario de Examen: Tema 1 (Diodos y Rectificadores)

> Documento simplificado para consulta rápida en exámenes. Contiene exclusivamente fórmulas, modelos ideales/prácticos y aproximaciones estandarizadas.

---

## 1. Análisis DC y Pequeña Señal

### 1.1 Modelo del Diodo en DC
* **Ecuación de Shockley:**
  $$ I_D = I_S \\left( e^{\\frac{V_D}{n V_T}} - 1 \\right) $$
* **Voltaje Térmico ($V_T$):**
  $$ V_T = \\frac{k T}{q} \\approx 25\\text{ mV a } 26\\text{ mV} \\quad \\text{(a temp. ambiente)} $$
* **LVK (Malla Simple):**
  $$ V_{in} - I_D R - V_D = 0 $$
* **Puntos de la Recta de Carga:**
  * Eje Y (Corto, $V_D=0$): $I_D = \\frac{V_{in}}{R}$
  * Eje X (Abierto, $I_D=0$): $V_D = V_{in}$

### 1.2 Pequeña Señal (AC)
* **Resistencia Dinámica ($r_d$):**
  $$ r_d \\approx \\frac{n V_T}{I_{DQ}} $$
* **Criterio de Pequeña Señal:**
  $$ \\hat{v}_d \\ll n V_T \\quad \\text{(Criterio práctico: } \\hat{v}_d < 5\\text{ mV o } 10\\text{ mV)} $$
* **Componentes de Señal Mixta:**
  $$ i_D(t) = I_{DQ} + \\frac{V_m}{R + r_d} \\sin(\\omega t) $$

---

## 2. Rectificadores

### 2.1 Transformador
* **Voltaje RMS y Pico del Secundario:**
  $$ V_{rms(\\text{sec})} = \\frac{N_s}{N_p} V_{rms(\\text{pri})} \\quad ; \\quad V_{s,\\text{pico}} = \\sqrt{2} V_{rms(\\text{sec})} $$

### 2.2 Rectificador de Media Onda
* **Voltaje Pico en Carga ($V_{o,m}$):**
  $$ V_{o,m} = V_{s,\\text{pico}} - V_D \\quad \\text{(Ideal: } V_D = 0\\text{V; Real: } V_D \\approx 0.7\\text{V)} $$
* **Componente DC (Promedio):**
  $$ V_{DC} = \\frac{V_{o,m}}{\\pi} \\approx 0.318 V_{o,m} $$
* **Componente RMS (Eficaz):**
  $$ V_{rms} = \\frac{V_{o,m}}{2} = 0.500 V_{o,m} $$
* **Eficiencia Máxima ($\\eta$):** $\\approx 40.6\\%$
* **Voltaje Inverso de Pico (PIV):**
  $$ \\text{PIV} \\approx V_m $$

### 2.3 Rectificador de Onda Completa (Derivación Central)
* **Voltaje Pico en Carga ($V_{o,m}$):**
  $$ V_{o,m} = V_m - V_D $$
* **Componente DC (Promedio):**
  $$ V_{DC} = \\frac{2 V_{o,m}}{\\pi} \\approx 0.636 V_{o,m} $$
* **Componente RMS (Eficaz):**
  $$ V_{rms} = \\frac{V_{o,m}}{\\sqrt{2}} \\approx 0.707 V_{o,m} $$
* **Eficiencia Máxima ($\\eta$):** $\\approx 81.2\\%$
* **Voltaje Inverso de Pico (PIV por diodo):**
  $$ \\text{PIV} \\approx 2 V_m $$

### 2.4 Rectificador de Onda Completa (Puente)
* **Voltaje Pico en Carga ($V_{o,m}$):** Conducen 2 diodos en serie.
  $$ V_{o,m} = V_m - 2V_D $$
* **Componente DC y RMS:** Mismas fórmulas que la derivación central.
* **Eficiencia Máxima ($\\eta$):** $\\approx 81.2\\%$
* **Voltaje Inverso de Pico (PIV por diodo):**
  $$ \\text{PIV} \\approx V_m $$

---

## 3. Rizo y Filtros (Series de Fourier)

### 3.1 Factor de Rizo ($FR$)
$$ FR = \\frac{V_{r(rms)}}{V_{DC}} \\times 100\\% $$

### 3.2 Serie de Fourier (Onda Completa Ideal sin filtro)
$$ v_o(t) = \\frac{2 V_m}{\\pi} - \\frac{4 V_m}{\\pi} \\sum_{n=1}^{\\infty} \\frac{\\cos(2n\\omega t)}{4n^2 - 1} $$
* **Frecuencia del rizo:** $f_{\\text{rizo}} = 2 f_{\\text{in}}$ (Onda Completa), $f_{\\text{rizo}} = f_{\\text{in}}$ (Media Onda).

### 3.3 Filtro Capacitivo de Entrada
* **Voltaje de Rizo (Aproximación lineal):**
  $$ V_{r(pp)} \\approx \\frac{V_{o,m}}{f_{\\text{rizo}} R_L C} $$
* **Voltaje DC Filtrado:**
  $$ V_{DC} \\approx V_{o,m} - \\frac{V_{r(pp)}}{2} $$
* **Criterios de Atenuación Rápida:**
  * $C \\uparrow \\implies FR \\downarrow$
  * $f \\uparrow \\implies FR \\downarrow$
  * $R_L \\downarrow \\implies FR \\uparrow$ (Carga pesada aumenta el rizo).

---

## 4. Diodos de Propósito Especial

### 4.1 Diodo Zener (Regulación de Voltaje)
* **Condición Estricta de Regulación:**
  $$ I_{Z(\\min)} < I_Z < I_{Z(\\max)} $$
  * $I_{Z(\\max)} = \\frac{P_{Z(\\max)}}{V_Z}$
* **Regulación de Línea:**
  $$ \\%Reg = \\frac{V_{NL} - V_{FL}}{V_{FL}} \\times 100\\% $$

### 4.2 Circuitos Clásicos
* **Sujetadores (Clampers):** Desplazan el nivel DC.
  $$ v_o(t) \\approx v_i(t) \\pm V_m $$
  * Condición de diseño: $RC \\gg T$
* **Multiplicadores de Voltaje:**
  $$ V_o \\approx n \\cdot V_m \\quad \\text{(Aproximación sin carga)} $$
* **Diodo Schottky:** Alta velocidad de conmutación.
  $$ V_D \\approx 0.2\\text{ V} - 0.3\\text{ V} $$
* **Diodo Varactor:** Capacitancia variable controlada por voltaje inverso ($V_R$).
  $$ C_j \\propto \\frac{1}{(V_R)^n} $$

---

## 5. Método de Análisis Rápido (Estado DC)
1. **Asumir:** ON ($0.7\\text{ V}$) u OFF (Circuito abierto).
2. **Resolver:** Ecuaciones de malla o nodo.
3. **Verificar:**
   * Si asumiste ON $\\implies I_D$ debe ser $> 0$.
   * Si asumiste OFF $\\implies V_D$ debe ser $< 0.7\\text{ V}$.

---

"""

final_text = exam_content + glossary_table

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Exam cheat sheet generated.")
