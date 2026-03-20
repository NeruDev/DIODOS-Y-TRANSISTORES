<!--
::METADATA::
type: theory
topic_id: rectificador-media-onda-transformador
file_id: Nota4
status: stable
audience: student
last_updated: 2026-02-23
-->

> 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md) | [🔙 Notas DIO](README.md)

---

# Rectificador de Media Onda con Transformador Reductor

## Datos del circuito

| Parámetro | Valor |
|-----------|-------|
| Voltaje primario | $V_p = 120\,\text{V}_{rms}$, $f = 60\,\text{Hz}$ |
| Relación de vueltas | $N_p : N_s = 10 : 1$ |
| Resistencia de carga | $R_L = 5\,\Omega$ |
| Modelo de diodo | Ideal ($V_D = 0\,\text{V}$) / Real ($V_D = 0.7\,\text{V}$) |

---

## 1. El transformador: reducción de voltaje

El transformador es el primer componente del circuito. Su función es reducir el voltaje de la línea de 120 V a un nivel apropiado para la carga. La relación fundamental que rige su operación es:

$$\frac{N_p}{N_s} = \frac{V_p}{V_s}$$

donde $N_p$ y $N_s$ son el número de vueltas en el devanado primario y secundario, respectivamente, y $V_p$, $V_s$ son los voltajes correspondientes.

Despejando el voltaje en el secundario:

$$V_s = \frac{N_s}{N_p} \cdot V_p = \frac{1}{10} \times 120\,\text{V} = 12\,\text{V}_{rms}$$

El voltaje pico asociado es:

$$V_{s,pico} = V_s \cdot \sqrt{2} = 12\sqrt{2} \approx 16.97\,\text{V}$$

> **Nota:** La relación de vueltas aplica a valores rms y a valores pico por igual, ya que es una relación de amplitudes.

---

## 2. El diodo como elemento rectificador

El **diodo de silicio** es un dispositivo semiconductor de unión P-N cuya característica esencial es la conducción unidireccional:

- **Semiciclo positivo** ($v_s > V_D$): el diodo está **polarizado en directa** (ánodo más positivo que cátodo). La corriente fluye y el voltaje aparece sobre $R_L$.
- **Semiciclo negativo** ($v_s < 0$): el diodo está **polarizado en inversa** (actúa como circuito abierto). No circula corriente por la carga.

El voltaje instantáneo en la salida del rectificador con diodo real es:

$$v_o(t) = \begin{cases} v_s(t) - V_D & \text{si } v_s(t) > V_D \\ 0 & \text{si } v_s(t) \leq V_D \end{cases}$$

Esto produce una **señal pulsante unipolar** — la parte negativa de la senoide queda eliminada.

---

## 3. Análisis completo — Diodo ideal

> **Modelo utilizado:** diodo ideal ($V_D = 0\,\text{V}$). Esto simplifica los cálculos y es el enfoque estándar en ejercicios de introducción a la rectificación. Al final de la sección se incluye la comparación con el modelo real ($V_D = 0.7\,\text{V}$).

---

### a) Voltaje pico

El secundario entrega $V_s = 12\,\text{V}_{rms}$. Para una señal senoidal, el valor pico se obtiene como:

$$V_m = \sqrt{2}\, V_s = \sqrt{2} \times 12\,\text{V} = 16.97\,\text{V}$$

---

### b) Voltaje promedio (DC)

En el rectificador de media onda solo conduce un semiciclo completo por período. Integrando la senoide sobre $[0, \pi]$ y normalizando por el período $2\pi$:

$$V_{DC} = \frac{V_m}{\pi}$$

$$V_{DC} = \frac{16.97}{\pi} = \mathbf{5.4\,\text{V}}$$

---

### c) Corriente promedio (DC)

La corriente media circulante por $R_L$ se obtiene directamente por la ley de Ohm aplicada al valor promedio:

$$I_{DC} = \frac{V_{DC}}{R_L} = \frac{V_m}{\pi\, R_L}$$

$$I_{DC} = \frac{16.97}{\pi \times 5} = \mathbf{1.08\,\text{A}}$$

---

### d) Voltaje RMS de salida

El voltaje RMS de salida **no es igual al RMS de entrada**. Al eliminar el semiciclo negativo, la energía se reduce a la mitad, y la integral cuadrática sobre el período completo da:

$$V_{rms} = \frac{V_m}{2}$$

$$V_{rms} = \frac{16.97}{2} = \mathbf{8.49\,\text{V}}$$

> **No confundir** $V_{rms} = 8.49\,\text{V}$ (salida del rectificador) con $V_s = 12\,\text{V}_{rms}$ (entrada). Son distintos porque la forma de onda cambió al eliminar los semiciclos negativos.

---

### e) Corriente RMS de carga

Aplicando la ley de Ohm sobre el valor RMS:

$$I_{rms} = \frac{V_{rms}}{R_L} = \frac{V_m}{2\,R_L}$$

$$I_{rms} = \frac{16.97}{2 \times 5} = \frac{16.97}{10} = \mathbf{1.69\,\text{A}}$$

> La corriente RMS es mayor que la corriente promedio ($1.08\,\text{A}$) porque el RMS pondera el efecto energético real. Es la magnitud relevante para calcular la **potencia disipada** en $R_L$.

---

### f) Voltaje de rizo RMS

El **voltaje de rizo** ($V_r$) es la componente alterna residual en la salida — todo lo que no es DC puro. Se calcula como:

$$V_{r(rms)} = \sqrt{V_{rms}^2 - V_{DC}^2}$$

$$V_{r(rms)} = \sqrt{(8.49)^2 - (5.4)^2} = \sqrt{72.08 - 29.16} = \sqrt{42.92} \approx \mathbf{6.55\,\text{V}}$$

Para el rectificador de media onda sin filtro, existe la relación simplificada:

$$V_{r(rms)} \approx 1.21\, V_{DC} = 1.21 \times 5.4 = \mathbf{6.53\,\text{V}}$$

> **Interpretación:** la salida tiene $5.4\,\text{V}$ de componente DC y $6.53\,\text{V}$ de rizo. El rizo **supera** a la componente continua, lo que evidencia que sin filtrado este circuito es una fuente DC de calidad muy baja. El **factor de rizo** es $r = V_{r(rms)}/V_{DC} = 1.21$ (121%), característico de la media onda no filtrada.

---

### g) Corriente RMS del diodo

En el rectificador de media onda el diodo y la resistencia de carga están en **serie**: la corriente que circula por el diodo durante el semiciclo positivo es exactamente la misma que circula por $R_L$. No existen ramas paralelas ni caminos alternativos:

$$I_{D(rms)} = I_{o(rms)} = \frac{V_m}{2\,R_L} = \mathbf{1.69\,\text{A}}$$

> Este valor es relevante para la **selección del diodo**: la hoja de datos del componente debe especificar una corriente RMS (o una corriente media de conducción) superior a $1.69\,\text{A}$.

---

### Tensión inversa de pico (PIV / PRV)

La **tensión inversa de pico** — también designada como $V_{PRD}$ (Voltaje Pico Repetitivo del Diodo) o PIV — es el máximo voltaje inverso que el diodo debe soportar. Ocurre cuando $v_s$ alcanza su valor más negativo y toda esa tensión cae sobre el diodo:

$$\text{PIV} = |V_{PRD}| = V_m = 12\sqrt{2} \approx 16.97\,\text{V}$$

> **Convención de signo:** el valor del PIV siempre se reporta como magnitud positiva. El signo negativo en la expresión $v_D = -V_m$ durante el semiciclo inverso únicamente indica polaridad; el parámetro de diseño es $|V_{PRD}| = 16.97\,\text{V}$. El diodo debe tener $V_{BR} > \text{PIV}$, con margen (típicamente $V_{BR} \geq 2 \times \text{PIV}$ en diseños reales).

---

### Resumen de parámetros (diodo ideal)

| Parámetro | Símbolo | Expresión | Valor |
|-----------|---------|-----------|-------|
| Voltaje pico | $V_m$ | $\sqrt{2}\,V_s$ | $\mathbf{16.97\,\text{V}}$ |
| Voltaje promedio DC | $V_{DC}$ | $V_m / \pi$ | $\mathbf{5.4\,\text{V}}$ |
| Corriente promedio DC | $I_{DC}$ | $V_m / (\pi R_L)$ | $\mathbf{1.08\,\text{A}}$ |
| Voltaje RMS de salida | $V_{rms}$ | $V_m / 2$ | $\mathbf{8.49\,\text{V}}$ |
| Corriente RMS de carga | $I_{rms}$ | $V_m / (2 R_L)$ | $\mathbf{1.69\,\text{A}}$ |
| Corriente RMS del diodo | $I_{D(rms)}$ | $= I_{rms}$ (serie) | $\mathbf{1.69\,\text{A}}$ |
| Voltaje de rizo RMS | $V_{r(rms)}$ | $1.21\,V_{DC}$ | $\mathbf{6.53\,\text{V}}$ |
| Tensión inversa de pico | PIV | $V_m$ | $\mathbf{16.97\,\text{V}}$ |

---

### Validación del modelo: ¿diodo ideal o real?

Todos los cálculos anteriores corresponden al **modelo de diodo ideal** ($V_D = 0\,\text{V}$). Las razones que lo confirman son:

1. **No se restó la caída de umbral al pico.** Con diodo real: $V_m^{(real)} = 16.97 - 0.7 = 16.27\,\text{V}$. Esa reducción propaga diferencias en todos los parámetros derivados.
2. **El voltaje promedio no incluye corrección.** Con diodo real: $V_{DC} = (V_m - 0.7)/\pi$.
3. **No se consideró resistencia dinámica** del diodo ($r_d = V_T/I_Q$), que introduciría una caída dependiente de corriente.
4. **No se consideró corriente inversa de saturación** ($I_S$), despreciable pero no nula en un dispositivo real.
5. **No se consideró caída dependiente de corriente** (modelo de Shockley: $i_D = I_S(e^{v_D/nV_T}-1)$).

Este modelo es el estándar en ejercicios introductorios. Las diferencias numéricas frente al modelo real son pequeñas (ver tabla siguiente), pero se vuelven significativas en aplicaciones de alta corriente o precisión.

---

### Comparación: diodo ideal vs. diodo real ($V_D = 0.7\,\text{V}$)

| Parámetro | Diodo ideal | Diodo real |
|-----------|------------|-----------|
| $V_m$ | $16.97\,\text{V}$ | $16.27\,\text{V}$ |
| $V_{DC}$ | $5.40\,\text{V}$ | $5.18\,\text{V}$ |
| $I_{DC}$ | $1.08\,\text{A}$ | $1.04\,\text{A}$ |
| $V_{rms}$ | $8.49\,\text{V}$ | $8.14\,\text{V}$ |
| $I_{rms}$ | $1.69\,\text{A}$ | $1.63\,\text{A}$ |

---

## 4. Esquemático del circuito

![Esquemático: rectificador de media onda con transformador 10:1 y RL = 5 Ω](../media/generated/nota4_circuito.png)

*Circuito rectificador de media onda: fuente de 120 V / 60 Hz → transformador 10:1 → diodo → $R_L = 5\,\Omega$.*

---

## 5. Formas de onda — diodo ideal

![Voltajes principales del rectificador de media onda (diodo ideal)](../media/generated/nota4_voltajes_ideales.png)

Las tres señales están graficadas en función de $\omega t$ (un ciclo completo de $0$ a $2\pi$):

1. **$v_s(\omega t)$** — señal senoidal completa del secundario del transformador. Oscila entre $+V_m = +16.97\,\text{V}$ y $-V_m = -16.97\,\text{V}$. Valor RMS: $12\,\text{V}$.

2. **$v_o(\omega t)$** — salida del rectificador con diodo ideal. Durante $[0,\pi]$ el diodo conduce y $v_o = v_s$; durante $[\pi, 2\pi]$ el diodo bloquea y $v_o = 0$. Se indican $V_{DC} = 5.4\,\text{V}$ (naranja), $V_{rms} = 8.49\,\text{V}$ (morado) y el voltaje de rizo $V_r = 6.53\,\text{V}$.

3. **$v_D(\omega t)$** — tensión en el diodo. En conducción cae $0\,\text{V}$ (ideal). En bloqueo aparece toda la tensión inversa: $v_D = -v_s$, con un pico de $V_{PRV} = 16.97\,\text{V}$ que el componente debe soportar.

---

## 6. Formas de onda — diodo real ($V_D = 0.7\,\text{V}$)

![Formas de onda con diodo real y tabla de parámetros](../media/generated/nota4_formas_onda.png)

*Mismo análisis con el modelo de diodo real ($V_D = 0.7\,\text{V}$). El voltaje pico de salida se reduce a $V_{o,m} = 16.27\,\text{V}$ y el promedio a $V_{o,avg} = 5.18\,\text{V}$. La tabla incluye los valores calculados en ambas condiciones.*

---

## 7. Resumen del circuito

El circuito implementa las siguientes tres etapas de procesamiento de señal:

1. **Reducción de voltaje** — el transformador baja 120 V AC a 12 V AC mediante la relación de vueltas 10:1.
2. **Rectificación de media onda** — el diodo elimina los semiciclos negativos, entregando pulsos positivos de tensión sobre $R_L$.
3. **Disipación de potencia** — la resistencia $R_L = 5\,\Omega$ convierte la corriente pulsante en potencia útil.

El resultado es una **señal DC pulsante** con un factor de rizo del 121%, lo que evidencia que sin filtrado la calidad de la rectificación es baja. El voltaje de rizo ($6.53\,\text{V}$) supera al voltaje DC ($5.4\,\text{V}$), convirtiendo este circuito en el punto de partida teórico que justifica la necesidad de un **filtro capacitivo** como siguiente etapa de diseño.

---

## Ver también

- [DIO-03 — Rectificación y Filtrado](../theory/DIO-03-Teoria-Rectificacion-Filtrado.md)
- [DIO-07 — Diodo Zener (regulación)](../theory/DIO-07-Teoria-Diodo-Zener.md)
- [Nota3.md — Rectificador de Media Onda básico](Nota3.md)
