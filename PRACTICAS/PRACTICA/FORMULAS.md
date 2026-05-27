<!--
::METADATA::
type: reference
topic_id: AMP
file_id: FORMULAS
status: stable
audience: both
last_updated: 2026-05-26
-->

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

NOTA: Valor usado para transistor BC548B: 
.model BC548B_Custom NPN(IS=7.049E-15 ISE=6.8E-14 NE=1.576 BF=290 IKF=0.08157 VAF=62.79 ISC=1.24E-14 NC=1.835 BR=1 IKR=3.924 RC=0.9747 XTB=1.5 EG=1.11 XTI=3 CJE=1.15E-11 VJE=0.5 MJE=0.6715 TF=4.102E-10 XTF=40.06 VTF=10 ITF=1.491 CJC=5.25E-12 VJC=0.5697 MJC=0.3147 TR=1.00E-08 FC=0.5 NK=0.4767 Vceo=30 Icrating=100m mfg=NeruDev)