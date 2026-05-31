filepath = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1-examen.md'

exam_content = r"""# Formulario de Examen: Tema 1 (Diodos y Rectificadores)

> Documento simplificado para consulta rápida en exámenes. Contiene exclusivamente fórmulas, modelos ideales/prácticos y aproximaciones estandarizadas.

---

## 1. Análisis DC y Pequeña Señal

### 1.1 Modelo del Diodo en DC
* **Caídas Típicas de Voltaje ($V_D$):**

  | Tipo | $V_D$ típico |
  | --- | --- |
  | Silicio | $0.7\text{ V}$ |
  | Germanio | $0.3\text{ V}$ |
  | Schottky | $0.2\text{ V} - 0.3\text{ V}$ |
  | LED | $1.8\text{ V} - 3.3\text{ V}$ |

* **Regla Visual Rápida (Análisis Gráfico):**
  * **Diodo OFF** $\implies I_D \approx 0$
  * **Diodo ON** $\implies V_D \approx 0.7\text{ V}$

* **Ecuación de Shockley:**
  $$ I_D = I_S \left( e^{\frac{V_D}{n V_T}} - 1 \right) $$
* **Voltaje Térmico ($V_T$):**
  $$ V_T = \frac{k T}{q} \approx 25\text{ mV a } 26\text{ mV} \quad \text{(a temp. ambiente)} $$
* **LVK (Malla Simple):**
  $$ V_{in} - I_D R - V_D = 0 $$
* **Puntos de la Recta de Carga:**
  * Eje Y (Corto, $V_D=0$): $I_D = \frac{V_{in}}{R}$
  * Eje X (Abierto, $I_D=0$): $V_D = V_{in}$

### 1.2 Método de Análisis Rápido (Estado DC)
1. **Asumir:** ON ($0.7\text{ V}$) u OFF (Circuito abierto).
2. **Resolver:** Ecuaciones de malla o nodo.
3. **Verificar:**
   * Si asumiste ON $\implies I_D$ debe ser $> 0$.
   * Si asumiste OFF $\implies V_D$ debe ser $< 0.7\text{ V}$.

### 1.3 Pequeña Señal (AC)
* **Resistencia Dinámica ($r_d$):**
  $$ r_d \approx \frac{n V_T}{I_{DQ}} $$
* **Criterio de Pequeña Señal:**
  $$ \hat{v}_d \ll n V_T \quad \text{(Criterio práctico: } \hat{v}_d < 5\text{ mV o } 10\text{ mV)} $$
* **Componentes de Señal Mixta:**
  $$ i_D(t) = I_{DQ} + \frac{V_m}{R + r_d} \sin(\omega t) $$

---

## 2. Rectificadores

> [!WARNING]
> **Condición de Validez:** Las aproximaciones estandarizadas de $V_{DC}$, $V_{rms}$ y eficiencia son válidas asumiendo **$V_m \gg V_D$**. Para señales pequeñas, el error se incrementa y se debe usar integración angular.

### Tabla Rápida de Rectificadores
| Circuito | $V_{DC}$ | $f_{\text{rizo}}$ |
| --- | --- | --- |
| **Media Onda** | $0.318 V_m$ | $f_{in}$ |
| **Onda Completa** | $0.636 V_m$ | $2f_{in}$ |

### 2.1 Transformador
* **Voltaje RMS y Pico del Secundario:**
  $$ V_{rms(\text{sec})} = \frac{N_s}{N_p} V_{rms(\text{pri})} \quad ; \quad V_{s,\text{pico}} = \sqrt{2} V_{rms(\text{sec})} $$

### 2.2 Rectificador de Media Onda
* **Voltaje Pico en Carga ($V_{o,m}$):**
  $$ V_{o,m} = V_{s,\text{pico}} - V_D \quad \text{(Ideal: } V_D = 0\text{V; Real: } V_D \approx 0.7\text{V)} $$
* **Componente DC (Promedio):**
  $$ V_{DC} = \frac{V_{o,m}}{\pi} \approx 0.318 V_{o,m} $$
* **Componente RMS (Eficaz):**
  $$ V_{rms} = \frac{V_{o,m}}{2} = 0.500 V_{o,m} $$
* **Eficiencia Máxima ($\eta$):** $\approx 40.6\%$
* **Voltaje Inverso de Pico (PIV):**
  $$ \text{PIV} \approx V_m $$

### 2.3 Rectificador de Onda Completa (Derivación Central)
* **Voltaje Pico en Carga ($V_{o,m}$):**
  $$ V_{o,m} = V_m - V_D $$
* **Componente DC (Promedio):**
  $$ V_{DC} = \frac{2 V_{o,m}}{\pi} \approx 0.636 V_{o,m} $$
* **Componente RMS (Eficaz):**
  $$ V_{rms} = \frac{V_{o,m}}{\sqrt{2}} \approx 0.707 V_{o,m} $$
* **Eficiencia Máxima ($\eta$):** $\approx 81.2\%$
* **Voltaje Inverso de Pico (PIV por diodo):**
  $$ \text{PIV} \approx 2 V_m $$

### 2.4 Rectificador de Onda Completa (Puente)
* **Voltaje Pico en Carga ($V_{o,m}$):** Conducen 2 diodos en serie.
  $$ V_{o,m} = V_m - 2V_D $$
* **Componente DC y RMS:** Mismas fórmulas que la derivación central.
* **Eficiencia Máxima ($\eta$):** $\approx 81.2\%$
* **Voltaje Inverso de Pico (PIV por diodo):**
  $$ \text{PIV} \approx V_m $$

---

## 3. Rizo y Filtros (Series de Fourier)

### 3.1 Factor de Rizo ($FR$)
$$ FR = \frac{V_{r(rms)}}{V_{DC}} \times 100\% $$

### 3.2 Serie de Fourier (Onda Completa Ideal sin filtro)
$$ v_o(t) = \frac{2 V_m}{\pi} - \frac{4 V_m}{\pi} \sum_{n=1}^{\infty} \frac{\cos(2n\omega t)}{4n^2 - 1} $$
* **Frecuencia del rizo:** $f_{\text{rizo}} = 2 f_{\text{in}}$ (Onda Completa), $f_{\text{rizo}} = f_{\text{in}}$ (Media Onda).

### 3.3 Filtro Capacitivo de Entrada
* **Voltaje de Rizo (Aproximación lineal):**
  $$ V_{r(pp)} \approx \frac{V_{o,m}}{f_{\text{rizo}} R_L C} $$
* **Voltaje DC Filtrado:**
  $$ V_{DC} \approx V_{o,m} - \frac{V_{r(pp)}}{2} $$
* **Criterios de Atenuación Rápida:**
  * $C \uparrow \implies FR \downarrow$
  * $f \uparrow \implies FR \downarrow$
  * $R_L \downarrow \implies FR \uparrow$ (Carga pesada aumenta el rizo).

---

## 4. Diodos de Propósito Especial y Aplicaciones

### 4.1 Diodo Zener (Regulación de Voltaje)
* **Condición Estricta de Regulación:**
  $$ I_{Z(\min)} < I_Z < I_{Z(\max)} $$
  * $I_{Z(\max)} = \frac{P_{Z(\max)}}{V_Z}$
* **Resistencia Limitadora (Diseño en el peor de los casos):**
  $$ R_{S(\max)} = \frac{V_{in(\min)} - V_Z}{I_{L(\max)} + I_{Z(\min)}} $$
  $$ R_{S(\min)} = \frac{V_{in(\max)} - V_Z}{I_{L(\min)} + I_{Z(\max)}} $$
* **Regulación de Línea:**
  $$ \%Reg = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\% $$

### 4.2 Recortadores (Clippers)
> Limitan o "recortan" una porción de la señal alterna sin distorsionar el resto de la forma de onda.
* **Recortador Serie:** Diodo en serie con la carga. Recorta la señal cuando el diodo está en OFF.
* **Recortador Paralelo:** Diodo en paralelo con la carga. Recorta la señal cuando el diodo está en ON.
* **Nivel de Recorte (Polarizado):**
  $$ V_{\text{recorte}} = V_{\text{ref}} \pm V_D $$
  *(Donde $V_{\text{ref}}$ es la fuente de DC conectada al diodo).*

### 4.3 Circuitos Clásicos Adicionales
* **Sujetadores (Clampers):** Desplazan el nivel DC.
  $$ v_o(t) \approx v_i(t) \pm V_m $$
  * Condición de diseño: $RC \gg T$
* **Multiplicadores de Voltaje:**
  $$ V_o \approx n \cdot V_m \quad \text{(Aproximación sin carga)} $$
* **Diodo Varactor:** Capacitancia variable controlada por voltaje inverso ($V_R$).
  $$ C_j \propto \frac{1}{(V_R)^n} $$

### 4.4 Otros Diodos Especiales
| Diodo | Característica Principal | Aplicación Clave |
| --- | --- | --- |
| **Túnel** | Región de resistencia negativa. Alta velocidad. | Osciladores de alta frecuencia y microondas. |
| **PIN** | Capa intrínseca entre las regiones P y N. Resistencia variable con DC. | Interruptores de RF, atenuadores, fotodetectores rápidos. |
| **Gunn** | No tiene unión PN (semiconductor masivo tipo N). Resistencia negativa. | Generadores y osciladores de microondas. |
| **Avalancha**| Diseñado para operar en ruptura por avalancha de forma segura. | Generación de ruido de RF, protección contra sobretensiones. |
| **LASER** | Emisión estimulada de luz coherente (espectralmente pura). | Comunicaciones por fibra óptica, lectura óptica. |

---

## Glosario de Variables

| Símbolo | Nombre y Descripción |
|---------|----------------------|
| **$A_n$** | Factor de atenuación del voltaje del armónico $n$ (adimensional). |
| **$C$** | Capacitancia del condensador de filtrado (F). Típicamente del tipo electrolítico en el orden de $\mu\text{F}$. |
| **$C_1, C_2$** | Capacitancias de los condensadores de almacenamiento (F). |
| **$C_j$** | Capacitancia de la unión del varactor (F). |
| **$E$** | Tensión de polarización en corriente continua (V). |
| **$E_{\max}, E_{\min}$** | Tensiones instantáneas máxima y mínima del generador de señal mixta (V). |
| **$FF$** | Factor de forma de voltaje (adimensional). |
| **$FR$** | Factor de rizo porcentual (%). |
| **$I_1, I_2$** | Corrientes continuas a través del diodo medidas en las dos condiciones asociadas (A). |
| **$I_D$** | Corriente instantánea en el diodo (A). |
| **$I_{D(avg)}$** | Corriente continua promedio individual por diodo (A). |
| **$I_{D(rms)}$** | Corriente eficaz individual por diodo (A). |
| **$I_{D,\max}, I_{D,\min}$** | Corrientes máxima y mínima reales en el diodo ante el swing de AC (A). |
| **$I_{DQ}$** | Corriente de polarización en el punto Q (A). |
| **$I_L, I_{L(\max)}, I_{L(\min)}$** | Corriente nominal, máxima y mínima demandada por la carga (A). |
| **$I_S$** | Corriente total de suministro provista por la fuente a través de $R_S$ (A). |
| **$I_Z$** | Corriente inversa que atraviesa el diodo Zener (A). |
| **$I_{Z(\max)}$** | Corriente máxima en inversa soportada por el Zener en condiciones críticas (A). |
| **$I_{Z(\min)}$** | Corriente mínima de polarización inversa de seguridad para garantizar la regulación (A). |
| **$I_{ZT}$** | Corriente de prueba de referencia proporcionada en la hoja de datos (A). |
| **$I_{\text{carga}}$** | Corriente continua promedio consumida por la carga (A). |
| **$I_m$** | Corriente de pico en la carga (A), definida como $I_m = V_{o,m} / R_L$. |
| **$I_{r(rms)}$** | Corriente eficaz del rizo en alterna (A). |
| **$L$** | Inductancia del filtro en serie (H). |
| **$N_p, N_s$** | Número de espiras en el devanado primario y secundario del transformador (adimensional). |
| **$P_{ac}$** | Potencia total eficaz alterna disipada en la carga (W). |
| **$P_{dc}$** | Potencia de corriente directa útil entregada a la carga (W). |
| **$P_{RMS}$** | Potencia total eficaz suministrada a la carga (W). |
| **$P_{Z(\max)}$** | Potencia térmica máxima disipada por el diodo Zener (W). |
| **$R, R_S$** | Resistencia limitadora de corriente serie ($\Omega$). |
| **$R_L$** | Resistencia de la carga ($\Omega$). |
| **$R_{\text{CD}}$** | Resistencia estática en corriente continua ($\Omega$). |
| **$T$** | Temperatura absoluta en Kelvin ($\text{K} = {^\circ\text{C}} + 273.15$). |
| **$V_1, V_2$** | Tensiones continuas en terminales del diodo medidas en dos condiciones distintas (V). |
| **$V_D, V_K$** | Voltaje de umbral del diodo en directa (V). Típicamente $0.7\text{ V}$ para silicio. |
| **$V_{D,\max}, V_{D,\min}$** | Caídas de tensión máxima y mínima reales en el diodo ante el swing de AC (V). |
| **$V_{DC}, I_{DC}$** | Voltaje y corriente promedio de continua en la carga (V, A). |
| **$V_{D_Q}, I_{D_Q}$** | Coordenadas del punto $Q$ en continua (V, A). |
| **$V_{FL}$** | Voltaje a plena carga (Full-Load) (V). |
| **$V_{NL}$** | Voltaje en vacío (No-Load) (V). |
| **$V_{PRD}$** | Voltaje pico repetitivo del diodo en inversa o *Peak Repetitive Reverse Voltage* (V). |
| **$V_R$** | Tensión inversa aplicada al varactor (V). |
| **$V_T$** | Voltaje térmico del semiconductor (V). Típicamente $\approx 26\text{ mV}$ a $25^\circ\text{C}$. |
| **$V_Z$** | Voltaje de regulación en terminales del diodo Zener (V). |
| **$V_{BR}$** | Voltaje de ruptura inversa del diodo o *Breakdown Voltage* (V). |
| **$V_{in}$** | Tensión continua de la fuente de entrada (V). |
| **$V_m$** | Amplitud pico de la señal de alterna de entrada (V). |
| **$V_o$** | Voltaje regulado final o rectificado en bornes de la carga (V). |
| **$V_{o,m}$** | Voltaje pico real corregido en la carga (V). |
| **$V_p, V_s$** | Tensiones eficaces (RMS) en el primario y secundario del transformador (V). |
| **$V_{r(rms)}$** | Voltaje eficaz del rizo de corriente alterna en la carga (V). |
| **$V_{rms}, I_{rms}$** | Voltaje y corriente eficaces en corriente alterna de la carga (V, A). |
| **$V_{rizado,pp}$** | Voltaje de rizo pico a pico en la carga (V). |
| **$V_s, V_{s(\min)}, V_{s(\max)}$** | Tensión nominal, mínima y máxima entregada por la fuente variable de DC (V). |
| **$V_{s,\text{pico}}$** | Tensión pico instantánea senoidal en el secundario (V). |
| **$V_{z0}$** | Voltaje de ruptura ideal intrínseco de la unión semiconductora (V). |
| **$\Delta V_D, \Delta I_D$** | Variaciones finitas en terminales del diodo entre sus límites de AC (V, A). |
| **$\Delta V_o$** | Amplitud eficaz del rizo de salida (V). |
| **$\eta$** | Eficiencia de rectificación (%). |
| **$\theta_{\text{on}}, \theta_{\text{off}}$** | Ángulo de encendido y apagado de conducción (rad o grados). |
| **$\omega$** | Frecuencia angular de la red de entrada (rad/s), $\omega = 2\pi f$. |
| **$\text{PIV}$** | Voltaje inverso de pico de diseño de los diodos (V). |
| **$\text{THD}$** | Distorsión armónica total de la tensión de salida (%). |
| **$a$** | Relación de transformación de vueltas ($a = N_1 / N_2$). |
| **$a_n$** | Coeficiente o amplitud pico del $n$-ésimo armónico (V). |
| **$f$** | Frecuencia de la señal alterna de entrada (Hz). |
| **$f_c$** | Frecuencia de corte a $-3\text{ dB}$ del filtro (Hz). |
| **$f_{\text{entrada}}, f_{\text{rizo}}$** | Frecuencias de entrada y de rizo en la salida (Hz). |
| **$k$** | Constante de Boltzmann ($1.3806 \times 10^{-23}\text{ J/K}$). |
| **$n$** | Número entero de etapas o multiplicador del circuito (adimensional). |
| **$q$** | Carga eléctrica del electrón ($1.6022 \times 10^{-19}\text{ C}$). |
| **$r_d$** | Resistencia dinámica diferencial teórica ($\Omega$). |
| **$r_z$** | Resistencia interna dinámica del Zener en la región de avalancha ($\Omega$). |
| **$r_{\text{obj}}$** | Factor de rizo porcentual objetivo deseado en el diseño (adimensional). |
| **$v_o(t), v_s(t)$** | Voltajes transitorios instantáneos de entrada/salida (V). |
| **$\|Z_n\|$** | Módulo de la impedancia reactiva del circuito para el armónico $n$ ($\Omega$). |
"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(exam_content)

print("Formulario-tema_1-examen.md completely rewritten with Zener formulas, Clippers, special diodes, reordering and glossary deduplication.")
