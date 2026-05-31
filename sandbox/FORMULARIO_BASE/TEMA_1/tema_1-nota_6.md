<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_6
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Rectificadores de Onda Completa tipo Puente (Graetz)

Este documento recopila y estructura las ecuaciones y modelos matemáticos del rectificador de onda completa en configuración de puente (puente de Graetz o tipo H) descritos en la Nota 6. Contempla la conducción por pares de diodos en serie ($2V_D$), los valores promedio (CD) y eficaces (RMS) corregidos en la carga, los parámetros de fatiga y corriente por diodo individual, el voltaje inverso de pico (PIV) y las relaciones de rizo, potencia y eficiencia.

---

## 1. Conducción en Puente y Pérdida por Par de Diodos

El rectificador tipo puente utiliza cuatro diodos que actúan por pares alternados en cada semiciclo para direccionar la corriente en la carga sin necesidad de derivación central en el secundario del transformador.

### 1.1 Voltaje de Salida Instantáneo por Semiciclo
Debido a que la corriente debe atravesar dos diodos en serie para retornar al secundario, se restan dos caídas de tensión directa de silicio ($2V_D$).

* **Semiciclo Positivo ($0 < \omega t < \pi$):** Conduce el par $D_1 - D_2$ ($D_3 - D_4$ en corte).
  $$
  v_o(t) = V_m \sin(\omega t) - 2V_D
  $$
* **Semiciclo Negativo ($\pi < \omega t < 2\pi$):** Conduce el par $D_3 - D_4$ ($D_1 - D_2$ en corte).
  $$
  v_o(t) = V_m |\sin(\omega t)| - 2V_D
  $$

### 1.2 Frecuencia de Rizo de Salida
Dado que la forma de onda posee dos pulsos positivos por cada periodo de la red de entrada, la frecuencia fundamental de la componente alterna se duplica.

$$
f_{\text{rizo}} = 2 \cdot f_{\text{entrada}}
$$

* **Nomenclatura:**
  * $v_o(t)$: Voltaje instantáneo en la carga resistiva (V).
  * $V_m$: Voltaje pico absoluto en el secundario del transformador (V).
  * $V_D$: Voltaje de umbral del diodo en directa (V). Típicamente $0.7\text{ V}$ para silicio.
  * $f_{\text{entrada}}, f_{\text{rizo}}$: Frecuencias de entrada y de rizo en la salida (Hz).

---

## 2. Valores Promedio (CD) y Eficaces (RMS) en la Carga

La etapa rectificadora altera los valores promedio y eficaces en bornes de la carga resistiva debido a la doble caída de diodo en directa.

### 2.1 Voltaje Pico en la Carga ($V_{o,m}$)
Amplitud máxima real del voltaje que experimenta la carga.

$$
V_{o,m} = V_m - 2V_D
$$

### 2.2 Voltaje Promedio de Salida ($V_{DC}$)
Componente continua o de CD real de salida.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  V_{DC} = \frac{2 V_m}{\pi} \approx 0.636 \cdot V_m
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  V_{DC} = \frac{2(V_m - 2V_D)}{\pi}
  $$

### 2.3 Corriente Promedio de Salida ($I_{DC}$)
Corriente continua real circulante a través de la carga $R_L$.

$$
I_{DC} = \frac{V_{DC}}{R_L} = \frac{2(V_m - 2V_D)}{\pi R_L}
$$

### 2.4 Voltaje Eficaz de Salida ($V_{rms}$)
Voltaje RMS real de la señal rectificada en bornes de la carga.

* **Modelo Ideal ($V_D = 0\text{ V}$):**
  $$
  V_{rms} = \frac{V_m}{\sqrt{2}} \approx 0.707 \cdot V_m
  $$
* **Modelo Real ($V_D = 0.7\text{ V}$):**
  $$
  V_{rms} = \frac{V_m - 2V_D}{\sqrt{2}}
  $$

### 2.5 Corriente Eficaz de Salida ($I_{rms}$)
Corriente alterna eficaz real útil para calcular la disipación térmica de la carga.

$$
I_{rms} = \frac{V_{rms}}{R_L} = \frac{V_m - 2V_D}{\sqrt{2} R_L}
$$

* **Nomenclatura:**
  * $V_{o,m}$: Voltaje pico real corregido en la carga (V).
  * $V_{DC}, I_{DC}$: Voltaje y corriente promedio en corriente continua de la carga (V, A).
  * $V_{rms}, I_{rms}$: Voltaje y corriente eficaces en corriente alterna de la carga (V, A).
  * $R_L$: Resistencia de la carga ($\Omega$).

---

## 3. Parámetros y Criterios por Diodo Individual

Cada diodo en la configuración de puente conduce solo durante un semiciclo completo de la señal de entrada, repartiendo la fatiga de corriente.

### 3.1 Corriente Promedio por Diodo ($I_{D(avg)}$)
Corriente continua media que circula por cada semiconductor individual. Es exactamente la mitad de la corriente total de CD en la carga.

$$
I_{D(avg)} = \frac{I_{DC}}{2} = \frac{V_m - 2V_D}{\pi R_L}
$$

### 3.2 Corriente Eficaz por Diodo ($I_{D(rms)}$)
Corriente RMS que experimenta cada semiconductor individual (idéntica a la corriente eficaz del rectificador de media onda).

$$
I_{D(rms)} = \frac{I_m}{2} = \frac{I_{rms}}{\sqrt{2}} = \frac{V_m - 2V_D}{2 R_L}
$$

### 3.3 Tensión Inversa de Pico (PIV)
Es la máxima caída de voltaje inverso que soporta cada diodo en su etapa de bloqueo.

$$
\text{PIV} = V_m - V_D
$$

* **Nomenclatura:**
  * $I_{D(avg)}$: Corriente continua promedio individual por diodo (A).
  * $I_{D(rms)}$: Corriente eficaz individual por diodo (A).
  * $I_m$: Corriente de pico en la carga (A), definida como $I_m = V_{o,m} / R_L$.
  * $\text{PIV}$: Tensión inversa de pico máxima por diodo (V).

> [!WARNING]
> **Tensión Inversa de Pico (PIV) Reducida**: En la topología de puente, cuando un par de diodos está bloqueado, cada uno de ellos solo soporta la tensión pico del secundario menos la caída de un diodo activo ($\text{PIV} = V_m - V_D$). Esto equivale a **la mitad** de la tensión inversa de pico requerida en la derivación central ($\text{PIV} \approx 2V_m$). Esto permite diseñar la etapa utilizando diodos comerciales con voltajes de ruptura ($V_{BR}$) significativamente menores y de menor costo.

---

## 4. Rizo, Potencia y Eficiencia de Conversión

La topología de puente mantiene los altos estándares de eficiencia y bajo rizo de la onda completa, simplificando el transformador de alimentación.

### 4.1 Voltaje de Rizo Eficaz ($V_{r(rms)}$)
Componente alterna de ruido residual sobre la carga sin filtrado capacitivo.

$$
V_{r(rms)} = \sqrt{V_{rms}^2 - V_{DC}^2} = V_{o,m} \sqrt{\frac{1}{2} - \frac{4}{\pi^2}} \approx 0.308 \cdot V_{o,m}
$$

### 4.2 Factor de Rizo ($FR$)
Índice de distorsión periódica alterna en la salida.

$$
FR = \frac{V_{r(rms)}}{V_{DC}} \times 100\% \approx 48.3\%
$$

### 4.3 Potencia en Corriente Directa ($P_{dc}$)
Potencia útil entregada en corriente continua a la carga resistiva.

$$
P_{dc} = V_{DC} \cdot I_{DC} = I_{DC}^2 \cdot R_L = \frac{4 (V_m - 2V_D)^2}{\pi^2 R_L}
$$

### 4.4 Potencia Total Disipada ($P_{ac}$)
Potencia eficaz absorbida total disipada en la carga (calor).

$$
P_{ac} = V_{rms} \cdot I_{rms} = I_{rms}^2 \cdot R_L = \frac{(V_m - 2V_D)^2}{2 R_L}
$$

### 4.5 Eficiencia de Conversión Máxima ($\eta$)
Fracción de potencia máxima teórica transferida de forma útil en corriente continua.

$$
\eta = \frac{P_{dc}}{P_{ac}} \times 100\% = \frac{8}{\pi^2} \times 100\% \approx 81.06\% \approx 81.2\%
$$

* **Nomenclatura:**
  * $V_{r(rms)}$: Voltaje eficaz del rizo de corriente alterna en la carga (V).
  * $FR$: Factor de rizo porcentual (%).
  * $P_{dc}$: Potencia de corriente directa útil entregada a la carga (W).
  * $P_{ac}$: Potencia total eficaz alterna disipada en la carga (W).
  * $\eta$: Eficiencia máxima de rectificación porcentual (%).

> [!IMPORTANT]
> **Compromiso de Diseño del Puente**: La topología de puente es comercialmente dominante porque simplifica la construcción del transformador al usar 2 hilos (sin derivación central) y requiere la mitad del PIV por diodo. El único compromiso técnico radica en la doble caída de diodo ($2V_D \approx 1.4\text{ V}$), la cual debe evaluarse cuidadosamente en aplicaciones de muy baja tensión donde la pérdida de $1.4\text{ V}$ en directa puede penalizar la eficiencia global del circuito.

---

## 5. Glosario de Términos Técnicos

* **Puente de Graetz (Full-Bridge):** Red eléctrica de cuatro diodos en configuración de diamante o lazo cerrado diseñada para realizar rectificación de onda completa sin requerir un transformador especial de tres terminales.
* **Doble Caída de Voltaje ($2V_D$):** Pérdida de potencial en directa debida a la conducción simultánea en serie de dos diodos semiconductores de silicio en cada semiciclo de oscilación.
* **PIV Reducido:** Ventaja del rectificador puente en la cual el voltaje inverso que soporta cada diodo es la mitad del requerido en la topología de derivación central, limitándose a $V_m - V_D$.
* **Corriente Promedio de Rama ($I_{D(avg)}$):** Corriente continua promedio individual que circula a través de cada diodo en régimen de onda completa, equivalente a la mitad de la corriente de continua total en la carga.
* **Factor de Forma ($FF$):** Relación adimensional entre el valor eficaz de la corriente y su valor promedio ($FF = I_{rms}/I_{DC}$). Para una onda completa senoidal pura es exactamente $\pi / (2\sqrt{2}) \approx 1.11$.
* **Eficiencia Teórica del 81%:** Límite máximo de conversión energética del circuito, que transfiere el $81.2\%$ de la energía de alterna a corriente continua útil.
