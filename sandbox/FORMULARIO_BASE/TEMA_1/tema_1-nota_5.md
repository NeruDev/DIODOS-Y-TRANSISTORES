<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_5
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Rectificadores de Onda Completa con Derivación Central

Este documento recopila y estructura las ecuaciones y modelos matemáticos del rectificador monofásico de onda completa con transformador de derivación central (punto medio o *center-tap*) descritos en la Nota 5. Contempla el análisis de conducción alternada de los diodos, el cálculo de los valores promedio (CD) y eficaces (RMS) corregidos para diodo real e ideal, la componente de rizado y los límites de potencia y eficiencia del sistema.

---

## 1. Comportamiento Temporal y Polarización de los Diodos

Esta topología emplea un transformador que divide la tensión del secundario en dos mitades simétricas de amplitud $V_m$ respecto al punto central de tierra. Los diodos conducen de forma alternada, permitiendo que la corriente circule por la carga $R_L$ en una única dirección en ambos semiciclos.

### 1.1 Voltaje de Salida Instantáneo por Semiciclo
Modelado del voltaje en la carga $R_L$ durante cada porción del ciclo senoidal de entrada, considerando la caída en el diodo de silicio real.

* **Semiciclo Positivo ($0 < \omega t < \pi$):** Conduce el diodo superior $D_1$ ($D_2$ en corte).
  $$
  v_o(t) = V_m \sin(\omega t) - V_D
  $$
* **Semiciclo Negativo ($\pi < \omega t < 2\pi$):** Conduce el diodo inferior $D_2$ ($D_1$ en corte).
  $$
  v_o(t) = V_m |\sin(\omega t)| - V_D
  $$

### 1.2 Frecuencia de Salida
Dado que se generan dos pulsos unipolares simétricos por cada ciclo completo de la fuente de alimentación, la frecuencia de la señal rectificada se duplica.

$$
f_{\text{salida}} = 2 \cdot f_{\text{entrada}}
$$

* **Nomenclatura:**
  * $v_o(t)$: Voltaje instantáneo en la resistencia de carga (V).
  * $V_m$: Voltaje pico de fase (del extremo al punto medio) en el secundario (V).
  * $V_D$: Voltaje de umbral en directa del diodo (V). Típicamente $0.7\text{ V}$ para silicio.
  * $f_{\text{entrada}}, f_{\text{salida}}$: Frecuencias de entrada y salida (Hz).

---

## 2. Valores Promedio (CD) y Eficaces (RMS) de Salida

Al rectificar la onda completa, la señal pulsante entrega el doble de tensión continua promedio y aumenta el contenido eficaz de la energía entregada a la carga.

### 2.1 Voltaje Promedio de Salida ($V_{CD}$)
Componente continua o valor medio en la carga. Es exactamente el doble del valor obtenido en media onda.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  V_{CD} = \frac{2 V_m}{\pi} \approx 0.636 \cdot V_m
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  V_{CD} = \frac{2 (V_m - V_D)}{\pi}
  $$

### 2.2 Corriente Promedio de Salida ($I_{CD}$)
Corriente continua útil que fluye a través de la resistencia de carga.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  I_{CD} = \frac{2 V_m}{\pi R_L}
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  I_{CD} = \frac{2 (V_m - V_D)}{\pi R_L}
  $$

### 2.3 Voltaje Eficaz de Salida ($V_{rms}$)
Voltaje RMS de la forma de onda. Coincide analíticamente con el valor RMS de una senoide completa sin rectificar debido a que la energía simétrica total no se ve alterada por la inversión de polaridad.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 \cdot V_m
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  V_{rms} = \frac{V_m - V_D}{\sqrt{2}}
  $$

### 2.4 Corriente Eficaz de Salida ($I_{rms}$)
Corriente eficaz requerida para dimensionar térmicamente la resistencia de carga.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  I_{rms} = \frac{V_m}{\sqrt{2} R_L}
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  I_{rms} = \frac{V_m - V_D}{\sqrt{2} R_L}
  $$

* **Nomenclatura:**
  * $V_{CD}, I_{CD}$: Voltaje y corriente promedio en corriente continua de la carga (V, A).
  * $V_{rms}, I_{rms}$: Voltaje y corriente eficaces en corriente alterna de la carga (V, A).
  * $R_L$: Resistencia de la carga ($\Omega$).

---

## 3. Rizo, Potencia y Eficiencia de Conversión

La eficiencia energética máxima del rectificador se duplica respecto a la de media onda y la componente de rizo residual se aminora. Sin embargo, la topología exige diodos con mayor tolerancia de voltaje en inversa.

### 3.1 Voltaje de Rizo Eficaz ($V_{r(rms)}$)
Componente de ruido AC residual calculada bajo el modelo ideal del diodo.

$$
V_{r(rms)} = \sqrt{V_{rms}^2 - V_{CD}^2} = V_m \sqrt{\frac{1}{2} - \frac{4}{\pi^2}} \approx 0.308 \cdot V_m
$$

### 3.2 Factor de Rizo ($FR$ o $r$)
Porcentaje adimensional de componente alterna en la salida rectificada.

$$
FR = \frac{V_{r(rms)}}{V_{CD}} \times 100\% \approx \frac{0.308}{0.636} \times 100\% \approx 48.3\%
$$

### 3.3 Potencia de Salida y de Entrada
* **Potencia de Corriente Directa Útil ($P_{CD}$):** Potencia útil en DC bajo el modelo ideal.
  $$
  P_{CD} = I_{CD}^2 R_L = \frac{4 V_m^2}{\pi^2 R_L} \approx 0.4053 \cdot \frac{V_m^2}{R_L}
  $$
* **Potencia de Corriente Alterna de Entrada ($P_{AC}$):** Potencia disipada total en AC bajo el modelo ideal.
  $$
  P_{AC} = I_{rms}^2 R_L = \frac{V_m^2}{2 R_L} = 0.500 \cdot \frac{V_m^2}{R_L}
  $$

### 3.4 Eficiencia de Conversión Máxima ($\eta$)
Relación porcentual máxima teórica de potencia útil en continua respecto a la total suministrada.

$$
\eta = \frac{P_{CD}}{P_{AC}} \times 100\% = \frac{8}{\pi^2} \times 100\% \approx 81.06\% \approx 81.2\%
$$

### 3.5 Tensión Inversa de Pico (PIV)
Tensión máxima de bloqueo que experimenta el diodo no activo cuando la otra mitad del secundario induce la conducción del diodo alterno.

$$
\text{PIV} = 2 \cdot V_m - V_D \approx 2 \cdot V_m
$$

* **Nomenclatura:**
  * $V_{r(rms)}$: Voltaje eficaz del rizo de corriente alterna en la carga (V).
  * $FR$: Factor de rizo porcentual (%).
  * $P_{CD}$: Potencia promedio útil de directa en la carga (W).
  * $P_{AC}$: Potencia eficaz total absorbida en alterna por la carga (W).
  * $\eta$: Eficiencia máxima de rectificación porcentual (%).
  * $\text{PIV}$: Tensión inversa de pico repetitiva requerida por diodo (V).

> [!WARNING]
> **Tensión Inversa Duplicada (PIV)**: En la topología con derivación central, cada diodo bloqueado debe soportar la diferencia de potencial completa de los dos devanados secundarios en serie ($2V_m$). Esto significa que el voltaje inverso de pico es el doble que en la media onda ($\text{PIV} \approx 2V_m$). Al seleccionar los diodos, se debe verificar que su voltaje de ruptura cumpla con $V_{BR} \geq 2 \times \text{PIV} = 4 V_m$ para garantizar la confiabilidad.

> [!IMPORTANT]
> **Superioridad de Rizo y Eficiencia**: La onda completa reduce el factor de rizo al $48.3\%$ (en comparación con el $121\%$ de la media onda) y duplica la frecuencia de oscilación a $2f$. Esto facilita enormemente el diseño del filtro capacitivo posterior, requiriendo capacitancias menores para lograr un nivel continuo plano. Además, su eficiencia teórica del $81.2\%$ minimiza las pérdidas por potencia armónica y calentamiento en la carga.

---

## 4. Glosario de Términos Técnicos

* **Derivación Central (Center-Tap):** Conexión física intermedia en el centro geométrico del bobinado secundario de un transformador que sirve como nodo neutro o común de referencia (tierra).
* **Rectificador de Onda Completa:** Topología que aprovecha tanto los semiciclos positivos como los negativos de la señal alterna de entrada para generar una salida de polaridad única constante.
* **Tensión Inversa Duplicada:** Fenómeno físico de la topología con toma central en el cual el diodo en bloqueo debe soportar la suma de tensiones de ambas mitades del devanado secundario.
* **Frecuencia de Rizo Duplicada:** Incremento de la frecuencia fundamental de la componente alterna de salida a $2f$, lo que aminora el tiempo de descarga del capacitor de filtrado.
* **Eficiencia de Conversión del 81%:** Porcentaje teórico de potencia eléctrica máxima que se logra transferir de forma útil como directa estable, duplicando el desempeño de la media onda.
* **Conducción Alternada:** Ciclo de conmutación donde los diodos se turnan de forma periódica la fase de conducción activa y bloqueo para direccionar de forma simétrica la corriente en la carga.
