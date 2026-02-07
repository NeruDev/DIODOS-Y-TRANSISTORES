<!--
::METADATA::
type: reference
topic_id: glosario-general
file_id: glossary
status: active
audience: both
last_updated: 2026-02-07
-->

# 📚 Glosario — Diodos y Transistores

> Diccionario centralizado de términos técnicos. Destino de enlaces automáticos.

---

## A

### amplificador

> **Definición formal:** Circuito electrónico que incrementa la amplitud de una señal eléctrica (voltaje, corriente o potencia) sin alterar significativamente su forma. Se caracteriza por su ganancia ($A_v$, $A_i$, $A_p$), impedancia de entrada ($Z_i$), impedancia de salida ($Z_o$) y ancho de banda.
>
> **Analogía:** Como un megáfono que toma tu voz débil y la convierte en una señal más fuerte.
>
> **Contexto:** En el curso se estudian amplificadores en configuración emisor común (BJT), base común (BJT), colector común (BJT), compuerta común (FET) y drenador común (FET), todos analizados mediante modelos de pequeña señal.
>
> **Ver también:** [ganancia](#ganancia), [pequeña señal](#pequeña-señal), [modelo re](#modelo-re), [modelo híbrido](#modelo-híbrido)

### ánodo

> **Definición formal:** Terminal positivo de un diodo. Corresponde al extremo de material semiconductor tipo P. Cuando el ánodo es más positivo que el cátodo en al menos $V_K$, el diodo conduce en polarización directa.
>
> **Símbolo:** La punta del triángulo en el símbolo esquemático del diodo.
>
> **Ver también:** [cátodo](#cátodo), [diodo](#diodo), [polarización directa](#polarización-directa)

### autopolarización

> **Definición formal:** Técnica de polarización para transistores JFET en la que el voltaje $V_{GS}$ se establece automáticamente mediante la caída de voltaje en una resistencia de fuente ($R_S$). No requiere fuente de alimentación adicional en la compuerta ($V_{GG} = 0$). El punto de operación se determina gráficamente por la intersección de la ecuación de transferencia con la recta $V_{GS} = -I_D R_S$.
>
> **Fórmula clave:** $V_{GS} = -I_D R_S$
>
> **Ver también:** [JFET](#jfet), [punto de operación](#punto-de-operación), [polarización fija (FET)](#polarización-fija-fet)

### avalancha

> **Definición formal:** Mecanismo de ruptura en semiconductores (predominante cuando $V_Z > 5\text{V}$) donde los portadores acelerados por un campo eléctrico intenso generan nuevos pares electrón-hueco al colisionar con átomos de la red cristalina, produciendo una multiplicación en cascada de portadores. Presenta coeficiente de temperatura **positivo** (el voltaje de ruptura aumenta con la temperatura).
>
> **Analogía:** Como una bola de nieve rodando colina abajo que se hace cada vez más grande al recoger más nieve.
>
> **Distinción:** Contrario al efecto Zener (predominante en $V_Z < 5\text{V}$), que tiene coeficiente de temperatura negativo.
>
> **Ver también:** [ruptura](#ruptura), [Zener](#zener)

---

## B

### base

> **Definición formal:** Terminal del transistor BJT que controla el flujo de corriente entre colector y emisor. Es la región central extremadamente delgada (< 1 μm) y ligeramente dopada del dispositivo. Una pequeña corriente de base ($I_B$) controla una corriente de colector mucho mayor ($I_C = \beta \cdot I_B$).
>
> **Ver también:** [colector](#colector), [emisor](#emisor), [BJT](#bjt), [beta](#beta)

### beta (β)

> **Definición formal:** Ganancia de corriente en DC del transistor BJT en configuración emisor común, también designada como $h_{FE}$. Representa la relación entre la corriente de colector y la corriente de base:
> $$ \beta = h_{FE} = \frac{I_C}{I_B} $$
> Valores típicos: 50–300 para transistores de propósito general. Varía con la temperatura, el punto de operación y el dispositivo específico.
>
> **Nota:** La beta de AC (pequeña señal) se designa $\beta_{ac}$ o $h_{fe}$ y puede diferir del valor DC.
>
> **Ver también:** [alfa](#alfa), [BJT](#bjt), [parámetros h](#parámetros-h)

### BJT

> **Definición formal:** Transistor de Unión Bipolar (*Bipolar Junction Transistor*). Dispositivo semiconductor de tres terminales (base, colector, emisor) donde la corriente de salida es controlada por la corriente de entrada en la base. Utiliza ambos tipos de portadores (electrones y huecos). Existen dos tipos: NPN (más común) y PNP. Relación fundamental: $I_E = I_C + I_B$.
>
> **Regiones de operación:**
> - **Activa:** $I_C = \beta I_B$ (amplificación)
> - **Saturación:** $V_{CE} \approx V_{CE(sat)}$ (interruptor ON)
> - **Corte:** $I_C \approx 0$ (interruptor OFF)
>
> **Ver también:** [base](#base), [colector](#colector), [emisor](#emisor), [beta](#beta)

---

## C

### canal

> **Definición formal:** Región conductora en un transistor FET entre las terminales de drenador y fuente por donde fluye la corriente. Puede ser tipo N (portadores mayoritarios = electrones) o tipo P (portadores mayoritarios = huecos). El ancho del canal es controlado por el voltaje aplicado en la compuerta.
>
> **Ver también:** [FET](#fet), [compuerta](#compuerta), [JFET](#jfet)

### cátodo

> **Definición formal:** Terminal negativo de un diodo. Corresponde al extremo de material semiconductor tipo N. Se identifica por una banda o marca en el encapsulado del diodo.
>
> **Símbolo:** La barra vertical en el símbolo esquemático del diodo.
>
> **Ver también:** [ánodo](#ánodo), [diodo](#diodo)

### colector

> **Definición formal:** Terminal del transistor BJT que recoge los portadores inyectados desde el emisor a través de la base. Generalmente conectado a la fuente de alimentación a través de la carga. La corriente de colector $I_C = \beta I_B$ en región activa. Región moderadamente dopada con área grande para disipar calor.
>
> **Ver también:** [base](#base), [emisor](#emisor), [beta](#beta)

### compuerta

> **Definición formal:** Terminal de control del transistor FET, análoga a la base del BJT. En un JFET forma una unión PN con el canal; en un MOSFET está aislada del canal por una capa de óxido (SiO₂). La corriente de compuerta es prácticamente cero ($I_G \approx 0$), lo que le confiere una impedancia de entrada extremadamente alta (~10⁹ a 10¹⁴ Ω).
>
> **Ver también:** [FET](#fet), [drenador](#drenador), [fuente (terminal)](#fuente-terminal)

### conmutación

> **Definición formal:** Operación de un transistor como interruptor electrónico, alternando entre los estados de saturación (ON: $V_{CE} \approx V_{CE(sat)}$) y corte (OFF: $I_C \approx 0$). La velocidad de conmutación está limitada por los tiempos de almacenamiento de carga en la base y las capacitancias parásitas del dispositivo.
>
> **Aplicaciones:** Control de relés, motores, LEDs, circuitos digitales.
>
> **Ver también:** [saturación](#saturación), [corte](#corte), [BJT](#bjt)

### corriente de fuga

> **Definición formal:** Corriente inversa de saturación ($I_S$ o $I_0$) que fluye a través de un diodo polarizado inversamente, debida a los portadores minoritarios generados térmicamente. Del orden de nanoamperios (Si) o microamperios (Ge). Se duplica aproximadamente cada 10°C de incremento en temperatura.
>
> **Valores típicos:**
> - Silicio: 1–10 nA
> - Germanio: 1–10 μA
>
> **Analogía:** Como una fuga muy pequeña en una presa: casi nada pasa, pero no es exactamente cero.
>
> **Ver también:** [polarización inversa](#polarización-inversa), [corriente de saturación inversa](#corriente-de-saturación-inversa)

### corriente de saturación inversa

> **Definición formal:** Corriente $I_S$ (también llamada corriente de fuga) que fluye cuando un diodo está polarizado inversamente. Se duplica aproximadamente cada 10°C de incremento en temperatura. Es un parámetro clave en la ecuación de Shockley.
>
> **Valor típico a 25°C:** ~10⁻¹² A (Si), ~10⁻⁶ A (Ge)
>
> **Ver también:** [corriente de fuga](#corriente-de-fuga), [ecuación de Shockley](#ecuación-de-shockley)

### corte

> **Definición formal:** Región de operación de un transistor BJT donde ambas uniones (base-emisor y base-colector) están polarizadas inversamente. La corriente $I_C \approx I_{CEO} \approx 0$ y $V_{CE} \approx V_{CC}$. El transistor actúa como un interruptor abierto.
>
> **Condición:** $V_{BE} < V_{BE(on)} \approx 0.7\text{V (Si)}$ o $I_B = 0$.
>
> **Ver también:** [saturación](#saturación), [conmutación](#conmutación), [región activa](#región-activa)

---

## D

### diodo

> **Definición formal:** Dispositivo semiconductor de dos terminales (ánodo y cátodo) que permite el flujo de corriente eléctrica preferentemente en una dirección (directa) y lo bloquea en la dirección opuesta (inversa). Basado en una unión PN. Su comportamiento se describe mediante la ecuación de Shockley.
>
> **Modelos de análisis:**
> - **Ideal:** Cortocircuito en directa, circuito abierto en inversa.
> - **Aproximado:** Fuente de voltaje $V_K$ en directa (0.7V Si, 0.3V Ge).
> - **Completo:** Incluye $V_K$ + $r_d$ (resistencia dinámica).
>
> **Analogía:** Como una válvula de agua que solo permite el flujo en una dirección.
>
> **Ver también:** [ánodo](#ánodo), [cátodo](#cátodo), [unión PN](#unión-pn), [ecuación de Shockley](#ecuación-de-shockley)

### diodo Gunn

> **Definición formal:** Dispositivo semiconductor que exhibe resistencia diferencial negativa en ciertas regiones de su curva I-V. No tiene unión PN; funciona por el efecto Gunn (transferencia de electrones entre valles de la banda de conducción en GaAs o InP). Se usa como oscilador de microondas (1–100 GHz).
>
> **Ver también:** [diodo](#diodo)

### diodo LASER

> **Definición formal:** Diodo semiconductor que emite luz coherente y monocromática por emisión estimulada de radiación (*Light Amplification by Stimulated Emission of Radiation*). Basado en una unión PN de materiales como GaAs/AlGaAs. Requiere una corriente umbral mínima para iniciar la acción láser.
>
> **Aplicaciones:** Telecomunicaciones por fibra óptica, lectores ópticos, punteros, cirugía.
>
> **Ver también:** [diodo](#diodo)

### diodo PIN

> **Definición formal:** Diodo con una región intrínseca (no dopada) entre las regiones P y N. La región intrínseca aumenta el ancho de la zona de deplexión, mejorando la capacidad de bloqueo en alta tensión y la velocidad de conmutación. Se usa como interruptor RF, atenuador variable y fotodetector.
>
> **Ver también:** [diodo](#diodo), [zona de deplexión](#zona-de-deplexión)

### diodo Schottky

> **Definición formal:** Diodo formado por la unión de un metal con un semiconductor (en lugar de una unión PN). Tiene un voltaje umbral menor (~0.2–0.3V) y tiempos de conmutación más rápidos que un diodo convencional de Si, ya que no hay almacenamiento de portadores minoritarios. Se usa en fuentes conmutadas, mezcladores RF y circuitos de alta velocidad.
>
> **Valores típicos:** $V_K \approx 0.2\text{–}0.3\text{V}$, frecuencias hasta GHz.
>
> **Ver también:** [diodo](#diodo), [voltaje de umbral](#voltaje-de-umbral)

### diodo túnel

> **Definición formal:** Diodo con dopaje muy alto (degenerado) en ambas regiones P y N, que presenta efecto túnel cuántico y una región de resistencia diferencial negativa en su curva I-V directa. Funciona a frecuencias extremadamente altas (> 10 GHz). Inventado por Leo Esaki (1958).
>
> **Aplicaciones:** Osciladores de microondas, amplificadores, circuitos de conmutación ultrarrápida.
>
> **Ver también:** [diodo](#diodo), [Zener](#zener)

### diodo varactor

> **Definición formal:** Diodo diseñado para explotar la variación de capacitancia de la unión PN con el voltaje inverso aplicado. La capacitancia $C_j$ disminuye al aumentar el voltaje inverso. Se usa como capacitor variable controlado por voltaje en circuitos sintonizadores, VCOs y multiplicadores de frecuencia.
>
> **Fórmula:** $C_j = \frac{C_0}{(1 + V_R/V_0)^n}$ donde $n \approx 0.33\text{–}0.5$
>
> **Ver también:** [diodo](#diodo), [zona de deplexión](#zona-de-deplexión)

### diodo Zener

> **Definición formal:** Diodo diseñado para operar en la región de ruptura inversa de manera controlada y reversible. Mantiene un voltaje prácticamente constante ($V_Z$) en sus terminales independientemente de la corriente que lo atraviesa (dentro de $I_{Z(min)}$ a $I_{Z(max)}$). Caracterizado por su resistencia dinámica $r_Z$ y potencia máxima $P_{Z(max)} = V_Z \cdot I_{Z(max)}$.
>
> **Valores comerciales típicos:** 2.4V, 3.3V, 5.1V, 6.2V, 9.1V, 12V, 15V, 24V.
>
> **Ver también:** [ruptura](#ruptura), [regulador de voltaje](#regulador-de-voltaje)

### divisor de voltaje

> **Definición formal:** Configuración de polarización de un transistor que utiliza dos resistencias ($R_1$ y $R_2$) conectadas entre $V_{CC}$ y tierra para establecer un voltaje fijo en la base (BJT) o compuerta (FET). Es la configuración más estable y más utilizada en la práctica, ya que el punto Q es relativamente independiente de $\beta$ (BJT) o de los parámetros del dispositivo (FET).
>
> **Ecuación (BJT):** $V_B = V_{CC} \frac{R_2}{R_1 + R_2}$, $I_C \approx \frac{V_B - V_{BE}}{R_E}$
>
> **Ver también:** [punto de operación](#punto-de-operación), [estabilidad](#estabilidad)

### drenador

> **Definición formal:** Terminal del transistor FET equivalente al colector del BJT. Es por donde sale (o entra) la corriente principal del canal. En un JFET canal N, los electrones fluyen de fuente a drenador.
>
> **Ver también:** [fuente (terminal)](#fuente-terminal), [compuerta](#compuerta), [FET](#fet)

---

## E

### ecuación de Shockley

> **Definición formal:** Ecuación que describe la relación corriente-voltaje (I-V) de un diodo ideal:
> $$ I_D = I_S (e^{V_D / nV_T} - 1) $$
> Donde $I_S$ es la corriente de saturación inversa ($10^{-12}$A típicamente para Si), $n$ el factor de idealidad (1 para Ge, 2 para Si en baja corriente), y $V_T = kT/q$ el voltaje térmico (≈ 25.86 mV a 25°C).
>
> **Casos especiales:**
> - Polarización directa ($V_D \gg V_T$): $I_D \approx I_S e^{V_D / nV_T}$
> - Polarización inversa ($V_D \ll -V_T$): $I_D \approx -I_S$
>
> **Ver también:** [voltaje térmico](#voltaje-térmico), [corriente de saturación inversa](#corriente-de-saturación-inversa)

### emisor

> **Definición formal:** Terminal del transistor BJT que emite (inyecta) portadores mayoritarios hacia la base. Es la región más fuertemente dopada del dispositivo, identificada con una flecha en el símbolo esquemático (hacia afuera en NPN, hacia adentro en PNP). Relación: $I_E = I_C + I_B$.
>
> **Ver también:** [base](#base), [colector](#colector), [alfa](#alfa)

### estabilidad

> **Definición formal:** Capacidad de un circuito de polarización para mantener el punto de operación (punto Q) constante ante variaciones de temperatura, reemplazo del transistor (variación de $\beta$) o tolerancias de componentes. Se cuantifica mediante factores de estabilidad como $S(\beta)$, $S(I_{CO})$ y $S(V_{BE})$.
>
> **Factor de estabilidad:** $S(\beta) = \frac{\partial I_C}{\partial \beta}\bigg|_{Q}$ — idealmente lo más bajo posible.
>
> **Mejor estabilidad:** Polarización por divisor de voltaje con $R_E$.
>
> **Ver también:** [punto de operación](#punto-de-operación), [divisor de voltaje](#divisor-de-voltaje)

---

## F

### factor de rizado

> **Definición formal:** Medida de la efectividad del filtro en un rectificador. Se define como la relación entre el componente AC residual (rizado) y el nivel DC de la señal de salida:
> $$ r = \frac{V_{r(rms)}}{V_{DC}} \times 100\% $$
> Un factor de rizado menor indica una mejor calidad de la señal DC. Un rectificador ideal tiene $r = 0\%$.
>
> **Ver también:** [rizado](#rizado), [filtrado](#filtrado), [rectificación](#rectificación)

### FET

> **Definición formal:** Transistor de Efecto de Campo (*Field Effect Transistor*). Dispositivo semiconductor de tres terminales (compuerta, drenador, fuente) donde la corriente es controlada por un campo eléctrico aplicado en la compuerta. Utiliza un solo tipo de portador (unipolar). Impedancia de entrada extremadamente alta ($10^9$–$10^{14}$ Ω). Ecuación de transferencia (JFET): $I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2$.
>
> **Ventajas sobre BJT:** Mayor impedancia de entrada, menor ruido, más fácil de fabricar en circuitos integrados.
>
> **Ver también:** [JFET](#jfet), [MOSFET](#mosfet), [compuerta](#compuerta), [I_DSS](#idss), [V_P](#voltaje-de-pinch-off)

### filtrado

> **Definición formal:** Proceso de suavizar la señal pulsante obtenida en la rectificación mediante el uso de capacitores (y/o inductores) para obtener una señal de DC lo más constante posible. El rizado resultante depende del valor del capacitor ($C$), la frecuencia ($f$) y la corriente de carga ($I_L$):
> $$ V_r \approx \frac{I_L}{fC} = \frac{V_{DC}}{fRC} $$
>
> **Ver también:** [rectificación](#rectificación), [rizado](#rizado), [factor de rizado](#factor-de-rizado)

### fuente (terminal)

> **Definición formal:** Terminal del transistor FET equivalente al emisor del BJT. Es la terminal de referencia desde donde se emiten los portadores hacia el drenador a través del canal. En un JFET canal N, es el terminal por donde entran los electrones al canal.
>
> **Ver también:** [drenador](#drenador), [compuerta](#compuerta), [FET](#fet)

---

## G

### ganancia

> **Definición formal:** Relación entre la señal de salida y la señal de entrada de un amplificador. Puede expresarse como:
> - **Ganancia de voltaje:** $A_v = V_o / V_i$
> - **Ganancia de corriente:** $A_i = I_o / I_i$
> - **Ganancia de potencia:** $A_p = A_v \cdot A_i$
> - **En decibeles:** $A_{v(dB)} = 20 \log_{10} |A_v|$
>
> Valores negativos indican inversión de fase (180°), común en emisor común y fuente común.
>
> **Ver también:** [amplificador](#amplificador), [transconductancia](#transconductancia)

---

## I

### I_DSS

> **Definición formal:** Corriente de drenador de saturación con compuerta cortocircuitada a fuente ($V_{GS} = 0$). Es la corriente máxima que puede fluir por un JFET canal N (o la mínima en canal P). Parámetro fundamental del JFET junto con $V_P$.
>
> **Valores típicos:** 1 mA – 30 mA (depende del dispositivo).
>
> **Ecuación de transferencia:** $I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2$
>
> **Ver también:** [JFET](#jfet), [voltaje de pinch-off](#voltaje-de-pinch-off)

### impedancia de entrada

> **Definición formal:** Impedancia vista desde las terminales de entrada de un amplificador o circuito ($Z_i$). En BJT depende de la configuración: alta en colector común (~$\beta R_E$), media en emisor común (~$\beta r_e$), baja en base común (~$r_e$). En FET es extremadamente alta (~MΩ a GΩ).
>
> **Importancia:** Determina cuánta señal de la fuente se transfiere al amplificador. Idealmente, $Z_i \to \infty$.
>
> **Ver también:** [impedancia de salida](#impedancia-de-salida), [amplificador](#amplificador)

### impedancia de salida

> **Definición formal:** Impedancia equivalente de Thévenin vista desde las terminales de salida de un amplificador ($Z_o$). Determina la capacidad del amplificador para entregar señal a la carga. Idealmente, $Z_o \to 0$ para un amplificador de voltaje.
>
> **Ver también:** [impedancia de entrada](#impedancia-de-entrada), [amplificador](#amplificador)

---

## J

### JFET

> **Definición formal:** Transistor de Efecto de Campo de Unión (*Junction Field Effect Transistor*). Tipo de FET donde la compuerta forma una unión PN con el canal, controlando su conductividad mediante la variación del ancho de la zona de deplexión. Dispositivo "normalmente ON" (conduce con $V_{GS} = 0$). Controlado por voltaje, con corriente de compuerta despreciable.
>
> **Parámetros clave:** $I_{DSS}$ (corriente máxima), $V_P$ o $V_{GS(off)}$ (voltaje de corte).
>
> **Ecuación de transferencia:** $I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2$
>
> **Ver también:** [FET](#fet), [MOSFET](#mosfet), [I_DSS](#idss), [voltaje de pinch-off](#voltaje-de-pinch-off)

---

## M

### modelo híbrido

> **Definición formal:** Modelo de pequeña señal del BJT basado en los parámetros h (híbridos) del dispositivo. Utiliza una fuente de corriente controlada y los parámetros $h_{ie}$ (impedancia de entrada), $h_{re}$ (fracción de realimentación), $h_{fe}$ (ganancia de corriente) y $h_{oe}$ (admitancia de salida). Es un modelo de dos puertos completo y más preciso que el modelo $r_e$.
>
> **Parámetros (emisor común):**
> - $h_{ie} \approx \beta r_e$ — impedancia de entrada
> - $h_{fe} \approx \beta$ — ganancia de corriente
> - $h_{re} \approx 0$ (se desprecia normalmente)
> - $h_{oe} \approx 1/r_o$ (se desprecia normalmente)
>
> **Ver también:** [modelo re](#modelo-re), [parámetros h](#parámetros-h), [red de dos puertos](#red-de-dos-puertos)

### modelo re

> **Definición formal:** Modelo simplificado de pequeña señal del BJT que utiliza la resistencia dinámica del emisor $r_e = V_T / I_E \approx 26\text{mV} / I_E$ como parámetro central. Es más intuitivo y directo que el modelo híbrido, aunque menos preciso al ignorar la resistencia de salida $r_o$ y el efecto de realimentación.
>
> **Valor de $r_e$:** $r_e = \frac{26\text{ mV}}{I_E}$ a 25°C
>
> **Ganancia de voltaje (emisor común):** $A_v = -\frac{R_C}{r_e}$ (sin $R_E$), $A_v = -\frac{R_C}{r_e + R_E}$ (con $R_E$)
>
> **Ver también:** [modelo híbrido](#modelo-híbrido), [amplificador](#amplificador)

### MOSFET

> **Definición formal:** Transistor de Efecto de Campo Metal-Óxido-Semiconductor. Tipo de FET donde la compuerta está aislada del canal por una capa de óxido (SiO₂), controlando la corriente por efecto de campo. Dos tipos principales:
>
> - **MOSFET de deplexión (Depletion):** Normalmente ON, similar al JFET. Puede operar con $V_{GS}$ positivo o negativo.
> - **MOSFET de enriquecimiento (Enhancement):** Normalmente OFF. Requiere $V_{GS} > V_{T(th)}$ para crear el canal.
>
> **Ecuación (enriquecimiento, zona activa):** $I_D = k(V_{GS} - V_T)^2$
>
> **Ver también:** [FET](#fet), [JFET](#jfet)

### multiplicador de voltaje

> **Definición formal:** Circuito que utiliza diodos y capacitores para producir un voltaje DC de salida que es múltiplo entero del voltaje pico de entrada AC. Tipos: doblador de voltaje (Villard, Greinacher), triplicador, cuadruplicador. La salida teórica de un multiplicador ×N es $V_{out} = N \cdot V_{pico}$.
>
> **Limitaciones:** La regulación de carga empeora con factores de multiplicación altos.
>
> **Ver también:** [rectificación](#rectificación), [filtrado](#filtrado)

---

## P

### parámetros h

> **Definición formal:** Conjunto de cuatro parámetros híbridos que caracterizan un dispositivo activo (como un transistor) como una red de dos puertos. Combinan condiciones de cortocircuito y circuito abierto. Para emisor común:
>
> | Parámetro | Nombre | Unidad | Significado |
> |-----------|--------|--------|-------------|
> | $h_{ie}$ | Impedancia de entrada | Ω | Impedancia con salida en cortocircuito AC |
> | $h_{re}$ | Fracción de realimentación | — | Realimentación de voltaje (usualmente ≈ 0) |
> | $h_{fe}$ | Ganancia de corriente | — | $\beta_{ac}$ (≈ $\beta_{dc}$) |
> | $h_{oe}$ | Admitancia de salida | S | $1/r_o$ (usualmente ≈ 0) |
>
> **Ver también:** [modelo híbrido](#modelo-híbrido), [red de dos puertos](#red-de-dos-puertos)

### pequeña señal

> **Definición formal:** Modelo de análisis de circuitos con transistores donde las variaciones de señal son lo suficientemente pequeñas (típicamente < 10% de los valores DC) para que el dispositivo opere en la región lineal alrededor de su punto de operación (punto Q). Permite sustituir el transistor por un modelo equivalente lineal ($r_e$ o híbrido) y analizar el circuito con técnicas de circuitos lineales.
>
> **Procedimiento de análisis:**
> 1. Determinar punto Q (análisis DC).
> 2. Calcular $r_e = 26\text{mV} / I_E$.
> 3. Sustituir modelo de pequeña señal.
> 4. Analizar $A_v$, $Z_i$, $Z_o$.
>
> **Ver también:** [punto de operación](#punto-de-operación), [amplificador](#amplificador), [modelo re](#modelo-re)

### polarización directa

> **Definición formal:** Condición en la que se aplica un voltaje positivo al ánodo respecto al cátodo de un diodo (o la configuración equivalente en un transistor), reduciendo la barrera de potencial y permitiendo el flujo de corriente. En un diodo de Si, la conducción significativa comienza a partir de $V_D \approx 0.7\text{V}$.
>
> **En transistor BJT:** La unión base-emisor está polarizada directamente en región activa ($V_{BE} \approx 0.7\text{V}$).
>
> **Ver también:** [polarización inversa](#polarización-inversa), [voltaje de umbral](#voltaje-de-umbral)

### polarización fija (BJT)

> **Definición formal:** Configuración más simple de polarización del BJT donde una sola resistencia $R_B$ conecta $V_{CC}$ a la base. Altamente dependiente de $\beta$, por lo que es la configuración menos estable.
>
> **Ecuaciones:** $I_B = \frac{V_{CC} - V_{BE}}{R_B}$, $I_C = \beta I_B$, $V_{CE} = V_{CC} - I_C R_C$
>
> **Ver también:** [punto de operación](#punto-de-operación), [estabilidad](#estabilidad), [divisor de voltaje](#divisor-de-voltaje)

### polarización fija (FET)

> **Definición formal:** Configuración de polarización del JFET donde el voltaje $V_{GS}$ se fija mediante una fuente independiente $V_{GG}$ (o mediante resistencias conectadas a una fuente). Al ser $I_G \approx 0$, $V_{GS} = -V_{GG}$ directamente. El punto de operación se lee de la curva de transferencia en $V_{GS} = -V_{GG}$.
>
> **Ver también:** [autopolarización](#autopolarización), [JFET](#jfet)

### polarización inversa

> **Definición formal:** Condición en la que se aplica un voltaje negativo al ánodo respecto al cátodo de un diodo, aumentando la barrera de potencial interna y la zona de deplexión, impidiendo el flujo significativo de corriente (excepto la corriente de fuga $I_S$). La capacitancia de la unión varía con el voltaje inverso (base del varactor).
>
> **Ver también:** [polarización directa](#polarización-directa), [corriente de fuga](#corriente-de-fuga), [diodo varactor](#diodo-varactor)

### punto de operación

> **Definición formal:** Punto Q (*Quiescent point*). Valores de corriente y voltaje en DC que definen el estado de reposo de un transistor en un circuito. Determinado por la red de polarización.
>
> **Para BJT:** Definido por ($I_{C_Q}$, $V_{CE_Q}$). Ubicado en la intersección de la recta de carga con la curva $I_B$ correspondiente.
>
> **Para FET:** Definido por ($I_{D_Q}$, $V_{DS_Q}$). Ubicado en la intersección de la ecuación de transferencia con la condición de polarización.
>
> **Ver también:** [recta de carga](#recta-de-carga), [estabilidad](#estabilidad)

---

## R

### recortador

> **Definición formal:** Circuito con diodos que "recorta" o elimina una porción de la forma de onda de entrada que excede (o está por debajo de) un nivel de referencia. Tipos principales:
> - **Serie:** El diodo en serie con la carga permite/bloquea la señal.
> - **Paralelo (shunt):** El diodo en paralelo con la carga desvía la corriente al conducir.
> - **Polarizado:** Se añade una fuente DC para ajustar el nivel de recorte.
>
> **Aplicaciones:** Protección de circuitos, conformación de ondas, limitadores de señal.
>
> **Ver también:** [sujetador](#sujetador), [diodo](#diodo)

### recta de carga

> **Definición formal:** Línea en el plano I-V que representa todas las combinaciones posibles de corriente y voltaje permitidas por el circuito externo (fuente y resistencias). Su intersección con la curva característica del dispositivo determina el punto de operación.
>
> **Recta de carga DC (BJT):** $V_{CE} = V_{CC} - I_C(R_C + R_E)$ — define dos puntos: $(0, V_{CC})$ y $(V_{CC}/(R_C+R_E), 0)$.
>
> **Recta de carga AC:** Pendiente diferente a la DC cuando hay capacitores de desacople; pasa por el punto Q con pendiente $-1/(R_C \| R_L)$.
>
> **Ver también:** [punto de operación](#punto-de-operación)

### rectificación

> **Definición formal:** Proceso de convertir corriente alterna (AC) en corriente directa (DC) pulsante mediante el uso de diodos. Configuraciones principales:
>
> | Tipo | Diodos | $V_{DC}$ (sin filtro) | Frecuencia de rizado |
> |------|--------|----------------------|---------------------|
> | Media onda | 1 | $V_p/\pi$ | $f$ |
> | Onda completa (tap central) | 2 | $2V_p/\pi$ | $2f$ |
> | Puente de diodos | 4 | $2V_p/\pi$ | $2f$ |
>
> **Ver también:** [filtrado](#filtrado), [diodo](#diodo), [rizado](#rizado)

### red de dos puertos

> **Definición formal:** Modelo de circuito con cuatro terminales (dos de entrada, dos de salida) utilizado para caracterizar dispositivos activos como transistores. Se describe mediante matrices de parámetros (h, z, y, ABCD). En el curso se utilizan principalmente los parámetros h (híbridos) para el BJT.
>
> **Ecuaciones del modelo h:**
> - $V_1 = h_{11}I_1 + h_{12}V_2$
> - $I_2 = h_{21}I_1 + h_{22}V_2$
>
> **Ver también:** [parámetros h](#parámetros-h), [modelo híbrido](#modelo-híbrido)

### región activa

> **Definición formal:** Región de operación del BJT donde la unión base-emisor está polarizada directamente y la unión base-colector está polarizada inversamente. En esta región $I_C = \beta I_B$ y el transistor funciona como amplificador lineal. Para el FET, es la región donde $I_D$ es relativamente constante para cambios en $V_{DS}$ (zona de saturación o pinch-off).
>
> **Ver también:** [saturación](#saturación), [corte](#corte), [punto de operación](#punto-de-operación)

### regulador de voltaje

> **Definición formal:** Circuito que mantiene un voltaje de salida constante independientemente de variaciones en la carga o en el voltaje de entrada. Tipos:
> - **Con Zener:** Simple, baja potencia, regulación limitada por $r_Z$.
> - **Transistorizado:** Usa transistor como elemento de paso, mejor regulación, mayor corriente.
> - **Con CI:** ICs dedicados (78xx, 79xx, LM317, LM337) con protecciones integradas.
>
> **Regulación de línea:** $\%Reg_{línea} = \frac{\Delta V_o}{\Delta V_i} \times 100\%$
>
> **Regulación de carga:** $\%Reg_{carga} = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\%$
>
> **Ver también:** [diodo Zener](#diodo-zener)

### resistencia dinámica

> **Definición formal:** Resistencia AC de un diodo, definida como la pendiente de la curva I-V en el punto de operación:
> $$ r_d = \frac{nV_T}{I_D} \approx \frac{26\text{ mV}}{I_D} $$
> Para $I_D = 1\text{ mA}$: $r_d \approx 26\text{ Ω}$. Disminuye al aumentar la corriente.
>
> **En el diodo Zener:** $r_Z = \Delta V_Z / \Delta I_Z$ (típicamente 2–20 Ω).
>
> **Ver también:** [ecuación de Shockley](#ecuación-de-shockley), [diodo](#diodo)

### rizado

> **Definición formal:** Componente de AC residual presente en la salida de un rectificador con filtro. Se expresa como voltaje pico a pico ($V_{r(pp)}$) o como factor de rizado ($r$).
>
> **Rizado con filtro capacitivo:**
> - Media onda: $V_{r(pp)} \approx \frac{V_p}{fRC}$
> - Onda completa: $V_{r(pp)} \approx \frac{V_p}{2fRC}$
>
> **Ver también:** [rectificación](#rectificación), [filtrado](#filtrado), [factor de rizado](#factor-de-rizado)

### ruptura

> **Definición formal:** Condición en la que un diodo polarizado inversamente permite un flujo súbito y grande de corriente al superarse el voltaje de ruptura ($V_{BR}$). Puede ocurrir por efecto Zener ($V_Z < 5\text{V}$, efecto túnel, coef. temp. negativo) o por efecto Avalancha ($V_Z > 5\text{V}$, multiplicación por impacto, coef. temp. positivo). En $V_Z \approx 5\text{V}$ ambos efectos coexisten, resultando en coeficiente de temperatura prácticamente nulo.
>
> **Ver también:** [avalancha](#avalancha), [Zener](#zener)

## S

### saturación

> **Definición formal:** Región de operación del BJT donde ambas uniones (base-emisor y base-colector) están polarizadas directamente. $V_{CE} \approx V_{CE(sat)} \approx 0.2\text{V}$ (Si). El transistor actúa como un interruptor cerrado con una caída mínima. La corriente de colector es limitada por el circuito externo, no por $\beta I_B$.
>
> **Condición:** $I_B > I_{B(sat)} = I_C / \beta$ o equivalentemente $I_C < \beta I_B$.
>
> **En FET:** La "región de saturación" (o pinch-off) es donde $I_D$ es relativamente constante — equivalente a la *región activa* del BJT (¡atención con la terminología!).
>
> **Ver también:** [corte](#corte), [conmutación](#conmutación), [región activa](#región-activa)

### sujetador

> **Definición formal:** Circuito con diodo y capacitor que desplaza (*clamp*) el nivel DC de una señal AC sin cambiar su forma de onda. El capacitor se carga al valor pico durante un semiciclo y mantiene esa carga, añadiendo o restando un nivel DC a la señal.
>
> **Tipos:**
> - **Sujetador positivo:** Desplaza la forma de onda hacia arriba.
> - **Sujetador negativo:** Desplaza la forma de onda hacia abajo.
> - **Polarizado:** Añade una fuente DC para ajustar el nivel de sujeción.
>
> **Regla práctica:** La señal de salida oscila entre 0 y $2V_p$ (sujetador simple sin polarización).
>
> **Ver también:** [recortador](#recortador), [diodo](#diodo)

---

## T

### transconductancia

> **Definición formal:** Parámetro de pequeña señal del FET que relaciona el cambio en la corriente de drenador con el cambio en el voltaje compuerta-fuente ($g_m = \Delta I_D / \Delta V_{GS}$). Es el equivalente FET de la ganancia de corriente $\beta$ del BJT. Unidad: Siemens (S) o mhos.
>
> **Fórmulas:**
> - $g_m = g_{m0}\left(1 - \frac{V_{GS}}{V_P}\right)$
> - $g_{m0} = \frac{2 I_{DSS}}{|V_P|}$ (transconductancia máxima, en $V_{GS} = 0$)
> - $g_m = \frac{2}{|V_P|}\sqrt{I_{DSS} \cdot I_D}$
>
> **Valores típicos:** 1–10 mS
>
> **Ver también:** [FET](#fet), [JFET](#jfet), [I_DSS](#idss), [ganancia](#ganancia)

---

## U

### unión PN

> **Definición formal:** Interfaz formada entre un semiconductor tipo P (exceso de huecos) y uno tipo N (exceso de electrones). Es la estructura fundamental del diodo y base de todos los dispositivos semiconductores. Al formarse, la difusión de portadores crea la zona de deplexión con un campo eléctrico interno (barrera de potencial $V_0 \approx 0.7\text{V}$ en Si, $\approx 0.3\text{V}$ en Ge).
>
> **Ver también:** [diodo](#diodo), [zona de deplexión](#zona-de-deplexión), [polarización directa](#polarización-directa)

---

## V

### voltaje de pinch-off

> **Definición formal:** Voltaje de compuerta-fuente ($V_P$ o $V_{GS(off)}$) que reduce la corriente de drenador a cero en un JFET. Es negativo para canal N y positivo para canal P. Junto con $I_{DSS}$, define completamente la curva de transferencia del JFET.
>
> **Valores típicos:** $-2\text{V}$ a $-8\text{V}$ (JFET canal N)
>
> **Relación con $I_{DSS}$:** $g_{m0} = 2I_{DSS}/|V_P|$
>
> **Ver también:** [I_DSS](#idss), [JFET](#jfet), [FET](#fet)

### voltaje de umbral

> **Definición formal:** Voltaje mínimo de polarización directa ($V_K$, $V_\gamma$ o $V_{th}$) necesario para que un diodo comience a conducir corriente significativa. Depende fuertemente del material semiconductor y disminuye con la temperatura.
>
> **Valores típicos:**
>
> | Material | $V_K$ | Coef. Temperatura |
> |----------|-------|-------------------|
> | Silicio (Si) | ≈ 0.7 V | −2.5 mV/°C |
> | Germanio (Ge) | ≈ 0.3 V | −2.5 mV/°C |
> | Schottky | ≈ 0.2–0.3 V | — |
> | LED (rojo) | ≈ 1.8 V | — |
> | LED (azul/blanco) | ≈ 3.0–3.6 V | — |
>
> **Ver también:** [polarización directa](#polarización-directa), [ecuación de Shockley](#ecuación-de-shockley)

### voltaje térmico

> **Definición formal:** Voltaje equivalente de la energía térmica de los portadores de carga:
> $$ V_T = \frac{kT}{q} $$
> Donde $k = 1.381 \times 10^{-23}$ J/K (constante de Boltzmann), $T$ la temperatura en Kelvin y $q = 1.602 \times 10^{-19}$ C (carga del electrón).
>
> **Valores a distintas temperaturas:**
>
> | T (°C) | T (K) | $V_T$ (mV) |
> |--------|-------|------------|
> | 0 | 273 | 23.54 |
> | 25 | 298 | 25.86 |
> | 50 | 323 | 27.85 |
> | 75 | 348 | 30.00 |
> | 100 | 373 | 32.16 |
>
> **Ver también:** [ecuación de Shockley](#ecuación-de-shockley)

---

## Z

### Zener

> **Definición formal:** Efecto de ruptura en diodos con voltajes de ruptura inferiores a ~5V, causado por el efecto túnel cuántico de electrones a través de la zona de deplexión estrecha bajo un campo eléctrico intenso (~$10^7$ V/m). Tiene coeficiente de temperatura **negativo** (el voltaje de ruptura disminuye con la temperatura).
>
> **Distinción con avalancha:** El efecto Zener predomina en $V_Z < 5\text{V}$, el efecto avalancha en $V_Z > 5\text{V}$.
>
> **Ver también:** [avalancha](#avalancha), [diodo Zener](#diodo-zener), [ruptura](#ruptura)

### zona de deplexión

> **Definición formal:** Región alrededor de la unión PN desprovista de portadores libres, formada por la difusión y recombinación de electrones y huecos. Crea un campo eléctrico interno (barrera de potencial) que se opone a la difusión adicional. Su ancho varía con el voltaje aplicado:
> - **Polarización directa:** se estrecha → permite corriente.
> - **Polarización inversa:** se ensancha → bloquea corriente.
>
> **Relación con capacitancia:** $C_j \propto 1/\sqrt{V_R + V_0}$ (base del varactor).
>
> **Ver también:** [unión PN](#unión-pn), [diodo varactor](#diodo-varactor)

---

## Α

### alfa (α)

> **Definición formal:** Ganancia de corriente en DC del transistor BJT en configuración base común. Definida como la relación entre la corriente de colector y la corriente de emisor:
> $$ \alpha = \frac{I_C}{I_E} $$
> El valor de $\alpha$ es siempre ligeramente menor que 1 (típicamente 0.95–0.998).
>
> **Relación con beta:** $\alpha = \frac{\beta}{1+\beta}$, $\beta = \frac{\alpha}{1-\alpha}$
>
> **Ver también:** [beta](#beta), [BJT](#bjt)
