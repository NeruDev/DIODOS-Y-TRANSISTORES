import re

filepath = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_3-examen.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Exact Analytic Solution for E-MOSFET to Section 2.3
div_voltage_old = r"""* **Diseño para Estabilización del Punto Q (JFET):**
  Para contrarrestar tolerancias de fabricación (entre $I_{D1}$ e $I_{D2}$):
  $$ |V_G| = \frac{I_{D1}(|V_{GS2}| - |V_{GS1}|)}{I_{D2} - I_{D1}} - |V_{GS1}| \quad ; \quad R_S = \frac{|V_{GS1}| - |V_{GS2}|}{I_{D2} - I_{D1}} $$"""

div_voltage_new = r"""* **Diseño para Estabilización del Punto Q (JFET):**
  Para contrarrestar tolerancias de fabricación (entre $I_{D1}$ e $I_{D2}$):
  $$ |V_G| = \frac{I_{D1}(|V_{GS2}| - |V_{GS1}|)}{I_{D2} - I_{D1}} - |V_{GS1}| \quad ; \quad R_S = \frac{|V_{GS1}| - |V_{GS2}|}{I_{D2} - I_{D1}} $$
* **Solución Analítica Exacta (E-MOSFET):**
  Sustituyendo la malla de entrada en la ecuación de $k$:
  $$ A = k R_S^2, \quad B = -\left[2 k R_S (V_G - V_{GS(Th)}) + 1\right], \quad C = k (V_G - V_{GS(Th)})^2 $$
  *Raíz física correcta:* Generalmente, para E-MOSFET se toma la raíz que asegure $V_{GS} > V_{GS(Th)}$."""

text = text.replace(div_voltage_old, div_voltage_new)

# 2. Add Exact Analytic Solution for E-MOSFET to Section 2.4
drain_fb_old = r"""### 2.4 Realimentación de Drenador (Solo E-MOSFET)
Asegura que el dispositivo opere siempre en zona de saturación (activa).
* **Mallas del circuito:**
  $$ V_{GS} = V_{DS} \quad ; \quad V_G = V_D $$
  $$ V_{DS} = V_{DD} - I_D R_D $$"""

drain_fb_new = r"""### 2.4 Realimentación de Drenador (Solo E-MOSFET)
Asegura que el dispositivo opere siempre en zona de saturación (activa).
* **Mallas del circuito:**
  $$ V_{GS} = V_{DS} \quad ; \quad V_G = V_D $$
  $$ V_{DS} = V_{DD} - I_D R_D $$
* **Solución Analítica Exacta (E-MOSFET en Realimentación):**
  Sustituyendo $V_{GS} = V_{DD} - I_D R_D$ en la ecuación de transferencia:
  $$ A = k R_D^2, \quad B = -\left[2 k R_D (V_{DD} - V_{GS(Th)}) + 1\right], \quad C = k (V_{DD} - V_{GS(Th)})^2 $$
  *Raíz física correcta:* $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$"""

text = text.replace(drain_fb_old, drain_fb_new)


# 3. Add Section 2.6
optimo_line_old = r"""### 2.5 Diseño Óptimo Lineal
Para máxima excursión simétrica (Punto Q central):
$$ V_{DSQ} \approx \frac{V_{DD}}{2} $$"""

optimo_line_new = r"""### 2.5 Diseño Óptimo Lineal
Para máxima excursión simétrica (Punto Q central):
$$ V_{DSQ} \approx \frac{V_{DD}}{2} $$

### 2.6 Configuraciones Especiales en DC (Compuerta y Drenador Común)
El análisis en corriente directa de estas configuraciones se deriva directamente de las topologías base:
* **Drenador Común (Seguidor de Surtidor):** Es análogo al divisor de voltaje o autopolarización, pero **sin resistencia de Drenador** ($R_D = 0\ \Omega$). El Drenador se conecta directo a $V_{DD}$.
  * *Malla de Salida:* $V_{DS} = V_{DD} - I_D R_S$
* **Compuerta Común:** La compuerta está a tierra ($V_G = 0\text{ V}$). La polarización se logra con una fuente negativa en el surtidor ($-V_{SS}$) o mediante autopolarización.
  * *Malla de Entrada:* $V_{GS} = -I_D R_S \quad \text{o} \quad V_{GS} = V_{SS} - I_D R_S$"""

text = text.replace(optimo_line_old, optimo_line_new)

# 4. Fix V_{Th} to V_{GS(Th)}
text = text.replace(r"V_{Th}", r"V_{GS(Th)}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Tema 3 Exam Form updated successfully with E-MOSFET quadratics and common configurations.")
