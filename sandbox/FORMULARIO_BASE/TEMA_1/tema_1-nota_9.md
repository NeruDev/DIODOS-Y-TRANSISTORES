<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_9
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Multiplicadores de Voltaje y Diodos Zener

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

* **Nomenclatura:**
  * $V_m$: Amplitud pico de la señal de alterna de entrada (V).
  * $f$: Frecuencia de la señal alterna de entrada (Hz).
  * $C_1, C_2$: Capacitancias de los condensadores de almacenamiento (F).
  * $R_L$: Resistencia de la carga ($\Omega$).
  * $V_{o,\text{DC}}, V_o$: Voltaje continuo promedio de salida en bornes de la carga (V).
  * $I_{\text{carga}}$: Corriente continua promedio consumida por la carga (A).
  * $\Delta V_o$: Amplitud eficaz del rizo de salida (V).
  * $V_{\text{rizado,pp}}$: Voltaje de rizo pico a pico en la carga (V).
  * $\text{PIV}$: Voltaje inverso de pico de diseño de los diodos (V).
  * $n$: Número entero de etapas o factor multiplicador del circuito (adimensional).

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

* **Nomenclatura:**
  * $V_Z$: Voltaje de regulación en terminales del diodo Zener (V).
  * $V_{z0}$: Voltaje de ruptura ideal intrínseco de la unión semiconductora (V).
  * $I_Z$: Corriente inversa que atraviesa el diodo Zener (A).
  * $r_z$: Resistencia interna dinámica del Zener en la región de avalancha ($\Omega$).
  * $I_{ZT}$: Corriente de prueba de referencia proporcionada en la hoja de datos (A).

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

* **Nomenclatura:**
  * $R_S$: Resistencia limitadora de corriente serie ($\Omega$).
  * $V_s, V_{s(\min)}, V_{s(\max)}$: Tensión nominal, mínima y máxima entregada por la fuente variable de DC (V).
  * $V_o$: Voltaje regulado final aplicado a la carga (V).
  * $I_S$: Corriente total de suministro provista por la fuente a través de $R_S$ (A).
  * $I_L, I_{L(\max)}$: Corriente nominal y máxima demandada por la carga (A).
  * $I_{z(\min)}$: Corriente mínima de polarización inversa de seguridad para garantizar la regulación (A).
  * $I_{z(\max)}$: Corriente máxima en inversa soportada por el Zener en condiciones críticas (A).
  * $P_{Z(\max)}$: Potencia térmica máxima disipada por el diodo Zener (W).

> [!WARNING]
> **Peligro de Destrucción Térmica en Vacío**: El diodo Zener disipa su máxima potencia térmica ($P_{Z(\max)}$) cuando la corriente de carga cae a cero ($I_L = 0$) y la fuente está en su punto de máxima amplitud ($V_{s(\max)}$). En esta condición, toda la corriente del circuito se desvía por el Zener. Para evitar daños irreversibles, el componente seleccionado debe disipar por lo menos un $50\%$ más de potencia nominal que la máxima calculada: $P_{\text{nominal}} \geq 1.5 \cdot P_{Z(\max)}$.

> [!IMPORTANT]
> **Criterio de Regulación en Peor Caso**: Para garantizar que el Zener mantenga el voltaje estable y no entre en zona de corte, la corriente de seguridad $I_{z(\min)}$ debe elegirse de forma prudente. Una regla de diseño estándar es asignarle un valor cercano al $10\%$ de la corriente nominal Zener o un margen mínimo fijo de $5\text{ mA}$ a $10\text{ mA}$.

---

## 4. Glosario de Términos Técnicos

* **Multiplicador de Voltaje:** Red rectificadora reactiva compuesta de diodos y capacitores interconectados diseñada para elevar la amplitud de alterna de entrada entregando una salida en corriente directa correspondiente a múltiplos enteros.
* **Duplicador de Voltaje:** Circuito elevador rectificador básico que acumula energía por semiciclo alternado en un par de condensadores para generar una salida de directa equivalente al doble de la tensión pico ($2V_m$).
* **Diodo Zener:** Componente semiconductor con dopaje selectivo diseñado para operar de forma continua, estable y reversible en la región de ruptura o avalancha inversa sin sufrir destrucción estructural.
* **Resistencia Dinámica Zener ($r_z$):** Resistencia equivalente interna del dispositivo Zener en conducción inversa que describe la pendiente incremental de voltaje frente a variaciones de corriente.
* **Regulación de Voltaje:** Capacidad de un circuito electrónico para mantener una tensión constante en bornes de la salida a pesar de variaciones en la tensión de alimentación de entrada o cambios en la corriente de carga.
* **Peor Caso de Regulación:** Condición crítica de diseño en la cual la fuente de tensión aporta su mínimo potencial histórico y la carga demanda su máximo consumo de corriente.
* **Potencia Zener:** Energía disipada como calor en el semiconductor en inversa igual al producto del voltaje Zener y la corriente inversa que lo atraviesa.
