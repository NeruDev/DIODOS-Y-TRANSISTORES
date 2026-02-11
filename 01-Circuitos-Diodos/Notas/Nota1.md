# Recta de Carga para el Diodo

La **recta de carga** es una herramienta gráfica fundamental en el análisis de circuitos con diodos. Representa la relación entre la tensión y la corriente impuesta por el circuito externo al diodo. La intersección de esta recta con la curva característica del diodo nos da el **punto de operación** (también conocido como punto Q o "Quiescent point") del circuito.

## Obtención de la Ecuación de la Recta de Carga

Consideremos un circuito simple compuesto por una fuente de tensión continua $V_{in}$, una resistencia $R$ y un diodo, todos conectados en una **malla cerrada serie** (la corriente $I_D$ circula por todos los elementos):

![Circuito DC con diodo](./../media/generated/circuito_dc_diodo.png)

Aplicando la **Ley de Tensiones de Kirchhoff (LVK)** a la malla cerrada — es decir, sumando todas las caídas de tensión alrededor del lazo y igualándolas a cero — obtenemos:

$$V_{in} - I_D R - V_D = 0$$

Donde:
- $V_{in}$ es la tensión de la fuente (conocida).
- $I_D$ es la corriente que circula por el diodo (incógnita).
- $V_D$ es la tensión en los terminales del diodo (incógnita).
- $R$ es la resistencia en serie (conocida).

> **Nota:** Tenemos **una ecuación con dos incógnitas** ($I_D$ y $V_D$). Por eso necesitamos una segunda ecuación — la curva característica del diodo — para resolver el circuito.

### Paso 1: Despejar la corriente $I_D$

Partimos de la LVK:

$$V_{in} - I_D R - V_D = 0$$

Pasamos el término $V_D$ al lado derecho:

$$V_{in} - I_D R = V_D$$

Ahora aislamos el término que contiene $I_D$. Restamos $V_D$ de ambos lados y sumamos $I_D R$:

$$V_{in} - V_D = I_D R$$

Dividimos ambos lados entre $R$:

$$I_D = \frac{V_{in} - V_D}{R}$$

### Paso 2: Reescribir como ecuación de recta $y = mx + b$

Separamos la fracción para identificar la forma de una recta:

$$I_D = \frac{V_{in}}{R} - \frac{V_D}{R}$$

Reordenando para hacer explícita la forma $y = mx + b$ (donde $x = V_D$ e $y = I_D$):

$$\boxed{I_D = -\frac{1}{R} \cdot V_D + \frac{V_{in}}{R}}$$

Identificamos:
- **Variable independiente ($x$):** $V_D$
- **Variable dependiente ($y$):** $I_D$
- **Pendiente ($m$):** $-1/R$ (negativa, por eso la recta "baja")
- **Ordenada al origen ($b$):** $V_{in}/R$

### Paso 3: Encontrar los puntos extremos de la recta

Para graficar la recta solo necesitamos dos puntos. Los más convenientes son las intersecciones con los ejes:

**Intersección con el eje Y** (cuando $V_D = 0$, el diodo es un cortocircuito):

$$I_D = -\frac{1}{R}(0) + \frac{V_{in}}{R} = \frac{V_{in}}{R}$$

$$\Rightarrow \text{Punto 1: } \left(0, \;\frac{V_{in}}{R}\right)$$

Este es el caso extremo donde **toda la tensión cae en R** y nada en el diodo. Representa la corriente máxima posible.

**Intersección con el eje X** (cuando $I_D = 0$, el diodo es un circuito abierto):

$$0 = -\frac{1}{R} \cdot V_D + \frac{V_{in}}{R}$$

Multiplicamos por $R$:

$$0 = -V_D + V_{in}$$

$$V_D = V_{in}$$

$$\Rightarrow \text{Punto 2: } \left(V_{in}, \; 0\right)$$

Este es el caso extremo donde **toda la tensión cae en el diodo** y no circula corriente.

## Representación Gráfica y Punto de Operación

Para encontrar el punto de operación del diodo en el circuito, se grafica la recta de carga sobre la curva característica del diodo (la relación I-V intrínseca del componente).

![Recta de carga y punto Q](./../media/generated/recta_de_carga_punto_q.png)

El punto donde ambas curvas se intersectan es el **punto de operación (Q)**. Las coordenadas de este punto $(V_{DQ}, I_{DQ})$ representan la tensión y la corriente reales que tendrá el diodo cuando está operando en ese circuito específico.

En la gráfica anterior (con $V_{in} = 5$ V y $R = 1\;k\Omega$):
- La **curva azul** es la relación I-V intrínseca del diodo (ecuación de Shockley).
- La **recta roja** es la restricción impuesta por el circuito externo (su pendiente es $-1/R$).
- El **punto Q** marca la única combinación $(V_{DQ}, I_{DQ})$ que satisface ambas ecuaciones simultáneamente.

Los dos puntos extremos de la recta son:
- $(0,\; V_{in}/R)$: caso en que el diodo es un cortocircuito (toda la tensión cae en $R$).
- $(V_{in},\; 0)$: caso en que el diodo es un circuito abierto (toda la tensión cae en el diodo).

> **¿Por qué el método gráfico?** Resolver analíticamente requiere resolver simultáneamente la ecuación lineal de la recta de carga y la ecuación exponencial de Shockley ($I_D = I_S(e^{V_D/nV_T} - 1)$). Este sistema no tiene solución algebraica cerrada, por lo que se usa el método gráfico o métodos numéricos iterativos.

---

## Análisis de Pequeña Señal

Una vez establecido el punto de operación Q mediante la polarización DC, se puede estudiar el efecto de una **pequeña señal AC** superpuesta. El objetivo es encontrar cómo responde el diodo a perturbaciones alrededor de Q sin tener que resolver la ecuación exponencial cada vez.

### Circuito con señal AC superpuesta

Cuando un diodo opera en el punto Q (establecido por la polarización DC), es posible aplicar una **pequeña señal de AC** que se superpone a la tensión de DC. El circuito completo se ve así:

![Circuito con señal AC superpuesta](./../media/generated/circuito_ac_superpuesto.png)

La tensión total en el diodo es la superposición de la componente DC y la componente AC:

$$v_D(t) = V_{DQ} + v_d(t)$$

donde $V_{DQ}$ es el voltaje DC en el punto de operación y $v_d(t)$ es la pequeña perturbación AC.

Para analizar el comportamiento del circuito ante esta pequeña señal, se puede **linealizar** el comportamiento del diodo alrededor del punto de operación. Gráficamente, esto equivale a sustituir la curva exponencial por su recta tangente en Q.

### Formas de Onda en el Dominio del Tiempo

Antes de entrar en la derivación formal, conviene visualizar qué ocurre con la corriente y el voltaje **en función del tiempo** cuando se superpone la señal AC.

Partimos de que la tensión de entrada total es:

$$v_{entrada}(t) = V_{DC} + v_s(t) = V_{DC} + V_m \sin(2\pi f \cdot t)$$

donde $V_m$ es la amplitud (pico) de la señal AC y $f$ su frecuencia.

#### Expresiones de $i_D(t)$ y $v_D(t)$

Usando el modelo de pequeña señal (que derivaremos en la siguiente sección), el circuito se reduce a un divisor resistivo entre $R$ y $r_d$. Esto permite escribir las señales totales como:

**Corriente total a través del diodo:**

$$i_D(t) = I_{DQ} + i_d(t) = I_{DQ} + \frac{v_s(t)}{R + r_d}$$

$$\boxed{i_D(t) = I_{DQ} + \frac{V_m}{R + r_d} \sin(2\pi f \cdot t)}$$

La corriente oscila alrededor del valor DC $I_{DQ}$ con una amplitud pico:

$$\hat{i}_d = \frac{V_m}{R + r_d}$$

**Voltaje total en el diodo:**

$$v_D(t) = V_{DQ} + v_d(t) = V_{DQ} + v_s(t) \cdot \frac{r_d}{R + r_d}$$

$$\boxed{v_D(t) = V_{DQ} + \frac{V_m \cdot r_d}{R + r_d} \sin(2\pi f \cdot t)}$$

La tensión en el diodo oscila alrededor de $V_{DQ}$ con amplitud pico:

$$\hat{v}_d = V_m \cdot \frac{r_d}{R + r_d}$$

#### Observaciones clave de las formas de onda

La siguiente gráfica muestra las tres señales en el dominio del tiempo para un ejemplo con $V_{in} = 5$ V, $R = 1\;k\Omega$, $V_m = 100$ mV y $f = 1$ kHz:

![Formas de onda temporales](./../media/generated/formas_de_onda_temporal.png)

Del gráfico se observa:

1. **La señal de entrada $v_s(t)$** (panel superior) es una senoidal pura de 100 mV de amplitud.

2. **La corriente $i_D(t)$** (panel central) oscila alrededor del valor DC $I_{DQ}$. La amplitud de la componente AC es extremadamente pequeña comparada con $I_{DQ}$ porque:

$$\hat{i}_d = \frac{V_m}{R + r_d} \approx \frac{V_m}{R} = \frac{0.1}{1000} = 0.1 \;\text{mA}$$

3. **El voltaje $v_D(t)$** (panel inferior) oscila alrededor de $V_{DQ}$ con una amplitud **mucho menor** que la señal de entrada, debido a que $r_d \ll R$:

$$\hat{v}_d = V_m \cdot \frac{r_d}{R + r_d} \approx V_m \cdot \frac{r_d}{R} \ll V_m$$

Esto confirma numéricamente que casi toda la señal AC cae en la resistencia $R$ y muy poco llega al diodo — exactamente lo que se predice del divisor de voltaje del modelo de pequeña señal.

> **Nota importante:** La forma senoidal de $i_D(t)$ y $v_D(t)$ es una consecuencia directa de la linealización. En realidad, la corriente del diodo crece exponencialmente, por lo que el semiciclo positivo sería ligeramente mayor que el negativo. Sin embargo, para señales pequeñas ($v_d \ll nV_T$), esta asimetría es despreciable y la aproximación lineal es excelente.

### Resistencia Dinámica — Derivación paso a paso

El modelo de pequeña señal del diodo se basa en sustituir el componente no lineal por una resistencia lineal equivalente, conocida como **resistencia dinámica** $r_d$.

**Paso 1: Definición de resistencia dinámica**

La resistencia dinámica es la inversa de la pendiente de la curva I-V en el punto de operación Q:

$$r_d = \frac{dV_D}{dI_D} \bigg|_{Q} = \left(\frac{dI_D}{dV_D}\bigg|_{Q}\right)^{-1}$$

Para calcularla, primero necesitamos derivar la ecuación del diodo.

**Paso 2: Ecuación de Shockley**

La corriente del diodo viene dada por:

$$I_D = I_S\left(e^{V_D / nV_T} - 1\right)$$

**Paso 3: Derivada de la corriente respecto al voltaje**

Derivamos aplicando la regla de la cadena. Sea $u = \frac{V_D}{nV_T}$, entonces $\frac{du}{dV_D} = \frac{1}{nV_T}$:

$$\frac{dI_D}{dV_D} = I_S \cdot \frac{d}{dV_D}\left(e^{u} - 1\right) = I_S \cdot e^{u} \cdot \frac{du}{dV_D}$$

Sustituyendo $u$ y su derivada:

$$\frac{dI_D}{dV_D} = I_S \cdot e^{V_D / nV_T} \cdot \frac{1}{nV_T}$$

$$\boxed{\frac{dI_D}{dV_D} = \frac{I_S}{nV_T} \cdot e^{V_D / nV_T}}$$

**Paso 4: Simplificación usando la ecuación de Shockley**

De la ecuación original: $I_D = I_S(e^{V_D/nV_T} - 1)$, despejamos el término exponencial:

$$I_S \cdot e^{V_D/nV_T} = I_D + I_S$$

En polarización directa, la corriente del diodo es mucho mayor que la corriente de saturación ($I_D \gg I_S$), por lo tanto:

$$I_S \cdot e^{V_D/nV_T} \approx I_D$$

Sustituyendo en la derivada:

$$\frac{dI_D}{dV_D} \approx \frac{I_D}{nV_T}$$

**Paso 5: Inversión para obtener $r_d$**

Evaluando en el punto Q ($I_D = I_{DQ}$) e invirtiendo:

$$r_d = \left(\frac{dI_D}{dV_D}\bigg|_Q\right)^{-1} = \left(\frac{I_{DQ}}{nV_T}\right)^{-1}$$

$$\boxed{r_d \approx \frac{nV_T}{I_{DQ}}}$$

**Paso 6: Interpretación de los parámetros**

| Parámetro | Significado | Valor típico |
|-----------|-------------|--------------|
| $I_{DQ}$ | Corriente de polarización DC en el punto Q | Depende del circuito |
| $V_T$ | Tensión térmica: $V_T = kT/q$ | ≈ 26 mV a 25°C |
| $n$ | Factor de idealidad del diodo | 1 (Si) a 2 (GaAs) |

> **Observación clave:** A mayor corriente de polarización $I_{DQ}$, menor es la resistencia dinámica $r_d$. Esto significa que el diodo se comporta más como un "cable" cuanto más corriente circula por él.

### Ejemplo numérico

Si $I_{DQ} = 5$ mA, $n = 1$ y $V_T = 26$ mV:

$$r_d = \frac{(1)(0.026)}{0.005} = \frac{0.026}{0.005} = 5.2\;\Omega$$

### Modelo Equivalente de Pequeña Señal

Para el análisis en AC, se aplica el **principio de superposición**:

1. **Las fuentes DC se "apagan"** → una fuente de voltaje DC se reemplaza por un cortocircuito (cable).
2. **El diodo se reemplaza** por su resistencia dinámica $r_d$.
3. **Los capacitores de acoplo** (si existen) se consideran cortocircuitos a la frecuencia de la señal.

El circuito resultante es puramente lineal, lo que permite analizarlo con las técnicas estándar de circuitos (divisor de voltaje, Thévenin, etc.):

![Modelo equivalente de pequeña señal](./../media/generated/modelo_pequena_senal.png)

En este circuito equivalente, la tensión de pequeña señal en el diodo se obtiene por **divisor de voltaje**:

$$v_d = v_s \cdot \frac{r_d}{R + r_d}$$

Dado que normalmente $r_d \ll R$ (por ejemplo, $r_d = 5.2\;\Omega$ vs $R = 1\;k\Omega$):

$$v_d \approx v_s \cdot \frac{r_d}{R} \ll v_s$$

Esto confirma que la señal en el diodo es efectivamente "pequeña" respecto a la señal de entrada.

### Gráfica de Linealización

El siguiente gráfico ilustra visualmente cómo el modelo de pequeña señal (la recta tangente roja) aproxima el comportamiento de la curva exponencial del diodo en las cercanías del punto de operación Q:

![Linealización alrededor del punto Q](./../media/generated/diodo_pequena_senal.png)

La zona sombreada en verde indica la región donde el modelo lineal es una buena aproximación. Fuera de esa zona, la curva exponencial se desvía significativamente de la recta tangente y el modelo pierde validez.

> **Condición de validez:** El modelo de pequeña señal es válido siempre que la amplitud de la señal AC cumpla $v_d \ll nV_T$ (típicamente $v_d < 5$ mV para $n=1$). Bajo esta condición, la operación del diodo se mantiene en la región lineal aproximada por la tangente.

---

## Ejemplo Resuelto: Análisis DC + AC de un Circuito con Diodo

### Enunciado

Considere el siguiente circuito de un solo lazo con un diodo de silicio ($V_K = 0.7$ V) que tiene una resistencia interna $r_d = 0.1\;\Omega$. La fuente DC es $E = 6$ V, la fuente AC es $e(t) = 2\sin(\omega t)$ V y la resistencia es $R = 270\;\Omega$.

Encontrar:
1. La corriente total $i_D(t)$ a través del circuito.
2. El voltaje total $v_D(t)$ a través del diodo.
3. Dibujar las señales resultantes.

![Circuito del ejemplo](./../media/generated/ejemplo_circuito_ps.png)

### Solución

Usamos el **modelo lineal por tramos** del diodo: se reemplaza el diodo por su tensión de rodilla $V_K$ en serie con su resistencia interna $r_d$.

#### Paso 1: Análisis DC — Encontrar el punto de operación Q

Apagamos la fuente AC ($e(t) = 0$) y analizamos solo el circuito DC.

Aplicando LVK a la malla:

$$E - I_{DQ} \cdot R - V_K - I_{DQ} \cdot r_d = 0$$

Factorizamos $I_{DQ}$:

$$E - V_K = I_{DQ}(R + r_d)$$

Despejamos:

$$I_{DQ} = \frac{E - V_K}{R + r_d} = \frac{6 - 0.7}{270 + 0.1} = \frac{5.3}{270.1}$$

$$\boxed{I_{DQ} = 19.62 \;\text{mA}}$$

El voltaje DC en el diodo es:

$$V_{DQ} = V_K + I_{DQ} \cdot r_d = 0.7 + (0.01962)(0.1) = 0.7 + 0.00196$$

$$\boxed{V_{DQ} = 701.96 \;\text{mV} \approx 0.702 \;\text{V}}$$

> **Verificación por LVK:** $E = I_{DQ} \cdot R + V_{DQ} = (0.01962)(270) + 0.702 = 5.298 + 0.702 = 6.0$ V ✓

#### Paso 2: Análisis AC — Componentes de pequeña señal

Apagamos la fuente DC ($E = 0 \Rightarrow$ cortocircuito) y el diodo se reemplaza por $r_d$. El circuito AC equivalente es un divisor de voltaje entre $R$ y $r_d$.

**Corriente AC (componente de pequeña señal):**

$$i_d(t) = \frac{e(t)}{R + r_d} = \frac{2\sin(\omega t)}{270 + 0.1} = \frac{2\sin(\omega t)}{270.1}$$

La amplitud pico de la corriente AC es:

$$\hat{i}_d = \frac{V_m}{R + r_d} = \frac{2}{270.1}$$

$$\boxed{\hat{i}_d = 7.40 \;\text{mA}}$$

**Voltaje AC en el diodo (componente de pequeña señal):**

$$v_d(t) = e(t) \cdot \frac{r_d}{R + r_d} = 2\sin(\omega t) \cdot \frac{0.1}{270.1}$$

La amplitud pico del voltaje AC en el diodo es:

$$\hat{v}_d = V_m \cdot \frac{r_d}{R + r_d} = 2 \cdot \frac{0.1}{270.1}$$

$$\boxed{\hat{v}_d = 0.740 \;\text{mV}}$$

> **Nota:** La amplitud del voltaje AC en el diodo ($\hat{v}_d = 0.74$ mV) es mucho menor que $nV_T \approx 26$ mV, por lo que el modelo de pequeña señal es perfectamente válido.

#### Paso 3: Señales totales (DC + AC)

Aplicando el **principio de superposición**, las señales completas son:

**Corriente total:**

$$i_D(t) = I_{DQ} + i_d(t) = 19.62 + 7.40\sin(\omega t) \;\;\text{[mA]}$$

$$\boxed{i_D(t) = 19.62 + 7.40\sin(\omega t) \;\;\text{mA}}$$

| Valor | Expresión | Resultado |
|-------|-----------|-----------|
| $i_{D,\text{max}}$ | $I_{DQ} + \hat{i}_d$ | $19.62 + 7.40 = 27.02$ mA |
| $i_{D,\text{min}}$ | $I_{DQ} - \hat{i}_d$ | $19.62 - 7.40 = 12.22$ mA |

**Voltaje total en el diodo:**

$$v_D(t) = V_{DQ} + v_d(t) = 701.96 + 0.740\sin(\omega t) \;\;\text{[mV]}$$

$$\boxed{v_D(t) = 701.96 + 0.740\sin(\omega t) \;\;\text{mV}}$$

| Valor | Expresión | Resultado |
|-------|-----------|-----------|
| $v_{D,\text{max}}$ | $V_{DQ} + \hat{v}_d$ | $701.96 + 0.74 = 702.70$ mV |
| $v_{D,\text{min}}$ | $V_{DQ} - \hat{v}_d$ | $701.96 - 0.74 = 701.22$ mV |

**Voltaje en la resistencia:**

$$v_R(t) = i_D(t) \cdot R = (I_{DQ} + i_d(t)) \cdot R$$

$$v_R(t) = I_{DQ} \cdot R + \frac{V_m \cdot R}{R + r_d}\sin(\omega t)$$

$$\boxed{v_R(t) = 5.298 + 1.999\sin(\omega t) \;\;\text{V}}$$

> **Observación:** Casi toda la señal AC cae en la resistencia ($\hat{v}_R \approx 2.0$ V $\approx V_m$), mientras que solo una fracción $r_d/(R+r_d) \approx 0.037\%$ llega al diodo. Esto ocurre porque $r_d \ll R$.

#### Paso 4: Formas de onda

Las siguientes gráficas muestran el comportamiento temporal de las tres señales. La componente DC se indica con la línea punteada y la zona sombreada representa la variación AC:

![Formas de onda del ejemplo](./../media/generated/ejemplo_formas_onda_ps.png)

Se observa que:
- La **corriente** oscila simétricamente alrededor de $I_{DQ}$ con amplitud considerable ($\hat{i}_d / I_{DQ} \approx 37.7\%$).
- El **voltaje en el diodo** prácticamente no cambia — la oscilación es de apenas $\pm 0.74$ mV sobre un nivel DC de $\approx 702$ mV.
- El **voltaje en $R$** absorbe casi toda la variación de la señal de entrada.

Esto confirma experimentalmente el resultado teórico: en un circuito serie con $r_d \ll R$, el diodo funciona como un elemento que fija un voltaje casi constante ($\approx V_K$), y toda la variación de la señal cae sobre la resistencia externa.