<!--
::METADATA::
type: cheatsheet
topic_id: BJT-02
file_id: tema_2-nota_4
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos de Polarización de Transistores BJT en Emisor Común

Este documento presenta de forma estructurada y analítica las ecuaciones y modelos matemáticos de las principales configuraciones de polarización en corriente directa (DC) para transistores bipolares (BJT) en emisor común (E-com) descritos en la Nota 4. Contempla el análisis de polarización fija, estabilización por resistencia de emisor, y la técnica de divisor de voltaje mediante la simplificación de equivalentes de Thévenin.

---

## 1. Relaciones Generales de Voltaje y Corriente en la Malla

Para cualquier transistor BJT operando en su región activa bajo configuración de emisor común, se cumplen las siguientes relaciones fundamentales de corriente y voltaje.

### 1.1 Ecuación de Corriente de Emisor en Región Activa
Relación directa obtenida de la Ley de Corrientes de Kirchhoff (LKC) sustituyendo la ganancia de colector ($I_C = \beta I_B$).

$$
I_E = I_B + I_C \implies I_E = (\beta + 1) I_B
$$

### 1.2 Potenciales de Nodo Respecto a Tierra
Tensiones estáticas absolutas medidas en cada terminal física del semiconductor con referencia al común (GND).

* **Voltaje de Emisor ($V_E$):** Caída de tensión debida al flujo de corriente por la resistencia de emisor.
  $$
  V_E = I_E R_E
  $$
* **Voltaje de Base ($V_B$):** Potencial de control en la base.
  $$
  V_B = V_E + V_{BE}
  $$
* **Voltaje de Colector ($V_C$):** Potencial de salida en el colector.
  $$
  V_C = V_{CC} - I_C R_C
  $$

### 1.3 Voltajes entre Terminales
Diferencia de potencial diferencial entre bornes del semiconductor.

$$
V_{CE} = V_C - V_E
$$

$$
V_{BE} = V_B - V_E
$$

* **Nomenclatura:**
  * $I_B, I_C, I_E$: Corrientes continuas de base, colector y emisor (A).
  * $\beta$: Ganancia de corriente del transistor en continua ($h_{FE}$, adimensional).
  * $R_C, R_E$: Resistencias de colector y de emisor respectivamente ($\Omega$).
  * $V_B, V_C, V_E$: Tensiones absolutas en bornes de base, colector y emisor (V).
  * $V_{BE}$: Caída de tensión directa base-emisor (V). Típicamente $0.7\text{ V}$ para silicio.
  * $V_{CE}$: Diferencia de potencial colector-emisor (V).
  * $V_{CC}$: Fuente única de alimentación en corriente continua (V).

---

## 2. Polarización Fija (Simple, $R_E = 0\ \Omega$)

Es la topología más simple, donde el emisor se acopla directamente a la tierra de referencia. Presenta una alta sensibilidad ante variaciones de temperatura y ganancias $\beta$.

### 2.1 Ecuación de la Malla de Entrada (Corriente de Base $I_B$)
Deducción obtenida por la Ley de Voltajes de Kirchhoff (LVK) en el lazo base-emisor.

$$
I_B = \frac{V_{CC} - V_{BE}}{R_B}
$$

### 2.2 Ecuación de la Malla de Salida (Recta de Carga DC)
Relación lineal de salida que delimita las combinaciones de voltaje y corriente.

$$
V_{CE} = V_{CC} - R_C I_C
$$

* **Puntos Extremos de la Recta:**
  * **Corte (Límite de Apagado, $I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación (Límite de Conducción Máxima, $V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C} \quad \left( \text{Real: } I_{C(\text{sat})} \approx \frac{V_{CC} - V_{CE(\text{sat})}}{R_C} \right)
    $$

---

## 3. Polarización Estabilizada por Resistencia de Emisor ($R_E \neq 0\ \Omega$)

La adición de una resistencia en el emisor introduce un lazo de retroalimentación negativa que estabiliza el punto de operación $Q$ frente a derivas térmicas o cambios en $\beta$.

### 3.1 Mecanismo de Estabilización Térmica
Cualquier factor térmico que intente elevar la corriente de colector ($I_C \uparrow$) desencadena la siguiente secuencia de compensación:

$$
I_C \uparrow \;\implies\; I_E \uparrow \;\implies\; V_E \uparrow \text{ (pues } V_E = I_E R_E\text{)} \;\implies\; V_{BE} \downarrow \text{ (pues } V_{BE} = V_B - V_E\text{)} \;\implies\; I_B \downarrow \;\implies\; I_C \downarrow
$$

### 3.2 Ecuación de la Malla de Salida (Recta de Carga DC)
Planteamiento de tensiones en el lazo colector-emisor asumiendo la aproximación $I_E \approx I_C$.

$$
V_{CE} = V_{CC} - (R_C + R_E) I_C
$$

* **Puntos Extremos de la Recta:**
  * **Corte ($I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación Ideal ($V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C + R_E}
    $$

---

## 4. Polarización por Divisor de Voltaje

Es la configuración más robusta y estable. Utiliza un divisor de tensión en la base ($R_1$ y $R_2$) para fijar el voltaje de base de manera independiente del parámetro $\beta$ del transistor. Su análisis se simplifica mediante el Teorema de Thévenin.

### 4.1 Resistencia Equivalente de Thévenin ($R_{TH}$)
Resistencia vista desde la base hacia el divisor de voltaje con la fuente DC anulada.

$$
R_{TH} = R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}
$$

### 4.2 Voltaje Equivalente de Thévenin ($V_{TH}$)
Voltaje a circuito abierto en el nodo de base (desconectando el transistor).

$$
V_{TH} = V_{CC} \cdot \frac{R_2}{R_1 + R_2}
$$

### 4.3 Ecuación de la Corriente de Base ($I_B$)
Deducción obtenida por LVK en la malla de entrada simplificada por Thévenin, donde la resistencia de emisor ($R_E$) aparece multiplicada (reflejada) en la base por el factor $(\beta + 1)$.

$$
I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1) R_E}
$$

### 4.4 Malla de Salida y Recta de Carga DC
* **Ecuación de la Malla de Salida Exacta:**
  $$
  V_{CE} = V_{CC} - I_C R_C - I_E R_E = V_{CC} - I_B \left[ \beta R_C + (\beta + 1) R_E \right]
  $$
* **Ecuación de la Recta de Carga DC Aproximada ($I_E \approx I_C$):**
  $$
  V_{CE} = V_{CC} - (R_C + R_E) I_C
  $$
* **Puntos Extremos de la Recta:**
  * **Corte ($I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación Ideal ($V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C + R_E}
    $$

* **Nomenclatura:**
  * $R_1$: Resistencia de polarización superior del divisor ($\Omega$).
  * $R_2$: Resistencia de polarización inferior del divisor ($\Omega$).
  * $R_{TH}$: Resistencia equivalente de Thévenin en la base ($\Omega$).
  * $V_{TH}$: Voltaje equivalente de Thévenin en la base (V).

> [!IMPORTANT]
> **Resistencia de Emisor Reflejada**: La ecuación de entrada por Thévenin demuestra que la resistencia de emisor $R_E$ se ve multiplicada por $(\beta + 1)$ cuando se analiza desde el circuito de base. Esta multiplicación virtual incrementa significativamente la impedancia vista por la fuente, limitando las variaciones de corriente de base $I_B$ ante cambios bruscos del parámetro $\beta$ debido a variaciones térmicas o de lote del transistor.

> [!WARNING]
> **Criterio de Linealidad (Polarización Inversa Colector-Base)**: Para garantizar el funcionamiento en la región activa lineal, se debe verificar que el voltaje de colector sea mayor al de base. Si no se cumple, el transistor caerá en saturación profunda.
> $$
> V_C > V_B \implies V_{CC} - I_C R_C > V_B
> $$

---

## 5. Glosario de Términos Técnicos

* **Polarización Fija:** Técnica básica de polarización DC que inyecta una corriente de base constante a través de un solo resistor conectado al voltaje de alimentación.
* **Estabilización de Emisor:** Método que introduce un resistor en la terminal de emisor para retroalimentar el voltaje de entrada, compensando automáticamente las derivas de corriente.
* **Divisor de Voltaje:** Configuración de resistencias en serie acopladas en paralelo con la fuente que reduce y fija la tensión de base a un nivel constante, aislando el punto Q de las fluctuaciones de ganancia.
* **Equivalente de Thévenin:** Teorema de análisis de redes que simplifica un circuito lineal complejo de dos terminales a una sola fuente de tensión equivalente en serie con una sola resistencia de paso.
* **Resistencia Reflejada:** Fenómeno eléctrico por el cual las impedancias conectadas en el emisor de un BJT incrementan su valor relativo en un factor de $(\beta + 1)$ al ser observadas o calculadas desde la terminal de base.
* **Retroalimentación Negativa:** Proceso mediante el cual una fracción de la señal de salida de un sistema se resta de la entrada para reducir las variaciones de la ganancia, mejorando la estabilidad.
* **Punto Q (Quiescent Point):** Coordenadas estáticas $(V_{CEQ}, I_{CQ})$ en el plano cartesiano que definen las condiciones físicas de reposo en corriente directa del transistor en vacío.
