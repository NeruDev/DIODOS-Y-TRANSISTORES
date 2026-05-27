# Fórmulas y Modelos para el Análisis y Diseño de Amplificadores

Este documento presenta de forma estructurada las fórmulas fundamentales para el análisis de circuitos amplificadores lineales, basándose en la teoría de cuadripolos (redes de dos puertos). Se incluyen explicaciones teóricas, nomenclatura estándar y valores típicos esperados en la práctica.

---

## 1. Parámetros Fundamentales del Amplificador

Las métricas más básicas de un amplificador describen cuánto aumenta la señal de entrada en términos de voltaje, corriente y potencia.

### 1.1 Ganancia de Voltaje ($A_v$)
Es la relación entre el cambio en el voltaje de salida y el cambio en el voltaje de entrada.

$$
A_v = \frac{\Delta V_o}{\Delta V_{in}} = \frac{v_o}{v_{in}}
$$

* **Nomenclatura:** 
  * $v_o$: Voltaje de salida (ac).
  * $v_{in}$: Voltaje de entrada en las terminales del amplificador (ac).
* **Valores típicos:** Dependen fuertemente del tipo de amplificador y su topología (Ej. Emisor Común: 10 a 500 V/V). A menudo se expresa en decibelios (dB) como $20 \log_{10}(|A_v|)$.

### 1.2 Ganancia de Corriente ($A_i$)
Es la relación entre la corriente entregada a la carga y la corriente absorbida en la entrada.

$$
A_i = \frac{\Delta I_o}{\Delta I_{in}} = \frac{i_{o\text{(rms)}}}{i_{in\text{(rms)}}}
$$

### 1.3 Ganancia de Potencia ($A_p$)
Es la relación entre la potencia entregada a la carga y la potencia de entrada absorbida por el amplificador. Se puede calcular multiplicando las ganancias de voltaje y corriente.

$$
A_p = \frac{P_o}{P_{in}} = A_v A_i
$$

* **Cálculo de potencias en AC:**
  * Potencia de entrada: $P_{in} = V_{in\text{(rms)}} \cdot I_{in\text{(rms)}} = \frac{V_{in\text{(rms)}}^2}{R_{in}} = I_{in\text{(rms)}}^2 \cdot R_{in}$
  * Potencia de salida: $P_o = V_{o\text{(rms)}} \cdot I_{o\text{(rms)}} = \frac{V_{o\text{(rms)}}^2}{R_L} = I_{o\text{(rms)}}^2 \cdot R_L$

---

## 2. Impedancias de Entrada y Salida

La manera en que el amplificador interactúa con la fuente de señal (micrófono, antena, otra etapa) y la carga (altavoz, motor, siguiente etapa) depende de sus resistencias de entrada y salida.

### 2.1 Resistencia de Entrada ($R_{in}$ o $r_{in}$)
Representa la carga que el amplificador le presenta a la fuente de señal. Se puede medir en corriente directa (cd) o alterna (ac).

$$
R_{in} = \frac{V_{in}}{I_{in}} \text{ (cd)} \quad ; \quad r_{in} = \frac{v_{in}}{i_{in}} \text{ (ac)}
$$

* **Valores teóricos ideales:** Para un amplificador de voltaje ideal, $r_{in} \to \infty$. Para un amplificador de corriente, $r_{in} \to 0$.
* **Valores prácticos:** BJT (Emisor Común) $\approx 1 \text{ k}\Omega - 10 \text{ k}\Omega$; FET o MOSFET $\approx 1 \text{ M}\Omega$ a decenas de $\text{M}\Omega$.

### 2.2 Resistencia de Salida ($r_o$)
Representa la resistencia interna del amplificador vista desde la carga.

$$
r_o = \frac{v_o}{i_o} \text{ (Con la entrada en corto/abierta según el modelo)}
$$

* **Valores teóricos ideales:** Para un amplificador de voltaje ideal, $r_o \to 0$. Para un amplificador de corriente ideal, $r_o \to \infty$.

---

## 3. Efectos de Carga (Loading Effects) y Modelos Equivalentes

Cuando un amplificador se conecta a una fuente de señal real (con resistencia interna $r_s$) y a una carga finita ($R_L$), las ganancias efectivas disminuyen. Para analizar esto se usan los modelos equivalentes de Thévenin y Norton.

### 3.1 Modelo de Thévenin (Amplificador de Voltaje)

En la entrada se forma un divisor de tensión entre la fuente y el amplificador:

$$
v_{in} = v_s \left( \frac{r_{in}}{r_s + r_{in}} \right)
$$

En la salida se forma otro divisor de tensión entre la salida del amplificador y la carga:

$$
v_L = v_o \left( \frac{R_L}{r_o + R_L} \right) = A_v v_{in} \left( \frac{R_L}{r_o + R_L} \right)
$$

**Ganancia de Voltaje Total ($A_{vs}$)**
Es la ganancia desde la fuente de señal original ($v_s$) hasta la carga ($v_L$):

$$
A_{vs} = \frac{v_L}{v_s} = \left( \frac{r_{in}}{r_s + r_{in}} \right) A_v \left( \frac{R_L}{r_o + R_L} \right)
$$

### 3.2 Modelo de Norton (Amplificador de Corriente)

En la entrada, la corriente de la fuente se divide entre su resistencia interna y la del amplificador:

$$
i_{in} = i_s \left( \frac{r_s}{r_s + r_{in}} \right)
$$

En la salida, la corriente generada se divide entre la resistencia interna de salida y la carga:

$$
i_L = i_o \left( \frac{r_o}{r_o + R_L} \right) = A_i i_{in} \left( \frac{r_o}{r_o + R_L} \right)
$$

**Ganancia de Corriente Total ($A_{is}$)**
Es la relación entre la corriente en la carga y la corriente total de la fuente:

$$
A_{is} = \frac{i_L}{i_s} = \left( \frac{r_s}{r_s + r_{in}} \right) A_i \left( \frac{r_o}{r_o + R_L} \right)
$$

---

## 4. Tipos Ideales de Amplificadores (Resumen de Diseño)

Al diseñar o elegir una topología, es fundamental entender el objetivo del circuito:

| Tipo de Amplificador | Ganancia Fundamental | $R_{in}$ Ideal | $R_o$ Ideal | Equivalente Práctico |
|----------------------|----------------------|----------------|-------------|----------------------|
| **Voltaje** | $A_v = v_o / v_{in}$ | $\infty$ | $0$ | Op-Amp, Colector Común (buffer) |
| **Corriente** | $A_i = i_o / i_{in}$ | $0$ | $\infty$ | Base Común |
| **Transconductancia**| $G_m = i_o / v_{in}$ | $\infty$ | $\infty$ | FET, MOSFET |
| **Transresistencia** | $R_m = v_o / i_{in}$ | $0$ | $0$ | Amplificador de fotodiodo |

---

## 5. Señales en el Dominio del Tiempo

La señal total en un amplificador lineal suele ser la superposición de un nivel de polarización en corriente continua (DC) y una pequeña señal alterna (AC).

$$
v_o(t) = V_B + A \sin(\omega t)
$$

Donde:
* $V_B$: Nivel de voltaje en DC (punto de operación $Q$).
* $A$: Amplitud máxima de la señal AC amplificada.
* $\omega$: Frecuencia angular de la señal ( $\omega = 2\pi f$ ).

> **Nota de diseño:** El punto de operación $V_B$ debe estar centrado para permitir la máxima excursión simétrica de la señal AC (swing) sin entrar en zonas de corte o saturación del transistor.

---

### Análisis de Cuadripolos (Redes de dos puertos)

Para este análisis, incorporaremos la resistencia de carga final ($R_L$) que figuraba en la netlist original (`R6 = 1 kΩ`) acoplada mediante $C_2$. Esto nos permitirá observar los verdaderos **efectos de carga (Loading Effects)** tanto en la entrada como en la salida.

#### 1. Extracción de Parámetros del Amplificador (Cuadripolo)

Primero, consolidamos los parámetros internos del amplificador calculados en la etapa previa (usando el emisor parcialmente desacoplado con $R_{E1} = 2 \, \Omega$):

* **Resistencia de Entrada ($r_{in}$):** Es la impedancia vista desde la fuente hacia el amplificador.

$$r_{in} = R_1 \parallel R_2 \parallel [r_\pi + (\beta + 1)R_{E1}] = 4654.5 \parallel 880 \parallel 502 = \mathbf{299 \, \Omega}$$

* **Resistencia de Salida ($r_o$):** Es la resistencia vista desde la carga hacia el amplificador, anulando la fuente de señal. En un BJT ideal (ignorando el Efecto Early), $r_o$ está dominada por la resistencia de colector.

$$r_o \approx R_C = \mathbf{135 \, \Omega}$$

* **Ganancia de Voltaje en Vacío ($A_v$):** Es la ganancia interna desde las terminales de entrada de la base hasta el colector, sin conectar carga alguna.

$$A_v = \frac{-\beta R_C}{r_\pi + (\beta + 1)R_{E1}} = \frac{-200 \times 135}{502} = \mathbf{-53.78 \, \text{V/V}}$$

#### 2. Cálculo de la Ganancia de Voltaje Total ($A_{vs}$) con Efectos de Carga

Aplicamos el **Modelo de Thévenin** para calcular las pérdidas por división de tensión en la entrada y en la salida.

* **Datos externos:** $r_s = 50 \, \Omega$, $R_L = 1000 \, \Omega$, $v_s = 100 \, \text{mV (pico)}$.

**A. Factor de Atenuación de Entrada:**

$$v_{in} = v_s \left( \frac{r_{in}}{r_s + r_{in}} \right) = 100 \text{ mV} \left( \frac{299}{50 + 299} \right) = 100 \text{ mV} (0.8567) = \mathbf{85.67 \, \text{mV}}$$

*(Se pierde un 14.3% de la señal en la resistencia interna del generador).*

**B. Factor de Atenuación de Salida:**

$$v_L = v_o \left( \frac{R_L}{r_o + R_L} \right) = v_o \left( \frac{1000}{135 + 1000} \right) = v_o (0.881)$$

*(Se pierde un 11.9% de la señal en la resistencia interna de salida del amplificador).*

**C. Ganancia de Voltaje Total ($A_{vs}$):**

$$A_{vs} = \frac{v_L}{v_s} = \left( \frac{r_{in}}{r_s + r_{in}} \right) A_v \left( \frac{R_L}{r_o + R_L} \right) = (0.8567) \times (-53.78) \times (0.881) = \mathbf{-40.59 \, \text{V/V}}$$

> **Verificación (Sanity Check):** $|A_{vs}| = 40.59$. Incluso después de las caídas de tensión por acoplamiento (Loading Effects), el sistema completo supera el requerimiento del diseño de la práctica de **$|A_v| \ge 40$**.

#### 3. Ganancia de Corriente ($A_i$) y Ganancia de Potencia ($A_p$)

**A. Ganancia de Corriente:**
Calculamos las corrientes de entrada y salida reales en ac:

* Corriente de entrada: $i_{in} = \frac{v_{in}}{r_{in}} = \frac{85.67 \text{ mV}}{299 \, \Omega} = 0.2865 \, \text{mA}$ (pico).
* Voltaje en la carga: $v_L = A_{vs} \cdot v_s = -40.59 \cdot 100 \text{ mV} = -4.059 \, \text{V}$ (pico).
* Corriente de salida: $i_o = \frac{v_L}{R_L} = \frac{-4.059 \text{ V}}{1000 \, \Omega} = -4.059 \, \text{mA}$ (pico).

$$A_i = \frac{i_o}{i_{in}} = \frac{-4.059 \text{ mA}}{0.2865 \text{ mA}} = \mathbf{-14.16 \, \text{A/A}}$$

**B. Ganancia de Potencia:**
Usando valores RMS (dividimos los picos por $\sqrt{2}$ para potencia promedio AC):

* Potencia de entrada: $P_{in} = \frac{(v_{in}/\sqrt{2})^2}{r_{in}} = \frac{(0.08567 / \sqrt{2})^2}{299} = \mathbf{12.27 \, \mu\text{W}}$
* Potencia de salida: $P_o = \frac{(v_L/\sqrt{2})^2}{R_L} = \frac{(4.059 / \sqrt{2})^2}{1000} = \mathbf{8.237 \, \text{mW}}$

$$A_p = \frac{P_o}{P_{in}} = \frac{8.237 \times 10^{-3}}{12.27 \times 10^{-6}} = \mathbf{671.3 \, \text{W/W}}$$

*(Nota: Como comprobación teórica, $A_p$ también puede calcularse como la ganancia de voltaje efectiva de la base a la carga $|v_L/v_{in}| \times |A_i| \approx 47.38 \times 14.16 = 670.9$. Los resultados son consistentes).*

#### 4. Recálculo del Paso 4 (Emisor Totalmente Desacoplado)

Si hacemos $R_{E1} = 0$ (emisor puro en AC), los parámetros del cuadripolo cambian drásticamente:

* **$r_{in}$ se desploma:** $r_{in} = 4654.5 \parallel 880 \parallel 100 = \mathbf{88.1 \, \Omega}$.
* **$A_v$ se dispara:** $A_v = -g_m R_C = -2(135) = \mathbf{-270 \, \text{V/V}}$.

El nuevo factor de atenuación de entrada es muy pobre: $\frac{88.1}{50 + 88.1} = \mathbf{0.638}$. Perdemos casi el 40% de la señal antes de que entre al amplificador por mal acoplamiento de impedancias.

$$A_{vs} = (0.638) \times (-270) \times (0.881) = \mathbf{-151.7 \, \text{V/V}}$$

---

### Resumen de Cálculos y Tablas Comparativas

Aquí tienes el resumen exacto de los valores de las resistencias diseñadas para cumplir con el punto de operación (Q-Point a $I_C = 50 \text{ mA}$) y la comparativa de los parámetros de pequeña señal antes y después de modificar la red de emisor (Paso 4 de tu práctica).

#### Tabla 1: Valores de Resistencias (Diseño DC Inicial)

Estos valores garantizan la estabilidad térmica, centran el voltaje colector-emisor ($V_{CE} = 6.75 \text{ V}$) para máxima excursión simétrica y preparan el circuito para cumplir la ganancia requerida.

| Componente | Valor Calculado ($\Omega$) | Función en el Circuito |
| --- | --- | --- |
| **$R_1$** | $4654.5$ | Resistencia superior del divisor de polarización de base. |
| **$R_2$** | $880.0$ | Resistencia inferior del divisor de polarización de base. |
| **$R_C$** | $135.0$ | Resistencia de colector (fija el voltaje $V_C$ y domina $r_o$). |
| **$R_E$ (Total)** | $29.85$ | Resistencia total de emisor para DC ($V_E \approx 1.5 \text{ V}$). |
| **$R_{E1}$** | $2.0$ | Fracción de $R_E$ **sin desacoplar** (fija la ganancia inicial $A_{vo} \ge 40$). |
| **$R_{E2}$** | $27.85$ | Fracción de $R_E$ **desacoplada** por el capacitor $C_3$. |

#### Tabla 2: Comparativa de Parámetros (Efecto del Paso 4)

El "Paso 4" del procedimiento indica eliminar $R_{E1}$ y dejar únicamente $R_E$ (lo que implica que toda la resistencia de emisor de $29.85 \, \Omega$ queda en paralelo con $C_3$, puenteándola completamente en corriente alterna, es decir, $R_{E1} = 0 \, \Omega$).

Aquí se muestran los parámetros del cuadripolo en ambos escenarios, asumiendo $R_S = 50 \, \Omega$ y una carga acoplada $R_L = 1 \text{ k}\Omega$.

| Parámetro (AC) | Circuito Inicial (Con $R_{E1} = 2 \, \Omega$) | Circuito Modificado ($R_{E1} = 0 \, \Omega$) | Impacto Físico / Observación |
| --- | --- | --- | --- |
| **Impedancia de entrada ($r_{in}$)** | $299 \, \Omega$ | $88.1 \, \Omega$ | **Caída drástica.** Al quitar $R_{E1}$, se pierde el efecto multiplicador de $(\beta+1)$ en la base. |
| **Atenuación de entrada ($v_{in}/v_s$)** | $0.856$ (Pasa el $85.6\%$) | $0.638$ (Pasa el $63.8\%$) | **Empeora el acoplamiento.** Mayor pérdida de señal en la resistencia interna del generador ($R_s$). |
| **Ganancia interna ($A_v$)** | $-53.78 \text{ V/V}$ | $-270.0 \text{ V/V}$ | **Aumento máximo.** La ganancia interna salta al límite teórico dependiente solo de $g_m$ y $R_C$. |
| **Ganancia fuente-colector ($A_{vo}$)** *(Req: $\ge 40$)* | $-46.03 \text{ V/V}$ | $-172.26 \text{ V/V}$ | Ambas cumplen la práctica, pero la modificada es inestable ante variaciones térmicas de $\beta$. |
| **Ganancia Total con carga ($A_{vs}$)** | $\mathbf{-40.59 \text{ V/V}}$ | $\mathbf{-151.7 \text{ V/V}}$ | Ganancia real medida de extremo a extremo (Generador $\to$ Carga de 1k$\Omega$). |

### Conclusión Técnica del Análisis

La práctica ilustra un compromiso clásico de diseño en electrónica analógica (Trade-off):

1. **Con $R_{E1}$ (Emisor parcialmente desacoplado):** Sacrificas ganancia total, pero obtienes una mayor impedancia de entrada, menor pérdida por acoplamiento con la fuente y una ganancia altamente lineal y estable que no depende fuertemente de la temperatura.
2. **Sin $R_{E1}$ (Emisor totalmente desacoplado):** Obtienes una ganancia de voltaje masiva (se cuadruplica), pero la impedancia de entrada se desploma, causando un grave "efecto de carga" en el generador de señales. Además, ante la señal de entrada solicitada de $100 \text{ mV}$, esta configuración provocará que el transistor entre en saturación o corte severo, generando una onda fuertemente distorsionada (recortada) en el osciloscopio, ya que $151.7 \times 100 \text{ mV} = 15.17 \text{ V}$, superando el límite físico de la fuente $V_{CC}$ de $15 \text{ V}$.
