<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_7
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Análisis de Fourier para Rectificadores de Onda Completa

Este documento recopila y estructura las ecuaciones y modelos del análisis en el dominio de la frecuencia (Serie de Fourier) aplicados al rectificador monofásico de onda completa, basados en la teoría descrita en la Nota 7. Incluye la descomposición armónica, la verificación energética mediante el teorema de Parseval, las métricas de calidad analíticas, el modelado matemático del filtro inductivo serie (carga reactiva) y el dimensionamiento del filtro capacitivo en paralelo.

---

## 1. Serie de Fourier de la Señal Rectificada

El voltaje unipolar pulsante de onda completa es una función periódica no senoidal. Sus simetrías intrínsecas (función par $f(-t) = f(t)$ y periodo de rizado duplicado $T_r = T/2$) eliminan los términos senoidales ($b_n = 0$) y restringen la expansión exclusivamente a componentes cosenoidales armónicos pares de la frecuencia de la red de alimentación.

### 1.1 Coeficiente de Corriente Directa ($a_0$)
Representa el doble del valor promedio estático (DC) de la señal.

$$
a_0 = \frac{4 V_m}{\pi} \implies V_{DC} = \frac{a_0}{2} = \frac{2 V_m}{\pi}
$$

### 1.2 Coeficientes de los Armónicos Cosenoidales ($a_n$)
Amplitudes pico del $n$-ésimo armónico de corriente alterna ($n = 1, 2, 3, \ldots$) correspondientes a las frecuencias pares $2n\omega$.

$$
a_n = \frac{-4 V_m}{\pi (4n^2 - 1)}
$$

### 1.3 Expresión Completa de la Serie de Fourier
Representación transitoria total en el dominio del tiempo como la suma de su nivel continuo y su serie armónica.

* **Modelo con Diodos Ideales ($V_D = 0\text{ V}$):**
  $$
  v_o(t) = \frac{2 V_m}{\pi} - \frac{4 V_m}{\pi} \sum_{n=1}^{\infty} \frac{\cos(2n\omega t)}{4n^2 - 1}
  $$
* **Modelo con Diodos Reales (Caída $2V_D$ en Puente):**
  $$
  v_o(t) = \frac{2(V_m - 2V_D)}{\pi} - \frac{4(V_m - 2V_D)}{\pi} \sum_{n=1}^{\infty} \frac{\cos(2n\omega t)}{4n^2 - 1}
  $$

### 1.4 Ley de Decaimiento Armónico y Componente Dominante
* **Decaimiento Asintótico:** La amplitud de los armónicos decrece de forma cuadrática inversa respecto a su orden $n$, disminuyendo drásticamente el ruido de alta frecuencia.
  $$
  |a_n| \propto \frac{1}{n^2} \quad (\text{para } n \gg 1)
  $$
* **Armónico Dominante ($n = 1$, Frecuencia $2f$):** Componente fundamental del rizo que aporta la mayor energía de ruido en corriente alterna (aproximadamente el $47.14\%$ del nivel $V_{DC}$).
  $$
  |a_1| = \frac{4 V_m}{3\pi} \approx 0.4244 \cdot V_m
  $$

* **Nomenclatura:**
  * $v_o(t)$: Voltaje rectificado instantáneo en bornes de la carga (V).
  * $V_m$: Voltaje pico sinusoidal del secundario del transformador (V).
  * $V_D$: Voltaje de umbral del diodo en directa (V).
  * $V_{DC}$: Voltaje promedio de corriente directa (V).
  * $a_n$: Coeficiente o amplitud pico del $n$-ésimo armónico (V).
  * $\omega$: Frecuencia angular de la red de entrada (rad/s), definida como $\omega = 2\pi f$.
  * $n$: Índice entero del armónico de rizo ($n = 1$ para frecuencia $2f$, $n = 2$ para $4f$, etc.).

---

## 2. Teorema de Parseval y Métricas de Calidad de Señal

La potencia disipada en la carga se analiza vinculando la energía cuadrática media total (RMS) con la suma algebraica de las potencias espectrales.

### 2.1 Identidad de Potencia de Parseval
Establece que el voltaje eficaz total al cuadrado equivale a la suma de la componente de continua al cuadrado más los valores eficaces al cuadrado de todas sus componentes armónicas de corriente alterna.

$$
V_{rms}^2 = V_{DC}^2 + \sum_{n=1}^{\infty} \frac{|a_n|^2}{2} = \left(\frac{2V_m}{\pi}\right)^2 + \frac{1}{2} \sum_{n=1}^{\infty} \left( \frac{4V_m}{\pi(4n^2 - 1)} \right)^2 = \frac{V_m^2}{2}
$$

### 2.2 Factor de Forma ($FF$)
Relación adimensional de la efectividad energética que mide qué tan plana es la señal.

$$
FF = \frac{V_{rms}}{V_{DC}} = \frac{\pi}{2\sqrt{2}} \approx 1.1107
$$

### 2.3 Factor de Rizo ($FR$ o $r$)
Índice de la componente armónica residual expresado porcentualmente.

* **Fórmula Analítica de Fourier:**
  $$
  FR = \sqrt{FF^2 - 1} = \sqrt{\frac{\pi^2 - 8}{8}} \approx 0.4834 \to 48.34\%
  $$
* **Aproximación por Armónico Dominante ($n=1$):**
  $$
  FR \approx \frac{|a_1|}{\sqrt{2} \cdot V_{DC}} = \frac{\sqrt{2}}{3} \approx 47.14\%
  $$

### 2.4 Eficiencia de Conversión ($\eta$)
Porcentaje de potencia activa de continua útil entregada respecto a la total.

$$
\eta = \frac{P_{CD}}{P_{ac}} = \frac{V_{DC}^2}{V_{rms}^2} = \frac{1}{FF^2} = \frac{8}{\pi^2} \approx 81.06\%
$$

### 2.5 Distorsión Armónica Total de Salida ($\text{THD}$)
Relación porcentual de la suma cuadrática de los armónicos superiores respecto a la amplitud del armónico fundamental de rizo ($2f$).

$$
\text{THD} = \frac{\sqrt{\sum_{n=2}^{\infty} a_n^2}}{|a_1|} = \sqrt{\sum_{n=2}^{\infty} \left( \frac{3}{4n^2-1} \right)^2} \approx 22.5\%
$$

* **Nomenclatura:**
  * $FF$: Factor de forma de voltaje (adimensional).
  * $FR$: Factor de rizo porcentual (%).
  * $\eta$: Eficiencia de rectificación (%).
  * $\text{THD}$: Distorsión armónica total de la tensión de salida (%).

---

## 3. Modelado de Carga Reactiva con Filtro Inductivo Serie

Al añadir un inductor ($L$) en serie con la carga, el circuito se convierte en una impedancia reactiva que limita las variaciones bruscas de corriente, filtrando el rizo armónico de AC sin disipar potencia útil de DC.

### 3.1 Impedancia Compleja y Ángulo de Desfase por Armónico
Oposición total y retraso angular que presenta la carga reactiva en el $n$-ésimo armónico (frecuencia $2n\omega$).

$$
|Z_n| = \sqrt{R_L^2 + (2n\omega L)^2}
$$

$$
\phi_n = \arctan\left(\frac{2n\omega L}{R_L}\right)
$$

### 3.2 Factor de Atenuación del Voltaje del Armónico ($A_n$)
Atenuación del rizo que la reactancia inductiva produce sobre la carga $R_L$ en función de la frecuencia del armónico.

$$
A_n = \frac{V_{n,\text{carga}}}{|a_n|} = \frac{1}{\sqrt{1 + \left(\frac{2n\omega L}{R_L}\right)^2}}
$$

### 3.3 Serie de Fourier de la Corriente de Salida ($i_o(t)$)
Expresión temporal de la corriente suavizada circulante a través del inductor.

$$
i_o(t) = \frac{2 V_m}{\pi R_L} - \frac{4 V_m}{\pi} \sum_{n=1}^{\infty} \frac{\cos(2n\omega t - \phi_n)}{(4n^2 - 1)\sqrt{R_L^2 + (2n\omega L)^2}}
$$

### 3.4 Corriente de Rizo RMS de Carga ($I_{r(rms)}$)
Componente eficaz de las variaciones de corriente alterna en la carga.

* **Fórmula Teórica (Truncada a los 2 primeros armónicos):**
  $$
  I_{r(rms)} = \frac{4V_m}{\pi\sqrt{2}} \sqrt{\sum_{n=1}^{2}\frac{1}{(4n^2-1)^2\big[R_L^2 + (2n\omega L)^2\big]}}
  $$
* **Aproximación por el Armónico Dominante ($n=1$):**
  $$
  I_{r(rms)} \approx \frac{2\sqrt{2} \cdot V_m}{3\pi\sqrt{R_L^2 + (2\omega L)^2}}
  $$

* **Nomenclatura:**
  * $|Z_n|$: Módulo de la impedancia reactiva del circuito para el armónico $n$ ($\Omega$).
  * $\phi_n$: Desfase inductivo de corriente en el armónico $n$ (rad o grados).
  * $L$: Inductancia del filtro en serie (H).
  * $A_n$: Factor de atenuación del voltaje del armónico $n$ (adimensional).
  * $i_o(t)$: Corriente instantánea suavizada a través de la carga (A).
  * $I_{r(rms)}$: Corriente eficaz del rizo en alterna (A).

---

## 4. Diseño y Dimensionamiento de Filtro Capacitivo en Paralelo

El filtro capacitivo se dimensiona como un filtro pasa-bajas para atenuar de forma dominante la frecuencia del primer armónico del rizo ($f_r = 120\text{ Hz}$).

### 4.1 Frecuencia de Corte ($f_c$)
Frecuencia límite a la cual el filtro inicia la atenuación de la componente alterna. Debe ser significativamente menor que la frecuencia fundamental del rizo.

$$
f_c = \frac{1}{2\pi R_L C} \ll 2f
$$

### 4.2 Voltaje de Rizo Filtrado ($V_{r(rms),\text{filtrado}}$)
Tensión eficaz del rizo remanente en bornes de la carga para constantes de tiempo grandes ($2\omega R_L C \gg 1$), deducida mediante atenuación del armónico dominante.

$$
V_{r(rms),\text{filtrado}} \approx \frac{|a_1|}{\sqrt{2}} \cdot \frac{1}{2\omega R_L C} = \frac{2 \cdot V_m}{3\pi \omega R_L C}
$$

### 4.3 Ecuación de Diseño del Condensador para Rizo Objetivo
Fórmula empleada para calcular la capacitancia mínima ($C$) necesaria para garantizar un factor de rizo objetivo porcentual ($r_{\text{obj}}$).

$$
C \geq \frac{\sqrt{\left( \frac{|a_1|}{\sqrt{2} \cdot V_{DC} \cdot r_{\text{obj}}} \right)^2 - 1}}{2\omega R_L} = \frac{\sqrt{\left( \frac{\sqrt{2}}{3 \cdot r_{\text{obj}}} \right)^2 - 1}}{4\pi f R_L}
$$

* **Nomenclatura:**
  * $f_c$: Frecuencia de corte a $-3\text{ dB}$ del filtro (Hz).
  * $C$: Capacitancia del condensador de filtrado (F). Típicamente del tipo electrolítico en el orden de $\mu\text{F}$.
  * $r_{\text{obj}}$: Factor de rizo porcentual objetivo deseado en el diseño (adimensional).
  * $V_{r(rms),\text{filtrado}}$: Voltaje de rizo eficaz suavizado final (V).

---

## 5. Glosario de Términos Técnicos

* **Descomposición Armónica:** Representación matemática de una forma de onda periódica no senoidal como la suma infinita de funciones trigonométricas senos y cosenos a frecuencias múltiplos de la fundamental.
* **Teorema de Parseval:** Principio fundamental de conservación de energía que establece la equivalencia de la potencia total de una señal en el dominio del tiempo con la suma de potencias de sus componentes en el dominio de la frecuencia.
* **Factor de Forma de Fourier:** Relación de voltaje RMS a promedio que cuantifica analíticamente el exceso de potencia efectiva asociada al rizo de alterna en señales rectificadas.
* **Atenuación Reactiva:** Reducción pasiva de la amplitud de señales de alterna a través de la impedancia selectiva en frecuencia de componentes reactivos (capacitores e inductores) sin pérdidas de energía activa.
* **Desfase Armónico ($\phi_n$):** Retraso de fase temporal que experimentan los armónicos de corriente respecto a la tensión debido a la constante de tiempo inductiva de la carga.
* **Frecuencia Dominante del Rizo:** Frecuencia del primer armónico espectral no nulo a la salida del rectificador; para onda completa es exactamente el doble de la frecuencia de red ($2f = 120\text{ Hz}$).
* **Decaimiento Cuadrático:** Caída asintótica de la amplitud armónica en función del inverso del cuadrado del orden ($1/n^2$), característica de funciones continuas con derivadas discontinuas que facilita su filtrado electrónico.
