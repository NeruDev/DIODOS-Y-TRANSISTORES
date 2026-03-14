¡Excelente iniciativa! Organizar el flujo de trabajo antes de entrar al laboratorio te ahorrará muchísimos problemas, especialmente cuando se trata de configurar el osciloscopio y hacer cálculos matemáticos con las series de Fourier.

Considerando tus datos:

* **Transformador $TX_1$:** Secundario de **12Vrms**.
* **Carga ($R$):** Resistor de potencia de **$10\Omega$**.
* **Inductor ($L$):** El primario de un transformador de 120V/12V a ~2A suele tener una inductancia alta y una resistencia de alambre considerable. Para efectos de este cálculo, propondremos valores típicos de **$L \approx 1.5H$** y una resistencia interna del devanado de **$R_L \approx 40\Omega$**. *(Deberás medirlos con precisión en el laboratorio).*
* **Capacitor ($C$):** **$2200\mu F$** (electrolítico).

A continuación, te desgloso paso a paso las fórmulas, los cálculos teóricos esperados y el instrumento de medición exacto a utilizar según el flujo de la práctica.

---

### Fase 1: Cálculos Base del Rectificador (Inciso a)

* **Instrumento:** Calculadora científica / Software analítico (Excel, Python, etc.)

Primero determinamos el voltaje pico rectificado ($V_m$). Un transformador de 12Vrms entrega un voltaje pico de $12\sqrt{2} \approx 16.97V$. Al pasar por el puente, la corriente atraviesa dos diodos (caída de $\approx 0.7V$ cada uno):


$$V_m = V_{sec(pico)} - 2V_D = 16.97V - 1.4V = 15.57V$$

Con $V_m$ y $R = 10\Omega$, calculamos el rendimiento teórico:

* **Voltaje de salida DC (Promedio):**

$$V_o(cd) = \frac{2V_m}{\pi} = \frac{2(15.57)}{\pi} \approx 9.91V$$


* **Corriente de salida DC:**

$$I_o(cd) = \frac{V_o(cd)}{R} = \frac{9.91}{10} \approx 0.991A$$


* **Voltaje de salida RMS:**

$$V_o(rms) = \frac{V_m}{\sqrt{2}} = \frac{15.57}{\sqrt{2}} \approx 11.01V$$


* **Corriente de salida RMS:**

$$I_o(rms) = \frac{V_o(rms)}{R} = \frac{11.01}{10} \approx 1.101A$$


* **Voltaje de Rizo (RMS):**

$$V_r(rizo) = \sqrt{V_o(rms)^2 - V_o(cd)^2} = \sqrt{11.01^2 - 9.91^2} \approx 4.80V$$


* **Corriente y Voltaje en los Diodos:**

$$I_D(prom) = \frac{I_o(cd)}{2} \approx 0.495A$$


$$I_D(rms) = \frac{I_o(rms)}{\sqrt{2}} \approx 0.778A$$


$$V_{PR} = V_{sec(pico)} \approx 16.97V \quad \text{(Voltaje Pico Inverso soportado)}$$


* **Potencias y Frecuencia:**

$$P_o(CA) = V_o(rms) \times I_o(rms) = 11.01 \times 1.101 \approx 12.12W$$


$$P_o(CD) = V_o(cd) \times I_o(cd) = 9.91 \times 0.991 \approx 9.82W$$


$$f = 2 \times f_{red} = 2 \times 60Hz = 120Hz$$



---

### Fase 2: Medición del Circuito Básico (Incisos b al h)

1. **(b, c) Voltajes de entrada y salida:**
* **Instrumento:** Osciloscopio Digital con puntas de voltaje (x10 recomendadas).
* **Acción:** Canal 1 al secundario (12Vrms). Canal 2 a la carga. **Precaución:** Nunca conectes la pinza de tierra de la sonda de salida a ningún nodo si estás midiendo la entrada al mismo tiempo con otra tierra en un punto diferente, provocarás un corto. Usa la función `Measure` para obtener Vrms, Vmean (promedio), Vpp y Frecuencia.


2. **(d, e, h) Corrientes $I_{in}$, $I_{out}$ e $I_{sec}$:**
* **Instrumento:** Sonda de corriente de Efecto Hall + Osciloscopio.
* **Acción:** Abraza el cable de la carga para $I_{out}$ y el cable del secundario para $I_{sec}$. La forma de onda de $I_{out}$ debe ser idéntica a la de $V_{out}$ (pulsante), mientras que $I_{sec}$ será alterna pero con distorsión cruzada.


3. **(f, g) Espectro de Frecuencia (Serie de Fourier):**
* **Instrumento:** Osciloscopio (Función `Math` -> `FFT`).
* **Acción:** Analiza el voltaje de salida. Teóricamente, el armónico fundamental de la salida DC es 0Hz (DC), y los armónicos de AC aparecen en múltiplos pares de la red: **120Hz ($n=2$), 240Hz ($n=4$), 360Hz ($n=6$), 480Hz ($n=8$), 600Hz ($n=10$)**.
* **Cálculo analítico de Fourier para corriente:**

$$I_o(t) = \frac{2V_m}{\pi R} - \frac{4V_m}{\pi R} \sum_{n=2,4,6...}^{\infty} \frac{1}{n^2-1} \cos(n\omega t)$$





---

### Fase 3: Filtro Inductivo (Incisos i, j, k)

* **Instrumentos:** Puente LCR portátil (para medir L y R del primario del transformador), Osciloscopio, Sonda de corriente.

1. **Medición de L y R:** Usa el puente LCR a 100Hz o 120Hz (lo más cercano a la frecuencia de rizo). Asumiremos los propuestos: $L = 1.5H$ y $R_L = 40\Omega$.
2. **Nueva Resistencia Total ($R_T$):**

$$R_T = R + R_L = 10\Omega + 40\Omega = 50\Omega$$


3. **Cálculo Analítico de $I_o(t)$ con filtro (Inciso j):**
La corriente DC disminuye drásticamente porque la resistencia del alambre del inductor absorbe energía:

$$I_{dc} = \frac{V_o(cd)}{R_T} = \frac{9.91V}{50\Omega} \approx 0.198A$$



Para el armónico principal ($n=2$, frecuencia 120Hz, $\omega = 2\pi \times 60 = 377$):

$$V_2 = \frac{4V_m}{3\pi} = \frac{4(15.57)}{3\pi} \approx 6.60V$$


$$Z_2 = \sqrt{R_T^2 + (2\omega L)^2} = \sqrt{50^2 + (2 \cdot 377 \cdot 1.5)^2} = \sqrt{2500 + 1279161} \approx 1131\Omega$$


$$I_2 = \frac{V_2}{Z_2} \approx \frac{6.60}{1131} \approx 5.8mA$$


4. **Factor de Rizo ($FR_i$) (Inciso k):**

$$I_r(rms) \approx \frac{I_2}{\sqrt{2}} \approx 4.1mA$$


$$FR_i = \frac{I_r(rms)}{I_{dc}} = \frac{0.0041}{0.198} = 2.07\%$$



*Efecto práctico:* El inductor alisa extremadamente bien la corriente, pero la caída de voltaje en su resistencia interna ($R_L$) hace que a la carga de $10\Omega$ le llegue muy poco voltaje ($V_{carga} = I_{dc} \cdot 10 \approx 1.98V$).

---

### Fase 4: Filtro Capacitivo (Incisos l, m)

* **Instrumentos:** Multímetro Digital (para $V_o(cd)$), Osciloscopio con FFT.

1. **Propuesta Comercial ($C = 2200\mu F$):**
Retiramos el inductor y colocamos el capacitor en paralelo con los $10\Omega$.
*Nota crítica:* El manual pide calcular un filtro para rizo $\le 5\%$. Evaluemos teóricamente tu propuesta de **$2200\mu F$**:

$$V_{r(pp)} \approx \frac{V_m}{f_{rizo} \cdot R \cdot C} = \frac{15.57}{120 \cdot 10 \cdot 2200 \times 10^{-6}} = \frac{15.57}{2.64} \approx 5.89V$$


$$V_o(cd) = V_m - \frac{V_{r(pp)}}{2} = 15.57 - \frac{5.89}{2} \approx 12.63V$$



Porcentaje de Rizo estimado:

$$\%Rizo = \frac{V_{r(rms)}}{V_o(cd)} = \frac{V_{r(pp)} / (2\sqrt{3})}{V_o(cd)} = \frac{5.89 / 3.464}{12.63} = \frac{1.70}{12.63} \approx 13.4\%$$



*Justificación para tu reporte:* Aunque el valor comercial de $2200\mu F$ reduce inmensamente el rizo en comparación al circuito sin filtro (del ~48% original baja a ~13%), **no es suficiente para llegar al $\le 5\%$ exigido**.
*Para cumplir estrictamente el $\le 5\%$, el cálculo teórico exige:*

$$C_{ideal} \ge \frac{V_m}{f_{rizo} \cdot R \cdot (V_o(cd) \cdot 2\sqrt{3} \cdot 0.05)} \approx 6000\mu F \quad \text{(Usarías un valor comercial de } 6800\mu F \text{ o poner tres de } 2200\mu F \text{ en paralelo)}.$$


2. **Espectro Final (Inciso m):**
Al aplicar la FFT en el osciloscopio, observarás que el componente de 0Hz (DC) se vuelve gigante, mientras que los picos en 120Hz, 240Hz, etc., disminuyen drásticamente su amplitud en comparación al inciso *f*.

¿Te gustaría que generemos el script de Python para automatizar estos cálculos con los valores reales una vez que midas el inductor con el puente LCR en el laboratorio?