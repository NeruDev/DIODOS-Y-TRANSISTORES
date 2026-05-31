<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_4
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Rectificadores de Media Onda con Diodo Real y Transformador

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

* **Nomenclatura:**
  * $N_p, N_s$: Número de espiras en el devanado primario y secundario del transformador (adimensional).
  * $V_p, V_s$: Tensiones eficaces (RMS) en el primario y secundario (V).
  * $V_{s,\text{pico}}$: Tensión pico instantánea senoidal en el secundario (V).

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

* **Nomenclatura:**
  * $v_o(t)$: Voltaje transitorio instantáneo en bornes de la carga (V).
  * $v_s(t)$: Voltaje transitorio instantáneo del secundario del transformador (V).
  * $V_D$: Caída de voltaje del diodo en polarización directa (V). Típicamente $0.7\text{ V}$ para diodos de silicio comerciales.
  * $V_{o,m}$: Voltaje pico corregido de la señal de salida en la carga (V).
  * $V_{CD}, I_{CD}$: Voltaje y corriente promedio reales en continua de la carga (V, A).
  * $V_{rms}, I_{rms}$: Voltaje y corriente eficaces reales en alterna de la carga (V, A).
  * $R_L$: Resistencia de la carga ($\Omega$).

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

* **Nomenclatura:**
  * $I_{D(rms)}$: Corriente eficaz a través del diodo rectificador (A).
  * $\text{PIV}$: Tensión inversa de pico o *Peak Inverse Voltage* (V).
  * $V_{PRD}$: Voltaje pico repetitivo del diodo en inversa o *Peak Repetitive Reverse Voltage* (V).
  * $V_{BR}$: Voltaje de ruptura inversa del diodo o *Breakdown Voltage* (V).

> [!IMPORTANT]
> **Efectos Despreciados en Modelados Simplificados**: En análisis introductorios se asume $V_D = 0\text{ V}$. Sin embargo, en aplicaciones de baja tensión (ej. secundario de $5\text{ V}$), ignorar la caída del diodo de $0.7\text{ V}$ induce errores superiores al $14\%$ en todos los cálculos de voltaje, potencia y corriente, afectando la estabilidad térmica esperada. Los modelos de alta fidelidad además incorporan la resistencia dinámica incremental ($r_d$) y la corriente de fuga inversa ($I_S$), las cuales suelen ser despreciables ante cargas de baja resistencia.

---

## 4. Glosario de Términos Técnicos

* **Voltaje de Umbral ($V_D$):** Voltaje de barrera de potencial mínimo (típicamente $0.7\text{ V}$ para silicio) necesario para superar la zona de depleción del semiconductor y establecer una corriente directa apreciable.
* **Tensión Inversa de Pico (PIV):** Voltaje de bloqueo máximo instantáneo que experimenta el diodo en sus extremos durante el semiciclo donde la fuente alterna posee polaridad inversa.
* **Voltaje de Ruptura ($V_{BR}$):** Tensión límite en polarización inversa a partir de la cual se genera una multiplicación por avalancha de portadores libres, dañando irreversiblemente el dispositivo si no se limita externamente la corriente.
* **Corriente RMS del Diodo:** Magnitud eficaz de la corriente de conducción directa unidireccional pulsante que fluye por el semiconductor, empleada para calcular su disipación de potencia disipada intrínseca en directa ($P_D = I_{D(rms)}^2 \cdot r_d + I_{CD} \cdot V_D$).
* **Transformador Reductor:** Dispositivo electromagnético de inducción mutua acoplado magnéticamente que disminuye el nivel de tensión alterna de entrada conservando la frecuencia de la línea.
