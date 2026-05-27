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

A continuación se presenta la conversión del circuito electrónico a formato de netlist compatible con simuladores tipo SPICE (LTspice, PSpice, Ngspice). 

Dado que los valores de las resistencias de polarización ($R_1$, $R_2$, $R_C$ y $R_E$) se especifican "según diseño" en la guía de la práctica, se han declarado utilizando la directiva `.param` con valores comerciales típicos a modo de marcador de posición (*placeholder*) para que la netlist sea completamente funcional desde el inicio.

```spice
* Amplificador Emisor Común - Transistor BC548B

* =================================================================
* PARÁMETROS DE DISEÑO (Modificar valores según cálculos de la práctica)
* =================================================================
.param r1_val = 22k      ; Resistencia de polarización superior
.param r2_val = 4.7k     ; Resistencia de polarización inferior
.param rc_val = 1.2k     ; Resistencia de colector
.param re_val = 150      ; Resistencia de emisor (RE total)

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
.tran 10u 5m             ; Análisis transitorio para observar la señal en el tiempo
.ac dec 20 10 100meg     ; Respuesta en frecuencia (Amplitud y Fase)

.end
```

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
