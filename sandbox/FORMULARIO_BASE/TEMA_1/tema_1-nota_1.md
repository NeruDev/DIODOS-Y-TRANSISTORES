<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_1
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para el Análisis de Diodos: Recta de Carga y Pequeña Señal

Este documento recopila y estructura las ecuaciones y modelos matemáticos fundamentales para el análisis de circuitos con diodos en corriente continua (DC) y corriente alterna (AC) bajo el régimen de pequeña señal. Está diseñado como una guía de referencia rápida que detalla la nomenclatura estándar, valores típicos y el sustento teórico de cada fórmula extraída de la Nota 1.

---

## 1. Recta de Carga en Corriente Continua (DC)

La recta de carga representa la restricción lineal impuesta por el circuito externo al diodo. Permite resolver gráficamente el punto de operación pasivo o punto de reposo (punto Q) al intersectarse con la curva exponencial del dispositivo.

### 1.1 Ecuación de la Malla (LVK)
Derivada de la Ley de Tensiones de Kirchhoff aplicada a una malla serie simple que contiene una fuente, una resistencia y el diodo.

$$
V_{in} - I_D R - V_D = 0
$$

### 1.2 Ecuación Explícita de la Recta de Carga
Expresión reordenada bajo la forma lineal $y = mx + b$, donde la corriente es la variable dependiente ($y = I_D$) y la tensión es la variable independiente ($x = V_D$).

$$
I_D = -\frac{1}{R} \cdot V_D + \frac{V_{in}}{R}
$$

* **Nomenclatura:**
  * $V_{in}$: Tensión continua de la fuente de entrada (V).
  * $I_D$: Corriente continua a través del diodo (A).
  * $V_D$: Caída de tensión continua en terminales del diodo (V).
  * $R$: Resistencia limitadora conectada en serie ($\Omega$).
* **Parámetros de la Recta:**
  * **Pendiente ($m$):** $-1/R$. Representa la conductancia del circuito externo.
  * **Ordenada al origen ($b$):** $V_{in}/R$. Corriente máxima teórica si el diodo fuese un cortocircuito ideal.

### 1.3 Puntos Extremos de la Recta de Carga
Puntos de intersección límite con los ejes coordenados empleados para trazar la recta en el plano $I_D - V_D$.

* **Intersección con el Eje Y (Diodo en Cortocircuito, $V_D = 0$):**
  $$
  \left(0, \;\frac{V_{in}}{R}\right)
  $$
* **Intersección con el Eje X (Diodo en Circuito Abierto, $I_D = 0$):**
  $$
  \left(V_{in}, \; 0\right)
  $$

---

## 2. Parámetros del Diodo y Resistencia Dinámica

La linealización del comportamiento no lineal del diodo en torno a su punto de operación DC requiere la determinación de su resistencia dinámica de pequeña señal.

### 2.1 Ecuación de Shockley (Curva Característica Exponencial)
Describe la corriente total a través de la unión PN bajo polarización directa o inversa.

$$
I_D = I_S \left( e^{\frac{V_D}{n V_T}} - 1 \right)
$$

### 2.2 Derivada de la Corriente del Diodo
Pendiente de la curva de corriente en cualquier voltaje dado, simplificada bajo polarización directa activa ($I_D \gg I_S$).

$$
\frac{dI_D}{dV_D} = \frac{I_S}{n V_T} \cdot e^{\frac{V_D}{n V_T}} \approx \frac{I_D}{n V_T}
$$

### 2.3 Resistencia Dinámica o de Pequeña Señal ($r_d$)
Es la resistencia lineal equivalente del diodo para variaciones infinitesimales de tensión y corriente en torno al punto Q de polarización ($I_D = I_{DQ}$). Es la recíproca de la derivada evaluada en Q.

$$
r_d \approx \frac{n V_T}{I_{DQ}}
$$

* **Nomenclatura:**
  * $I_S$: Corriente de saturación inversa del diodo (A). Típicamente entre $10^{-15}\text{ A}$ y $10^{-9}\text{ A}$.
  * $V_T$: Voltaje térmico (V).
  * $n$: Factor de idealidad del diodo (adimensional). Varía entre $1$ (para silicio en condiciones ideales) y $2$.
  * $I_{DQ}$: Corriente de polarización en el punto Q (A).
* **Valores típicos de $r_d$:**
  * Para $I_{DQ} = 1\text{ mA}$ y $n=1$, $r_d \approx 26\ \Omega$.
  * Para $I_{DQ} = 10\text{ mA}$ y $n=1$, $r_d \approx 2.6\ \Omega$.
  * *Nota de diseño:* A mayor corriente de polarización en el punto Q ($I_{DQ}$), menor será la resistencia de pequeña señal, lo que reduce la atenuación de la señal AC sobre el componente.

### 2.4 Voltaje Térmico ($V_T$)
Voltaje equivalente a la energía térmica de los portadores de carga a una temperatura dada.

$$
V_T = \frac{k T}{q}
$$

* **Nomenclatura:**
  * $k$: Constante de Boltzmann ($1.3806 \times 10^{-23}\text{ J/K}$).
  * $T$: Temperatura absoluta en Kelvin ($\text{K} = {^\circ\text{C}} + 273.15$).
  * $q$: Carga eléctrica del electrón ($1.6022 \times 10^{-19}\text{ C}$).
* **Valores de referencia:**
  * A temperatura ambiente estándar ($T = 25^\circ\text{C} = 298.15\text{ K}$): $V_T \approx 25.69\text{ mV} \approx 26\text{ mV}$.

---

## 3. Análisis de Pequeña Señal (AC)

Bajo el régimen de pequeña señal, el diodo se comporta como un elemento lineal cuya resistencia es la resistencia dinámica $r_d$. Se utiliza el principio de superposición para modelar tensiones y corrientes totales como la suma algebraica de sus componentes de DC y AC.

### 3.1 Superposición de Señales
El voltaje y la corriente instantáneos totales son la suma del punto de operación (DC) y la componente oscilatoria (AC).

* **Voltaje Instantáneo Total:**
  $$
  v_D(t) = V_{DQ} + v_d(t)
  $$
* **Corriente Instantánea Total:**
  $$
  i_D(t) = I_{DQ} + i_d(t)
  $$

### 3.2 Formas de Onda Temporales con Señal Senoidal
Si la fuente de entrada AC es de la forma $v_s(t) = V_m \sin(\omega t) = V_m \sin(2\pi f \cdot t)$, las magnitudes en el circuito serie de un solo lazo se modelan linealmente como:

* **Corriente Total Instantánea ($i_D(t)$):**
  $$
  i_D(t) = I_{DQ} + \frac{V_m}{R + r_d} \sin(2\pi f \cdot t)
  $$
* **Voltaje Total Instantáneo en el Diodo ($v_D(t)$):**
  $$
  v_D(t) = V_{DQ} + \frac{V_m \cdot r_d}{R + r_d} \sin(2\pi f \cdot t)
  $$

### 3.3 Amplitudes Pico de Pequeña Señal (AC)
Valores máximos de las variaciones alternas en la corriente y la tensión del diodo.

* **Corriente Alterna Pico ($\hat{i}_d$):**
  $$
  \hat{i}_d = \frac{V_m}{R + r_d}
  $$
* **Voltaje Alterno Pico en el Diodo ($\hat{v}_d$):**
  $$
  \hat{v}_d = V_m \cdot \frac{r_d}{R + r_d}
  $$

* **Nomenclatura:**
  * $v_d(t)$, $i_d(t)$: Componentes variables de voltaje y corriente en el diodo (AC).
  * $V_m$: Amplitud pico de la señal de entrada alterna (V).
  * $f$: Frecuencia de la señal alterna (Hz).
  * $r_d$: Resistencia dinámica del diodo calculada en el punto Q ($\Omega$).
* **Condición de Validez:**
  El análisis de pequeña señal es matemáticamente válido si y solo si la variación de voltaje alterno pico es significativamente menor que la energía térmica térmica del diodo:
  $$
  \hat{v}_d \ll n V_T \quad (\text{típicamente } \hat{v}_d < 5\text{ mV})
  $$

---

## 4. Glosario de Términos Técnicos

* **Punto de Operación (Punto Q):** Estado estable de polarización en corriente continua (DC) definido por un par ordenado de voltaje y corriente $(V_{DQ}, I_{DQ})$ en el cual se estabiliza el diodo sin señal de entrada variable.
* **Recta de Carga:** Representación gráfica en el plano $I-V$ que delimita los valores de corriente y tensión físicamente realizables impuestos por los elementos lineales del circuito externo (fuentes de tensión y resistencias).
* **Resistencia Dinámica ($r_d$):** Resistencia interna efectiva que el diodo presenta al flujo de corriente alterna de baja amplitud. Gráficamente equivale a la recíproca de la pendiente de la recta tangente a la curva del diodo en el punto Q.
* **Linealización:** Proceso matemático de aproximar el comportamiento de un componente altamente no lineal (como la ecuación exponencial de un diodo) mediante un modelo lineal de primer orden (recta tangente) en un rango restringido alrededor de un punto específico (Punto Q).
* **Pequeña Señal:** Régimen de operación donde la amplitud de las perturbaciones de corriente alterna (AC) es tan pequeña que la distorsión armónica debida a la no linealidad del diodo es despreciable, permitiendo la aplicación de teoremas lineales y el principio de superposición.
* **Voltaje Térmico ($V_T$):** Parámetro físico que relaciona la temperatura absoluta de la unión semiconductora con el voltaje equivalente a la agitación térmica de los portadores libres.
