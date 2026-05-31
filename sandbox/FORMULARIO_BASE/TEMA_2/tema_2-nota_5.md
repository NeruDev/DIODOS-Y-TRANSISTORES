<!--
::METADATA::
type: cheatsheet
topic_id: BJT-02
file_id: tema_2-nota_5
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos de Diseño de Polarización y Conmutación con BJT

Este documento recopila y estructura las metodologías analíticas, criterios prácticos y fórmulas de diseño electrónico para transistores bipolares (BJT) presentadas en la Nota 5. Contempla el diseño sistemático de la polarización por divisor de voltaje (caso de estudio del transistor 2N2222) y el dimensionamiento de componentes para la operación del transistor como interruptor (switch de lado bajo) en corte y saturación.

---

## 1. Diseño de Polarización por Divisor de Voltaje (Región Activa Lineal)

El diseño de una red de polarización por divisor de voltaje estable busca fijar un punto de operación Q ($I_C, V_{CEQ}$) robusto frente a variaciones severas en el factor de ganancia de corriente ($\beta$) del transistor.

### 1.1 Criterio de Reparto de Tensiones en Tercios
Regla práctica de ingeniería empleada para distribuir simétricamente el voltaje de la fuente única $V_{CC}$ entre las caídas de los resistores de malla y el transistor, maximizando la estabilidad térmica y la excursión simétrica de señal.

$$
V_E \approx \frac{V_{CC}}{3} \quad ; \quad V_{CEQ} \approx \frac{V_{CC}}{3} \quad ; \quad V_{RC} \approx \frac{V_{CC}}{3}
$$

### 1.2 Corrientes de Malla en el Peor Caso
Cálculo de la corriente de base máxima ($I_{B,\max}$) y la corriente de emisor ($I_E$) asociadas a la mínima ganancia comercial del componente ($\beta_{\min}$), asegurando que el transistor nunca abandone la región activa.

$$
I_{B,\max} = \frac{I_C}{\beta_{\min}}
$$

$$
I_E = \frac{I_C}{\alpha_{\min}} = I_C \left( 1 + \frac{1}{\beta_{\min}} \right) \quad \text{donde} \quad \alpha_{\min} = \frac{\beta_{\min}}{\beta_{\min} + 1}
$$

### 1.3 Dimensionamiento de las Resistencias de Colector y Emisor
Cálculo de los valores óhmicos de las resistencias principales y sus potencias térmicas de disipación disipadas nominales.

*   **Resistencia de Emisor ($R_E$):**
    $$
    R_E = \frac{V_E}{I_E} \quad \implies \quad P_{R_E} = I_E^2 \cdot R_E
    $$
*   **Resistencia de Colector ($R_C$):**
    $$
    R_C = \frac{V_{CC} - V_C}{I_C} = \frac{V_{RC}}{I_C} \quad \implies \quad P_{R_C} = I_C^2 \cdot R_C
    $$
    *(Nota: El potencial estático de colector es $V_C = V_E + V_{CEQ}$).*

### 1.4 Criterio de Rigidez del Divisor (Cálculo de $R_{TH}$)
Fórmula de diseño empleada para definir la resistencia máxima equivalente del divisor en la base ($R_{TH}$). Impone que la corriente que fluye por el divisor sea al menos 10 veces mayor que la corriente de base para independizar el voltaje de base de la carga.

$$
R_{TH} \approx \frac{(\beta_{\min} + 1) R_E}{10}
$$

### 1.5 Voltaje Equivalente de Thévenin Requerido ($V_{TH}$)
Tensión de base equivalente requerida que incorpora la caída del diodo directa ($V_{BE}$) y la caída en la resistencia de Thévenin.

$$
V_{TH} = V_E + V_{BE} + I_{B,\max} R_{TH}
$$

### 1.6 Determinación Directa de las Resistencias del Divisor ($R_1$ y $R_2$)
Cálculo analítico de los resistores superior ($R_1$) e inferior ($R_2$) a partir del voltaje y resistencia de Thévenin deseados.

$$
R_1 = \frac{V_{CC}}{V_{TH}} R_{TH}
$$

$$
R_2 = \frac{V_{CC}}{V_{CC} - V_{TH}} R_{TH}
$$

*   **Potencia disipada real en las resistencias del divisor (con carga):**
    $$
    P_{R_1} \approx \frac{(V_{CC} - V_B)^2}{R_1} \quad ; \quad P_{R_2} \approx \frac{V_B^2}{R_2} \quad \text{donde} \quad V_B = V_E + V_{BE}
    $$

### 1.7 Verificación de Sensibilidad frente a Variaciones de $\beta$
Ecuaciones de validación para calcular la deriva de las corrientes de emisor y colector ante cualquier fluctuación de $\beta$.

$$
I_E(\beta) = \frac{V_{TH} - V_{BE}}{R_E + \frac{R_{TH}}{\beta + 1}} \quad \implies \quad I_C(\beta) \approx \frac{\beta}{\beta + 1} I_E(\beta)
$$

---

## 2. Transistor BJT como Interruptor (Switch de Lado Bajo)

En aplicaciones de conmutación digital, el BJT opera de manera discreta alternando entre dos zonas extremas: Corte (estado OFF, circuito abierto) y Saturación (estado ON, cortocircuito virtual).

### 2.1 Corriente de Saturación de Colector Ideal ($I_{C(\text{sat})}$)
Corriente máxima posible en la carga, limitada únicamente por la resistencia externa en serie del colector.

$$
I_{C(\text{sat})} \approx \frac{V_{CC}}{R_C} \quad \left( \text{Real: } I_{C(\text{sat})} = \frac{V_{CC} - V_{CE(\text{sat})}}{R_C} \right)
$$

### 2.2 Corriente Mínima de Base de Conmutación ($I_{B(\text{sat},\min)}$)
Corriente de control mínima requerida en la base para forzar al transistor a entrar en la región de saturación profunda.

$$
I_{B(\text{sat},\min)} = \frac{I_{C(\text{sat})}}{\beta}
$$

### 2.3 Criterios de Diseño para la Resistencia de Base de Control ($R_B$)
Cuando el circuito de control (por ejemplo, un microcontrolador o compuerta lógica) entrega una tensión de nivel alto ($V_{HI}$), la resistencia de base ($R_B$) debe limitarse para inyectar suficiente corriente y garantizar el estado ON.

*   **Límite Óhmico de la Resistencia de Base ($R_B$):**
    $$
    R_B \le \frac{(V_{HI} - V_{BE}) \cdot \beta \cdot R_C}{V_{CC}}
    $$
*   **Límite de la Resistencia de Carga de Colector ($R_C$):**
    $$
    R_C \ge \frac{V_{CC} \cdot R_B}{\beta \cdot (V_{HI} - V_{BE})}
    $$

* **Nomenclatura:**
  * $V_{HI}$: Voltaje lógico de nivel alto entregado por la etapa de control de entrada (V).
  * $V_{CE(\text{sat})}$: Voltaje de saturación de conmutación del transistor en directa (V). Típicamente $0.2\text{ V}$.
  * $I_{C(\text{sat})}$: Corriente de colector en saturación profunda (A).
  * $R_B$: Resistencia de limitación conectada en serie con la base para control digital ($\Omega$).

> [!IMPORTANT]
> **Estabilidad del Divisor de Tensión**: El criterio de rigidez del divisor ($R_{TH} \approx (\beta + 1)R_E / 10$) es el pilar de la polarización estable. Asegura que la corriente circulante por el divisor sea muy superior a la corriente de base consumida por el BJT. Esto independiza de forma efectiva la tensión $V_B$ del transistor, garantizando que el punto de operación Q se mantenga casi inmóvil ante amplias variaciones de $\beta$.

> [!WARNING]
> **Factor de Sobrediseño en Conmutación**: Para asegurar una saturación profunda y confiable en aplicaciones industriales, la corriente de base real inyectada en el diseño debe ser de 2 a 5 veces superior al mínimo teórico calculado ($I_B = k \cdot I_{B(\text{sat},\min)}$ donde $k \geq 2$). Esto protege al interruptor contra caídas imprevistas del factor $\beta$ debidas a bajas temperaturas.

---

## 3. Glosario de Términos Técnicos

* **División en Tercios:** Criterio práctico de diseño que asigna simétricamente un tercio del voltaje de fuente a la caída en la resistencia de colector, otro a la caída en el transistor y el restante a la resistencia de emisor para optimizar la excursión simétrica.
* **Rigidez del Divisor:** Capacidad de una red resistiva en divisor de voltaje para mantener una tensión constante en su nodo central a pesar de la corriente extraída por la base del transistor en paralelo.
* **Peor Caso de Diseño:** Metodología que evalúa las tolerancias límites de los componentes (como la ganancia mínima $\beta_{\min}$) para asegurar el funcionamiento del circuito bajo condiciones extremas.
* **Realimentación de Voltaje:** Lazo de compensación pasivo que utiliza la caída de tensión en la resistencia de emisor ($I_E R_E$) para contrarrestar automáticamente cualquier incremento indeseado en la corriente del colector.
* **Switch de Lado Bajo:** Configuración de conmutación donde el interruptor (transistor BJT) se coloca entre la carga y la tierra de referencia, controlando el retorno de la corriente del circuito.
* **Voltaje de Conmutación ($V_{CE(\text{sat})}$):** Tensión en bornes de colector-emisor cuando el BJT está en estado de conducción plena (ON), típicamente de $0.2\text{ V}$.
* **Región de Saturación Profunda:** Estado físico donde ambas uniones PN del BJT están en directa, provocando una caída mínima de tensión colector-emisor y una corriente controlada exclusivamente por la red externa.
* **Región de Corte Absoluto:** Estado físico donde la corriente de base es nula, interrumpiendo el flujo del colector (OFF) a excepción de las corrientes mínimas de fuga inversa.
