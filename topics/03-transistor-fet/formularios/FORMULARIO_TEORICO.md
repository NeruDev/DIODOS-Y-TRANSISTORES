# Formulario Teórico: Transistores de Efecto de Campo (FET)

Para todos los transistores unipolares de efecto de campo (JFET y MOSFET), independientemente de la topología o configuración del circuito de polarización, aplican estas dos condiciones ideales básicas para el análisis en corriente directa (DC):

*   **Corriente de compuerta nula:**
    $$I_G \approx 0 \text{ A}$$
    *(Nota: Debida a la polarización inversa de la unión en JFET o a la capa de óxido aislante en MOSFET).*
*   **Igualdad de corriente de drenador y fuente:**
    $$I_D = I_S$$

A continuación se presentan las ecuaciones fundamentales de análisis y diseño organizadas rigurosamente según el tipo de dispositivo y su región física de operación.

---

## 3.1. Dispositivos de Empobrecimiento: JFET y D-MOSFET

Las siguientes ecuaciones gobiernan el comportamiento eléctrico estático del Transistor de Efecto de Campo de Unión (JFET) y del MOSFET de Empobrecimiento (D-MOSFET).

### 3.1.1. Regiones Físicas de Operación

#### A. Región Lineal u Óhmica (Triodo)
Ocurre cuando el voltaje aplicado en el canal es bajo y el dispositivo se comporta esencialmente como un resistor controlado por voltaje.
*   **Condición de operación:**
    $$V_{DS} < V_{GS} - V_P$$
    *(Nota: La conducción en esta región depende fuertemente de la geometría del canal y no obedece al modelo puro de fuente de corriente).*

#### B. Región Activa o de Saturación
Esta es la región estándar para amplificación.

> **Precaución Conceptual:** En la literatura introductoria, para el JFET los términos *"estrangulamiento" (pinch-off)* y *"saturación"* se emplean de manera intercambiable. Físicamente, el *pinch-off* describe el cierre del canal, mientras que en la teoría general (y específicamente en MOSFETs), la "saturación" se define estrictamente por su frontera matemática de voltaje.

*   **Frontera de Saturación (Límite de Estrangulamiento):**
    $$V_{DS(\text{sat})} = V_{GS} - V_P$$
*   **Condición Algebraica de Saturación:**
    $$V_{DS} \ge V_{GS} - V_P$$
    *(Nota Didáctica Alternativa: En cursos introductorios, para evitar errores de signo con transistores Canal-N, se suele expresar en magnitudes absolutas: $|V_{DS}| \ge |V_P| - |V_{GS}|$)*.
*   **Ecuación de Shockley (Corriente en Saturación):**
    $$I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2$$
*   **Expresión en términos de la frontera $V_{DS(\text{sat})}$:**
    $$I_D = I_{DSS} \left(\frac{V_{DS(\text{sat})}}{V_P}\right)^2$$
    > **[!] Nota de Rigor:** Esta es una forma derivada algebraicamente al sustituir la frontera de estrangulamiento dentro de la ecuación de Shockley. Es útil **exclusivamente** para evaluaciones teóricas de la condición de saturación; **NO** es una ecuación de variable independiente para control primario o análisis de polarización estándar.

---

### 3.1.2. Transconductancia en DC (Conexión a Pequeña Señal)

La transconductancia mutua ($g_m$) vincula el análisis DC con la amplificación en AC.
*   **Transconductancia del dispositivo:**
    $$g_m = g_{m0} \left(1 - \frac{V_{GS}}{V_P}\right)$$
*   **Transconductancia máxima a $V_{GS} = 0$ ($g_{m0}$):**
    $$g_{m0} = \frac{2 I_{DSS}}{|V_P|}$$
    *(Nota: Se utiliza $|V_P|$ para asegurar un valor de ganancia positivo acorde a las convenciones de cuadripolos).*

---

### 3.1.3. Ecuaciones de Mallas de Polarización (DC)

> **Nota Metodológica:** Para los polinomios de segundo orden presentados a continuación, se emplean magnitudes absolutas ($|V_P|, |V_G|$) como notación didáctica. Esto asegura que la raíz obtenida funcione numéricamente en transistores de Canal-N sin inducir conflictos de signos. En un análisis matemático puro, se deben preservar los valores algebraicos reales y sus signos.

#### A. Configuración Fija (JFET y D-MOSFET)
Requiere dos fuentes DC ($V_{DD}$ y $V_{GG}$).
*   **Mallas del circuito:**
    $$V_{GS} = -V_{GG}$$
    $$V_{DS} = V_{DD} - I_D R_D$$

#### B. Autopolarización
Elimina $V_{GG}$ empleando una resistencia de fuente ($R_S$).
*   **Mallas del circuito:**
    $$V_G = 0 \text{ V}$$
    $$V_{GS} = -I_D R_S$$
    $$V_{DS} = V_{DD} - I_D(R_D + R_S)$$
*   **Solución Analítica Exacta (Cuadrática):**
    Resolviendo $V_{GS}$ en Shockley:
    $$A I_D^2 + B I_D + C = 0 \quad \text{donde} \quad A = R_S^2, \quad B = -\left[2 R_S |V_P| + \frac{V_P^2}{I_{DSS}}\right], \quad C = V_P^2$$
    Solución: $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$ (raíz negativa para solución físicamente realizable).
*   **Diseño de $R_S$ exacto:** Para un punto $Q$ objetivo $(I_D, V_{DS})$:
    $$R_S = \frac{-B - \sqrt{B^2 - 4AC}}{2A} \quad \text{donde} \quad A = I_D^2, \quad B = -2|V_P| I_D, \quad C = V_P^2 \left(1 - \frac{I_D}{I_{DSS}}\right)$$
    *(Resolución directa recomendada: $R_S = \frac{|V_P|}{I_D} \left(1 - \sqrt{\frac{I_D}{I_{DSS}}}\right)$)*.

#### C. Polarización por Divisor de Voltaje
Independiza parcialmente el punto Q de las características intrínsecas del JFET.
*   **Mallas del circuito:**
    $$V_G = \left(\frac{R_2}{R_1 + R_2}\right) V_{DD}$$
    $$V_{GS} = V_G - I_D R_S$$
    $$V_{DS} = V_{DD} - I_D(R_D + R_S)$$
*   **Solución Analítica Exacta (Cuadrática):**
    $$A I_D^2 + B I_D + C = 0$$
    $$A = R_S^2, \quad B = -\left[2 (|V_P| + |V_G|) R_S + \frac{V_P^2}{I_{DSS}}\right], \quad C = (|V_P| + |V_G|)^2$$
    Solución física: $I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}$
*   **Diseño para estabilización de Punto Q:** (Frente a tolerancias $I_{D1}, I_{D2}$):
    $$|V_G| = \frac{I_{D1}(|V_{GS2}| - |V_{GS1}|)}{I_{D2} - I_{D1}} - |V_{GS1}|$$
    $$R_S = \frac{|V_{GS1}| - |V_{GS2}|}{I_{D2} - I_{D1}}$$
    $$R_1 = \frac{R_2 (V_{DD} - |V_G|)}{|V_G|}$$

---

## 3.2. Dispositivos de Enriquecimiento: E-MOSFET

El MOSFET de Enriquecimiento (E-MOSFET) opera exclusivamente mejorando su conductividad; permanece en estado de corte ($I_D \approx 0$) hasta que el voltaje supera un umbral formal ($V_{GS(\text{th})}$ o $V_{th}$).

> **Nota sobre el D-MOSFET:** Las ecuaciones de polarización DC del D-MOSFET son equivalentes a las del JFET **únicamente** cuando opera en su región de empobrecimiento. A diferencia del JFET, el D-MOSFET permite polarización en región de enriquecimiento ($V_{GS} > 0$ en canal-N), rigiéndose por las mismas expansiones algebraicas.

### 3.2.1. Regiones Físicas de Operación (E-MOSFET)

#### A. Región Lineal u Óhmica (Triodo)
*   **Condición de operación:**
    $$V_{DS} < V_{GS} - V_{GS(\text{th})}$$
*   **Ecuación de control:**
    $$I_D = k \left[ (V_{GS} - V_{GS(\text{th})})V_{DS} - \frac{V_{DS}^2}{2} \right]$$

#### B. Región Activa de Saturación
*   **Condición de operación formal:**
    $$V_{DS} \ge V_{GS} - V_{GS(\text{th})}$$
*   **Ecuación de transferencia:**
    $$I_D = k \left(V_{GS} - V_{GS(\text{th})}\right)^2$$
*   **Constante física de conductancia ($k$):**
    $$k = \frac{I_{D(\text{on})}}{\left(V_{GS(\text{on})} - V_{GS(\text{th})}\right)^2}$$
    > **[!] Limitación del Modelo:** La constante $k$ y esta ecuación cuadrática representan un modelo clásico ideal de canal largo. Modelos físicos modernos (como BSIM) y simuladores exactos como SPICE consideran fenómenos críticos como la Modulación de Longitud de Canal (CLM, parámetro $\lambda$) y movilidad dependiente del campo, resultando en desviaciones numéricas.

### 3.2.2. Ecuaciones de Mallas de Polarización (E-MOSFET)

#### A. Realimentación de Drenador (Drain-Feedback Bias)
Asegura que el dispositivo siempre opere dentro de la zona activa de saturación gracias al acople de voltaje.
*   **Mallas del circuito:**
    $$V_{GS} = V_{DS} \quad (\text{satisface la condición de saturación por defecto})$$
    $$V_G = V_D \quad (\text{porque } I_G \approx 0 \text{ A, no hay caída en } R_G)$$
    $$V_{DS} = V_{DD} - I_D R_D$$

#### B. Divisor de Voltaje
Análogo al JFET, pero acoplado a la ecuación cuadrática del E-MOSFET.
*   **Mallas del circuito:**
    $$V_G = \left(\frac{R_2}{R_1 + R_2}\right) V_{DD}$$
    $$V_{GS} = V_G - I_D R_S \quad (\text{si } R_S = 0, \text{ entonces } V_{GS} = V_G)$$
    $$V_{DS} = V_{DD} - I_D(R_D + R_S)$$

---

## 4. Configuraciones de Amplificador FET (Pequeña Señal y AC)

Las siguientes clasificaciones describen las **topologías de inyección y extracción de señal (AC)** de los amplificadores implementados con transistores FET. **No** deben confundirse con el método de polarización estático DC, el cual es independiente y debe calcularse previamente.

*   **Fuente Común (Common Source):**
    *   La señal de entrada ingresa por la compuerta y la salida amplificada se extrae por el drenador. La terminal de fuente funciona como la referencia compartida en AC. Desfasa la señal $180^\circ$.
*   **Compuerta Común (Common Gate):**
    *   La señal ingresa a través de la terminal de fuente.
    *   La compuerta se encuentra desacoplada a tierra a través de un capacitor, por lo que su potencial en AC es $0 \text{ V}$.
    *   El análisis DC obedece al circuito de autopolarización modificado.
*   **Drenador Común (Common Drain / Seguidor de Fuente):**
    *   El drenador está conectado de forma directa (o por baja impedancia) a la fuente de alimentación $+V_{DD}$, convirtiéndose en la tierra de señal AC.
    *   La señal de salida se toma desde la fuente. Ofrece ganancia de tensión ligeramente menor a la unidad sin desfase, con alta capacidad de acople de corriente.

---

## 5. Parámetros Típicos y Componentes Comunes

La siguiente tabla presenta los valores y órdenes de magnitud teóricos esperados en transistores FET de silicio:

| Parámetro | Símbolo | JFET Canal-N | D-MOSFET Canal-N | E-MOSFET Canal-N | Descripción |
| :--- | :---: | :---: | :---: | :---: | :--- |
| Corriente de compuerta en CD | $I_G$ | $\approx 10^{-12} \text{ A}$ (pA) | $\approx 10^{-15} \text{ A}$ (fA) | $\approx 10^{-15} \text{ A}$ (fA) | Fuga de entrada extremadamente baja debido al aislamiento (unión inversa / capa de óxido). |
| Resistencia de entrada | $R_i$ o $Z_i$ | $10^9 \ \Omega$ ($1\text{ G}\Omega$) | $10^{12} \text{ a } 10^{15} \ \Omega$ | $10^{12} \text{ a } 10^{15} \ \Omega$ | Impedancia sumamente elevada; actúa casi como circuito abierto en DC. |
| Corriente máx. de saturación | $I_{DSS}$ | $1 \text{ a } 20 \text{ mA}$ | $1 \text{ a } 30 \text{ mA}$ | No aplica | Corriente de drenador operando con canal abierto ($V_{GS} = 0 \text{ V}$) en saturación. |
| Voltaje de estrangulamiento / umbral | $V_P$ o $V_{GS(\text{th})}$ | $V_P: -0.5 \text{ a } -8 \text{ V}$ | $V_P: -1 \text{ a } -8 \text{ V}$ | $V_{GS(\text{th})}: 0.8 \text{ a } 4 \text{ V}$ | Voltaje compuerta-fuente para interrumpir o iniciar la conducción del canal. |
| Constante de conductancia | $k$ | No aplica | No aplica | $0.1 \text{ a } 10 \text{ A/V}^2$ | Constante de amplificación geométrica típica de modelos de canal largo. |
| Voltaje de saturación | $V_{DS(\text{sat})}$ | $V_{GS} - V_P$ | $V_{GS} - V_P$ | $V_{GS} - V_{GS(\text{th})}$ | Caída mínima necesaria para que el transistor sostenga la región activa constante. |

### Transistores FET y MOSFET comunes en el laboratorio

| Transistor | Tipo | Tecnología | $I_{DSS}$ / $I_{D(\text{on})}$ | $V_P$ / $V_{GS(\text{th})}$ | $V_{DS}$ máx. | $P_D$ máx. | Aplicación típica |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **2N3819** | JFET Canal-N | Pequeña señal | $2 \text{ a } 20 \text{ mA}$ | $-0.5 \text{ a } -8 \text{ V}$ | $25 \text{ V}$ | $350 \text{ mW}$ | Amplificadores y mezcladores de RF/VHF. |
| **2N5457** | JFET Canal-N | Pequeña señal | $1 \text{ a } 5 \text{ mA}$ | $-0.5 \text{ a } -6 \text{ V}$ | $25 \text{ V}$ | $310 \text{ mW}$ | Preamplificadores de audio de muy bajo ruido. |
| **2N7000** | E-MOSFET N | Pequeña señal | $75 \text{ mA}$ (mín.) | $0.8 \text{ a } 3 \text{ V}$ | $60 \text{ V}$ | $350 \text{ mW}$ | Conmutador digital y control lógico directo. |
| **BS170** | E-MOSFET N | Pequeña señal | $500 \text{ mA}$ | $0.8 \text{ a } 3 \text{ V}$ | $60 \text{ V}$ | $830 \text{ mW}$ | Interface lógica a reles, señales de baja potencia. |
| **IRF540N** | E-MOSFET N | Potencia | $110 \text{ A}$ (pulsado) | $2.0 \text{ a } 4.0 \text{ V}$ | $100 \text{ V}$ | $130 \text{ W}$ | Conmutación robusta (motores, puentes H, fuentes). |
| **IRF9540** | E-MOSFET P | Potencia | $76 \text{ A}$ (pulsado) | $-2.0 \text{ a } -4.0 \text{ V}$ | $-100 \text{ V}$ | $140 \text{ W}$ | Conmutación de potencia (par complementario del IRF540). |

---

## 6. Glosario de Variables y Símbolos

| Símbolo | Variable | Descripción | Unidad |
| :---: | :--- | :--- | :---: |
| $I_D$ | Corriente de drenador | Corriente principal de carga que atraviesa el canal conductor. | A |
| $I_S$ | Corriente de fuente | Corriente que sale de la terminal de fuente (homóloga a $I_D$ estáticamente). | A |
| $I_G$ | Corriente de compuerta | Corriente parásita/fuga que ingresa a la compuerta. Idealmente se asume cero. | A |
| $I_{DSS}$ | Corriente de saturación | Corriente de drenaje máxima nominal cuando el canal JFET/D-MOSFET está abierto a $V_{GS}=0$. | A |
| $I_{D(\text{on})}$ | Corriente de prueba de encendido | Valor de drenador asegurado bajo una condición de voltaje de compuerta específico. | A |
| $V_G, V_D, V_S$ | Voltajes nodales | Potenciales eléctricos absolutos medidos en los terminales respecto a la tierra general. | V |
| $V_{GS}$ | Voltaje compuerta-fuente | Tensión diferencial de entrada responsable de modular el ancho/apertura del canal. | V |
| $V_{DS}$ | Voltaje drenador-fuente | Tensión diferencial de salida sobre la que se disipa la potencia estática de control. | V |
| $V_P$ | Voltaje de estrangulamiento | Valor límite $V_{GS}$ en JFETs donde se alcanza el estado de corte (*Pinch-off*). | V |
| $V_{GS(\text{th})}$ | Voltaje de umbral (*Threshold*) | Tensión $V_{GS}$ límite donde un E-MOSFET comienza a establecer un canal conductor. | V |
| $V_{DS(\text{sat})}$ | Tensión de saturación frontera | Diferencial mínimo de salida exigido para sostener la región de amplificación lineal. | V |
| $g_m$ | Transconductancia mutua | Tasa de conversión de variaciones de voltaje de entrada a corriente de salida ($g_m = \Delta I_D / \Delta V_{GS}$). | S (A/V) |
| $g_{m0}$ | Transconductancia nominal | Valor máximo de transconductancia del dispositivo, medido operando con $V_{GS} = 0 \text{ V}$. | S (A/V) |
| $k$ | Cte. de conductancia geométrica | Parámetro que modela la capacidad de conducción cuadrática de un E-MOSFET de canal largo. | $\text{A/V}^2$ |
| $R_1, R_2$ | Red divisora de voltaje | Conjunto resistivo usado para establecer un $V_G$ estable que independice el diseño del transistor. | $\Omega$ |
| $R_D$ | Resistencia de drenador | Componente de carga que transforma la corriente controlada en variaciones de tensión útiles. | $\Omega$ |
| $R_S$ | Resistencia de fuente | Elemento estabilizador térmico o elemento principal de autopolarización del circuito. | $\Omega$ |
| $Q$ | Punto de operación (Quiescente) | Estado continuo del transistor en ausencia de señal AC temporal $(V_{DS_Q}, I_{D_Q})$. | - |

---
**Bibliografía:** 
*   Boylestad, R. & Nashelsky, L. *Electronic Devices and Circuit Theory*, 11va Ed. Cap. 5 y 6.
*   Sedra, A. & Smith, K. *Microelectronic Circuits*, 7ma Ed. Cap. 5.

<!--
::METADATA::
type: reference
topic_id: transistor-fet
file_id: FORMULARIO_TEORICO
status: stable
audience: both
last_updated: 2026-05-22
-->