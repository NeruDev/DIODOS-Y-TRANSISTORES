import re

filepath = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_3-examen.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Section 2 completely
old_section_2 = r"""## 2. Configuraciones de Polarización (DC)

### 2.1 Polarización Fija
* **Malla de Entrada:** $V_{GS} = -V_{GG}$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D R_D$

### 2.2 Autopolarización
* **Malla de Entrada:** $V_{GS} = -I_D R_S$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D (R_D + R_S)$

### 2.3 Polarización por Divisor de Voltaje
* **Voltaje en la Compuerta ($V_G$):**
  $$ V_G = V_{DD} \frac{R_2}{R_1 + R_2} $$
  *(Aproximación universalmente válida en DC gracias a que $I_G \approx 0$)*
* **Malla de Entrada:** $V_{GS} = V_G - I_D R_S$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D (R_D + R_S)$

### 2.4 Diseño Óptimo Lineal
Para máxima excursión simétrica (Punto Q central):
$$ V_{DSQ} \approx \frac{V_{DD}}{2} $$"""

new_section_2 = r"""## 2. Configuraciones de Polarización (DC)

### 2.1 Polarización Fija
* **Malla de Entrada:** $V_{GS} = -V_{GG}$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D R_D$

### 2.2 Autopolarización (JFET / D-MOSFET)
* **Malla de Entrada:** $V_{GS} = -I_D R_S$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D (R_D + R_S)$
* **Solución Analítica Exacta (Fórmula General):**
  Al sustituir en Shockley resulta $A I_D^2 + B I_D + C = 0$:
  $$ A = R_S^2, \quad B = -\left[2 R_S |V_P| + \frac{V_P^2}{I_{DSS}}\right], \quad C = V_P^2 $$
  *Raíz física correcta:* $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$
* **Diseño Exacto de $R_S$ para un Punto Q:**
  $$ R_S = \frac{|V_P|}{I_{DQ}} \left( 1 - \sqrt{\frac{I_{DQ}}{I_{DSS}}} \right) $$

### 2.3 Polarización por Divisor de Voltaje
* **Voltaje en la Compuerta ($V_G$):**
  $$ V_G = V_{DD} \frac{R_2}{R_1 + R_2} $$
  *(Aproximación universalmente válida en DC gracias a que $I_G \approx 0$)*
* **Malla de Entrada:** $V_{GS} = V_G - I_D R_S$
* **Malla de Salida:** $V_{DS} = V_{DD} - I_D (R_D + R_S)$
* **Solución Analítica Exacta (JFET / D-MOSFET):**
  $$ A = R_S^2, \quad B = -\left[2 (|V_P| + |V_G|) R_S + \frac{V_P^2}{I_{DSS}}\right], \quad C = (|V_P| + |V_G|)^2 $$
  *Raíz física correcta:* $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$
* **Diseño para Estabilización del Punto Q (JFET):**
  Para contrarrestar tolerancias de fabricación (entre $I_{D1}$ e $I_{D2}$):
  $$ |V_G| = \frac{I_{D1}(|V_{GS2}| - |V_{GS1}|)}{I_{D2} - I_{D1}} - |V_{GS1}| \quad ; \quad R_S = \frac{|V_{GS1}| - |V_{GS2}|}{I_{D2} - I_{D1}} $$

### 2.4 Realimentación de Drenador (Solo E-MOSFET)
Asegura que el dispositivo opere siempre en zona de saturación (activa).
* **Mallas del circuito:**
  $$ V_{GS} = V_{DS} \quad ; \quad V_G = V_D $$
  $$ V_{DS} = V_{DD} - I_D R_D $$

### 2.5 Diseño Óptimo Lineal
Para máxima excursión simétrica (Punto Q central):
$$ V_{DSQ} \approx \frac{V_{DD}}{2} $$"""

text = text.replace(old_section_2, new_section_2)

# Also adding a quick fix to method steps (Step 4) to tell the user they can use the exact formulas
old_step_4 = r"""4. **Calcula** $I_D$ usando Shockley o la ecuación $k$ del E-MOSFET. (Resuelve la cuadrática y escoge la raíz físicamente posible: para JFET canal N, $V_P < V_{GS} < 0$)."""
new_step_4 = r"""4. **Calcula** $I_D$ usando Shockley (o la ecuación $k$ para E-MOSFET). Aplica las fórmulas analíticas exactas (Sección 2) o traza la recta de carga sobre la curva universal."""

text = text.replace(old_step_4, new_step_4)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Theoretical formulas injected successfully.")
