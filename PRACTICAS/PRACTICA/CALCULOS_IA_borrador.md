revisa el siguiente circuito y calcula los voltajes necesarios para cumplir lo siguiente, usa formulas teoricas exactas, los valores de param en la netlist son de referencia, no son los valores solicitados: 
**Objetivo.** — La presente práctica tiene como objetivo el aplicar un transistor como amplificador de señal configurado en emisor común, en donde para esto se determinarán los parámetros de pequeña señal y valores de ganancia.

### ➢ Material:

1. Transistor BC-548-B
2. Resistencias según diseño
3. Capacitores: $C_1 = 47 \, \mu\text{F}$, $C_2 = 100 \, \mu\text{F}$ y $C_3 = 10 \, \mu\text{F}$

### ➢ Equipo:

1. Multímetro digital
2. Fuente de Alimentación
3. Generador de Señales
4. Osciloscopio

### Procedimiento:

1. Diseñe un amplificador de señal con base al transistor BC 548B en configuración de emisor común, utilizando la $\beta$ mínima, $I_C = 50 \, \text{mA}$, $V_{CC} = 15 \, \text{V}$, $V_{BE} = 0.7 \, \text{V}$, $R_S = 50 \, \Omega$, $V_s = 100 \, \text{mV}$, en donde la ganancia requerida en lazo abierto es de:

$$
|A_{vo}| \ge 40
$$

2. Aplique el procedimiento visto en clase para calcular los parámetros de pequeña señal y sus ganancias.
3. Mida la ganancia de voltaje en el osciloscopio:

$$
A_v = \frac{V_o}{V_s}
$$

4. Elimine $R_{E1}$ y cambie a $R_E$ y nuevamente verifique la ganancia en voltaje total; $A_v$
5. Varíe la frecuencia del generador y observe el cambio que existe en amplitud y fase con respecto a las señales de entrada y salida.

> **[Diagrama de Circuito]:** En el fondo del documento se aprecia una marca de agua tenue que muestra el esquema de un amplificador emisor común con polarización por divisor de tensión. El circuito consta de una fuente de alimentación $V_{CC}$ de $15 \, \text{V}$, resistencias de polarización en la base ($R_1$ y $R_2$), resistencia de colector ($R_C$) y una red de emisor con resistencias de estabilización ($R_{E1}$ y $R_{E2}$ o $R_E$). Cuenta con capacitores de acoplamiento de entrada ($C_1$), de salida ($C_2$) y un capacitor de desacoplo de emisor ($C_3$).


# Netlist de SPICE — Amplificador Emisor Común

A continuación se presenta la conversión del circuito electrónico de la segunda imagen a formato de netlist compatible con simuladores tipo SPICE (LTspice, PSpice, Ngspice). 

Dado que los valores de las resistencias de polarización ($R_1$, $R_2$, $R_C$ y $R_E$) se especifican "según diseño" en la guía de la práctica, se han declarado utilizando la directiva `.param` con valores comerciales típicos a modo de marcador de posición (*placeholder*) para que la netlist sea completamente funcional desde el inicio.

```spice
* Amplificador Emisor Común - Transistor BC548B
* Conversión automatizada por MarkLaTeX

* =================================================================
* PARÁMETROS DE DISEÑO (Modificar valores según cálculos de la práctica)
* =================================================================
.param r1_val = 22k      ; Resistencia de polarización superior
.param r2_val = 4.7k     ; Resistencia de polarización inferior
.param rc_val = 1.2k     ; Resistencia de colector
.param re_val = 150      ; Resistencia de emisor (RE total)

* =================================================================
* FUENTES DE ALIMENTACIÓN Y SEÑAL
* =================================================================
* Fuente de alimentación de CD (15V)
Vcc VCC 0 DC 15V

* Generador de señales (VOFF=0, VAMPL=1mV, FREQ=1kHz)
V2 N_source 0 SIN(0 1mV 1k) AC 1mV

* =================================================================
* COMPONENTES DEL CIRCUITO
* =================================================================
* Red de entrada y acoplamiento
R5 N_source N_in 50
C1 N_in N_B 47uF

* Red de polarización y carga del transistor
R1 VCC N_B {r1_val}
R2 N_B 0 {r2_val}
RC VCC N_C {rc_val}
RE N_E 0 {re_val}
C3 N_E 0 100uF

* Transistor BJT (Conexión: Colector Base Emisor)
Q1 N_C N_B N_E BC548B

* Red de salida y carga
C2 N_C N_out 10uF
R6 N_out 0 1k

* =================================================================
* MODELO DEL TRANSISTOR Y COMANDOS DE SIMULACIÓN
* =================================================================
* Modelo estándar para el transistor NPN BC548B
.model BC548B NPN(Is=14.17f Xti=3 Eg=1.11 Vaf=100 Bf=300 Ne=1.428 Ise=14.17f 
+ Ikf=99.27m Xtb=1.5 Br=4.444 Nc=2 Isc=0 Ikr=0 Rc=1 Cjc=9.377p Mjc=.3526 
+ Vjc=.5 Fc=.5 Cje=13p Mje=.3347 Vje=.5 Tr=474.3n Tf=411.1p Itf=.17 Vtf=5 Xtf=8 Rb=10)

* Análisis propuestos:
.tran 10u 5m             ; Análisis transitorio para observar la señal en el tiempo
.ac dec 20 10 100meg     ; Respuesta en frecuencia (Amplitud y Fase)

.end
```

Saludos. Soy **Ampere Node**, experto en análisis y diseño de circuitos eléctricos. He evaluado la topología de tu diagrama, la netlist proporcionada y las especificaciones de diseño.

Aplicaré el procedimiento de diseño paso a paso utilizando fórmulas teóricas exactas para calcular las resistencias y parámetros de pequeña señal, garantizando un punto de operación (Q-point) estable y verificando el cumplimiento de la ganancia requerida.

---

### 1. Pre-Verificación y Análisis de Inconsistencias

Antes de proceder con los cálculos, es imperativo realizar un análisis de rangos físicos:

* **Corriente de Colector:** El diseño exige 50 mA. Aunque es factible teóricamente, es un valor inusualmente alto y agresivo para un BJT de pequeña señal como el BC548B (cuya máxima absoluta es de 100 mA). El transistor disipará una potencia considerable.
* **INCONSISTENCIA FÍSICA (Régimen Lineal):** La práctica solicita aplicar una señal de entrada de 100 mV. Para que el modelo de pequeña señal sea válido, el voltaje base-emisor en AC debe ser mucho menor al voltaje térmico (aproximadamente 25 mV). Una señal de 100 mV provocará severa distorsión no lineal en la salida. No obstante, procederemos con el análisis matemático lineal estricto como lo requiere la metodología académica.
* **Parámetro Beta:** Se especifica usar la beta mínima. Según la hoja de datos estándar y el grupo B del BC548, asumiremos **$\beta = 200$**.
* **Voltaje Térmico:** Utilizaremos **$V_T = 25$ mV**.

---

### 2. Análisis de Estado Estable (DC) para Diseño del Q-Point

En $t < 0$ (estado estable DC), los capacitores de acoplamiento ($C_1$, $C_2$) y desacoplo ($C_3$) se comportan como **circuitos abiertos**. Esto aísla la red de polarización.

Para garantizar la máxima excursión simétrica de la señal sin recorte y asegurar estabilidad térmica, diseñaremos los voltajes nodales bajo las heurísticas clásicas:

1. Asignamos al emisor aproximadamente el 10% de $V_{CC}$ para estabilidad térmica: **$V_E = 1.5$ V**.
2. Ubicamos el voltaje colector-emisor ($V_{CE}$) en el punto medio del voltaje restante para maximizar la excursión:

$$V_{CE} = \frac{V_{CC} - V_E}{2} = \frac{15 - 1.5}{2} = 6.75 \text{ V}$$

Con esto, el voltaje en el colector es **$V_C = 8.25$ V**. Ahora calculamos las resistencias exactas de la malla de salida usando la Ley de Ohm:

$$R_C = \frac{V_{CC} - V_C}{I_C} = \frac{15 - 8.25}{50 \text{ mA}} = 135 \, \Omega$$

Para el emisor, considerando que $I_E = I_C + I_B$:

$$I_B = \frac{I_C}{\beta} = \frac{50 \text{ mA}}{200} = 250 \, \mu\text{A}$$

$$I_E = 50 \text{ mA} + 0.25 \text{ mA} = 50.25 \text{ mA}$$

$$R_E = \frac{V_E}{I_E} = \frac{1.5 \text{ V}}{50.25 \text{ mA}} = 29.85 \, \Omega$$

**Polarización de Base ($R_1$ y $R_2$):**
El voltaje en la base es **$V_B = V_E + V_{BE} = 1.5 + 0.7 = 2.2$ V**. Para que el divisor de tensión sea rígido y no dependa de la $\beta$, la corriente que atraviesa $R_2$ debe ser al menos 10 veces $I_B$ ($I_{R2} = 2.5$ mA).

$$R_2 = \frac{V_B}{I_{R2}} = \frac{2.2 \text{ V}}{2.5 \text{ mA}} = 880 \, \Omega$$

$$R_1 = \frac{V_{CC} - V_B}{I_{R2} + I_B} = \frac{15 - 2.2}{2.75 \text{ mA}} = 4654.5 \, \Omega$$

---

### 3. Parámetros de Pequeña Señal y Diseño de Ganancia (Pasos 1 y 2)

Apagamos las fuentes independientes de voltaje DC para cortocircuitarlas y modelar la respuesta AC. Los parámetros del modelo híbrido-$\pi$ son:

$$g_m = \frac{I_C}{V_T} = \frac{50 \text{ mA}}{25 \text{ mV}} = 2 \text{ A/V} \text{ (S)}$$

$$r_\pi = \frac{\beta}{g_m} = \frac{200}{2} = 100 \, \Omega$$

**División de la Resistencia de Emisor:**
El paso 4 sugiere "eliminar $R_{E1}$ y cambiar a $R_E$". Esto implica que para lograr la ganancia controlada objetivo en el paso 1 ($|A_{vo}| \ge 40$), la resistencia de emisor DC ($29.85 \, \Omega$) debe dividirse en dos partes:

* **$R_{E1}$**: Resistencia sin desacoplar (establece la ganancia AC).
* **$R_{E2}$**: Resistencia desacoplada por $C_3$.

Si buscamos una ganancia teórica cercana a 46 para cumplir la holgura:
Elegimos **$R_{E1} = 2 \, \Omega$** y **$R_{E2} = 27.85 \, \Omega$**.

**Cálculo de Impedancias (Paso 2):**
La impedancia vista hacia la base se incrementa por la resistencia sin desacoplar:

$$Z_{in(base)} = r_\pi + (\beta + 1)R_{E1} = 100 + (201)(2) = 502 \, \Omega$$

$$Z_{in} = R_1 \parallel R_2 \parallel Z_{in(base)} = 4654.5 \parallel 880 \parallel 502 = 299 \, \Omega$$

**Cálculo de la Ganancia ($A_{vo}$):**
La ganancia total de la fuente al colector (sin incluir la carga final, tal como dictan las definiciones teóricas de lazo abierto $A_{vo}$) está sujeta al divisor resistivo en la entrada:

$$A_{vo} = \left( \frac{Z_{in}}{Z_{in} + R_S} \right) \left( \frac{-\beta R_C}{r_\pi + (\beta + 1)R_{E1}} \right)$$

$$A_{vo} = \left( \frac{299}{299 + 50} \right) \left( \frac{-200 \times 135}{502} \right) = (0.856)(-53.78) = -46.03$$

Magnitud de ganancia = **$46.03$**. Cumple perfectamente con el objetivo **$|A_{vo}| \ge 40$**.

---

### 4. Modificación de la Red de Emisor (Paso 4)

El procedimiento pide: *"Elimine $R_{E1}$ y cambie a $R_E$ y nuevamente verifique la ganancia en voltaje total"*.
Esto se refiere a colocar la totalidad de la resistencia de emisor ($29.85 \, \Omega$) en paralelo con el capacitor $C_3$, de modo que todo el emisor queda conectado a la tierra AC (Emisor Común Puro).

Al estar el emisor totalmente desacoplado, $R_{E1} = 0$:

$$Z_{in(base)} = r_\pi = 100 \, \Omega$$

$$Z_{in} = 4654.5 \parallel 880 \parallel 100 = 88.1 \, \Omega$$

La nueva atenuación en la entrada es más severa, pero la ganancia intrínseca del transistor se dispara:

$$A_v = \left( \frac{Z_{in}}{Z_{in} + R_S} \right) (-g_m R_C) = \left( \frac{88.1}{88.1 + 50} \right) (-2 \times 135)$$

$$A_v = (0.638) (-270) = -172.26$$

Al puentear completamente la resistencia de emisor con $C_3$, la magnitud de la ganancia se cuadruplica a **$172.26$**.

---

### 5. Verificación Rigurosa de Energía (Obligatoria)

Para validar la coherencia física del diseño, aplicamos la ecuación de balance de potencias, comprobando que la potencia entregada por la fuente iguale a la potencia disipada en DC:

* **Corriente total extraída de $V_{CC}$:** $I_{total} = I_C + I_{R1} = 50 \text{ mA} + 2.75 \text{ mA} = 52.75 \text{ mA}$.
* **Potencia entregada (convención pasiva):** $P_S = - (15 \text{ V} \times 52.75 \text{ mA}) = -791.25 \text{ mW}$.

**Potencias disipadas ($i^2R$ y $V \times I$):**

* $P_{R1} = (2.75 \text{ mA})^2 \times 4654.5 = 35.2 \text{ mW}$
* $P_{R2} = (2.5 \text{ mA})^2 \times 880 = 5.5 \text{ mW}$
* $P_{RC} = (50 \text{ mA})^2 \times 135 = 337.5 \text{ mW}$
* $P_{RE} = (50.25 \text{ mA})^2 \times 29.85 = 75.3 \text{ mW}$
* $P_{Q (Transistor)} = V_{CE} \times I_C = 6.75 \text{ V} \times 50 \text{ mA} = 337.5 \text{ mW}$

**Suma de potencias disipadas:** $35.2 + 5.5 + 337.5 + 75.3 + 337.5 = 791.0 \text{ mW}$.
La suma de potencias entregadas y disipadas ($\Sigma P \approx 0$) es consistente, validando topológicamente el análisis de nudos y KCL/KVL aplicado.


ahora aplica las siguientes formulas donde correponda y recalcula el circuito:  

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


Saludos. Como **Ampere Node**, procedo a recalcular el circuito aplicando rigurosamente la teoría de cuadripolos (redes de dos puertos) y los modelos equivalentes de Thévenin/Norton que has proporcionado.

Para este análisis, incorporaremos la resistencia de carga final ($R_L$) que figuraba en la netlist original (`R6 = 1 kΩ`) acoplada mediante $C_2$. Esto nos permitirá observar los verdaderos **efectos de carga (Loading Effects)** tanto en la entrada como en la salida.

---

### 1. Extracción de Parámetros del Amplificador (Cuadripolo)

Primero, consolidamos los parámetros internos del amplificador calculados en la etapa previa (usando el emisor parcialmente desacoplado con $R_{E1} = 2 \, \Omega$):

* **Resistencia de Entrada ($r_{in}$):** Es la impedancia vista desde la fuente hacia el amplificador.

$$r_{in} = R_1 \parallel R_2 \parallel [r_\pi + (\beta + 1)R_{E1}] = 4654.5 \parallel 880 \parallel 502 = \mathbf{299 \, \Omega}$$


* **Resistencia de Salida ($r_o$):** Es la resistencia vista desde la carga hacia el amplificador, anulando la fuente de señal. En un BJT ideal (ignorando el Efecto Early), $r_o$ está dominada por la resistencia de colector.

$$r_o \approx R_C = \mathbf{135 \, \Omega}$$


* **Ganancia de Voltaje en Vacío ($A_v$):** Es la ganancia interna desde las terminales de entrada de la base hasta el colector, sin conectar carga alguna.

$$A_v = \frac{-\beta R_C}{r_\pi + (\beta + 1)R_{E1}} = \frac{-200 \times 135}{502} = \mathbf{-53.78 \, \text{V/V}}$$



---

### 2. Cálculo de la Ganancia de Voltaje Total ($A_{vs}$) con Efectos de Carga

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

---

### 3. Ganancia de Corriente ($A_i$) y Ganancia de Potencia ($A_p$)

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

---

### 4. Recálculo del Paso 4 (Emisor Totalmente Desacoplado)

Si hacemos $R_{E1} = 0$ (emisor puro en AC), los parámetros del cuadripolo cambian drásticamente:

* **$r_{in}$ se desploma:** $r_{in} = 4654.5 \parallel 880 \parallel 100 = \mathbf{88.1 \, \Omega}$.
* **$A_v$ se dispara:** $A_v = -g_m R_C = -2(135) = \mathbf{-270 \, \text{V/V}}$.

El nuevo factor de atenuación de entrada es muy pobre: $\frac{88.1}{50 + 88.1} = \mathbf{0.638}$. Perdemos casi el 40% de la señal antes de que entre al amplificador por mal acoplamiento de impedancias.

$$A_{vs} = (0.638) \times (-270) \times (0.881) = \mathbf{-151.7 \, \text{V/V}}$$

Saludos. Como **Ampere Node**, he recopilado y estructurado los resultados de los cálculos analíticos previos en las tablas solicitadas.

Aquí tienes el resumen exacto de los valores de las resistencias diseñadas para cumplir con el punto de operación (Q-Point a $I_C = 50 \text{ mA}$) y la comparativa de los parámetros de pequeña señal antes y después de modificar la red de emisor (Paso 4 de tu práctica).

### Tabla 1: Valores de Resistencias (Diseño DC Inicial)

Estos valores garantizan la estabilidad térmica, centran el voltaje colector-emisor ($V_{CE} = 6.75 \text{ V}$) para máxima excursión simétrica y preparan el circuito para cumplir la ganancia requerida.

| Componente | Valor Calculado ($\Omega$) | Función en el Circuito |
| --- | --- | --- |
| **$R_1$** | $4654.5$ | Resistencia superior del divisor de polarización de base. |
| **$R_2$** | $880.0$ | Resistencia inferior del divisor de polarización de base. |
| **$R_C$** | $135.0$ | Resistencia de colector (fija el voltaje $V_C$ y domina $r_o$). |
| **$R_E$ (Total)** | $29.85$ | Resistencia total de emisor para DC ($V_E \approx 1.5 \text{ V}$). |
| **$R_{E1}$** | $2.0$ | Fracción de $R_E$ **sin desacoplar** (fija la ganancia inicial $A_{vo} \ge 40$). |
| **$R_{E2}$** | $27.85$ | Fracción de $R_E$ **desacoplada** por el capacitor $C_3$. |

---

### Tabla 2: Comparativa de Parámetros (Efecto del Paso 4)

El "Paso 4" de tu procedimiento indica eliminar $R_{E1}$ y dejar únicamente $R_E$ (lo que implica que toda la resistencia de emisor de $29.85 \, \Omega$ queda en paralelo con $C_3$, puenteándola completamente en corriente alterna, es decir, $R_{E1} = 0 \, \Omega$).

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


realiza las tablas de los valores de las 4 resistencias en el circuito inicial y los parametros que se modifican una vez se quita R_11 y R_E como lo señala la practica: # INSTITUTO TECNOLOGICO DE TOLUCA

## Diodos y Transistores
### Examen Práctico UNIDAD-IV

**Objetivo.** — La presente práctica tiene como objetivo el aplicar un transistor como amplificador de señal configurado en emisor común, en donde para esto se determinarán los parámetros de pequeña señal y valores de ganancia.

### ➢ Material:

1. Transistor BC-548-B
2. Resistencias según diseño
3. Capacitores: $C_1 = 47 \, \mu\text{F}$, $C_2 = 100 \, \mu\text{F}$ y $C_3 = 10 \, \mu\text{F}$

### ➢ Equipo:

1. Multímetro digital
2. Fuente de Alimentación
3. Generador de Señales
4. Osciloscopio

### Procedimiento:

1. Diseñe un amplificador de señal con base al transistor BC 548B en configuración de emisor común, utilizando la $\beta$ mínima, $I_C = 50 \, \text{mA}$, $V_{CC} = 15 \, \text{V}$, $V_{BE} = 0.7 \, \text{V}$, $R_S = 50 \, \Omega$, $V_s = 100 \, \text{mV}$, en donde la ganancia requerida en lazo abierto es de:

$$
|A_{vo}| \ge 40
$$

2. Aplique el procedimiento visto en clase para calcular los parámetros de pequeña señal y sus ganancias.
3. Mida la ganancia de voltaje en el osciloscopio:

$$
A_v = \frac{V_o}{V_s}
$$

4. Elimine $R_{E1}$ y cambie a $R_E$ y nuevamente verifique la ganancia en voltaje total; $A_v$
5. Varíe la frecuencia del generador y observe el cambio que existe en amplitud y fase con respecto a las señales de entrada y salida.

> **[Diagrama de Circuito]:** En el fondo del documento se aprecia una marca de agua tenue que muestra el esquema de un amplificador emisor común con polarización por divisor de tensión. El circuito consta de una fuente de alimentación $V_{CC}$ de $15 \, \text{V}$, resistencias de polarización en la base ($R_1$ y $R_2$), resistencia de colector ($R_C$) y una red de emisor con resistencias de estabilización ($R_{E1}$ y $R_{E2}$ o $R_E$). Cuenta con capacitores de acoplamiento de entrada ($C_1$), de salida ($C_2$) y un capacitor de desacoplo de emisor ($C_3$).


# Netlist de SPICE — Amplificador Emisor Común

A continuación se presenta la conversión del circuito electrónico de la segunda imagen a formato de netlist compatible con simuladores tipo SPICE (LTspice, PSpice, Ngspice). 

Dado que los valores de las resistencias de polarización ($R_1$, $R_2$, $R_C$ y $R_E$) se especifican "según diseño" en la guía de la práctica, se han declarado utilizando la directiva `.param` con valores comerciales típicos a modo de marcador de posición (*placeholder*) para que la netlist sea completamente funcional desde el inicio.

```spice
* Amplificador Emisor Común - Transistor BC548B
* Conversión automatizada por MarkLaTeX

* =================================================================
* PARÁMETROS DE DISEÑO (Modificar valores según cálculos de la práctica)
* =================================================================
.param r1_val = 22k      ; Resistencia de polarización superior
.param r2_val = 4.7k     ; Resistencia de polarización inferior
.param rc_val = 1.2k     ; Resistencia de colector
.param re_val = 150      ; Resistencia de emisor (RE total)

* =================================================================
* FUENTES DE ALIMENTACIÓN Y SEÑAL
* =================================================================
* Fuente de alimentación de CD (15V)
Vcc VCC 0 DC 15V

* Generador de señales (VOFF=0, VAMPL=1mV, FREQ=1kHz)
V2 N_source 0 SIN(0 1mV 1k) AC 1mV

* =================================================================
* COMPONENTES DEL CIRCUITO
* =================================================================
* Red de entrada y acoplamiento
R5 N_source N_in 50
C1 N_in N_B 47uF

* Red de polarización y carga del transistor
R1 VCC N_B {r1_val}
R2 N_B 0 {r2_val}
RC VCC N_C {rc_val}
RE N_E 0 {re_val}
C3 N_E 0 100uF

* Transistor BJT (Conexión: Colector Base Emisor)
Q1 N_C N_B N_E BC548B

* Red de salida y carga
C2 N_C N_out 10uF
R6 N_out 0 1k

* =================================================================
* MODELO DEL TRANSISTOR Y COMANDOS DE SIMULACIÓN
* =================================================================
* Modelo estándar para el transistor NPN BC548B
.model BC548B NPN(Is=14.17f Xti=3 Eg=1.11 Vaf=100 Bf=300 Ne=1.428 Ise=14.17f 
+ Ikf=99.27m Xtb=1.5 Br=4.444 Nc=2 Isc=0 Ikr=0 Rc=1 Cjc=9.377p Mjc=.3526 
+ Vjc=.5 Fc=.5 Cje=13p Mje=.3347 Vje=.5 Tr=474.3n Tf=411.1p Itf=.17 Vtf=5 Xtf=8 Rb=10)

* Análisis propuestos:
.tran 10u 5m             ; Análisis transitorio para observar la señal en el tiempo
.ac dec 20 10 100meg     ; Respuesta en frecuencia (Amplitud y Fase)

.end
```
---

si decido colocar las resistencias de R_C y R_E a 100 ohms ambas, que cambia y como se amortigua el efecto de un transistor con beta alta (entre 300 a 450)? realiza los calculos


Saludos. Como **Ampere Node**, analizo tu propuesta de modificar la topología ajustando **$R_C = 100 \, \Omega$** y **$R_E = 100 \, \Omega$**.

Este es un excelente ejercicio de diseño. Al incrementar el valor de la resistencia de emisor a $100 \, \Omega$, estás introduciendo un fenómeno conocido como **Realimentación Negativa en DC (Degeneración de Emisor)**.

A continuación, te explico teóricamente cómo este cambio "amortigua" las variaciones de un transistor con beta alta y realizo los cálculos exactos para demostrarlo.

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


con estos nuevos valores calcula 2 variantes, los calculos teoricos (con los valores de R_E y R_C = 100 ohms) y los practicos (las resistencias mas cercanas a esos valores teoricos anteriores) del circuito para el divisor de voltaje que va a la base del BC548B, presenta el resultado en 2 tablas 

Saludos. Como **Ampere Node**, procedo a realizar el diseño exacto del divisor de voltaje para las nuevas condiciones ($R_C = 100 \, \Omega$ y $R_E = 100 \, \Omega$) buscando una corriente de colector $I_C = 50 \text{ mA}$.

### Criterio de Diseño (Divisor Rígido)

Para garantizar la estabilidad (que el divisor de voltaje no se "caiga" al conectar la base del transistor), aplicamos la regla de diseño robusto: la corriente que fluye por $R_2$ debe ser al menos 10 veces la corriente máxima de base esperada.

* Asumiendo el peor caso ($\beta_{min} = 200$), la corriente de base es $I_B = 50 \text{ mA} / 200 = 0.25 \text{ mA}$.
* Fijamos la corriente del divisor $I_{R2} = 2.5 \text{ mA}$.

Con $V_E \approx 5.0 \text{ V}$ (por la caída en $R_E$), requerimos un voltaje en la base $V_B = 5.7 \text{ V}$.

---

### TABLA 1: Variante Teórica Exacta

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

---

### TABLA 2: Variante Práctica (Valores Comerciales Serie E12)

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

### Conclusión de Implementación

Si montas este circuito en la protoboard (Paso 1 de tu práctica) utilizando $R_1 = 3.3 \text{ k}\Omega$, $R_2 = 2.2 \text{ k}\Omega$, y $R_C = R_E = 100 \, \Omega$, lograrás el punto de operación deseado de $50 \text{ mA}$ a la primera, sin necesidad de calibración, siendo inmune a si tu BC548B específico tiene una ganancia $\beta$ de 200, 300 o 450.