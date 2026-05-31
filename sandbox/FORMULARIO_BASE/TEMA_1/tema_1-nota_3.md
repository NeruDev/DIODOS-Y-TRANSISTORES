<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_3
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Rectificadores de Señal: Rectificación de Media Onda

Este documento recopila y estructura las ecuaciones y modelos matemáticos del rectificador monofásico de media onda presentados en la Nota 3. Se incluyen las relaciones de transformación en corriente alterna (AC), el cálculo analítico de los valores promedio (CD) y eficaces (RMS) en la carga, la evaluación de las componentes de rizo y la determinación de las potencias de salida junto con la eficiencia de conversión.

---

## 1. Señal de Entrada y Transformación de Voltaje

En fuentes de alimentación de gran señal, el voltaje de la red de corriente alterna se reduce y aísla comúnmente mediante un transformador antes de la etapa de rectificación.

### 1.1 Relación de Voltaje Pico a RMS
Conversión matemática para obtener el voltaje de amplitud máxima ($V_m$) a partir de su valor eficaz en una onda senoidal pura.

$$
V_m = \sqrt{2} \cdot V_{rms}
$$

### 1.2 Relación de Transformación de Voltaje ($a$)
Voltaje eficaz en el devanado secundario ($V_{rms(\text{sec})}$) en función de la relación de vueltas del transformador ($a$) y el voltaje eficaz de entrada en el primario ($V_{rms(\text{pri})}$).

$$
V_{rms(\text{sec})} = \frac{V_{rms(\text{pri})}}{a}
$$

* **Nomenclatura:**
  * $V_{rms}, V_{rms(\text{pri})}, V_{rms(\text{sec})}$: Tensiones eficaces (RMS) en general, del primario y del secundario del transformador (V).
  * $V_m$: Voltaje de amplitud pico de la onda senoidal (V).
  * $a$: Relación de transformación de vueltas (adimensional), definido como $a = N_1 / N_2$.
* **Valores típicos comerciales:** 
  * Red eléctrica estándar: $120\text{ V}_{rms}$ en América (a $60\text{ Hz}$) o $230\text{ V}_{rms}$ en Europa (a $50\text{ Hz}$).
  * Relación de vueltas típica para fuentes comunes de baja tensión: $10:1$ o $5:1$.

---

## 2. Valores Promedio (CD) y Eficaces (RMS) en la Carga

La rectificación de media onda suprime un semiciclo de la señal de entrada, modificando los valores integrales de voltaje y corriente en la resistencia de carga ($R_L$).

### 2.1 Voltaje Promedio de Salida ($V_{CD}$)
Es el valor medio o componente continua del voltaje rectificado en la carga, calculado como la integral del semiciclo de conducción sobre el periodo completo ($T = 2\pi$).

$$
V_{CD} = \frac{V_m}{\pi} \approx 0.318 \cdot V_m
$$

### 2.2 Corriente Promedio de Salida ($I_{CD}$)
Componente continua de la corriente obtenida aplicando la Ley de Ohm en corriente continua a partir de $V_{CD}$.

$$
I_{CD} = \frac{V_m}{\pi R_L} \approx 0.318 \cdot \frac{V_m}{R_L}
$$

### 2.3 Voltaje Eficaz de Salida ($V_{rms}$)
Voltaje equivalente de AC que disipa la misma potencia sobre la resistencia de carga. En el rectificador de media onda es exactamente la mitad de la amplitud pico.

$$
V_{rms} = \frac{V_m}{2} = 0.500 \cdot V_m
$$

### 2.4 Corriente Eficaz de Salida ($I_{rms}$)
Corriente alterna eficaz calculada como la mitad de la corriente pico del circuito ($I_m = V_m / R_L$).

$$
I_{rms} = \frac{I_m}{2} = \frac{V_m}{2 R_L}
$$

* **Nomenclatura:**
  * $V_{CD}, I_{CD}$: Voltaje y corriente promedio en corriente continua de la carga (V, A).
  * $V_{rms}, I_{rms}$: Voltaje y corriente eficaces en corriente alterna de la carga (V, A).
  * $R_L$: Resistencia de carga del circuito ($\Omega$).
  * $I_m$: Corriente pico del circuito en el semiciclo de conducción directa (A).

---

## 3. Rizo, Potencias de Salida y Eficiencia de Conversión

La salida de un rectificador sin filtrar no es una corriente continua perfecta; consta de un nivel estable de continua superpuesto con una señal oscilante indeseada denominada voltaje de rizo.

### 3.1 Descomposición Ortogonal de Tensiones
El voltaje eficaz total al cuadrado es la suma geométrica de las componentes estática (CD) y alterna (rizo).

$$
V_{rms}^2 = V_{CD}^2 + V_{r(rms)}^2
$$

### 3.2 Voltaje de Rizo Eficaz ($V_{r(rms)}$)
Componente eficaz de las oscilaciones de voltaje en la carga.

* **Fórmula General:**
  $$
  V_{r(rms)} = \sqrt{V_{rms}^2 - V_{CD}^2}
  $$
* **Expresión en Función de $V_m$ (Media Onda):**
  $$
  V_{r(rms)} = V_m \sqrt{\frac{1}{4} - \frac{1}{\pi^2}} \approx 0.385 \cdot V_m
  $$
* **Expresión en Función de $V_{CD}$ (Media Onda):**
  $$
  V_{r(rms)} \approx 1.21 \cdot V_{CD}
  $$

### 3.3 Factor de Rizo ($FR$)
Medida adimensional de la pureza de la señal rectificada. Expresa la magnitud del rizo como un porcentaje de la componente directa de CD.

$$
FR = \frac{V_{r(rms)}}{V_{CD}} \times 100\% = \sqrt{\left(\frac{V_{rms}}{V_{CD}}\right)^2 - 1} \times 100\%
$$

* **Valor Teórico para Media Onda:**
  $$
  FR = \sqrt{\left(\frac{\pi}{2}\right)^2 - 1} \approx 1.21 \to 121\%
  $$

### 3.4 Potencias disipadas en la carga
* **Potencia Total Disipada ($P_{RMS}$):** Incorpora tanto la componente continua como la de rizo AC.
  $$
  P_{RMS} = \frac{V_{rms}^2}{R_L} = \frac{V_m^2}{4 R_L}
  $$
* **Potencia Útil de Corriente Directa ($P_{CD}$):** Energía efectiva aprovechada como corriente directa estable.
  $$
  P_{CD} = \frac{V_{CD}^2}{R_L} = \frac{V_m^2}{\pi^2 R_L} \approx 0.1013 \cdot \frac{V_m^2}{R_L}
  $$
* **Potencia de Corriente Alterna o Ruido ($P_{CA}$):** Energía disipada como calor debido al rizo armónico.
  $$
  P_{CA} = \frac{V_{r(rms)}^2}{R_L} = P_{RMS} - P_{CD} \approx 0.1487 \cdot \frac{V_m^2}{R_L}
  $$

### 3.5 Eficiencia de Conversión del Rectificador ($\eta$)
Relación de la potencia útil entregada en corriente directa respecto a la potencia total suministrada por la fuente.

$$
\eta = \frac{P_{CD}}{P_{RMS}} \times 100\% = \frac{4}{\pi^2} \times 100\% \approx 40.53\% \approx 40.6\%
$$

* **Nomenclatura:**
  * $V_{r(rms)}$: Voltaje eficaz del rizo de corriente alterna en la carga (V).
  * $FR$: Factor de rizo porcentual (%).
  * $P_{RMS}$: Potencia total eficaz suministrada a la carga (W).
  * $P_{CD}$: Potencia útil promedio de directa en la carga (W).
  * $P_{CA}$: Potencia variable del rizo disipada como calor en la carga (W).
  * $\eta$: Eficiencia de rectificación porcentual (%).

> [!WARNING]
> **Deficiencia del Rectificador de Media Onda**: El factor de rizo de $121\%$ indica que la componente indeseada de ruido AC supera a la componente útil de directa. Además, su límite máximo de eficiencia de conversión de apenas $40.6\%$ demuestra que el $59.4\%$ de la potencia suministrada se pierde como potencia reactiva o ruido armónico de AC, lo que restringe el uso de esta topología para aplicaciones eficientes de suministro de energía sin una etapa crítica de filtrado capacitivo.

---

## 4. Glosario de Términos Técnicos

* **Rectificador:** Circuito electrónico de potencia no lineal que tiene como propósito transformar una señal de corriente alterna en una señal pulsante en una sola dirección.
* **Valor Promedio ($V_{CD}$):** Componente continua equivalente de una forma de onda periódica calculada matemáticamente como la integral del área bajo la curva dividida entre el periodo fundamental.
* **Valor Eficaz ($V_{rms}$):** Magnitud de voltaje que produce el mismo efecto de calentamiento resistivo y disipación de potencia en régimen de alterna que un voltaje constante equivalente en corriente directa.
* **Voltaje de Rizo ($V_{r(rms)}$):** Magnitud eficaz del componente variable armónico periódico de corriente alterna que queda superpuesto al nivel de corriente directa a la salida de un rectificador.
* **Factor de Rizo ($FR$):** Índice porcentual empleado para evaluar la calidad de un rectificador; relaciona la magnitud del rizo de alterna con el nivel de continua de salida.
* **Eficiencia de Rectificación ($\eta$):** Fracción porcentual de potencia eléctrica alterna total que se logra transferir de forma útil como potencia de corriente directa a la carga.
* **Relación de Transformación ($a$):** Factor de proporcionalidad adimensional definido por el cociente del número de espiras del primario entre el número de espiras del secundario en un transformador de voltaje.
