# Formulario Tema 1

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

### 2.4 Voltaje Térmico ($V_T$)
Voltaje equivalente a la energía térmica de los portadores de carga a una temperatura dada.

$$
V_T = \frac{k T}{q}
$$

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

  El análisis de pequeña señal es matemáticamente válido si y solo si la variación de voltaje alterno pico es significativamente menor que la energía térmica térmica del diodo:
  $$
  \hat{v}_d \ll n V_T \quad (\text{típicamente } \hat{v}_d < 5\text{ mV})
  $$

---

---

Este documento recopila y estructura las ecuaciones para el análisis avanzado de diodos en corriente continua (DC) y corriente alterna (AC) presentadas en la Nota 2. Se incluyen las fórmulas de variación instantánea por señal mixta, la metodología para la extracción de parámetros de Shockley a partir de mediciones experimentales y la diferenciación analítica entre resistencia estática (DC) y dinámica (AC).

---

## 1. Recta de Carga y Límites Instantáneos bajo Señal Mixta (DC + AC)

Cuando una fuente alterna está acoplada en serie con una fuente continua (señal mixta), la recta de carga sufre un desplazamiento dinámico paralelo que desplaza el punto de operación instantáneo entre límites extremos.

### 1.1 Ecuación de la Malla en CD
Planteamiento de tensiones estático que define la recta de carga nominal en corriente continua.

$$
R I_D + V_D = E
$$

### 1.2 Límites de Voltaje Efectivo Instantáneo
Amplitudes extremas que alcanza la tensión efectiva total en la malla debido a la adición de una señal AC superpuesta de la forma $v_s(t) = V_m \sin(\omega t)$.

$$
E_{\max} = E + V_m
$$

$$
E_{\min} = E - V_m
$$

### 1.3 Límites Teóricos de Corriente Instantánea
Aproximación ideal de corriente máxima y mínima en la malla, asumiendo un cortocircuito ideal en el diodo ($V_D \approx 0$).

$$
I_{D,\max} \approx \frac{E_{\max}}{R} = \frac{E + V_m}{R}
$$

$$
I_{D,\min} \approx \frac{E_{\min}}{R} = \frac{E - V_m}{R}
$$

### 1.4 Ajuste de Tensión de Fuente para Q Objetivo
Ecuación empleada para calcular la tensión continua de fuente ($E$) necesaria para posicionar un punto Q de operación deseado $(I_D, V_D)$ con una resistencia de malla $R$ dada.

$$
E = R I_D + V_D
$$

---

## 2. Ajuste de Parámetros del Modelo de Shockley

Para obtener alta precisión en modelos no lineales, los parámetros intrínsecos de la ecuación exponencial del diodo se extraen analíticamente empleando dos puntos de operación conocidos bajo conducción directa directa ($(V_1, I_1)$ y $(V_2, I_2)$ donde $I \gg I_S$).

### 2.1 Ecuación del Factor de Idealidad ($n$)
Deducción analítica obtenida al relacionar los cocientes de corriente directa para anular la corriente de saturación inversa $I_S$.

$$
n = \frac{V_2 - V_1}{V_T \ln\left(\frac{I_2}{I_1}\right)}
$$

### 2.2 Ecuación de la Corriente de Saturación Inversa ($I_S$)
Cálculo de la corriente de fuga inversa del dispositivo sustituyendo el factor de idealidad ($n$) determinado en cualquiera de los puntos conocidos.

$$
I_S = \frac{I_1}{e^{\frac{V_1}{n V_T}} - 1}
$$

---

## 3. Resistencias en Corriente Directa (DC) y Dinámica (AC)

La resistencia de un diodo semiconductor varía según el régimen de excitación. Es crítico distinguir entre la resistencia estática absoluta y la resistencia dinámica diferencial.

### 3.1 Resistencia Estática o en CD ($R_{\text{CD}}$)
Representa la oposición total al paso de la corriente continua. Gráficamente equivale a la inversa de la pendiente de la recta secante que conecta el origen del plano cartesiano $(0,0)$ con el punto de operación $Q(V_{DQ}, I_{DQ})$.

$$
R_{\text{CD}} = \frac{V_{D_Q}}{I_{D_Q}}
$$

### 3.2 Resistencia Dinámica o de AC Diferencial Analítica ($r_d$)
Es la resistencia equivalente ante perturbaciones infinitesimales de pequeña señal. Gráficamente es la recíproca de la recta tangente local a la curva exponencial evaluada en el punto $Q$.

$$
r_d = \frac{n V_T}{I_{D_Q}}
$$

### 3.3 Resistencia Dinámica Promedio Gráfica (Secante)
Aproximación de la resistencia de pequeña señal para variaciones finitas medibles ($\Delta V_D$ y $\Delta I_D$) alrededor de $Q$.

$$
r_d \approx \frac{\Delta V_D}{\Delta I_D} = \frac{V_{D,\max} - V_{D,\min}}{I_{D,\max} - I_{D,\min}}
$$

> [!WARNING]
> **Diferencia entre $R_{\text{CD}}$ y $r_d$**: En la zona de conducción del diodo, la resistencia estática es significativamente mayor que la dinámica ($R_{\text{CD}} \gg r_d$). Esto ocurre porque $R_{\text{CD}}$ incorpora el voltaje umbral o de rodilla necesario para iniciar la conducción ($V_K \approx 0.6\text{ V}$), el cual no genera incrementos de corriente. La resistencia dinámica $r_d$ representa únicamente la pendiente de la curva en el punto de operación directa, donde el diodo presenta una resistencia incremental muy baja.

> [!IMPORTANT]
> **Desviación del Modelo Lineal**: La resistencia dinámica promedio gráfica ($\Delta V_D / \Delta I_D$) sobre una variación finita difiere ligeramente de la resistencia analítica instantánea en $Q$. Esto ocurre porque el swing alterno real no es infinitesimal y recorre un arco curvo de la exponencial en lugar de la recta tangente teórica. Además, emplear un modelo lineal simplificado por tramos suele sobreestimar severamente el valor de $r_d$ en comparación con el modelo exponencial de Shockley, debido a que asume pendientes promedio constantes de bajo gradiente.

---

---

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

> [!WARNING]
> **Deficiencia del Rectificador de Media Onda**: El factor de rizo de $121\%$ indica que la componente indeseada de ruido AC supera a la componente útil de directa. Además, su límite máximo de eficiencia de conversión de apenas $40.6\%$ demuestra que el $59.4\%$ de la potencia suministrada se pierde como potencia reactiva o ruido armónico de AC, lo que restringe el uso de esta topología para aplicaciones eficientes de suministro de energía sin una etapa crítica de filtrado capacitivo.

---

---

Este documento recopila y estructura las ecuaciones avanzadas de rectificación de media onda que incorporan los efectos físicos del modelo de diodo real (tensión de umbral de silicio $V_D = 0.7\text{ V}$) y el uso de transformadores reductores de voltaje, basados en la teoría y el análisis de la Nota 4.

---

## 1. Transformación de Voltaje y Parámetros del Secundario

El transformador reductor acopla la tensión de línea residencial al circuito de potencia, modificando la amplitud eficaz de entrada pero preservando la frecuencia de oscilación.

### 1.1 Ecuación de Relación de Devanados
Vincula la relación de espiras del primario y secundario con sus correspondientes tensiones eficaces o picos.

$$
\frac{N_p}{N_s} = \frac{V_p}{V_s}
$$

### 1.2 Voltaje Eficaz (RMS) del Secundario
Tensión reducida disponible para la etapa de rectificación.

$$
V_s = \frac{N_s}{N_p} \cdot V_p
$$

### 1.3 Voltaje Pico del Secundario
Amplitud máxima de la señal sinusoidal en bornes del devanado secundario.

$$
V_{s,\text{pico}} = \sqrt{2} \cdot V_s = \sqrt{2} \cdot \left( \frac{N_s}{N_p} \cdot V_p \right)
$$

---

## 2. Parámetros de Rectificación con Diodo Real ($V_D = 0.7\text{ V}$)

A diferencia del modelo ideal, el diodo de silicio real requiere una caída de voltaje mínima en directa ($V_D$) para entrar en conducción, lo que desplaza y reduce todas las magnitudes eléctricas a la salida del rectificador.

### 2.1 Ecuación Dinámica del Voltaje de Salida Instantáneo
Describe la señal a la salida del rectificador incorporando el umbral de conducción del semiconductor.

$$
v_o(t) = \begin{cases} v_s(t) - V_D & \text{si } v_s(t) > V_D \\ 0 & \text{si } v_s(t) \leq V_D \end{cases}
$$

### 2.2 Voltaje de Salida Pico Corregido ($V_{o,m}$)
Tensión máxima real que alcanza la forma de onda sobre la resistencia de carga $R_L$.

$$
V_{o,m} = V_{s,\text{pico}} - V_D
$$

### 2.3 Voltaje Promedio de Salida Corregido ($V_{CD}$)
Componente continua o de CD real de salida, calculada tras deducir la tensión de umbral del diodo.

$$
V_{CD} = \frac{V_{o,m}}{\pi} = \frac{V_{s,\text{pico}} - V_D}{\pi}
$$

### 2.4 Corriente Promedio de Salida Corregida ($I_{CD}$)
Corriente continua real circulante a través del circuito de carga.

$$
I_{CD} = \frac{V_{CD}}{R_L} = \frac{V_{s,\text{pico}} - V_D}{\pi R_L}
$$

### 2.5 Voltaje Eficaz de Salida Corregido ($V_{rms}$)
Voltaje RMS real de la señal pulsante unipolar a la salida del diodo.

$$
V_{rms} = \frac{V_{o,m}}{2} = \frac{V_{s,\text{pico}} - V_D}{2}
$$

### 2.6 Corriente Eficaz de Salida Corregida ($I_{rms}$)
Corriente de AC eficaz real que determina la potencia térmica disipada en la carga.

$$
I_{rms} = \frac{V_{rms}}{R_L} = \frac{V_{s,\text{pico}} - V_D}{2 R_L}
$$

---

## 3. Criterios de Selección del Diodo y Diseño Seguro

El diodo rectificador debe ser seleccionado garantizando tolerancias frente a disipación térmica y tensiones de ruptura inversa.

### 3.1 Corriente RMS del Diodo ($I_{D(rms)}$)
Debido a que el diodo y la resistencia de carga se encuentran conectados en una malla serie cerrada, la corriente RMS que soporta el semiconductor es idéntica a la corriente eficaz de la carga.

$$
I_{D(rms)} = I_{rms} = \frac{V_{s,\text{pico}} - V_D}{2 R_L}
$$

### 3.2 Tensión Inversa de Pico (PIV / $V_{PRD}$)
Es la máxima caída de voltaje inverso que soporta la unión P-N en el semiciclo negativo de bloqueo. Se define siempre como una magnitud escalar positiva.

$$
\text{PIV} = |V_{PRD}| = V_{s,\text{pico}}
$$

### 3.3 Voltaje de Ruptura Inversa Requerido ($V_{BR}$)
Criterio de seguridad en el diseño de ingeniería electrónica para evitar la destrucción del diodo por avalancha térmica.

$$
V_{BR} \geq 2 \times \text{PIV} = 2 \cdot V_{s,\text{pico}}
$$

> [!IMPORTANT]
> **Efectos Despreciados en Modelados Simplificados**: En análisis introductorios se asume $V_D = 0\text{ V}$. Sin embargo, en aplicaciones de baja tensión (ej. secundario de $5\text{ V}$), ignorar la caída del diodo de $0.7\text{ V}$ induce errores superiores al $14\%$ en todos los cálculos de voltaje, potencia y corriente, afectando la estabilidad térmica esperada. Los modelos de alta fidelidad además incorporan la resistencia dinámica incremental ($r_d$) y la corriente de fuga inversa ($I_S$), las cuales suelen ser despreciables ante cargas de baja resistencia.

---

---

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

> [!WARNING]
> **Tensión Inversa Duplicada (PIV)**: En la topología con derivación central, cada diodo bloqueado debe soportar la diferencia de potencial completa de los dos devanados secundarios en serie ($2V_m$). Esto significa que el voltaje inverso de pico es el doble que en la media onda ($\text{PIV} \approx 2V_m$). Al seleccionar los diodos, se debe verificar que su voltaje de ruptura cumpla con $V_{BR} \geq 2 \times \text{PIV} = 4 V_m$ para garantizar la confiabilidad.

> [!IMPORTANT]
> **Superioridad de Rizo y Eficiencia**: La onda completa reduce el factor de rizo al $48.3\%$ (en comparación con el $121\%$ de la media onda) y duplica la frecuencia de oscilación a $2f$. Esto facilita enormemente el diseño del filtro capacitivo posterior, requiriendo capacitancias menores para lograr un nivel continuo plano. Además, su eficiencia teórica del $81.2\%$ minimiza las pérdidas por potencia armónica y calentamiento en la carga.

---

---

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

> [!IMPORTANT]
> **Compromiso de Diseño del Puente**: La topología de puente es comercialmente dominante porque simplifica la construcción del transformador al usar 2 hilos (sin derivación central) y requiere la mitad del PIV por diodo. El único compromiso técnico radica en la doble caída de diodo ($2V_D \approx 1.4\text{ V}$), la cual debe evaluarse cuidadosamente en aplicaciones de muy baja tensión donde la pérdida de $1.4\text{ V}$ en directa puede penalizar la eficiencia global del circuito.

---

---

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

---

---

Este documento recopila y estructura las ecuaciones y modelos matemáticos de los recortadores (también llamados circuitos limitadores o *clippers*) presentados en la Nota 8. Incluye el análisis de recortadores en paralelo (simples y polarizados) y recortadores en serie (polarizados con diodo directo y con diodo invertido), detallando las condiciones de umbral, tensiones límites, corrientes de conducción, voltajes de bloqueo y ángulos de conmutación.

---

## 1. Recortador Paralelo Simple y Polarizado (Biased Parallel Clipper)

En esta topología, la rama del diodo se conecta en paralelo con los terminales de salida del circuito. Su función es "fijar" la salida al voltaje umbral del diodo, absorbiendo el excedente de la tensión de entrada a través de una resistencia en serie.

### 1.1 Ecuación de la Señal de Entrada
Tensión alterna periódica sinusoidal de excitación aplicada al circuito limitador.

$$
v_s(t) = V_m \sin(\omega t)
$$

### 1.2 Condición de Polarización Directa (Conducción)
Umbral de tensión en el cual el diodo paralelo entra en estado activo, estableciendo una caída fija en la salida.

* **Caso Simple (Sin polarización externa):**
  $$
  v_s > V_K
  $$
* **Caso Polarizado (Con fuente DC en serie con el diodo):**
  $$
  v_s > V_{DC} + V_K
  $$

### 1.3 Comportamiento Dinámico del Voltaje de Salida
Voltaje transitorio en bornes de la carga en función de la tensión instantánea de entrada.

* **Caso Polarizado Positivo:**
  $$
  v_o(t) = \begin{cases} V_{DC} + V_K & \text{si } v_s(t) > V_{DC} + V_K \\ v_s(t) & \text{si } v_s(t) \leq V_{DC} + V_K \end{cases}
  $$

### 1.4 Parámetros Límites del Recortador Paralelo Polarizado
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Nivel superior de recorte fijado.
  $$
  v_{o,\max} = V_{DC} + V_K
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Semiciclo negativo que atraviesa íntegramente al diodo en bloqueo.
  $$
  v_{o,\min} = -V_m
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Voltaje máximo de bloqueo soportado cuando la entrada alcanza su mínimo negativo.
  $$
  \text{PIV} = V_m + V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Circula en el instante en que la señal de entrada alcanza su amplitud máxima positiva ($v_s = V_m$).
  $$
  I_{D,\max} = \frac{V_m - (V_{DC} + V_K)}{R}
  $$

---

## 2. Recortador Serie Polarizado (Diodo Directo)

En la configuración serie, la rama del diodo y la fuente de polarización están en serie con la carga. Su propósito es eliminar por completo la porción inferior de la señal, permitiendo el paso únicamente cuando la entrada supera el umbral establecido.

### 2.1 Ecuación Dinámica del Voltaje de Salida
La salida $v_o(t)$ se mide a través de la resistencia de carga de salida $R$.

$$
v_o(t) = \begin{cases} v_s(t) - V_{DC} - V_K & \text{si } v_s(t) > V_{DC} + V_K \\ 0 & \text{si } v_s(t) \leq V_{DC} + V_K \end{cases}
$$

### 2.2 Parámetros Límites del Recortador Serie
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Voltaje pico alcanzado en la carga.
  $$
  v_{o,\max} = V_{m} - V_{DC} - V_K
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Salida nula en el semiciclo de corte.
  $$
  v_{o,\min} = 0\text{ V}
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Tensión de bloqueo en el pico negativo de entrada.
  $$
  \text{PIV} = V_m + V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Ocurre en el pico positivo de la señal de entrada.
  $$
  I_{D,\max} = \frac{V_m - V_{DC} - V_K}{R}
  $$

### 2.3 Ángulo de Inicio de Conducción ($\theta_{\text{on}}$)
Ángulo eléctrico en el cual el diodo inicia la conducción durante la pendiente ascendente del semiciclo positivo.

$$
\theta_{\text{on}} = \arcsin\left(\frac{V_{DC} + V_K}{V_m}\right)
$$

---

## 3. Recortador Serie Polarizado (Diodo Invertido)

Al invertir el diodo (ánodo conectado a la fuente continua $V_{DC}$ y cátodo al nodo de salida), el circuito modifica su lógica: en lugar de anular la salida, fija un nivel de voltaje mínimo de recorte, impidiendo que la señal descienda por debajo de él.

### 3.1 Condición de Polarización Directa (Conducción)
El diodo invertido se polariza directamente cuando la entrada desciende por debajo del umbral diferencial.

$$
v_s < V_{DC} - V_K
$$

### 3.2 Ecuación Dinámica del Voltaje de Salida
El voltaje se mide en el cátodo del diodo (nodo de salida en la resistencia).

$$
v_o(t) = \begin{cases} v_s(t) & \text{si } v_s(t) \geq V_{DC} - V_K \\ V_{DC} - V_K & \text{si } v_s(t) < V_{DC} - V_K \end{cases}
$$

### 3.3 Parámetros Límites del Diodo Invertido
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Amplitud máxima positiva, la cual pasa sin alteración.
  $$
  v_{o,\max} = V_{m}
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Nivel inferior de recorte fijado.
  $$
  v_{o,\min} = V_{DC} - V_K
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Voltaje máximo de bloqueo soportado, que ocurre en el pico positivo de la entrada ($v_s = V_m$).
  $$
  \text{PIV} = V_m - V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Circula cuando la entrada alcanza su mínimo absoluto en el semiciclo negativo ($v_s = -V_m$).
  $$
  I_{D,\max} = \frac{V_{DC} - V_K + V_m}{R}
  $$

### 3.4 Ángulo de Corte de Conducción ($\theta_{\text{off}}$)
Ángulo eléctrico en el cual la señal cruza el límite de umbral y el diodo apaga.

$$
\theta_{\text{off}} = \arcsin\left(\frac{V_{DC} - V_K}{V_m}\right)
$$

> [!WARNING]
> **Tensión Inversa de Pico (PIV) en Recortadores**: La adición de una fuente DC de polarización modifica severamente el voltaje de bloqueo inverso. En recortadores paralelo y serie directos, el PIV es la suma de voltajes ($\text{PIV} = V_m + V_{DC}$). Si $V_{DC}$ es elevado, el diodo puede entrar fácilmente en ruptura inversa en el semiciclo opuesto. El diodo seleccionado debe cumplir con holgura la condición $V_{BR} > V_m + V_{DC}$.

> [!IMPORTANT]
> **Diferencia Fundamental entre Serie y Paralelo**: 
> * El **recortador paralelo** preserva la forma de onda original de la señal en bornes de la carga y únicamente "corta" o recorta los picos que exceden el umbral establecido.
> * El **recortador serie** tradicional (diodo directo) **elimina** por completo la señal que se encuentra por debajo del umbral, provocando que la salida sea nula ($0\text{ V}$) durante los intervalos de corte.

---

---

Este documento recopila y estructura las ecuaciones y modelos matemáticos de multiplicadores de voltaje (enfocados en el circuito duplicador) y diodos Zener como reguladores de voltaje descritos en la Nota 9. Incluye las expresiones de rizado, el modelado del diodo Zener real con resistencia dinámica y las fórmulas para el diseño por el peor caso de regulación y potencia del regulador Zener.

---

## 1. Circuitos Multiplicadores (Duplicador de Voltaje)

Los multiplicadores elevan la tensión de alterna (AC) y la rectifican a corriente directa (DC) a valores que son múltiplos enteros del valor pico de la señal de entrada senoidal ($v_s(t) = V_m \sin(\omega t)$).

### 1.1 Condición de Mantenimiento de Carga
Constante de tiempo de descarga mínima necesaria para que los capacitores retengan la carga entre los ciclos de alterna, garantizando una salida estable.

$$
R_L C_1 > \frac{1}{f} \quad ; \quad R_L C_2 > \frac{1}{f}
$$

### 1.2 Voltaje de Salida en Régimen Permanente
Voltaje de continua real en la carga que incorpora la caída debida a la descarga parcial entre ciclos de conducción.

$$
V_{o,\text{DC}} \approx 2 V_m - \frac{I_{\text{carga}}}{f \cdot C_2}
$$

### 1.3 Amplitud del Rizado de Salida ($\Delta V_o$)
Oscilación alterna residual presente en la carga.

$$
\Delta V_o \approx \frac{V_o}{f \cdot R_L \cdot C_2}
$$

### 1.4 Voltaje de Rizo Pico a Pico ($V_{\text{rizado,pp}}$)
Magnitud máxima de oscilación alterna de extremo a extremo en bornes de la salida.

$$
V_{\text{rizado,pp}} = \frac{I_{\text{carga}}}{f \cdot C_2}
$$

### 1.5 Tensión Inversa de Pico del Diodo (PIV)
Tensión inversa máxima que debe soportar cada uno de los diodos rectificadores de la etapa multiplicadora.

$$
\text{PIV} \geq 2 V_m
$$

### 1.6 Generalización para Multiplicadores de Orden $n$
Tensión DC de salida teórica obtenida al encadenar en cascada $n$ etapas duplicadoras o multiplicadoras de voltaje.

$$
V_o \approx n \cdot V_m
$$

---

## 2. Modelado del Diodo Zener Práctico

El diodo Zener está diseñado para operar en polarización inversa en la región de ruptura o avalancha. Un Zener real posee una resistencia dinámica intrínseca ($r_z$) que altera su caída en bornes en función de la corriente inversa que lo atraviesa.

### 2.1 Ecuación del Voltaje Zener Real
Voltaje total de regulación en terminales del diodo para una corriente de operación inversa $I_Z$ dada.

$$
V_Z = V_{z0} + I_Z \cdot r_z
$$

### 2.2 Voltaje Intrínseco de Ruptura Ideal ($V_{z0}$)
Voltaje ideal extrapolado de la región de avalancha libre de corrientes. Se calcula a partir del voltaje comercial ($V_Z$) medido por el fabricante a una corriente de prueba de referencia ($I_{ZT}$).

$$
V_{z0} = V_Z - I_{ZT} \cdot r_z
$$

---

## 3. Diseño y Ecuaciones del Regulador Zener

El regulador Zener utiliza una resistencia limitadora $R_S$ conectada en serie con la fuente variable $V_s$ para mantener un voltaje constante de salida en paralelo con la carga.

### 3.1 Ecuaciones de Kirchhoff (LKC y LVK)
Leyes fundamentales de interconexión aplicadas al regulador.

* **Ley de Corrientes (Nodo Regulado):**
  $$
  I_S = I_Z + I_L
  $$
* **Ley de Voltajes (Malla de Entrada):**
  $$
  V_s - I_S \cdot R_S - V_o = 0
  $$

### 3.2 Resistencia Limitadora de Corriente General ($R_S$)
Ecuación fundamental de la malla serie del regulador, donde el voltaje de salida $V_o$ equivale a la caída real del Zener.

$$
R_S = \frac{V_s - V_o}{I_Z + I_L} = \frac{V_s - (V_{z0} + I_Z \cdot r_z)}{I_Z + I_L}
$$

### 3.3 Ecuación de Diseño de $R_S$ bajo el "Peor Caso"
Fórmula empleada para calcular la resistencia limitadora máxima para asegurar que el diodo Zener no abandone la región de avalancha bajo las condiciones más exigentes (voltaje de entrada mínimo $V_{s(\min)}$ y corriente de carga máxima $I_{L(\max)}$). Se define una corriente mínima de seguridad $I_{z(\min)}$.

$$
R_S = \frac{V_{s(\min)} - V_{z0} - r_z \cdot I_{z(\min)}}{I_{z(\min)} + I_{L(\max)}}
$$

### 3.4 Corriente Máxima Zener ($I_{z(\max)}$) en Vacío
Ocurre en la condición de entrada más favorable (voltaje de entrada máximo $V_{s(\max)}$) y en condiciones de carga ausente o desconectada ($I_L = 0\text{ A}$).

$$
I_{z(\max)} \approx \frac{V_{s(\max)} - V_Z}{R_S}
$$

### 3.5 Disipación de Potencia Máxima del Zener ($P_{Z(\max)}$)
Potencia térmica máxima que experimenta el componente en vacío. Se utiliza para seleccionar comercialmente el diodo con una potencia nominal adecuada.

$$
P_{Z(\max)} = V_Z \cdot I_{z(\max)}
$$

> [!WARNING]
> **Peligro de Destrucción Térmica en Vacío**: El diodo Zener disipa su máxima potencia térmica ($P_{Z(\max)}$) cuando la corriente de carga cae a cero ($I_L = 0$) y la fuente está en su punto de máxima amplitud ($V_{s(\max)}$). En esta condición, toda la corriente del circuito se desvía por el Zener. Para evitar daños irreversibles, el componente seleccionado debe disipar por lo menos un $50\%$ más de potencia nominal que la máxima calculada: $P_{\text{nominal}} \geq 1.5 \cdot P_{Z(\max)}$.

> [!IMPORTANT]
> **Criterio de Regulación en Peor Caso**: Para garantizar que el Zener mantenga el voltaje estable y no entre en zona de corte, la corriente de seguridad $I_{z(\min)}$ debe elegirse de forma prudente. Una regla de diseño estándar es asignarle un valor cercano al $10\%$ de la corriente nominal Zener o un margen mínimo fijo de $5\text{ mA}$ a $10\text{ mA}$.

---

---

## Glosario de Variables

* **$A_n$**: Factor de atenuación del voltaje del armónico $n$ (adimensional).
* **$C$**: Capacitancia del condensador de filtrado (F). Típicamente del tipo electrolítico en el orden de $\mu\text{F}$.
* **$C_1, C_2$**: Capacitancias de los condensadores de almacenamiento (F).
* **$E$**: Tensión de polarización en corriente continua (V).
* **$E_{\max}, E_{\min}$**: Tensiones instantáneas máxima y mínima del generador de señal mixta (V).
* **$FF$**: Factor de forma de voltaje (adimensional).
* **$FR$**: Factor de rizo porcentual (%).
* **$I_1, I_2$**: Corrientes continuas a través del diodo medidas en las dos condiciones asociadas (A).
* **$I_D$**: Corriente instantánea en el diodo (A).
* **$I_L, I_{L(\max)}$**: Corriente nominal y máxima demandada por la carga (A).
* **$I_S$**: Corriente total de suministro provista por la fuente a través de $R_S$ (A).
* **$I_Z$**: Corriente inversa que atraviesa el diodo Zener (A).
* **$I_m$**: Corriente de pico en la carga (A), definida como $I_m = V_{o,m} / R_L$.
* **$I_{D(avg)}$**: Corriente continua promedio individual por diodo (A).
* **$I_{D(rms)}$**: Corriente eficaz individual por diodo (A).
* **$I_{D,\max}$**: Corriente máxima de conducción en directa a través del diodo (A).
* **$I_{D,\max}, I_{D,\min}$**: Corrientes máxima y mínima reales en el diodo ante el swing de AC (A).
* **$I_{DQ}$**: Corriente de polarización en el punto Q (A).
* **$I_{ZT}$**: Corriente de prueba de referencia proporcionada en la hoja de datos (A).
* **$I_{\text{carga}}$**: Corriente continua promedio consumida por la carga (A).
* **$I_{r(rms)}$**: Corriente eficaz del rizo en alterna (A).
* **$I_{z(\max)}$**: Corriente máxima en inversa soportada por el Zener en condiciones críticas (A).
* **$I_{z(\min)}$**: Corriente mínima de polarización inversa de seguridad para garantizar la regulación (A).
* **$L$**: Inductancia del filtro en serie (H).
* **$N_p, N_s$**: Número de espiras en el devanado primario y secundario del transformador (adimensional).
* **$P_{AC}$**: Potencia eficaz total absorbida en alterna por la carga (W).
* **$P_{CA}$**: Potencia variable del rizo disipada como calor en la carga (W).
* **$P_{CD}$**: Potencia promedio útil de directa en la carga (W).
* **$P_{RMS}$**: Potencia total eficaz suministrada a la carga (W).
* **$P_{Z(\max)}$**: Potencia térmica máxima disipada por el diodo Zener (W).
* **$P_{ac}$**: Potencia total eficaz alterna disipada en la carga (W).
* **$P_{dc}$**: Potencia de corriente directa útil entregada a la carga (W).
* **$R$**: Resistencia limitadora de corriente en serie ($\Omega$).
* **$R_L$**: Resistencia de la carga ($\Omega$).
* **$R_S$**: Resistencia limitadora de corriente serie ($\Omega$).
* **$R_{\text{CD}}$**: Resistencia estática en corriente continua ($\Omega$).
* **$T$**: Temperatura absoluta en Kelvin ($\text{K} = {^\circ\text{C}} + 273.15$).
* **$V_1, V_2$**: Tensiones continuas en terminales del diodo medidas en dos condiciones distintas (V).
* **$V_D$**: Voltaje de umbral del diodo en directa (V).
* **$V_K$**: Voltaje de umbral en directa del diodo (V). Típicamente $0.7\text{ V}$ para silicio.
* **$V_T$**: Voltaje térmico del semiconductor (V). Típicamente $\approx 26\text{ mV}$ a $25^\circ\text{C}$.
* **$V_Z$**: Voltaje de regulación en terminales del diodo Zener (V).
* **$V_m$**: Amplitud pico de la señal de alterna de entrada (V).
* **$V_o$**: Voltaje regulado final aplicado a la carga (V).
* **$V_p, V_s$**: Tensiones eficaces (RMS) en el primario y secundario (V).
* **$V_s, V_{s(\min)}, V_{s(\max)}$**: Tensión nominal, mínima y máxima entregada por la fuente variable de DC (V).
* **$V_{BR}$**: Voltaje de ruptura inversa del diodo o *Breakdown Voltage* (V).
* **$V_{CD}, I_{CD}$**: Voltaje y corriente promedio en corriente continua de la carga (V, A).
* **$V_{D,\max}, V_{D,\min}$**: Caídas de tensión máxima y mínima reales en el diodo ante el swing de AC (V).
* **$V_{DC}$**: Voltaje de la fuente continua de polarización serie en la rama (V).
* **$V_{DC}, I_{DC}$**: Voltaje y corriente promedio en corriente continua de la carga (V, A).
* **$V_{D_Q}, I_{D_Q}$**: Coordenadas del punto $Q$ en continua (V, A).
* **$V_{PRD}$**: Voltaje pico repetitivo del diodo en inversa o *Peak Repetitive Reverse Voltage* (V).
* **$V_{\text{rizado,pp}}$**: Voltaje de rizo pico a pico en la carga (V).
* **$V_{in}$**: Tensión continua de la fuente de entrada (V).
* **$V_{o,\text{DC}}, V_o$**: Voltaje continuo promedio de salida en bornes de la carga (V).
* **$V_{o,m}$**: Voltaje pico real corregido en la carga (V).
* **$V_{r(rms),\text{filtrado}}$**: Voltaje de rizo eficaz suavizado final (V).
* **$V_{r(rms)}$**: Voltaje eficaz del rizo de corriente alterna en la carga (V).
* **$V_{rms}, I_{rms}$**: Voltaje y corriente eficaces en corriente alterna de la carga (V, A).
* **$V_{rms}, V_{rms(\text{pri})}, V_{rms(\text{sec})}$**: Tensiones eficaces (RMS) en general, del primario y del secundario del transformador (V).
* **$V_{s,\text{pico}}$**: Tensión pico instantánea senoidal en el secundario (V).
* **$V_{z0}$**: Voltaje de ruptura ideal intrínseco de la unión semiconductora (V).
* **$\Delta V_D, \Delta I_D$**: Variaciones finitas en terminales del diodo entre sus límites de AC (V, A).
* **$\Delta V_o$**: Amplitud eficaz del rizo de salida (V).
* **$\eta$**: Eficiencia de rectificación (%).
* **$\omega$**: Frecuencia angular de la red de entrada (rad/s), definida como $\omega = 2\pi f$.
* **$\phi_n$**: Desfase inductivo de corriente en el armónico $n$ (rad o grados).
* **$\text{PIV}$**: Voltaje inverso de pico de diseño de los diodos (V).
* **$\text{THD}$**: Distorsión armónica total de la tensión de salida (%).
* **$\theta_{\text{off}}$**: Ángulo de conmutación de apagado (rad o grados).
* **$\theta_{\text{on}}$**: Ángulo de conmutación de encendido (rad o grados).
* **$a$**: Relación de transformación de vueltas (adimensional), definido como $a = N_1 / N_2$.
* **$a_n$**: Coeficiente o amplitud pico del $n$-ésimo armónico (V).
* **$f$**: Frecuencia de la señal alterna de entrada (Hz).
* **$f_c$**: Frecuencia de corte a $-3\text{ dB}$ del filtro (Hz).
* **$f_{\text{entrada}}, f_{\text{rizo}}$**: Frecuencias de entrada y de rizo en la salida (Hz).
* **$f_{\text{entrada}}, f_{\text{salida}}$**: Frecuencias de entrada y salida (Hz).
* **$i_o(t)$**: Corriente instantánea suavizada a través de la carga (A).
* **$k$**: Constante de Boltzmann ($1.3806 \times 10^{-23}\text{ J/K}$).
* **$n$**: Número entero de etapas o factor multiplicador del circuito (adimensional).
* **$q$**: Carga eléctrica del electrón ($1.6022 \times 10^{-19}\text{ C}$).
* **$r_d$**: Resistencia dinámica diferencial teórica ($\Omega$).
* **$r_z$**: Resistencia interna dinámica del Zener en la región de avalancha ($\Omega$).
* **$r_{\text{obj}}$**: Factor de rizo porcentual objetivo deseado en el diseño (adimensional).
* **$v_o(t)$**: Voltaje rectificado instantáneo en bornes de la carga (V).
* **$v_s(t)$**: Voltaje transitorio instantáneo del secundario del transformador (V).
* **$v_s(t), v_o(t)$**: Voltajes transitorios instantáneos de entrada y de salida (V).
* **$|Z_n|$**: Módulo de la impedancia reactiva del circuito para el armónico $n$ ($\Omega$).
