# REPORTE DE PRÁCTICA 1

## INTRODUCCIÓN
La rectificación es el proceso fundamental mediante el cual se convierte una señal de corriente alterna (AC), típicamente de la red eléctrica, en corriente continua (DC). En esta práctica se analiza y comprueba el funcionamiento del rectificador puente monofásico de onda completa (puente de Graetz), el cual aprovecha ambos semiciclos de la onda de entrada mediante un arreglo de cuatro diodos.

Debido a que la salida de este rectificador es pulsante (y posee un alto factor de rizo), no es adecuada para alimentar directamente a la mayoría de los circuitos electrónicos. Para "aplanar" esta señal, de forma práctica se hace uso de filtros pasivos. Primero, se analiza un filtro inductivo (colocando una bobina en serie) que se opone a los cambios bruscos de corriente, y posteriormente un filtro capacitivo (en paralelo a la carga), el cual almacena energía y mantiene el voltaje más estable, disminuyendo considerablemente la componente alterna de la señal hasta alcanzar el rizo deseado.

## OBJETIVO
El objetivo de la práctica es que el alumno sea capaz de diseñar rectificadores monofásicos, así como realizar los cálculos de voltajes y corrientes promedio y rms, también la determinación de las formas de onda de voltaje y corriente mediante osciloscopio y finalmente diseñar los filtros pasivos adecuados para reducir rizo de salida.

## MATERIAL Y EQUIPO
**Equipo:**
- Osciloscopio digital con FFT
- Sonda de efecto Hall para medición de corriente en osciloscopio

**Material:**
- 4 - Diodos 1N 4005 o equivalente
- 1 - Transformador reductor 120V primario 12V secundario a 2 o 3 Amp.
- 1 - Tablilla protoboard
- Alambre para conexión
- Capacitor electrolítico e inductor con base al diseño.
- Resistor de potencia de 10Ω/25W

## CÁLCULOS
*(Valores teóricos basados en $V_{s(rms)} = 12$ V, $f = 60$ Hz, $R = 10\ \Omega$, $V_D = 0.7$ V)*

- **Voltaje pico del secundario:** $V_m = V_{s(rms)} \times \sqrt{2} = 12 \times \sqrt{2} = 16.97$ V
  > **Práctico:** $V_m = 13.8\text{ V} + 2(0.6\text{ V}) = 15.0$ V

- **Voltaje pico rectificado:** $V_{m,red} = V_m - 2V_D = 16.97 - 1.4 = 15.57$ V
  > **Práctico:** $V_{m,red} = 15.0\text{ V} - 2(0.6\text{ V}) = 13.8$ V *(Amplitud rectificada mostrada en osciloscopio)*

- **Voltaje DC promedio:** $V_o(cd) = \frac{2V_{m,red}}{\pi} = \frac{2(15.57)}{\pi} \approx 9.91$ V
  > **Práctico:** $V_o(cd) = \frac{2(13.8\text{ V})}{\pi} \approx 8.78$ V

- **Corriente DC promedio:** $I_o(cd) = \frac{V_o(cd)}{R} = \frac{9.91}{10} \approx 0.991$ A
  > **Práctico:** $I_o(cd) = \frac{8.78\text{ V}}{10\ \Omega} \approx 0.878$ A

- **Voltaje RMS de salida:** $V_o(rms) = \frac{V_{m,red}}{\sqrt{2}} = \frac{15.57}{\sqrt{2}} \approx 11.01$ V
  > **Práctico:** $V_o(rms) = \frac{13.8\text{ V}}{\sqrt{2}} \approx 9.75$ V

- **Corriente RMS de salida:** $I_o(rms) = \frac{V_o(rms)}{R} = \frac{11.01}{10} \approx 1.101$ A
  > **Práctico:** $I_o(rms) = \frac{9.75\text{ V}}{10\ \Omega} \approx 0.975$ A

- **Voltaje de rizo RMS:** $V_{r(rms)} = \sqrt{V_o(rms)^2 - V_o(cd)^2} = \sqrt{11.01^2 - 9.91^2} \approx 4.79$ V
  > **Práctico:** $V_{r(rms)} = \sqrt{9.75^2 - 8.78^2} \approx 4.23$ V

- **Factor de rizo (FR):** $FR = \frac{V_{r(rms)}}{V_o(cd)} = \frac{4.79}{9.91} \approx 0.4834$ (48.34%)
  > **Práctico:** $FR = \frac{4.23}{8.78} \approx 0.4817$ (48.17%)

- **Corriente promedio por diodo:** $I_{D(prom)} = \frac{I_o(cd)}{2} \approx 0.495$ A
  > **Práctico:** $I_{D(prom)} = \frac{0.878\text{ A}}{2} = 0.439$ A

- **Corriente RMS por diodo:** $I_{D(rms)} = \frac{I_o(rms)}{\sqrt{2}} \approx 0.778$ A
  > **Práctico:** $I_{D(rms)} = \frac{0.975\text{ A}}{\sqrt{2}} \approx 0.689$ A

*(Valores prácticos de filtros medidos: Capacitor $C = 4775\ \mu$F, Inductor $L = 2976$ mH con resistencia $R_L = 19.1\ \Omega$)*

## DESARROLLO:

### Rectificador puente monofásico de onda completa
#### Circuito 1: Análisis e implementación del rectificador puente
# Inciso a
Con base al valor del voltaje de alimentación de AC, calcule los parámetros de rendimiento: Vo(cd), Io(cd), Vo(rms), Io(rms), Vr(rizo), ID(prom), ID(rms), VPR, Po(CA), Po(CD) y f.

![1575fb7a7b78007f96ed945ccf4d4d39.png](:/0bf931fb7c964d4690ea75b9912ed189)
# Inciso b
Implemente el circuito para ser analizado en laboratorio como se muestra en la figura 1.

![fa540565cf267dc78279cc189a7037ec.png](:/4cf18f8e2f334ace8eeb5f6f7ff74c6c)
Implementación física del rectificador puente de onda completa en tablilla.*

# Inciso c
De manera práctica mediante el osciloscopio, determine: las formas de onda del voltaje de entrada al rectificador, voltaje de salida del rectificador, midiendo sus valores promedio, rms, pico a pico, y frecuencia.

![11b3d320d22f1a1b4da3b69003e58847.png](:/ed1dbdd1c7f74c4d8a6d11791cf9f9f6)
Formas de onda del voltaje de entrada y salida rectificada medida con osciloscopio. Muestra valores pico a pico, promedio, rms y frecuencia.*

# Inciso d
Posteriormente mediante la sonda de efecto Hall mida la corriente promedio y rms en la fuente de AC, así como su forma de onda.

![4ff4d3b793da4a278add06f79d40a79c.png](:/cbc267a1b2e34549b6a1a8eecead6ffa)
*Forma de onda de corriente AC medida con sonda Hall.*

# Inciso e
Posteriormente mida la corriente promedio y rms en la carga, así como su forma de onda con la sonda de efecto Hall.

![c2fec53b36deab44996dca458a6842a1.png](:/6ba03098e3ba4a1ba7ac338a76be79db)
*Corriente en la carga medida con sonda Hall.*

# Inciso f
Utilizando la función de transformada rápida de Fourier, verifique el espectro de frecuencia en el osciloscopio, midiendo la frecuencia de los primeros cinco armónicos, verificando las frecuencias de los armónicos con el análisis visto.

![a808f82fb6ca771f4e44ebb83a1d9b15.png](:/9af1c31357e4484ab526ea24c55afbf1)
*FFT en dispositivo mostrando la frecuencia de los primeros armónicos.*

![4ee30383f4370b261a29cea8276104e6.png](:/83e06e618fab4bb181c67f17352557e4)
*Frecuencia de los primeros 5 armónicos.*

![11048fca7483315651d161548ad12807.png](:/eba684ca1c414496b5f25e2e9dbab8a9)
*Frecuencia del segun armonico*

### Rectificador con filtro inductivo
#### Circuito 2: Rectificador tipo H con filtro inductivo
# Inciso i
Agregue un inductor en serie con la resistencia de carga después de medirlo con el puente LCR a una frecuencia de 100HZ. Posteriormente verifique la forma de onda de la corriente del secundario del transformador Is.
> **Valor práctico:** Inductor medido: $L = 2976$ mH, Resistencia de choque: $R_L = 19.1\ \Omega$

![280c0b556c1b31eaf33b199b58d82a8a.png](:/439d13ab5bd74d5ea230e21cc3020471)
*Corriente con inductor en serie.*

# Inciso j
Con base a los valores de R y L prácticos, construya la serie de Fourier de la corriente de salida de manera analítica y posteriormente verifique la serie de manera práctica con el osciloscopio comparándola con el espectro.

![c123fcc9c9aea43fc89844c401c63cdf.png](:/dab88bf60619496386916c56764d8238)
*Análisis de Fourier de corriente con filtro inductivo en osciloscopio.*

**Análisis Teórico de la Serie de Fourier (componente $n=2$):**
Con los valores prácticos $V_{m,red} = 13.8$ V, $L = 2976$ mH, $R_L = 19.1\ \Omega$, $R = 10\ \Omega$.
- **Resistencia Total ($R_T$):** 
$$R_T = R + R_L = 10 + 19.1 = 29.1\ \Omega$$
- **Componente de Corriente Directa ($I_{o(dc)}$):** 
$$I_{o(dc)} = \frac{V_{o(cd)}}{R_T} = \frac{8.78\text{ V}}{29.1\ \Omega} \approx 0.3017\text{ A} = 301.7\text{ mA}$$
- **Amplitud del armónico $n=2$:**
$$V_{2(pico)} = \frac{4 V_{m,red}}{3\pi} = \frac{4(13.8)}{3\pi} \approx 5.86\text{ V}$$
- **Impedancia reactiva para $n=2$ ($120$ Hz):**
$$Z_2 = \sqrt{R_T^2 + (2 \pi (120) L)^2} = \sqrt{29.1^2 + 2244^2} \approx 2244\ \Omega$$
- **Corriente del segundo armónico ($I_{2(pico)}$):**
$$I_{2(pico)} = \frac{V_{2(pico)}}{|Z_2|} = \frac{5.86}{2244} \approx 2.61\text{ mA}$$

**Serie de Fourier de Corriente (componentes principales):**
$$i_o(t) \approx 0.3017 - 0.0026 \cos(2\omega t) \ldots \text{ A}$$

# Inciso k
Mida la corriente de rizo Ir(rms) mediante el osciloscopio y calcule Ir(rms) considerando el armónico de menor orden n=2, compare los valores y finalmente calcule el factor de rizo (FRi).

![b2fa24d7a20214b515a507707195f81f.png](:/d356c475435e43b086821fc93aa431ac)
*Medición de la corriente de rizo para inciso k.*

**Cálculo del rizo y Factor de Rizo ($FR_i$) considerando el armónico $n=2$:**
- **Corriente RMS de rizo ($I_{r(rms)}$):**
$$I_{r(rms)} \approx \frac{I_{2(pico)}}{\sqrt{2}} = \frac{2.61\text{ mA}}{\sqrt{2}} \approx 1.84\text{ mA}$$

- **Factor de rizo analítico ($FR_i$):**
$$FR_i = \frac{I_{r(rms)}}{I_{o(dc)}} = \frac{1.84\text{ mA}}{301.7\text{ mA}} \approx 0.0061 \implies 0.61\%$$
*Este valor indica una fuerte atenuación en la componente alterna debido a la elevación de la reactancia inductiva.*


### Rectificador con filtro capacitivo
#### Circuito 3: Implementación del filtro capacitivo

# Inciso l
Calcule un filtro capacitivo para reducir el rizo de salida a un valor <= 5%, también calcule el voltaje real de salida (Vo(cd)) y verifíquelo con el instrumento de medición.
> **Valor experimental:** $C = 4775\ \mu$F

![d50bbc15c4a552ffa1205cef2935bd2d.png](:/ff01244a3af34f94a9548efc36f09115)
*Voltaje Vo(cd) y análisis del rizo con el filtro capacitivo (colocado en tablilla).*

![4a8dc77a5a96adfe338f80f0e59db62b.png](:/224ab6f892954293be74a087894b004c)
*Verificación de rizo.*

![18d9dcfce2ecb36441b20aab22d5922f.png](:/948ef7ab12964311b6e9cde7d0d3a741)
*Medición detallada del voltaje.*

**Análisis Teórico con Filtro Capacitivo:**
A partir de $V_{m,red} = 13.8$ V, $C = 4775\ \mu$F, $R = 10\ \Omega$, $f_{red} = 120$ Hz.

- **Voltaje Pico a Pico de Rizo ($V_{r(pp)}$):**
$$V_{r(pp)} \approx \frac{V_{m,red}}{f_{red} R C} = \frac{13.8}{(120)(10)(4775 \times 10^{-6})} \approx 2.41\text{ V}$$

- **Voltaje Directo Real ($V_{o(cd)_C}$):**
$$V_{o(cd)_C} = V_{m,red} - \frac{V_{r(pp)}}{2} = 13.8 - \frac{2.41}{2} = 12.59\text{ V}$$

- **Voltaje Rizo RMS ($V_{r(rms)}$):**
$$V_{r(rms)} \approx \frac{V_{r(pp)}}{2\sqrt{3}} = \frac{2.41}{3.464} \approx 0.69\text{ V}$$

- **Factor de Rizo ($FR_c$):**
$$FR_c = \frac{V_{r(rms)}}{V_{o(cd)_C}} \times 100 = \frac{0.69}{12.59} \times 100 \approx 5.48 \%$$
*Este resultado teórico comprueba el funcionamiento del filtro experimentalmente, disminuyendo notablemente la oscilación frente al 48% original, dejándolo muy cercano al <=5% solicitado.*

# Inciso m
Adicione el filtro capacitivo y mediante el osciloscopio nuevamente obtenga el espectro de la serie de Fourier para el voltaje de salida y compárelo con el espectro del inciso f.

![e765e7aac5d9c60b08617a760b4713b2.png](:/5bbbe9c60b194420b292db0b073e178e)
*Análisis de FFT con filtro capacitivo.*

![afac41724ffc61f9ade82ab976ddec66.png](:/bf6112bb062f4b45acab65c4b446767f)
*FFT comparativo con los armónicos anteriores atenuados.*

## CONCLUSIÓN
En esta práctica se implementaron y analizaron tres circuitos fundamentales para la conversión AC-DC: un rectificador puente de onda completa y dos etapas de filtrado pasivo (inductiva y capacitiva). En la primera parte, se realizaron mediciones directas de la red con el osciloscopio sobre el puente de diodos, lo que permitió asentar las bases prácticas para los parámetros observados. Posteriormente, al incorporar el filtro inductivo en serie, las mediciones con la sonda de efecto Hall lograron capturar exitosamente el característico desfase que ejerce una bobina oponiéndose a los cambios entre la tensión y la corriente circulante. Finalmente, en el tercer circuito se analizó el filtro capacitivo en paralelo, donde el osciloscopio evidenció de cerca el comportamiento drástico para aplastar y asentar el rizo porcentual de la señal.

Como observación analítica de esta implementación, se documentó un cambio significativo en las disipaciones térmicas de los componentes dependiendo de la topología utilizada. Concretamente, se notó que al utilizar el filtro inductivo impulsado por un gran choque real, la resistencia de carga (resistencia de potencia) apenas presentó calentamiento debido a que la gran impedancia del inductor en la malla bloqueó violentamente el nivel de la corriente general que circulaba sobre la sección. En contraste, tanto interactuando con la carga rectificada sin protección inicial, como al usar el filtro capacitivo paralelo, dicha carga experimentó un calentamiento inmediato sumamente alto. Este comportamiento es vital, pues corrobora en laboratorio que las alteraciones de temperatura (y valores de resistencia reales variables) provocan que las mediciones lógicas de los voltajes en una carga pura lleguen a diferir ampliamente de sus contrapartes teóricas ideales.

A manera concluyente general, los análisis del desempeño y formas de onda constatan que la mayor estabilidad en el tiempo, rectitud en la señal de corriente continua y reducción eficiente del rizado se alcanza utilizando el filtro capacitivo probado. Sumado a su destacable reducida talla espacial frente a voluminosos y pesados inductores estáticos de alta capacitancia, se concluye con toda razón que este es el componente predominantemente preferido y estandarizado actualmente en el diseño versátil, eficaz y barato de microcircuitos y fuentes comerciales de electrónica analógica regular.


**Firma del Maestro:** ____________________________
