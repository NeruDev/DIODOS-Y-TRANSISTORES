# Formulario de Examen: Tema 3 (Transistor Unipolar FET y MOSFET)

> Documento simplificado para consulta rápida en exámenes. Contiene exclusivamente fórmulas, modelos y aproximaciones estandarizadas.

---

## 1. Relaciones Fundamentales del FET

### 1.1 Corrientes y Condiciones Ideales
* **Impedancia de Entrada Infinita:**
  $$ I_G \approx 0\text{ A} $$
* **Igualdad de Corrientes de Canal:**
  $$ I_D = I_S $$

### 1.2 Ecuaciones de Transferencia (Shockley)
Válidas para JFET y MOSFET de Deplexión (D-MOSFET).
* **Corriente de Drenador ($I_D$):**
  $$ I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2 $$
* **Corriente Máxima ($I_{DSS}$):** Corriente teórica máxima con compuerta cortocircuitada al surtidor ($V_{GS} = 0\text{ V}$).
* **Voltaje de Estrangulamiento o Pinch-off ($V_P$):** Voltaje donde $I_D \approx 0\text{ A}$. (Para canal N, $V_P$ es negativo).

### 1.3 Transferencia para MOSFET de Enriquecimiento (E-MOSFET)
* **Corriente de Drenador (Región de Saturación / Activa):**
  $$ I_D = k (V_{GS} - V_{GS(Th)})^2 $$
* **Constante del Dispositivo ($k$):**
  $$ k = \frac{I_{D(on)}}{(V_{GS(on)} - V_{GS(Th)})^2} $$
* **Corriente en Región Óhmica/Triodo ($V_{DS} < V_{GS} - V_{GS(Th)}$):**
  $$ I_D = k \left[ 2(V_{GS} - V_{GS(Th)})V_{DS} - V_{DS}^2 \right] $$

---

## 2. Configuraciones de Polarización (DC)

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
* **Solución Analítica Exacta (E-MOSFET):**
  Sustituyendo la malla de entrada en la ecuación de $k$:
  $$ A = k R_S^2, \quad B = -\left[2 k R_S (V_G - V_{GS(Th)}) + 1\right], \quad C = k (V_G - V_{GS(Th)})^2 $$
  *Raíz física correcta:* Generalmente, para E-MOSFET se toma la raíz que asegure $V_{GS} > V_{GS(Th)}$.

### 2.4 Realimentación de Drenador (Solo E-MOSFET)
Asegura que el dispositivo opere siempre en zona de saturación (activa).
* **Mallas del circuito:**
  $$ V_{GS} = V_{DS} \quad ; \quad V_G = V_D $$
  $$ V_{DS} = V_{DD} - I_D R_D $$
* **Solución Analítica Exacta (E-MOSFET en Realimentación):**
  Sustituyendo $V_{GS} = V_{DD} - I_D R_D$ en la ecuación de transferencia:
  $$ A = k R_D^2, \quad B = -\left[2 k R_D (V_{DD} - V_{GS(Th)}) + 1\right], \quad C = k (V_{DD} - V_{GS(Th)})^2 $$
  *Raíz física correcta:* $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$

### 2.5 Diseño Óptimo Lineal
Para máxima excursión simétrica (Punto Q central):
$$ V_{DSQ} \approx \frac{V_{DD}}{2} $$

### 2.6 Configuraciones Especiales en DC (Compuerta y Drenador Común)
El análisis en corriente directa de estas configuraciones se deriva directamente de las topologías base:
* **Drenador Común (Seguidor de Surtidor):** Es análogo al divisor de voltaje o autopolarización, pero **sin resistencia de Drenador** ($R_D = 0\ \Omega$). El Drenador se conecta directo a $V_{DD}$.
  * *Malla de Salida:* $V_{DS} = V_{DD} - I_D R_S$
* **Compuerta Común:** La compuerta está a tierra ($V_G = 0\text{ V}$). La polarización se logra con una fuente negativa en el surtidor ($-V_{SS}$) o mediante autopolarización.
  * *Malla de Entrada:* $V_{GS} = -I_D R_S \quad \text{o} \quad V_{GS} = V_{SS} - I_D R_S$

---

## 3. Uso de la Curva de Polarización Universal

Permite resolver el punto $Q$ gráficamente sin ecuaciones cuadráticas.

### 3.1 Ejes Normalizados y Curva
* **Eje Horizontal:** $V_{GS} / |V_P|$
* **Eje Vertical:** $I_D / I_{DSS}$
* **Curva Fija universal:** $y = (1 - |x|)^2$

### 3.2 Recta de Carga (Autopolarización)
* **Ecuación:** $I_D = -\frac{V_{GS}}{R_S}$
* Interseca siempre el origen $(0,0)$. Usa un punto de prueba (ej: $I_D = I_{DSS} / 2$) para trazarla.

### 3.3 Recta de Carga (Divisor de Voltaje)
* **Ecuación:** $I_D = \frac{V_G}{R_S} - \frac{V_{GS}}{R_S}$
* **Puntos de cruce:** Eje X en $V_{GS} = V_G$; Eje Y en $I_D = \frac{V_G}{R_S}$.
* La intersección con la curva universal da ($V_{GSQ}, I_{DQ}$).

---

## 4. Modelos de Pequeña Señal (AC)

### 4.1 Transconductancia ($g_m$)
* **Para JFET / D-MOSFET:**
  $$ g_m = g_{m0} \left( 1 - \frac{V_{GSQ}}{V_P} \right) = g_{m0} \sqrt{\frac{I_{DQ}}{I_{DSS}}} \quad ; \quad g_{m0} = \frac{2 I_{DSS}}{|V_P|} $$
* **Para E-MOSFET:**
  $$ g_m = 2k (V_{GSQ} - V_{GS(Th)}) $$

### 4.2 Impedancia de Salida ($r_d$)
  $$ r_d = \frac{1}{g_{os}} \quad \text{o} \quad r_d = \frac{1}{y_{os}} $$
*(Se asume $r_d \approx \infty$ idealmente en exámenes si no se especifica el efecto de Modulación de Longitud de Canal).*

### 4.3 Configuraciones Amplificadoras (Desempeño)
| Parámetro | Surtidor Común (S-com)* | Drenador Común (Seguidor) | Compuerta Común (G-com) |
|-----------|--------------------------|---------------------------|-------------------------|
| **$A_v$** | Alta Negativa ($\approx -g_m R_D$) | $\approx 1$ (siempre $<1$) | Alta Positiva |
| **$Z_{in}$**| Muy Alta ($\approx R_G$) | Muy Alta ($\approx R_G$) | Muy Baja ($\approx 1/g_m$) |
| **$Z_{out}$**| Alta ($\approx R_D$) | Baja ($\approx 1/g_m$) | Alta ($\approx R_D$) |

*(Nota: Fórmulas de ganancia asumen $r_d \approx \infty$)*

---

## 5. Resumen Visual y Redes Combinadas

> [!WARNING]
> **Peligro Conceptual: "Saturación" en FET vs BJT**
> La nomenclatura teórica es una trampa mortal en exámenes.
> - En **BJT**, Saturación = Switch Cerrado (Voltaje mínimo).
> - En **FET**, Saturación = Región Activa / Amplificador Lineal (Fuente de corriente constante).

### 5.1 Zonas de Operación Matemáticas
**Para JFET y D-MOSFET:**
| Región | Condición de Voltaje | Comportamiento en Circuito |
|--------|----------------------|----------------------------|
| **Corte** | $V_{GS} \le V_P$ | Switch Abierto ($I_D \approx 0$) |
| **Óhmica/Triodo** | $V_{DS} < V_{GS} - V_P$ | Resistor Controlado por Voltaje |
| **Saturación**| $V_{DS} \ge V_{GS} - V_P$ | Fuente de Corriente Constante |

**Para E-MOSFET:**
| Región | Condición de Voltaje | Comportamiento en Circuito |
|--------|----------------------|----------------------------|
| **Corte** | $V_{GS} < V_{GS(Th)}$ | Switch Abierto ($I_D \approx 0$) |
| **Óhmica/Triodo** | $V_{DS} < V_{GS} - V_{GS(Th)}$ | Resistor Controlado (Ecuación Larga) |
| **Saturación**| $V_{DS} \ge V_{GS} - V_{GS(Th)}$ | Fuente de Corriente Constante ($I_D = k(V_{GS}-V_{GS(Th)})^2$) |

### 5.2 Método Universal de Examen (Resolución Analítica)
Sigue siempre esta secuencia en DC:
1. **Asume** $I_G = 0\text{ A}$.
2. **Calcula** $V_G$ (por divisor de tensión o malla externa).
3. **Plantea** $V_{GS}$ usando la malla de entrada.
4. **Calcula** $I_D$ usando Shockley (o la ecuación $k$ para E-MOSFET). Aplica las fórmulas analíticas exactas (Sección 2) o traza la recta de carga sobre la curva universal.
5. **Calcula** $V_{DS}$ usando la malla de salida.
6. **Verifica la Región** usando las tablas de la Sección 5.1.

### 5.3 Redes Combinadas (FET + BJT)
* **Independencia en DC:** Como $I_G = 0$, el FET **nunca** carga a la etapa anterior en continua. Separa las mallas DC de cada transistor y resuélvelas independientemente. Resuelve primero la que tenga valores fijos y propaga el voltaje resultante.

---

## Glosario de Variables

| Símbolo | Nombre y Descripción |
|---------|----------------------|
| **$A_v$** | Ganancia de voltaje de la configuración en AC (V/V). |
| **$I_D$** | Corriente de drenador (A). |
| **$I_G$** | Corriente de compuerta, se asume $0\text{ A}$ idealmente (A). |
| **$I_S$** | Corriente de surtidor, siempre idéntica a $I_D$ en estado estable (A). |
| **$I_{DSS}$** | Corriente teórica de drenador a surtidor con compuerta en cortocircuito ($V_{GS} = 0$), máxima para JFET (A). |
| **$I_{D(on)}$** | Corriente de drenador de prueba proporcionada por el fabricante para E-MOSFETs (A). |
| **$R_D, R_S, R_G$** | Resistencias físicas conectadas en Drenador, Surtidor y Compuerta ($\Omega$). |
| **$V_P$** | Voltaje de Pinch-off o estrangulamiento (V). |
| **$V_{DD}$** | Fuente principal de alimentación del circuito de Drenador en DC (V). |
| **$V_{DS}$** | Voltaje diferencial entre Drenador y Surtidor (V). |
| **$V_{GG}$** | Fuente independiente de polarización de DC para la Compuerta (V). |
| **$V_{GS}$** | Voltaje diferencial de control entre Compuerta y Surtidor (V). |
| **$V_{GS(Th)}$** | Voltaje de umbral (Threshold) necesario para iniciar el canal en un E-MOSFET (V). |
| **$V_{GS(on)}$** | Voltaje de compuerta de prueba correspondiente a la corriente $I_{D(on)}$ en E-MOSFETs (V). |
| **$g_m$** | Transconductancia en el punto de operación estático $Q$ (S o A/V). |
| **$g_{m0}$** | Transconductancia máxima teórica (ocurre cuando $V_{GS} = 0\text{ V}$) del dispositivo (S). |
| **$k$** | Constante constructiva de conducción paramétrica para MOSFET de Enriquecimiento (A/V²). |
| **$r_d$** | Resistencia dinámica de salida del transistor (inverso de $y_{os}$ u $g_{os}$) ($\Omega$). |
