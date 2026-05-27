# Análisis y Cálculos para $R_C = 100 \, \Omega$ y $R_E = 100 \, \Omega$

Al incrementar el valor de la resistencia de emisor a $100 \, \Omega$, estás introduciendo un fenómeno conocido como **Realimentación Negativa en DC (Degeneración de Emisor)**.

A continuación, se explica teóricamente cómo este cambio "amortigua" las variaciones de un transistor con beta alta y se realizan los cálculos exactos para demostrarlo.

---

### 1. El Principio Físico del Amortiguamiento (Estabilidad del Q-Point)

El problema de los BJTs es que el parámetro $\beta$ varía enormemente entre lotes de fabricación y con la temperatura. Si el circuito dependiera fuertemente de $\beta$, el punto de operación (Q-Point) se desplazaría, llevando al transistor al corte o a la saturación.

La corriente de emisor ($I_E \approx I_C$) en un circuito polarizado por divisor de tensión se rige por la ecuación de malla de entrada (Equivalente de Thévenin):

$$I_E = \frac{V_{TH} - V_{BE}}{R_E + \frac{R_{TH}}{\beta + 1}}$$

Donde:

* $V_{TH}$: Voltaje de Thévenin del divisor de base.
* $R_{TH}$: Resistencia equivalente del divisor ($R_1 \parallel R_2$).

**La Magia de $R_E$ Alta:** Si logramos que $R_E \gg \frac{R_{TH}}{\beta + 1}$, el término dependiente de la $\beta$ en el denominador se vuelve matemáticamente insignificante. La corriente $I_E$ dependerá casi exclusivamente de $V_{TH}$ y $R_E$ (elementos pasivos de alta precisión), volviendo al circuito "inmune" a variaciones masivas de $\beta$.

---

### 2. Diseño del Nuevo Punto de Operación (Q-Point)

Para mantener la corriente objetivo de la práctica ($I_C \approx 50 \text{ mA}$) con las nuevas resistencias de $100 \, \Omega$, recalculemos los voltajes nodales ideales:

* **Voltaje de Emisor:** $V_E = I_E \times R_E \approx 50 \text{ mA} \times 100 \, \Omega = \mathbf{5.0 \text{ V}}$
* **Voltaje de Colector:** $V_C = V_{CC} - (I_C \times R_C) = 15 \text{ V} - (50 \text{ mA} \times 100 \, \Omega) = \mathbf{10.0 \text{ V}}$
* **Voltaje Colector-Emisor:** $V_{CE} = V_C - V_E = 10 - 5 = \mathbf{5.0 \text{ V}}$ *(Q-Point muy estable, centrado en la zona activa)*.
* **Voltaje de Base Requerido:** $V_B = V_E + V_{BE} = 5.0 + 0.7 = \mathbf{5.7 \text{ V}}$

Para lograr este $V_B$, diseñamos un divisor de tensión "rígido" ($R_1 = 4.3 \text{ k}\Omega$, $R_2 = 2.7 \text{ k}\Omega$).
Sus parámetros de Thévenin son:

* $V_{TH} = 15 \text{ V} \left( \frac{2700}{4300 + 2700} \right) = \mathbf{5.785 \text{ V}}$
* $R_{TH} = 4300 \parallel 2700 = \mathbf{1658.5 \, \Omega}$

---

### 3. Cálculos Demostrativos: $\beta = 300$ vs $\beta = 450$

Ahora, apliquemos la fórmula exacta para observar el amortiguamiento real ante un salto del 50% en el valor de la beta.

#### Caso A: Transistor con $\beta = 300$

$$I_E = \frac{5.785 \text{ V} - 0.7 \text{ V}}{100 + \frac{1658.5}{301}} = \frac{5.085 \text{ V}}{100 + 5.51 \, \Omega} = \frac{5.085}{105.51} = \mathbf{48.19 \text{ mA}}$$

$$I_C = I_E \left(\frac{\beta}{\beta+1}\right) = 48.19 \text{ mA} \left(\frac{300}{301}\right) = \mathbf{48.03 \text{ mA}}$$

#### Caso B: Transistor con $\beta = 450$

$$I_E = \frac{5.785 \text{ V} - 0.7 \text{ V}}{100 + \frac{1658.5}{451}} = \frac{5.085 \text{ V}}{100 + 3.67 \, \Omega} = \frac{5.085}{103.67} = \mathbf{49.05 \text{ mA}}$$

$$I_C = I_E \left(\frac{\beta}{\beta+1}\right) = 49.05 \text{ mA} \left(\frac{450}{451}\right) = \mathbf{48.94 \text{ mA}}$$

> **Conclusión del Amortiguamiento:** A pesar de que la ganancia de corriente interna del transistor ($\beta$) aumentó brutalmente en un **$50\%$**, la corriente de colector real del circuito solo se desvió un mínimo **$1.89\%$** (de 48.03 mA a 48.94 mA). La estabilización es un éxito rotundo.

---

### 4. Consecuencias en la Señal AC (El Trade-off)

Colocar $R_C = R_E = 100 \, \Omega$ tiene consecuencias severas en las métricas de tu amplificador, dependiendo de cómo manejes el capacitor $C_3$:

1. **Si NO desacoplas $R_E$ (Sin capacitor $C_3$):**
La ganancia de voltaje teórica se aproxima a $A_v \approx -\frac{R_C}{R_E}$.

$$A_v \approx -\frac{100}{100} = \mathbf{-1 \text{ V/V}}$$

**Efecto:** El circuito ya no funciona como amplificador, sino como un *inversor de ganancia unitaria* (Phase Splitter). No cumplirías el requisito de la práctica ($|A_{vo}| \ge 40$).

2. **Si desacoplas totalmente $R_E$ (Con capacitor $C_3$ en paralelo):**
La resistencia de emisor AC se vuelve $0 \, \Omega$. La ganancia depende del $g_m$.

$$g_m = \frac{I_C}{V_T} = \frac{48 \text{ mA}}{25 \text{ mV}} = 1.92 \text{ S}$$

$$A_v = -g_m \times R_C = -1.92 \times 100 = \mathbf{-192 \text{ V/V}}$$

**Efecto:** Tienes una ganancia altísima y muy estable (porque logramos estabilizar $I_C$, lo que estabiliza $g_m$), pero tu impedancia de entrada se desploma y saturarás el amplificador si le inyectas los 100 mV solicitados en la práctica.

---

### 5. Verificación Rigurosa Ampere Node (Balance de Potencia)

Para validar la coherencia del análisis con $\beta = 300$ ($I_C = 48.03 \text{ mA}$):

* **Potencia Entregada por la Fuente ($V_{CC}$):** La fuente alimenta la rama del divisor y la rama del transistor.
$I_{total} \approx 48.03 \text{ mA} + \frac{15 \text{ V}}{7000 \, \Omega} = 48.03 + 2.14 = 50.17 \text{ mA}$
$P_S = - (15 \text{ V} \times 50.17 \text{ mA}) = \mathbf{-752.5 \text{ mW}}$
* **Potencias Disipadas:**
  * $P_{R1, R2} \text{ (Divisor)} = \frac{(15)^2}{7000} \approx \mathbf{32.1 \text{ mW}}$
  * $P_{RC} = (48.03 \text{ mA})^2 \times 100 = \mathbf{230.7 \text{ mW}}$
  * $P_{RE} = (48.19 \text{ mA})^2 \times 100 = \mathbf{232.2 \text{ mW}}$
  * $P_{Transistor} = V_{CE} \times I_C = (15 - 4.80 - 4.82) \text{ V} \times 48.03 \text{ mA} = 5.38 \text{ V} \times 48.03 \text{ mA} = \mathbf{258.4 \text{ mW}}$

* **Balance ($\Sigma P \approx 0$):**
$32.1 + 230.7 + 232.2 + 258.4 = \mathbf{753.4 \text{ mW}}$ (La ligera discrepancia < 0.2% se debe a la omisión de la potencia disipada por la pequeña corriente de base). **El circuito es energéticamente coherente y el análisis es exacto.**

---

### Tablas Comparativas de Diseño (Teórico vs Práctico)

A continuación, se presenta el diseño exacto del divisor de voltaje para las nuevas condiciones ($R_C = 100 \, \Omega$ y $R_E = 100 \, \Omega$) buscando una corriente de colector $I_C = 50 \text{ mA}$.

#### Criterio de Diseño (Divisor Rígido)
Para garantizar la estabilidad (que el divisor de voltaje no se "caiga" al conectar la base del transistor), aplicamos la regla de diseño robusto: la corriente que fluye por $R_2$ debe ser al menos 10 veces la corriente máxima de base esperada.
* Asumiendo el peor caso ($\beta_{min} = 200$), la corriente de base es $I_B = 50 \text{ mA} / 200 = 0.25 \text{ mA}$.
* Fijamos la corriente del divisor $I_{R2} = 2.5 \text{ mA}$.

Con $V_E \approx 5.0 \text{ V}$ (por la caída en $R_E$), requerimos un voltaje en la base $V_B = 5.7 \text{ V}$.

#### TABLA 1: Variante Teórica Exacta

Estos son los valores matemáticos ideales que producen **exactamente** $I_C = 50 \text{ mA}$. En la práctica, requerirían potenciómetros de precisión o arreglos en serie/paralelo para conseguirse.

| Parámetro / Componente | Valor Calculado | Función / Observación Física |
| --- | --- | --- |
| **$R_1$** (Teórica) | **$3372.7 \, \Omega$** | Resistencia superior. Pasa $I_{R2} + I_B = 2.75 \text{ mA}$. |
| **$R_2$** (Teórica) | **$2290.0 \, \Omega$** | Resistencia inferior. Fija el voltaje y pasa $I_{R2} = 2.5 \text{ mA}$. |
| $R_C$ y $R_E$ | $100 \, \Omega$ | Valores fijados por requerimiento. |
| **$V_{TH}$** (Voltaje de Thévenin) | **$6.065 \text{ V}$** | Voltaje ideal en vacío generado por el divisor de base. |
| **$R_{TH}$** (Resistencia de Thévenin) | **$1364.0 \, \Omega$** | Impedancia del divisor vista por la base. |
| **$I_C$ Resultante** ($\beta=200$) | **$49.99 \text{ mA}$** | El punto de operación cumple el objetivo con un error $< 0.02\%$. |
| **$V_{CE}$ Resultante** | **$4.97 \text{ V}$** | Voltaje Colector-Emisor centrado en la zona activa. |

#### TABLA 2: Variante Práctica (Valores Comerciales Serie E12)

Para armar el circuito real, seleccionamos las resistencias estándar más cercanas de la serie E12 ($10\%$, $5\%$) a los valores teóricos, y recalculamos el circuito para verificar cuánto se desvía el punto de operación.

* Acercamos $R_1$ de $3372 \, \Omega \rightarrow \mathbf{3.3 \text{ k}\Omega}$
* Acercamos $R_2$ de $2290 \, \Omega \rightarrow \mathbf{2.2 \text{ k}\Omega}$

| Parámetro / Componente | Valor Práctico | Función / Impacto en el Circuito Real |
| --- | --- | --- |
| **$R_1$** (Comercial E12) | **$3300 \, \Omega$** ($3.3 \text{ k}\Omega$) | Valor estándar muy común. |
| **$R_2$** (Comercial E12) | **$2200 \, \Omega$** ($2.2 \text{ k}\Omega$) | Valor estándar muy común. Mantiene la rigidez del divisor. |
| $R_C$ y $R_E$ | $100 \, \Omega$ | Valores fijados. |
| **$V_{TH}$** (Voltaje de Thévenin) | **$6.000 \text{ V}$** | Ligeramente menor al teórico por el ajuste comercial. |
| **$R_{TH}$** (Resistencia de Thévenin) | **$1320.0 \, \Omega$** | Menor resistencia, el divisor es marginalmente "más fuerte". |
| **$I_C$ Resultante** ($\beta=200$) | **$49.48 \text{ mA}$** | **Extremadamente preciso.** Apenas se desvía un $1\%$ del objetivo. |
| **$I_C$ Resultante** ($\beta=300$) | **$50.60 \text{ mA}$** | Demuestra el *excelente amortiguamiento*. Un cambio brutal de $\beta$ apenas mueve $I_C$. |
| **$V_{CE}$ Resultante** | **$5.08 \text{ V}$** | El punto $Q$ se mantiene perfectamente estable y seguro. |

#### Conclusión de Implementación
Si montas este circuito en la protoboard (Paso 1 de tu práctica) utilizando $R_1 = 3.3 \text{ k}\Omega$, $R_2 = 2.2 \text{ k}\Omega$, y $R_C = R_E = 100 \, \Omega$, lograrás el punto de operación deseado de $50 \text{ mA}$ a la primera, sin necesidad de calibración, siendo inmune a si tu BC548B específico tiene una ganancia $\beta$ de 200, 300 o 450.
