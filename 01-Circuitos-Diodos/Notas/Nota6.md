<!--
::METADATA::
type: theory
topic_id: rectificador-puente-completo
file_id: Nota6
status: draft
audience: student
last_updated: 2026-02-27
-->

> 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md) | [🔙 Notas DIO](README.md)

---

# Rectificador Monolítico Tipo H o Puente (Full-Bridge Rectifier)

## Introducción

El rectificador tipo puente — también conocido como **puente de Graetz**, **rectificador tipo H** o **full-bridge rectifier** — es la topología de rectificación de onda completa **más utilizada en aplicaciones comerciales e industriales**. Su principal ventaja frente al rectificador de derivación central radica en que emplea un **único devanado secundario** del transformador, es decir, utiliza una fuente de **2 hilos** en lugar de los 3 hilos que requiere el rectificador con toma central (center-tap). Esto simplifica el diseño del transformador, reduce su costo y lo hace más compacto.

El circuito está formado por **cuatro diodos rectificadores** dispuestos en configuración de puente (forma de "H" o rombo), los cuales **trabajan por pares** de manera alternada:

- **Par 1 ($D_1$ y $D_2$):** Conduce durante el semiciclo positivo de la señal de entrada.
- **Par 2 ($D_3$ y $D_4$):** Conduce durante el semiciclo negativo.

Esta operación por pares garantiza que la corriente fluya siempre en la **misma dirección** a través de la carga $R_L$, produciendo una señal rectificada de onda completa sin necesidad de derivación central en el transformador.

---

## Datos del circuito

| Parámetro | Valor |
|-----------|-------|
| Voltaje secundario | $V_s = V_m \sin(\omega t)$ |
| Transformador | Devanado secundario simple (sin derivación central) |
| Diodos | $D_1$, $D_2$, $D_3$, $D_4$ — silicio ($V_D = 0.7\,\text{V}$) / ideal ($V_D = 0$) |
| Resistencia de carga | $R_L$ |

---

## 1. Principio de funcionamiento

Los cuatro diodos se colocan en una disposición de puente tal que, en cada semiciclo, dos de ellos conducen simultáneamente mientras los otros dos permanecen bloqueados. La carga $R_L$ se conecta entre los puntos medios del puente, recibiendo corriente unidireccional en ambos semiciclos.

### Semiciclo positivo ($0 < \omega t < \pi$)

Durante el semiciclo positivo de la señal de entrada:

- El terminal superior del secundario es **positivo** y el inferior es **negativo**.
- **$D_1$ y $D_2$ conducen** (polarizados en directa): la corriente fluye desde el terminal positivo del secundario → $D_1$ → $R_L$ → $D_2$ → terminal negativo del secundario.
- **$D_3$ y $D_4$ están en corte** (polarizados en inversa).
- El voltaje en la carga es:

$$v_o(t) = V_m \sin(\omega t) - 2V_D$$

> **Nota:** Aparece $2V_D$ porque la corriente atraviesa **dos diodos en serie** en cada semiciclo — esta es una diferencia importante respecto al rectificador con derivación central, donde solo se pierde $V_D$ por un diodo.

### Semiciclo negativo ($\pi < \omega t < 2\pi$)

Durante el semiciclo negativo:

- El terminal inferior del secundario se vuelve **positivo** y el superior se vuelve **negativo**.
- **$D_3$ y $D_4$ conducen**: la corriente circula desde el terminal inferior (ahora positivo) → $D_3$ → $R_L$ → $D_4$ → terminal superior (ahora negativo).
- **$D_1$ y $D_2$ están en corte**.
- El voltaje en la carga es nuevamente:

$$v_o(t) = V_m |\sin(\omega t)| - 2V_D$$

> **Resultado clave:** Al igual que en el rectificador con derivación central, la carga recibe pulsos de corriente durante ambos semiciclos, pero aquí **cada pulso pierde dos caídas de diodo** ($2V_D$) en lugar de una.

---

## 2. Circuito esquemático

El circuito del rectificador monolítico tipo puente y la disposición de los cuatro diodos se muestra en la siguiente figura:

![Esquemático del rectificador tipo puente (full-bridge)](../media/generated/nota6_circuito.png)

---

## 2.1 Flujo de corriente por semiciclo

Para comprender el funcionamiento del puente, es útil analizar la ruta de la corriente en cada semiciclo. La siguiente figura emplea la representación en **forma de diamante (rombo)** del puente, que es la disposición canónica para visualizar los caminos de conducción. La fuente $V_s$ se conecta entre los nodos laterales (LEFT y RIGHT) y la carga $R_L$ entre los nodos superior (+$V_o$) e inferior (−$V_o$/GND).

![Flujo de corriente en el rectificador tipo puente](../media/generated/nota6_flujo_corriente.png)

**Diagrama (a) — Semiciclo positivo** ($0 < \omega t < \pi$, en azul):

- El nodo LEFT es positivo (+) y RIGHT es negativo (−).
- **$D_1$ y $D_3$ conducen** (polarizados en directa).
- Ruta de la corriente convencional:

$$\text{LEFT}(+) \;\xrightarrow{D_1}\; \text{TOP}(+V_o) \;\xrightarrow{R_L}\; \text{BOTTOM}(-V_o) \;\xrightarrow{D_3}\; \text{RIGHT}(-)$$

- Los diodos $D_2$ y $D_4$ permanecen **en corte** (polarizados en inversa, mostrados en gris).

**Diagrama (b) — Semiciclo negativo** ($\pi < \omega t < 2\pi$, en rojo):

- La polaridad se invierte: RIGHT es ahora positivo (+) y LEFT es negativo (−).
- **$D_2$ y $D_4$ conducen**.
- Ruta de la corriente convencional:

$$\text{RIGHT}(+) \;\xrightarrow{D_2}\; \text{TOP}(+V_o) \;\xrightarrow{R_L}\; \text{BOTTOM}(-V_o) \;\xrightarrow{D_4}\; \text{LEFT}(-)$$

- Los diodos $D_1$ y $D_3$ permanecen **en corte**.

> **Observación clave:** En ambos semiciclos, la corriente a través de $R_L$ fluye siempre en la **misma dirección** (de TOP a BOTTOM), lo que produce un voltaje de salida $V_o$ siempre positivo — es decir, una señal rectificada de onda completa.

---

## 2.2 Resumen de operación y formas de onda

Para el intervalo $0 \leq \omega t \leq \pi$, los diodos $D_1$ y $D_2$ están polarizados directamente, por lo que la fuente $v_s = V_m \sin(\omega t)$ se transfiere a la carga $R_L$. Para el intervalo $\pi \leq \omega t \leq 2\pi$, los diodos $D_1$ y $D_2$ se polarizan inversamente; por el contrario, los diodos $D_3$ y $D_4$ se polarizan directamente, transfiriendo la fuente a la carga mediante la rectificación del semiciclo negativo. En ambos semiciclos, la corriente atraviesa **dos diodos en serie**, lo que produce una caída total de $2V_D$ respecto al voltaje pico del secundario.

Las formas de onda correspondientes se muestran en la siguiente figura:

![Formas de onda del rectificador tipo puente](../media/generated/nota6_formas_onda.png)

> **Nota:** En la gráfica (b) se aprecia la diferencia entre la salida ideal ($V_m |\sin(\omega t)|$) y la real ($V_m |\sin(\omega t)| - 2V_D$). El sombreado azul indica los intervalos donde $D_1$ y $D_2$ conducen, mientras que el sombreado rojo corresponde a la conducción de $D_3$ y $D_4$. Las gráficas (c) y (d) ilustran los voltajes inversos: $D_3$ bloquea durante el semiciclo positivo y $D_1$ durante el negativo. En ambos casos, el pico inverso (PIV $= V_m - V_D$) es notablemente menor que en el rectificador con derivación central ($2V_m - V_D$), lo cual es una gran ventaja de esta topología.

---

## 2.3 Ejemplo de cálculo

Como se observa, el comportamiento de las señales de voltaje y corriente son iguales a las del rectificador con derivación central, por lo que se pueden utilizar las expresiones analíticas de voltaje y corriente ya obtenidas.

**Ejercicio:**
El rectificador monolítico de onda completa de la figura anterior se alimenta con $120\,\text{V}_{AC}$ @ $60\,\text{Hz}$ en el primario del transformador con una relación de voltajes de 10:1. Si la resistencia de carga es de $5\,\Omega$, determine:

| # | Parámetro solicitado |
|---|----------------------|
| a) | Voltaje pico del secundario ($V_m$) |
| b) | Voltaje pico rectificado en la carga ($V_{o,m}$) |
| c) | Voltaje promedio en la carga ($V_{DC}$) |
| d) | Corriente promedio en la carga ($I_{DC}$) |
| e) | Voltaje eficaz en la carga ($V_{rms}$) |
| f) | Corriente eficaz en la carga ($I_{rms}$) |
| g) | Voltaje inverso de pico en los diodos (PIV) |
| h) | Voltaje de rizo RMS en la carga ($V_{r(rms)}$) |
| i) | Corriente promedio por diodo ($I_{D(avg)}$) |
| j) | Corriente RMS por diodo ($I_{D(rms)}$) |
| k) | Potencia en CD ($P_{dc}$) y potencia en CA ($P_{ac}$) |
| l) | Frecuencia de rizado ($f_r$) |

**Datos:**

| Dato | Valor |
|------|-------|
| $V_{pri(rms)}$ | $120\,\text{V}$ |
| $f$ | $60\,\text{Hz}$ |
| $a$ (relación de transformación) | $10:1$ |
| $R_L$ | $5\,\Omega$ |
| $V_D$ (silicio) | $0.7\,\text{V}$ |

---

### a) Voltaje pico del secundario — $V_m$

El voltaje RMS en el secundario se obtiene de la relación de transformación:

$$V_{sec(rms)} = \frac{V_{pri(rms)}}{a} = \frac{120\,\text{V}}{10} = 12\,\text{V}$$

El voltaje pico es:

$$\boxed{V_m = \sqrt{2} \cdot V_{sec(rms)} = 1.4142 \times 12\,\text{V} \approx 16.97\,\text{V}}$$

> **Comprobación:** Se puede obtener el mismo resultado transformando primero al pico y luego reduciendo: $V_m = \frac{V_{pri,pico}}{a} = \frac{\sqrt{2} \times 120}{10} = \frac{169.71}{10} = 16.97\,\text{V}$ ✓

---

### b) Voltaje pico rectificado en la carga — $V_{o,m}$

En el rectificador puente, la corriente atraviesa **dos diodos en serie** en cada semiciclo, por lo que se restan dos caídas de diodo:

$$\boxed{V_{o,m} = V_m - 2V_D = 16.97\,\text{V} - 2(0.7\,\text{V}) = 15.57\,\text{V}}$$

---

### c) Voltaje promedio (DC) en la carga — $V_{DC}$

Para una onda completa rectificada, el valor promedio es $\frac{2V_p}{\pi}$:

$$\boxed{V_{DC} = \frac{2 \cdot V_{o,m}}{\pi} = \frac{2(15.57\,\text{V})}{\pi} = \frac{31.14\,\text{V}}{3.1416} \approx 9.91\,\text{V}}$$

> **Comprobación:** Usando el factor decimal: $V_{DC} = 0.6366 \times V_{o,m} = 0.6366 \times 15.57 = 9.91\,\text{V}$ ✓

---

### d) Corriente promedio (DC) en la carga — $I_{DC}$

Por Ley de Ohm:

$$\boxed{I_{DC} = \frac{V_{DC}}{R_L} = \frac{9.91\,\text{V}}{5\,\Omega} \approx 1.98\,\text{A}}$$

La corriente pico en la carga es:
$$I_m = \frac{V_{o,m}}{R_L} = \frac{15.57\,\text{V}}{5\,\Omega} = 3.11\,\text{A}$$

> **Comprobación:** Usando la fórmula directa con corriente pico: $I_{DC} = \frac{2 I_m}{\pi} = \frac{2(3.11)}{3.1416} = 1.98\,\text{A}$ ✓

---

### e) Voltaje eficaz (RMS) en la carga — $V_{rms}$

Para una senoidal rectificada de onda completa, el valor eficaz se relaciona con el pico mediante $\sqrt{2}$:

$$\boxed{V_{rms} = \frac{V_{o,m}}{\sqrt{2}} = \frac{15.57\,\text{V}}{1.4142} \approx 11.01\,\text{V}}$$

> **Comprobación:** Usando el factor decimal: $V_{rms} = 0.7071 \times V_{o,m} = 0.7071 \times 15.57 = 11.01\,\text{V}$ ✓

---

### f) Corriente eficaz (RMS) en la carga — $I_{rms}$

$$\boxed{I_{rms} = \frac{V_{rms}}{R_L} = \frac{11.01\,\text{V}}{5\,\Omega} \approx 2.20\,\text{A}}$$

> **Comprobación:** Con corriente pico: $I_{rms} = \frac{I_m}{\sqrt{2}} = \frac{3.11}{1.4142} = 2.20\,\text{A}$ ✓

> **Nota:** $I_{rms} > I_{DC}$ debido al factor de forma de la onda rectificada. Podemos verificar: $FF = \frac{I_{rms}}{I_{DC}} = \frac{2.20}{1.98} = 1.11$, que coincide con el valor teórico $FF = \frac{\pi}{2\sqrt{2}} = 1.1107$ ✓

---

### g) Voltaje Inverso de Pico — PIV

Cuando un par de diodos conduce, los bloqueados soportan la tensión pico del secundario menos la caída del diodo que comparte nodo:

$$\boxed{\text{PIV} = V_m - V_D = 16.97\,\text{V} - 0.7\,\text{V} = 16.27\,\text{V}}$$

> **Comprobación por KVL:** Cuando $D_1$ y $D_2$ conducen y el voltaje del secundario está en su pico ($V_m$), la malla que incluye a $D_3$ da: $V_{D_3} = -(V_m - V_{D_2}) = -(16.97 - 0.7) = -16.27\,\text{V}$. El signo negativo confirma polarización inversa y $|V_{D_3}| = 16.27\,\text{V}$ ✓

> Comparación: en derivación central sería $\text{PIV} = 2V_m - V_D = 33.24\,\text{V}$ — más del doble.

---

### h) Voltaje de rizo RMS — $V_{r(rms)}$

El voltaje de rizo es la componente de corriente alterna presente en la señal rectificada (sin filtro).

$$V_{r(rms)} = \sqrt{V_{rms}^2 - V_{DC}^2}$$
$$\boxed{V_{r(rms)} = \sqrt{(11.01\,\text{V})^2 - (9.91\,\text{V})^2} \approx 4.80\,\text{V}}$$

El factor de rizo es $r = \frac{V_{r(rms)}}{V_{DC}} = \frac{4.80}{9.91} \approx 48.4\%$.

> **Comprobación:** El factor de rizo teórico para onda completa sin filtro es $r = \sqrt{\left(\frac{\pi}{2\sqrt{2}}\right)^2 - 1} = \sqrt{1.2337 - 1} = \sqrt{0.2337} = 0.4834 = 48.3\%$ ✓

---

### i) Corriente promedio por diodo — $I_{D(avg)}$

En el puente rectificador, cada par de diodos conduce la corriente de carga durante solo un semiciclo. Por lo tanto, la corriente promedio que soporta cada diodo individual es la mitad de la corriente promedio total en la carga ($I_{DC}$).

$$\boxed{I_{D(avg)} = \frac{I_{DC}}{2} = \frac{1.98\,\text{A}}{2} = 0.99\,\text{A}}$$

> **Comprobación:** La integral directa de media onda da $I_{D(avg)} = \frac{I_m}{\pi} = \frac{3.11}{3.1416} = 0.99\,\text{A}$ ✓

---

### j) Corriente RMS por diodo — $I_{D(rms)}$

Cada diodo conduce corriente con forma de medio seno (como en media onda). La corriente RMS para un diodo es:

$$\boxed{I_{D(rms)} = \frac{I_m}{2} = \frac{3.11\,\text{A}}{2} \approx 1.56\,\text{A}}$$
> **Comprobación:** También se obtiene como $I_{D(rms)} = \frac{I_{rms(carga)}}{\sqrt{2}} = \frac{2.20}{1.414} = 1.56\,\text{A}$ ✓

---

### k) Potencia Promedio entregada a la carga (CD) — $P_{dc}$

Esta es la potencia útil de corriente continua que entrega el rectificador.

$$\boxed{P_{dc} = V_{DC} \cdot I_{DC} = (9.91\,\text{V})(1.98\,\text{A}) \approx 19.6\,\text{W}}$$

> **Comprobación por otras formas de Ley de Watt:**
> - $P_{dc} = I_{DC}^2 \cdot R_L = (1.98)^2 \times 5 = 19.6\,\text{W}$ ✓
> - $P_{dc} = \frac{V_{DC}^2}{R_L} = \frac{(9.91)^2}{5} = \frac{98.2}{5} = 19.6\,\text{W}$ ✓

---

### l) Potencia Eficaz disipada en la carga (CA) — $P_{ac}$

Esta es la potencia real total disipada por la resistencia de carga (calentamiento), debida tanto a la componente DC como al rizado AC.

$$\boxed{P_{ac} = I_{rms}^2 \cdot R_L = (2.20\,\text{A})^2 \cdot 5\,\Omega \approx 24.2\,\text{W}}$$

> **Comprobación por otras formas de Ley de Watt:**
> - $P_{ac} = V_{rms} \cdot I_{rms} = (11.01)(2.20) = 24.2\,\text{W}$ ✓
> - $P_{ac} = \frac{V_{rms}^2}{R_L} = \frac{(11.01)^2}{5} = \frac{121.2}{5} = 24.2\,\text{W}$ ✓

> **Eficiencia de conversión:** $\eta = \frac{P_{dc}}{P_{ac}} \times 100\% = \frac{19.6}{24.2} \approx 81\%$.
>
 **Comprobación:** El valor teórico de eficiencia para onda completa es $\eta = \frac{8}{\pi^2} = 81.06\%$ ✓

---

### m) Frecuencia de rizado — $f_r$

En un rectificador de onda completa, cada semiciclo de la entrada produce un pulso en la salida. Por tanto, la frecuencia de la señal rectificada es el doble de la frecuencia de entrada:

$$\boxed{f_r = 2f = 2 \times 60\,\text{Hz} = 120\,\text{Hz}}$$

El periodo de rizado es:
$$T_r = \frac{1}{f_r} = \frac{1}{120\,\text{Hz}} \approx 8.33\,\text{ms}$$

> **Comprobación:** El periodo de entrada es $T = \frac{1}{f} = \frac{1}{60} = 16.67\,\text{ms}$. Si hay dos pulsos por periodo, entonces $T_r = \frac{T}{2} = \frac{16.67}{2} = 8.33\,\text{ms}$, y $f_r = \frac{1}{T_r} = 120\,\text{Hz}$ ✓

---

### Tabla resumen de resultados

| Parámetro | Símbolo | Valor |
|-----------|:-------:|------:|
| Voltaje pico secundario | $V_m$ | $16.97\,\text{V}$ |
| Voltaje pico en carga | $V_{o,m}$ | $15.57\,\text{V}$ |
| Corriente pico | $I_m$ | $3.11\,\text{A}$ |
| Voltaje promedio (DC) | $V_{DC}$ | $9.91\,\text{V}$ |
| Corriente promedio (DC) | $I_{DC}$ | $1.98\,\text{A}$ |
| Potencia promedio (CD) | $P_{dc}$ | $19.6\,\text{W}$ |
| Voltaje eficaz en carga (RMS) | $V_{rms}$ | $11.01\,\text{V}$ |
| Corriente eficaz en carga (RMS) | $I_{rms}$ | $2.20\,\text{A}$ |
| Potencia eficaz (CA) | $P_{ac}$ | $24.2\,\text{W}$ |
| Eficiencia de rectificación | $\eta$ | $81\%$ |
| Voltaje de rizo RMS | $V_{r(rms)}$ | $4.80\,\text{V}$ |
| Factor de rizo | $r$ | $48.4\%$ |
| Corriente promedio por diodo | $I_{D(avg)}$ | $0.99\,\text{A}$ |
| Corriente RMS por diodo | $I_{D(rms)}$ | $1.56\,\text{A}$ |
| Tensión inversa de pico | PIV | $16.27\,\text{V}$ |
| Frecuencia de rizado | $f_r$ | $120\,\text{Hz}$ |
| Periodo de rizado | $T_r$ | $8.33\,\text{ms}$ |

---

## 3. Ventajas y desventajas respecto al rectificador con derivación central

| Característica | Derivación Central | Puente (Tipo H) |
|---|:---:|:---:|
| **Número de diodos** | 2 | 4 |
| **Devanado del transformador** | Con toma central (3 hilos) | Simple (2 hilos) |
| **Caída de diodo por semiciclo** | $V_D$ (1 diodo) | $2V_D$ (2 diodos en serie) |
| **PIV por diodo** | $2V_m - V_D$ | $V_m - V_D$ |
| **Costo del transformador** | Mayor (toma central) | Menor (devanado simple) |
| **Uso comercial** | Limitado | **Dominante** |

### Ventajas del puente

1. **Transformador simple:** No requiere derivación central, lo que reduce significativamente el costo y tamaño del transformador — especialmente importante en aplicaciones de potencia.
2. **Menor PIV por diodo:** Cada diodo solo soporta $V_m$ de tensión inversa (frente a $2V_m$ en derivación central), permitiendo usar diodos de menor voltaje de ruptura.
3. **Disponibilidad comercial:** Se fabrican módulos integrados de puente rectificador en un solo encapsulado (por ejemplo, la serie KBP, KBPC, W04M), lo que simplifica el montaje.

### Desventajas del puente

1. **Doble caída de diodo:** Al circular la corriente por dos diodos en serie, la pérdida total es $2V_D \approx 1.4\,\text{V}$ (silicio), lo cual puede ser significativo en aplicaciones de bajo voltaje.
2. **Mayor número de componentes:** Requiere 4 diodos en lugar de 2 (aunque los puentes integrados mitigan esto).

---

## 4. Ecuaciones fundamentales

Las ecuaciones del rectificador puente son esencialmente las mismas que las del rectificador de onda completa con derivación central, con la salvedad de que se **restan dos caídas de diodo** ($2V_D$) en lugar de una.

### Diodo ideal ($V_D = 0$)

| Parámetro | Expresión | Descripción |
|-----------|-----------|-------------|
| Voltaje pico de salida | $V_{o,m} = V_m$ | Igual al pico del secundario |
| Voltaje promedio (DC) | $V_{DC} = \dfrac{2V_m}{\pi} \approx 0.636\, V_m$ | Igual que derivación central |
| Voltaje rms de salida | $V_{rms} = \dfrac{V_m}{\sqrt{2}} \approx 0.707\, V_m$ | Igual que una senoide completa |
| PIV por diodo | $\text{PIV} = V_m$ | **Mitad** del PIV en derivación central |
| Frecuencia de rizado | $f_r = 2f$ | Doble de la frecuencia de entrada |
| Corriente promedio diodo | $I_{D(avg)} = \frac{I_{DC}}{2}$ | Cada par conduce medio ciclo |
| Corriente rms diodo | $I_{D(rms)} = \frac{I_m}{2}$ | RMS de media onda |
| Eficiencia máxima | $\eta_{max} = \dfrac{8}{\pi^2} \approx 81.2\%$ | Idéntica a onda completa |

### Diodo real ($V_D = 0.7\,\text{V}$)

| Parámetro | Expresión |
|-----------|-----------|
| Voltaje pico de salida | $V_{o,m} = V_m - 2V_D$ |
| Voltaje promedio (DC) | $V_{DC} = \dfrac{2(V_m - 2V_D)}{\pi}$ |
| Corriente promedio | $I_{DC} = \dfrac{V_{DC}}{R_L}$ |

> **Observación:** La única diferencia algebraica con el rectificador de derivación central es el factor $2V_D$ en lugar de $V_D$, y el PIV reducido a $V_m$.

---

## 5. PIV — Tensión Inversa de Pico

El cálculo del PIV en el rectificador puente merece atención especial, ya que es una de sus ventajas más importantes.

Cuando $D_1$ y $D_2$ conducen (semiciclo positivo), los diodos $D_3$ y $D_4$ están en corte. Para $D_3$ (por ejemplo), la tensión inversa es:

$$v_{D_3} = -(V_m \sin(\omega t) - V_D) \approx -V_m \sin(\omega t)$$

El valor máximo de tensión inversa ocurre en el pico:

$$\boxed{\text{PIV} = V_m - V_D \approx V_m}$$

> Esto es exactamente **la mitad** del PIV del rectificador con derivación central ($2V_m$), lo cual es una ventaja significativa en la selección de diodos.

---

## Referencias

- Boylestad & Nashelsky, *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*, 11ª ed., Cap. 2.
- Sedra & Smith, *Microelectronic Circuits*, 7ª ed., Cap. 4.
- Malvino & Bates, *Principios de Electrónica*, 7ª ed., Cap. 4.
