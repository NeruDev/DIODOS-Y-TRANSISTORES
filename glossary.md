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

> **Definición formal:** Circuito electrónico que incrementa la amplitud de una señal eléctrica (voltaje, corriente o potencia) sin alterar significativamente su forma.
>
> **Analogía:** Como un megáfono que toma tu voz débil y la convierte en una señal más fuerte.
>
> **Ver también:** [ganancia](#ganancia), [pequeña señal](#pequeña-señal)

### avalancha

> **Definición formal:** Mecanismo de ruptura en semiconductores donde los portadores acelerados por un campo eléctrico intenso generan nuevos pares electrón-hueco al colisionar con átomos de la red cristalina, produciendo una multiplicación en cascada de portadores.
>
> **Analogía:** Como una bola de nieve rodando colina abajo que se hace cada vez más grande al recoger más nieve.
>
> **Ver también:** [ruptura](#ruptura), [Zener](#zener)

---

## B

### base

> **Definición formal:** Terminal del transistor BJT que controla el flujo de corriente entre colector y emisor. Es la región central extremadamente delgada y ligeramente dopada del dispositivo.
>
> **Ver también:** [colector](#colector), [emisor](#emisor), [BJT](#bjt)

### BJT

> **Definición formal:** Transistor de Unión Bipolar (*Bipolar Junction Transistor*). Dispositivo semiconductor de tres terminales (base, colector, emisor) donde la corriente de salida es controlada por la corriente de entrada en la base. Utiliza ambos tipos de portadores (electrones y huecos).
>
> **Ver también:** [base](#base), [colector](#colector), [emisor](#emisor)

---

## C

### colector

> **Definición formal:** Terminal del transistor BJT que recoge los portadores inyectados desde el emisor a través de la base. Generalmente conectado a la fuente de alimentación a través de la carga.
>
> **Ver también:** [base](#base), [emisor](#emisor)

### corriente de fuga

> **Definición formal:** Corriente inversa de saturación ($I_S$) que fluye a través de un diodo polarizado inversamente, debida a los portadores minoritarios generados térmicamente. Del orden de nanoamperios o picoamperios.
>
> **Analogía:** Como una fuga muy pequeña en una presa: casi nada pasa, pero no es exactamente cero.
>
> **Ver también:** [polarización inversa](#polarización-inversa), [corriente de saturación inversa](#corriente-de-saturación-inversa)

### corriente de saturación inversa

> **Definición formal:** Corriente $I_S$ (también llamada corriente de fuga) que fluye cuando un diodo está polarizado inversamente. Se duplica aproximadamente cada 10°C de incremento en temperatura.
>
> **Ver también:** [corriente de fuga](#corriente-de-fuga), [ecuación de Shockley](#ecuación-de-shockley)

---

## D

### diodo

> **Definición formal:** Dispositivo semiconductor de dos terminales (ánodo y cátodo) que permite el flujo de corriente eléctrica preferentemente en una dirección (directa) y lo bloquea en la dirección opuesta (inversa).
>
> **Analogía:** Como una válvula de agua que solo permite el flujo en una dirección.
>
> **Ver también:** [ánodo](#ánodo), [cátodo](#cátodo), [unión PN](#unión-pn)

### diodo Zener

> **Definición formal:** Diodo diseñado para operar en la región de ruptura inversa de manera controlada y reversible. Mantiene un voltaje prácticamente constante ($V_Z$) en sus terminales independientemente de la corriente que lo atraviesa, usado para regulación de voltaje.
>
> **Ver también:** [ruptura](#ruptura), [regulador de voltaje](#regulador-de-voltaje)

### drenador

> **Definición formal:** Terminal del transistor FET equivalente al colector del BJT. Es por donde sale (o entra) la corriente principal del canal.
>
> **Ver también:** [fuente](#fuente-terminal), [compuerta](#compuerta)

---

## E

### ecuación de Shockley

> **Definición formal:** Ecuación que describe la relación corriente-voltaje (I-V) de un diodo ideal:
> $$ I = I_S (e^{V/nV_T} - 1) $$
> Donde $I_S$ es la corriente de saturación inversa, $n$ el factor de idealidad y $V_T$ el voltaje térmico.
>
> **Ver también:** [voltaje térmico](#voltaje-térmico), [corriente de saturación inversa](#corriente-de-saturación-inversa)

### emisor

> **Definición formal:** Terminal del transistor BJT que emite (inyecta) portadores mayoritarios hacia la base. Es la región más fuertemente dopada del dispositivo.
>
> **Ver también:** [base](#base), [colector](#colector)

---

## F

### FET

> **Definición formal:** Transistor de Efecto de Campo (*Field Effect Transistor*). Dispositivo semiconductor de tres terminales (compuerta, drenador, fuente) donde la corriente es controlada por un campo eléctrico aplicado en la compuerta. Utiliza un solo tipo de portador (unipolar).
>
> **Ver también:** [JFET](#jfet), [MOSFET](#mosfet), [compuerta](#compuerta)

### filtrado

> **Definición formal:** Proceso de suavizar la señal pulsante obtenida en la rectificación mediante el uso de capacitores (y/o inductores) para obtener una señal de DC lo más constante posible.
>
> **Ver también:** [rectificación](#rectificación), [rizado](#rizado)

---

## G

### ganancia

> **Definición formal:** Relación entre la señal de salida y la señal de entrada de un amplificador. Puede expresarse como ganancia de voltaje ($A_v$), de corriente ($A_i$) o de potencia ($A_p$).
>
> **Ver también:** [amplificador](#amplificador)

---

## J

### JFET

> **Definición formal:** Transistor de Efecto de Campo de Unión (*Junction Field Effect Transistor*). Tipo de FET donde la compuerta forma una unión PN con el canal, controlando su conductividad mediante la variación del ancho de la zona de deplexión.
>
> **Ver también:** [FET](#fet), [MOSFET](#mosfet)

---

## M

### MOSFET

> **Definición formal:** Transistor de Efecto de Campo Metal-Óxido-Semiconductor. Tipo de FET donde la compuerta está aislada del canal por una capa de óxido (SiO₂), controlando la corriente por efecto de campo. Puede ser de enriquecimiento o de deplexión.
>
> **Ver también:** [FET](#fet), [JFET](#jfet)

---

## P

### pequeña señal

> **Definición formal:** Modelo de análisis de circuitos con transistores donde las variaciones de señal son lo suficientemente pequeñas para que el dispositivo opere en la región lineal alrededor de su punto de operación (punto Q).
>
> **Ver también:** [punto de operación](#punto-de-operación), [amplificador](#amplificador)

### polarización directa

> **Definición formal:** Condición en la que se aplica un voltaje positivo al ánodo respecto al cátodo de un diodo (o la configuración equivalente en un transistor), reduciendo la barrera de potencial y permitiendo el flujo de corriente.
>
> **Ver también:** [polarización inversa](#polarización-inversa), [voltaje de umbral](#voltaje-de-umbral)

### polarización inversa

> **Definición formal:** Condición en la que se aplica un voltaje negativo al ánodo respecto al cátodo de un diodo, aumentando la barrera de potencial interna e impidiendo el flujo significativo de corriente (excepto la corriente de fuga $I_S$).
>
> **Ver también:** [polarización directa](#polarización-directa), [corriente de fuga](#corriente-de-fuga)

### punto de operación

> **Definición formal:** Punto Q (*Quiescent point*). Valores de corriente y voltaje en DC que definen el estado de reposo de un transistor en un circuito. Determinado por la red de polarización.
>
> **Ver también:** [recta de carga](#recta-de-carga), [polarización directa](#polarización-directa)

---

## R

### recta de carga

> **Definición formal:** Línea en el plano I-V que representa todas las combinaciones posibles de corriente y voltaje permitidas por el circuito externo (fuente y resistencias). Su intersección con la curva característica del dispositivo determina el punto de operación.
>
> **Ver también:** [punto de operación](#punto-de-operación)

### rectificación

> **Definición formal:** Proceso de convertir corriente alterna (AC) en corriente directa (DC) pulsante mediante el uso de diodos. Puede ser de media onda (un diodo) o de onda completa (puente de diodos o transformador con tap central).
>
> **Ver también:** [filtrado](#filtrado), [diodo](#diodo)

### regulador de voltaje

> **Definición formal:** Circuito que mantiene un voltaje de salida constante independientemente de variaciones en la carga o en el voltaje de entrada. Puede implementarse con diodo Zener, transistores o circuitos integrados.
>
> **Ver también:** [diodo Zener](#diodo-zener)

### rizado

> **Definición formal:** Componente de AC residual presente en la salida de un rectificador con filtro. Se expresa como voltaje pico a pico ($V_{rpp}$) o como factor de rizado.
>
> **Ver también:** [rectificación](#rectificación), [filtrado](#filtrado)

### ruptura

> **Definición formal:** Condición en la que un diodo polarizado inversamente permite un flujo súbito y grande de corriente al superarse el voltaje de ruptura ($V_{BR}$). Puede ocurrir por efecto Zener ($V_Z < 5V$) o por efecto Avalancha ($V_Z > 5V$).
>
> **Ver también:** [avalancha](#avalancha), [Zener](#zener)

---

## U

### unión PN

> **Definición formal:** Interfaz formada entre un semiconductor tipo P (exceso de huecos) y uno tipo N (exceso de electrones). Es la estructura fundamental del diodo y base de todos los dispositivos semiconductores.
>
> **Ver también:** [diodo](#diodo), [zona de deplexión](#zona-de-deplexión)

---

## V

### voltaje de umbral

> **Definición formal:** Voltaje mínimo de polarización directa ($V_K$ o $V_{th}$) necesario para que un diodo comience a conducir corriente significativa. Aproximadamente 0.7V para silicio y 0.3V para germanio. Disminuye ~2.5 mV/°C.
>
> **Ver también:** [polarización directa](#polarización-directa), [ecuación de Shockley](#ecuación-de-shockley)

### voltaje térmico

> **Definición formal:** Voltaje equivalente de la energía térmica de los portadores:
> $$ V_T = \frac{kT}{q} $$
> Donde $k$ es la constante de Boltzmann, $T$ la temperatura en Kelvin y $q$ la carga del electrón. A 25°C, $V_T \approx 25.86 \text{ mV}$.
>
> **Ver también:** [ecuación de Shockley](#ecuación-de-shockley)

---

## Z

### Zener

> **Definición formal:** Efecto de ruptura en diodos con voltajes de ruptura inferiores a ~5V, causado por el efecto túnel cuántico de electrones a través de la zona de deplexión estrecha bajo un campo eléctrico intenso. Tiene coeficiente de temperatura negativo.
>
> **Ver también:** [avalancha](#avalancha), [diodo Zener](#diodo-zener)

### zona de deplexión

> **Definición formal:** Región alrededor de la unión PN desprovista de portadores libres, formada por la difusión y recombinación de electrones y huecos. Crea un campo eléctrico interno (barrera de potencial) que se opone a la difusión adicional.
>
> **Ver también:** [unión PN](#unión-pn)
