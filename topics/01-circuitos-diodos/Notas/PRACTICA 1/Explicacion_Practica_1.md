# Explicación a Fondo — Práctica 1: Rectificadores Monofásicos

**Instituto Tecnológico de Toluca — Diodos y Transistores**

> Este documento complementa la [PRACTICA_1.md](PRACTICA_1.md) y el script [practica1_calculadora.py](practica1_calculadora.py). Aquí se explican en detalle las fórmulas empleadas, las variables involucradas, la lógica de cada paso, y se verifica la correspondencia entre los incisos de la práctica y la cobertura del script.

---

## Tabla de Contenidos

1. [Resumen de correspondencia: incisos vs. script](#1-resumen-de-correspondencia-incisos-vs-script)
2. [Variables del sistema](#2-variables-del-sistema)
3. [PASO 1 — Parámetros del transformador](#3-paso-1--parámetros-del-transformador)
4. [PASO 2 — Voltaje y corriente DC promedio](#4-paso-2--voltaje-y-corriente-dc-promedio)
5. [PASO 3 — Voltaje y corriente RMS](#5-paso-3--voltaje-y-corriente-rms)
6. [PASO 4 — Factor de forma y rizo](#6-paso-4--factor-de-forma-y-rizo)
7. [PASO 5 — Parámetros de los diodos](#7-paso-5--parámetros-de-los-diodos)
8. [PASO 6 — Potencias y rendimiento](#8-paso-6--potencias-y-rendimiento)
9. [PASO 7 — Serie de Fourier (5 armónicos)](#9-paso-7--serie-de-fourier-5-armónicos)
10. [PASO 8 — Filtro inductivo R-L](#10-paso-8--filtro-inductivo-r-l)
11. [PASO 9 — Filtro capacitivo](#11-paso-9--filtro-capacitivo)
12. [Revisión de fórmulas: verificación y observaciones](#12-revisión-de-fórmulas-verificación-y-observaciones)
13. [Notas sobre los incisos experimentales](#13-notas-sobre-los-incisos-experimentales)
14. [Referencias teóricas internas](#14-referencias-teóricas-internas)

---

## 1. Resumen de correspondencia: incisos vs. script

La práctica define 13 incisos (a–m). El script `practica1_calculadora.py` organiza los cálculos en 9 pasos. A continuación se muestra la correspondencia y si cada inciso está cubierto:

| Inciso | Descripción | Paso en script | Cubierto | Notas |
|:---:|---|:---:|:---:|---|
| **a** | Cálculos teóricos: Vo(cd), Io(cd), Vo(rms), Io(rms), Vr(rizo), ID(prom), ID(rms), VPR, Po(CA), Po(CD), f | Pasos 1–6 | **Sí** | Todos los parámetros de rendimiento se calculan |
| **b** | Implementar el circuito (Figura 1) | — | N/A | Inciso de laboratorio, no requiere cálculo |
| **c** | Medir voltajes con osciloscopio (promedio, rms, pico a pico, frecuencia) | — | N/A | Experimental; el script ofrece columna "medido" para ingresar valores |
| **d** | Medir corriente AC con sonda Hall (promedio y rms) | — | N/A | Experimental |
| **e** | Medir corriente en la carga con sonda Hall | — | N/A | Experimental |
| **f** | FFT en osciloscopio: 5 primeros armónicos | Paso 7 | **Sí** | El script calcula frecuencias y amplitudes de 5 armónicos |
| **g** | Forma de onda de corriente de salida + serie de Fourier | Paso 7 | **Parcial** | El script calcula la serie de voltaje; la serie de corriente (sin filtro) es proporcional: $i_o(t) = v_o(t)/R$ |
| **h** | Medir Is (corriente del secundario) con osciloscopio | — | N/A | Experimental |
| **i** | Agregar inductor en serie (medir L con puente LCR a 100 Hz) | Paso 8 | **Sí** | Cálculo del filtro R-L con atenuación de armónicos |
| **j** | Serie de Fourier de corriente con filtro L (analítica y práctica) | Paso 8 | **Sí** | La serie de corriente se construye con $I_n = V_n / Z_n$ |
| **k** | Medir Ir(rms) y calcular factor de rizo FRi con n=2 | Paso 8 | **Sí** | Se calcula $I_{r(rms)}$ con armónico dominante ($n=1$ en la expansión = 120 Hz) y FRi |
| **l** | Diseñar filtro capacitivo para FR ≤ 5 % y calcular Vo(cd) real | Paso 9 | **Sí** | Calcula $C_{min}$, voltaje DC real, y factor de rizo resultante |
| **m** | Medir FFT con filtro capacitivo y comparar con inciso f | Paso 7 / Tab | **Parcial** | El tab "Formas de Onda" muestra la señal filtrada; la comparación de espectros es visual/experimental |

### Veredicto general

- Los **9 incisos calculables** (a, f, g, i, j, k, l y parcialmente m) están cubiertos por los pasos 1–9 del script.
- Los **4 incisos puramente experimentales** (b, c, d, e, h) no requieren cálculo algorítmico; la interfaz proporciona espacio para ingresar valores medidos.
- El inciso **g** (serie de Fourier de **corriente** sin filtro) se cubre implícitamente porque $i_o(t) = v_o(t) / R$ en carga puramente resistiva.
- El inciso **m** (comparación de espectros con/sin filtro capacitivo) es esencialmente experimental; el script no genera la FFT del voltaje filtrado con capacitor, aunque las formas de onda se muestran en la pestaña correspondiente.

---

## 2. Variables del sistema

Antes de entrar en las fórmulas, es fundamental conocer cada variable, su origen y cómo se mide experimentalmente.

### 2.1 Variables de entrada (datos)

| Variable | Símbolo | Unidad | Valor típico | Cómo se obtiene |
|---|:---:|:---:|:---:|---|
| Voltaje RMS del secundario | $V_{s(rms)}$ | V | 12 | Multímetro en AC sobre terminales del secundario del transformador |
| Frecuencia de la red | $f$ | Hz | 60 | Osciloscopio: medir periodo $T$ de la señal AC → $f = 1/T$ |
| Caída de voltaje por diodo | $V_D$ | V | 0.7 | Multímetro en modo "diodo" o osciloscopio comparando $V_m$ con $V_{o,pico}$ |
| Resistencia de carga | $R$ | $\Omega$ | 10 | Multímetro en modo ohmímetro, con el resistor desconectado |
| Inductancia del filtro | $L$ | H | 1.5 | Puente LCR a 100 Hz (inciso i de la práctica) |
| Resistencia del devanado | $R_L$ | $\Omega$ | 40 | Puente LCR o multímetro en $\Omega$ |
| Capacitancia del filtro | $C$ | $\mu$F | 2200 | Valor nominal del capacitor; verificar con capacímetro si es posible |
| Factor de rizo objetivo | $FR_{obj}$ | — | 0.05 | Especificado por el enunciado (≤ 5%) |

### 2.2 Variables intermedias y de salida

| Variable | Símbolo | Unidad | Paso | Descripción física |
|---|:---:|:---:|:---:|---|
| Voltaje pico del secundario | $V_m$ | V | 1 | Amplitud máxima de la senoide del secundario |
| Voltaje pico rectificado | $V_{m,red}$ | V | 1 | Voltaje pico disponible en la carga (restando 2 caídas de diodo) |
| Frecuencia de salida | $f_{out}$ | Hz | 1 | Frecuencia de la señal rectificada de onda completa |
| Voltaje DC promedio | $V_o(cd)$ | V | 2 | Componente continua del voltaje sobre la carga |
| Corriente DC promedio | $I_o(cd)$ | A | 2 | Corriente promedio entregada a la carga |
| Voltaje RMS de salida | $V_o(rms)$ | V | 3 | Valor eficaz del voltaje rectificado |
| Corriente RMS de salida | $I_o(rms)$ | A | 3 | Valor eficaz de la corriente en la carga |
| Factor de forma | $FF$ | — | 4 | Relación $V_{rms}/V_{DC}$ (mide cuán "plana" es la señal) |
| Voltaje de rizo RMS | $V_{r(rms)}$ | V | 4 | Componente de alterna (rizo) del voltaje de salida |
| Factor de rizo | $FR$ | — | 4 | Porcentaje de rizo respecto a DC |
| Corriente promedio por diodo | $I_{D(prom)}$ | A | 5 | Corriente media por cada diodo individual |
| Corriente RMS por diodo | $I_{D(rms)}$ | A | 5 | Corriente eficaz por cada diodo individual |
| Voltaje pico inverso | $VPR$ | V | 5 | Máxima tensión inversa que soporta cada diodo |
| Potencia disipada por diodo | $P_{diodo}$ | W | 5 | Calor generado en cada diodo |
| Potencia DC | $P_o(cd)$ | W | 6 | Potencia útil de corriente continua |
| Potencia AC (total) | $P_o(CA)$ | W | 6 | Potencia total disipada en la carga |
| Rendimiento | $\eta$ | % | 6 | Eficiencia de rectificación |
| Impedancia armónica | $Z_n$ | $\Omega$ | 8 | Impedancia del circuito R-L para el n-ésimo armónico |
| Factor de rizo con filtro L | $FR_i$ | % | 8 | Rizo de corriente con filtro inductivo |
| Rizo pico a pico (filtro C) | $V_{r(pp)}$ | V | 9 | Rizo de voltaje con filtro capacitivo |
| Capacitor mínimo | $C_{min}$ | $\mu$F | 9 | Mínimo capacitor para cumplir FR ≤ 5% |

---

## 3. PASO 1 — Parámetros del transformador

### Contexto físico

El transformador reductor baja el voltaje de la red (120 V) a un nivel seguro y manejable (12 V RMS). La señal del secundario es senoidal:

$$v_s(t) = V_m \sin(\omega t)$$

donde $\omega = 2\pi f$ es la frecuencia angular.

### Fórmulas

**Voltaje pico del secundario:**

$$V_m = V_{s(rms)} \times \sqrt{2}$$

- **¿Por qué $\sqrt{2}$?** Para una señal senoidal pura, la relación entre el valor pico y el valor RMS (eficaz) es exactamente $\sqrt{2} \approx 1.414$. Esto se demuestra integrando $\sin^2(\omega t)$ sobre un periodo completo.
- **Ejemplo:** $V_m = 12 \times \sqrt{2} = 16.97$ V

**Voltaje pico rectificado (disponible en la carga):**

$$V_{m,red} = V_m - 2V_D$$

- **¿Por qué 2$V_D$?** En el puente de Graetz, la corriente siempre atraviesa **dos diodos en serie** por cada semiciclo. Cada diodo de silicio tiene una caída de aproximadamente 0.7 V, lo que resulta en $2 \times 0.7 = 1.4$ V de "pérdida" total.
- **Ejemplo:** $V_{m,red} = 16.97 - 1.4 = 15.57$ V

**Frecuencia de salida:**

$$f_{out} = 2f$$

- **¿Por qué se duplica?** El rectificador de onda completa invierte el semiciclo negativo, produciendo **dos pulsos por cada ciclo** de la señal de entrada. Si la red es de 60 Hz, la salida rectificada tiene $f_{out} = 120$ Hz.

### En el script

```python
r["Vm"]      = Vs * np.sqrt(2)          # V pico del secundario
r["Vm_red"]  = r["Vm"] - 2.0 * Vd      # V pico disponible (con 2 diodos)
r["f_out"]   = 2.0 * f                  # Hz (onda completa ↔ 2×f_red)
```

**Verificación:** Las fórmulas coinciden exactamente con las desarrolladas en la [Nota 6](../Nota6.md) y la [Nota 7](../Nota7.md).

---

## 4. PASO 2 — Voltaje y corriente DC promedio

### Contexto físico

El voltaje DC (promedio) es el valor que mediría un multímetro en modo DC sobre la carga. Es la **componente útil** de la señal rectificada: lo que realmente "alimenta" un circuito de corriente continua.

### Derivación de la fórmula

La señal rectificada de onda completa es $v_o(t) = V_{m,red}|\sin(\omega t)|$. Su valor promedio sobre un periodo $T_r = T/2$ es:

$$V_o(cd) = \frac{1}{T_r}\int_0^{T_r} v_o(t)\, dt = \frac{\omega}{\pi}\int_0^{\pi/\omega} V_{m,red}\sin(\omega t)\, dt$$

Resolviendo la integral:

$$V_o(cd) = \frac{V_{m,red}}{\pi}\Big[-\cos(\omega t)\Big]_0^{\pi/\omega} = \frac{V_{m,red}}{\pi}\Big[-\cos(\pi) + \cos(0)\Big] = \frac{V_{m,red}}{\pi}\Big[1 + 1\Big]$$

$$\boxed{V_o(cd) = \frac{2V_{m,red}}{\pi} \approx 0.6366 \times V_{m,red}}$$

**Corriente DC:**

$$I_o(cd) = \frac{V_o(cd)}{R}$$

por la ley de Ohm directamente, ya que la carga es puramente resistiva.

### Significado del factor $2/\pi$

El factor $2/\pi \approx 0.6366$ es una constante geométrica intrínseca a la rectificación de onda completa. Representa que, en promedio, una señal $|\sin(\theta)|$ vale $\approx 63.7\%$ de su valor pico. Esto es una consecuencia directa de la forma curva de la sinusoide: la señal pasa más tiempo alejada del pico que cerca de él.

### Valores esperados

Con $V_{m,red} = 15.57$ V y $R = 10\ \Omega$:

- $V_o(cd) = \frac{2 \times 15.57}{\pi} \approx 9.91$ V
- $I_o(cd) = \frac{9.91}{10} \approx 0.991$ A

---

## 5. PASO 3 — Voltaje y corriente RMS

### Contexto físico

El valor RMS (root mean square, o valor eficaz) mide la **potencia real** que la señal entrega a la carga. Un voltaje RMS de $X$ voltios disipa la misma potencia en una resistencia que una fuente DC de $X$ voltios.

### Derivación

Para $v_o(t) = V_{m,red}|\sin(\omega t)|$:

$$V_o(rms)^2 = \frac{1}{T_r}\int_0^{T_r} v_o(t)^2\, dt = \frac{\omega}{\pi}\int_0^{\pi/\omega} V_{m,red}^2\sin^2(\omega t)\, dt$$

Usando la identidad $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$:

$$V_o(rms)^2 = \frac{V_{m,red}^2}{\pi}\int_0^{\pi}\frac{1-\cos(2\theta)}{2}\, d\theta = \frac{V_{m,red}^2}{\pi}\cdot\frac{\pi}{2} = \frac{V_{m,red}^2}{2}$$

$$\boxed{V_o(rms) = \frac{V_{m,red}}{\sqrt{2}} \approx 0.7071 \times V_{m,red}}$$

**Dato importante:** Este es exactamente el mismo resultado que para una senoide **no** rectificada. Esto tiene sentido porque al rectificar no cambiamos las amplitudes instantáneas, solo reflejamos el semiciclo negativo, lo que no altera el valor cuadrático medio.

### Corriente RMS

$$I_o(rms) = \frac{V_o(rms)}{R}$$

### Valores esperados

- $V_o(rms) = \frac{15.57}{\sqrt{2}} \approx 11.01$ V
- $I_o(rms) = \frac{11.01}{10} \approx 1.101$ A

---

## 6. PASO 4 — Factor de forma y rizo

### Factor de forma ($FF$)

$$FF = \frac{V_o(rms)}{V_o(cd)} = \frac{V_{m,red}/\sqrt{2}}{2V_{m,red}/\pi} = \frac{\pi}{2\sqrt{2}} \approx 1.1107$$

**Interpretación:** Un $FF = 1.0$ significaría DC puro (sin rizo). El valor $1.11$ indica que la señal rectificada tiene $\approx 11\%$ más de "energía eficaz" de la que correspondería a DC puro. Este exceso proviene de la componente de alterna (rizo).

### Voltaje de rizo RMS ($V_{r(rms)}$)

La señal rectificada puede descomponerse en DC + rizo:

$$v_o(t) = V_o(cd) + v_{rizo}(t)$$

Como $V_{rms}^2 = V_{DC}^2 + V_{rizo,rms}^2$ (por ser ortogonales en Fourier):

$$\boxed{V_{r(rms)} = \sqrt{V_o(rms)^2 - V_o(cd)^2}}$$

### Factor de rizo ($FR$)

$$\boxed{FR = \frac{V_{r(rms)}}{V_o(cd)} = \sqrt{FF^2 - 1} \approx 0.4834 = 48.34\%}$$

**Interpretación:** Sin ningún filtro, el rizo es casi la mitad del voltaje DC útil. Esto es inaceptable para la mayoría de circuitos electrónicos sensibles, lo que justifica la necesidad de filtros (incisos i–m).

### En el script

```python
r["FF"]      = r["Vo_rms"] / r["Vo_dc"]
r["Vr_rms"]  = np.sqrt(max(r["Vo_rms"]**2 - r["Vo_dc"]**2, 0.0))
r["FR"]      = r["Vr_rms"] / r["Vo_dc"]
```

> El `max(..., 0.0)` es una protección numérica para evitar raíces cuadradas de valores negativos por errores de redondeo.

---

## 7. PASO 5 — Parámetros de los diodos

### Corriente promedio por diodo

En el puente de Graetz, cada diodo individual conduce **solo durante un semiciclo** (50% del tiempo), mientras que la corriente total de la carga fluye durante ambos semiciclos (repartida entre dos pares):

$$\boxed{I_{D(prom)} = \frac{I_o(cd)}{2}}$$

### Corriente RMS por diodo

Por la misma razón (conducción al 50%), la corriente RMS por diodo es:

$$\boxed{I_{D(rms)} = \frac{I_o(rms)}{\sqrt{2}}}$$

**¿Por qué $\sqrt{2}$ y no simplemente 2?** Porque el RMS involucra la raíz cuadrada de la media del cuadrado. Al conducir solo medio ciclo, la integral se reduce a la mitad del valor cuadrado, y la raíz de eso da $1/\sqrt{2}$ del RMS total.

### Voltaje de pico inverso (VPR o PIV)

Cuando un par de diodos conduce, los otros dos soportan tensión inversa. En el puente de Graetz:

$$\boxed{VPR = V_m}$$

**Ventaja clave del puente:** En un rectificador con derivación central, $VPR = 2V_m$, es decir, el doble. Esto significa que en el puente se pueden usar diodos con menor voltaje de ruptura, lo que reduce costos.

Para el 1N4005 ($V_{BR} = 600$ V) y $V_m \approx 17$ V, el factor de seguridad es $600/17 \approx 35\times$, ampliamente suficiente.

### Potencia disipada por diodo

$$P_{diodo} = V_D \times I_{D(prom)}$$

Esta es la potencia que se convierte en calor en cada diodo. Con $V_D = 0.7$ V e $I_{D(prom)} \approx 0.5$ A:

$$P_{diodo} \approx 0.35\ \text{W}$$

### Nota sobre la fórmula del VPR en el script

El script usa `r["VPR"] = r["Vm"]`, que es el voltaje pico del secundario **sin** restar $V_D$. La expresión exacta por KVL es $VPR = V_m - V_D$ (ver [Nota 6](../Nota6.md), sección de PIV). En la práctica, $V_D = 0.7$ V es despreciable frente a $V_m = 16.97$ V, y usar $V_m$ directamente es la **convención conservadora** (sobredimensiona ligeramente el requerimiento del diodo, lo cual es preferible en diseño).

---

## 8. PASO 6 — Potencias y rendimiento

### Potencia DC (útil)

$$\boxed{P_o(cd) = \frac{V_o(cd)^2}{R} = V_o(cd) \times I_o(cd)}$$

Es la potencia que un circuito DC equivalente entregaría.

### Potencia AC (total disipada en la carga)

$$\boxed{P_o(CA) = \frac{V_o(rms)^2}{R} = V_o(rms) \times I_o(rms)}$$

Incluye tanto la componente DC como la componente de rizo. La diferencia $P_o(CA) - P_o(cd)$ es la potencia "desperdiciada" por el rizo.

### Rendimiento (eficiencia de rectificación)

$$\boxed{\eta = \frac{P_o(cd)}{P_o(CA)} \times 100\% = \frac{1}{FF^2} \times 100\%}$$

Para onda completa ideal:

$$\eta = \frac{8}{\pi^2} \times 100\% \approx 81.06\%$$

**Interpretación:** El $\approx 19\%$ restante es potencia disipada como calor adicional debido a la forma pulsante del rizo, que no contribuye al trabajo útil DC.

---

## 9. PASO 7 — Serie de Fourier (5 armónicos)

### Fundamento teórico

La señal rectificada de onda completa se puede representar como una suma de componentes senoidales (serie de Fourier). Esto permite identificar **qué frecuencias** contiene la señal y diseñar filtros que las eliminen.

### Fórmula general

$$\boxed{v_o(t) = \frac{2V_{m,red}}{\pi} - \frac{4V_{m,red}}{\pi}\sum_{n=1}^{\infty}\frac{\cos(2n\omega t)}{4n^2 - 1}}$$

La señal se compone de:
- Una **componente DC** (nivel constante): $V_{DC} = \frac{2V_{m,red}}{\pi}$
- Infinitos **armónicos coseno** a frecuencias $2f, 4f, 6f, 8f, 10f, \ldots$

> **¿Por qué solo armónicos pares?** Porque la función $|\sin(\omega t)|$ tiene periodo $T/2$ (la mitad del periodo de la entrada). Al ser simétrica y par, solo aparecen cosenos a frecuencias múltiplos de $2f$.

### Amplitud del n-ésimo armónico

$$|C_n| = \frac{4V_{m,red}}{\pi(4n^2 - 1)}$$

| $n$ | Frecuencia | $4n^2 - 1$ | Amplitud pico | % de $V_{DC}$ |
|:---:|:---:|:---:|:---:|:---:|
| 1 | 120 Hz | 3 | $\frac{4V_{m,red}}{3\pi} \approx 6.61$ V | 66.7% |
| 2 | 240 Hz | 15 | $\frac{4V_{m,red}}{15\pi} \approx 1.32$ V | 13.3% |
| 3 | 360 Hz | 35 | $\frac{4V_{m,red}}{35\pi} \approx 0.57$ V | 5.7% |
| 4 | 480 Hz | 63 | $\frac{4V_{m,red}}{63\pi} \approx 0.31$ V | 3.2% |
| 5 | 600 Hz | 99 | $\frac{4V_{m,red}}{99\pi} \approx 0.20$ V | 2.0% |

**Observación clave:** El primer armónico (120 Hz) **domina** ampliamente el rizo. Contiene más del 95% de la potencia total de rizo. Esto significa que para filtrar, basta con atenuar significativamente la frecuencia de 120 Hz.

### En el script

```python
r["fourier_freqs"] = [2.0*(k+1)*f for k in range(N_HARM)]
r["fourier_amps"]  = [abs(4.0*r["Vm_red"]/(np.pi*(4.0*(k+1)**2-1.0))) for k in range(N_HARM)]
```

**Verificación:** Con `k=0` → $n=1$: frecuencia $= 2 \times 1 \times 60 = 120$ Hz, amplitud $= 4 \times 15.57 / (\pi \times 3) = 6.61$ V. Correcto.

### Relación con la práctica

- **Inciso f:** El osciloscopio con FFT debe mostrar picos en exactamente estas 5 frecuencias (120, 240, 360, 480, 600 Hz).
- **Inciso g:** La serie de Fourier de la **corriente** de salida (sin filtro inductivo, solo R) es simplemente $i_o(t) = v_o(t)/R$, ya que la carga es puramente resistiva.

---

## 10. PASO 8 — Filtro inductivo R-L

### Principio de operación

Al colocar un inductor $L$ en serie con la carga $R$ (Figura 2 de la práctica), se crea un filtro pasa-bajas que:
- **Deja pasar** la componente DC íntegramente (el inductor es un cortocircuito a $f = 0$).
- **Atenúa** los armónicos de mayor frecuencia (la reactancia inductiva $X_L = 2\pi f L$ crece con $f$).

### Efecto en la componente DC

El inductor real tiene una resistencia de devanado $R_L$, por lo que la resistencia total es:

$$R_T = R + R_L$$

La corriente DC con el filtro se reduce:

$$I_{o(dc),RL} = \frac{V_o(cd)}{R_T}$$

Y el voltaje que **realmente llega a la carga** $R$ es:

$$V_{carga} = I_{o(dc),RL} \times R$$

> **Efecto práctico importante:** Con $R = 10\ \Omega$ y $R_L = 40\ \Omega$, la resistencia total es 50 $\Omega$. Esto significa que solo $10/50 = 20\%$ del voltaje DC original llega a la carga. Aunque el inductor reduce mucho el rizo, también reduce drásticamente el voltaje útil en la carga.

### Impedancia para el n-ésimo armónico

$$Z_n = \sqrt{R_T^2 + (n \cdot \omega_{out} \cdot L)^2}$$

donde $\omega_{out} = 2\pi f_{out} = 2\pi \times 120$ rad/s.

### Corriente del n-ésimo armónico con filtro

$$I_n = \frac{V_n}{Z_n} = \frac{|C_n|}{\sqrt{R_T^2 + (n \cdot \omega_{out} \cdot L)^2}}$$

### Factor de atenuación respecto al caso sin filtro

$$\text{Atenuación}_n = \frac{R}{Z_n} \times 100\%$$

Para el armónico dominante ($n = 1$, 120 Hz), con $L = 1.5$ H:

$$X_{L1} = 1 \times 2\pi \times 120 \times 1.5 = 1131\ \Omega$$

$$Z_1 = \sqrt{50^2 + 1131^2} \approx 1132\ \Omega$$

$$\text{Atenuación}_1 = \frac{10}{1132} \times 100\% \approx 0.88\%$$

Es decir, la corriente del primer armónico se reduce al $\approx 0.9\%$ de su valor sin filtro.

### Factor de rizo con filtro inductivo (Inciso k)

Usando solo el armónico dominante (que contiene >95% de la potencia del rizo):

$$I_{r(rms)} \approx \frac{I_1}{\sqrt{2}}$$

$$FR_i = \frac{I_{r(rms)}}{I_{o(dc),RL}} \times 100\%$$

### En el script

```python
for k in range(N_HARM):
    n_k  = k + 1
    Vn   = r["fourier_amps"][k]
    Zn   = np.sqrt(RT**2 + (n_k * w_out * L)**2)
    r["Z_RL_arms"].append(Zn)
    r["IL_arms"].append(Vn / Zn)
    r["aten_RL"].append(R / Zn * 100.0)

r["Ir_rms_RL"] = r["IL_arms"][0] / np.sqrt(2.0)
r["FRi_RL"]    = (r["Ir_rms_RL"] / r["Io_dc_RL"]) * 100.0
```

**Nota sobre el inciso k de la práctica:** El enunciado pide calcular $I_{r(rms)}$ "considerando el armónico de menor orden $n=2$". En la convención del enunciado, "$n=2$" se refiere al **segundo armónico de la frecuencia de la red** (es decir, $2 \times 60 = 120$ Hz), que es el **primer armónico de la serie de Fourier de la salida** ($n=1$ en la expansión). El script usa correctamente el índice $k=0$ (equivalente a $n=1$ en la serie) que corresponde a la frecuencia de 120 Hz. No hay discrepancia real, solo diferencia de convención de indexación.

---

## 11. PASO 9 — Filtro capacitivo

### Principio de operación

Se retira el inductor y se conecta un capacitor $C$ en **paralelo** con la carga $R$ (Figura 3 de la práctica). El capacitor almacena energía durante los picos de voltaje y la libera durante los valles, reduciendo la variación (rizo) del voltaje sobre la carga.

### Modelo simplificado: descarga RC

Entre un pico y el siguiente (periodo $T_r = 1/f_{out}$), el capacitor se descarga exponencialmente a través de $R$. Si $RC \gg T_r$, la descarga es aproximadamente lineal y el rizo pico a pico es:

$$\boxed{V_{r(pp)} \approx \frac{V_{m,red}}{f_{out} \cdot R \cdot C}}$$

### Voltaje DC real con filtro capacitivo

El voltaje DC no es $2V_{m,red}/\pi$ (ya no hay una onda rectificada pura). El capacitor mantiene el voltaje cerca del pico, y el promedio se desplaza:

$$\boxed{V_o(cd)_C = V_{m,red} - \frac{V_{r(pp)}}{2}}$$

El voltaje DC es ahora mucho mayor que sin filtro, acercándose al valor pico.

### Rizo RMS (aproximación de onda triangular)

Para la forma de onda del rizo (diente de sierra), el valor RMS de una señal triangular de amplitud pico a pico $V_{r(pp)}$ es:

$$\boxed{V_{r(rms)_C} = \frac{V_{r(pp)}}{2\sqrt{3}}}$$

### Factor de rizo con filtro capacitivo

$$FR_C = \frac{V_{r(rms)_C}}{V_o(cd)_C}$$

### Diseño: capacitor mínimo para $FR \leq 5\%$

El script resuelve exactamente la ecuación:

$$FR_{obj} = \frac{V_{r(pp)} / (2\sqrt{3})}{V_{m,red} - V_{r(pp)}/2}$$

Definiendo $x = \frac{1}{f_{out} \cdot R \cdot C}$ (la razón $V_{r(pp)}/V_{m,red}$), se despeja:

$$x = \frac{2\sqrt{3} \cdot FR_{obj}}{1 + \sqrt{3} \cdot FR_{obj}}$$

Y el capacitor mínimo es:

$$\boxed{C_{min} = \frac{1}{x \cdot f_{out} \cdot R}}$$

### Valores esperados

Con $C = 2200\ \mu$F, $R = 10\ \Omega$, $f_{out} = 120$ Hz, $V_{m,red} = 15.57$ V:

| Parámetro | Valor |
|---|---|
| $V_{r(pp)}$ | $\frac{15.57}{120 \times 10 \times 2200 \times 10^{-6}} = 5.89$ V |
| $V_o(cd)_C$ | $15.57 - 5.89/2 = 12.63$ V |
| $V_{r(rms)_C}$ | $5.89 / (2\sqrt{3}) = 1.70$ V |
| $FR_C$ | $1.70 / 12.63 = 13.4\%$ |

**Conclusión:** Con $C = 2200\ \mu$F, el rizo baja de 48% a 13.4%, pero **no cumple** el requisito de ≤ 5%.

Para $FR_{obj} = 5\%$:

$$x_{min} = \frac{2\sqrt{3} \times 0.05}{1 + \sqrt{3} \times 0.05} = \frac{0.1732}{1.0866} = 0.1594$$

$$C_{min} = \frac{1}{0.1594 \times 120 \times 10} = 5229\ \mu\text{F}$$

**Valores comerciales sugeridos:** 5600 $\mu$F, 6800 $\mu$F, o tres capacitores de 2200 $\mu$F en paralelo (6600 $\mu$F).

---

## 12. Revisión de fórmulas: verificación y observaciones

Se realizó una revisión cruzada entre las fórmulas del script, las del [PROCEDIMIENTO_PRACTICA_1.md](PROCEDIMIENTO_PRACTICA_1.md), la [Nota 6](../Nota6.md) (rectificador puente) y la [Nota 7](../Nota7.md) (análisis de Fourier). A continuación se documentan los hallazgos:

### Fórmulas verificadas como correctas

| Fórmula | Paso | Fuente de verificación |
|---|:---:|---|
| $V_m = V_{s(rms)} \sqrt{2}$ | 1 | Nota 6, ecuación estándar de señales AC |
| $V_{m,red} = V_m - 2V_D$ | 1 | Nota 6 §2.1 — puente con 2 diodos en serie |
| $V_o(cd) = 2V_{m,red}/\pi$ | 2 | Nota 6 §c, Nota 7 §2.2 |
| $V_o(rms) = V_{m,red}/\sqrt{2}$ | 3 | Nota 6 §e |
| $FF = \pi/(2\sqrt{2})$ | 4 | Nota 7 §5.1 |
| $V_{r(rms)} = \sqrt{V_{rms}^2 - V_{DC}^2}$ | 4 | Nota 6 §h, Nota 7 §5.2 |
| $FR = \sqrt{FF^2 - 1}$ | 4 | Nota 7 §5.2, identidad derivada |
| $I_{D(prom)} = I_o(cd)/2$ | 5 | Nota 6 §i |
| $I_{D(rms)} = I_o(rms)/\sqrt{2}$ | 5 | Nota 6 §j |
| $VPR = V_m$ (conservador) | 5 | Nota 6 §g — exacto: $V_m - V_D$, script usa $V_m$ |
| $\eta = 8/\pi^2 \approx 81.1\%$ | 6 | Nota 7 §5.3 |
| $C_n = -4V_{m,red}/[\pi(4n^2-1)]$ | 7 | Nota 7 §2.3 — derivación completa paso a paso |
| $Z_n = \sqrt{R_T^2 + (n\omega_{out}L)^2}$ | 8 | Nota 7 §7.1 |
| $V_{r(pp)} = V_{m,red}/(f_{out} \cdot R \cdot C)$ | 9 | PROCEDIMIENTO §Fase 4 |

### Observaciones

1. **VPR en el script vs. teoría:** El script usa $VPR = V_m$ (sin restar $V_D$). La expresión exacta por KVL (Nota 6) es $VPR = V_m - V_D$. La diferencia es $\approx 0.7$ V, lo cual es insignificante para la selección del diodo y representa un enfoque conservador (sobredimensionado) correcto para diseño.

2. **Indexación de armónicos:** El enunciado de la práctica (inciso k) habla del "armónico de menor orden $n = 2$" refiriéndose a la frecuencia $2f = 120$ Hz. El script indexa con `k = 0` para este armónico (primer término de la serie de Fourier de la **salida**). Ambas convenciones son válidas; el cálculo numérico es idéntico.

3. **Filtro capacitivo — modelo:** La fórmula $V_{r(pp)} \approx V_{m,red}/(f \cdot R \cdot C)$ es una **aproximación** que asume descarga lineal del capacitor (válida cuando $RC \gg T_r$). Para capacitores pequeños donde el rizo es grande, esta aproximación pierde precisión. El script maneja esto correctamente con la fórmula exacta para $C_{min}$.

4. **Corriente del secundario ($I_s$) — inciso h:** La corriente del secundario del transformador en un rectificador puente **no** es simplemente $I_o(rms)$. Teóricamente, en el caso idealizado sin filtro, la corriente del secundario es una señal sinusoidal rectificada (idéntica a la corriente de carga, pero alternando de dirección). Su valor RMS es el mismo que $I_o(rms)$. Sin embargo, al agregar filtros (especialmente capacitivos), la corriente del secundario se convierte en pulsos estrechos de alta amplitud, y la relación cambia. Este efecto es observable experimentalmente con la sonda de efecto Hall.

---

## 13. Notas sobre los incisos experimentales

Para los incisos que requieren trabajo en el osciloscopio, las siguientes notas son relevantes:

### Inciso c — Medición simultánea de voltajes

> "Cuando se mida la parte de AC no conectar los dos canales del osciloscopio"

**¿Por qué?** Las sondas del osciloscopio comparten la misma referencia de tierra (GND) a través del conector BNC. Si conectas las dos tierras de las sondas a puntos diferentes del circuito, crearás un **cortocircuito** a través del cable de tierra del osciloscopio. Esto puede dañar los componentes o falsear las mediciones.

**Solución práctica:** Medir el voltaje de entrada y de salida **por separado** (no simultáneamente), o usar una sonda diferencial.

### Inciso f — FFT del osciloscopio

Los picos esperados en la FFT del voltaje de salida (sin filtro) están en:

| Frecuencia | Amplitud esperada (aprox.) |
|:---:|:---:|
| 0 Hz (DC) | 9.91 V |
| 120 Hz | 6.61 V |
| 240 Hz | 1.32 V |
| 360 Hz | 0.57 V |
| 480 Hz | 0.31 V |
| 600 Hz | 0.20 V |

> **No deberían aparecer** picos en 60 Hz, 180 Hz, 300 Hz, etc. (armónicos impares). Su ausencia confirma la correcta rectificación de onda completa.

### Inciso i — Medición del inductor

El puente LCR debe configurarse a $f_{prueba} = 100$ Hz (lo más cercano a 120 Hz que suelen ofrecer los instrumentos estándar). Se obtienen simultáneamente $L$ y $R_L$ (resistencia del devanado). Estos valores **reales** deben sustituirse en el script para obtener cálculos precisos.

### Inciso m — Comparación de espectros

Al agregar el filtro capacitivo, se espera:
- **El pico DC** (0 Hz) **aumenta** drásticamente (se acerca a $V_{m,red}$ en lugar de $2V_{m,red}/\pi$).
- **Los armónicos** (120 Hz, 240 Hz, etc.) **disminuyen** drásticamente en amplitud.
- La magnitud de la atenuación depende del valor de $C$ utilizado.

---

## 14. Referencias teóricas internas

Los siguientes documentos del repositorio contienen la teoría detallada que sustenta los cálculos de esta práctica:

| Documento | Contenido relevante |
|---|---|
| [Nota 6](../Nota6.md) | Rectificador tipo puente: principio de funcionamiento, cálculo completo de $V_{DC}$, $V_{rms}$, PIV, corrientes de diodo, potencias y eficiencia |
| [Nota 7](../Nota7.md) | Análisis de Fourier completo: derivación paso a paso de los coeficientes, verificación por Parseval, métricas de calidad ($FF$, $r$, $\eta$, THD), filtro inductivo y filtro capacitivo |
| [PROCEDIMIENTO_PRACTICA_1.md](PROCEDIMIENTO_PRACTICA_1.md) | Cálculos numéricos con valores específicos, instrumentos de medición por fase, y diseño del filtro capacitivo |

### Bibliografía externa

- Boylestad, R. L. & Nashelsky, L. — *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*, 11ª ed. — Cap. 2
- Rashid, M. H. — *Electrónica de Potencia*, 4ª ed. — Cap. 3
- Sedra, A. S. & Smith, K. C. — *Circuitos Microelectrónicos*, 7ª ed. — Cap. 4
