<!--
::METADATA::
type: reference
topic_id: dio-formulario-principal
file_id: Formulario_principal
status: active
audience: both
last_updated: 2026-03-25
-->

> 🏠 **Navegación:** [← Módulo 01](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md) | [📁 Formularios](./)

# 📐 Formulario: Circuitos de Aplicación con Diodos (Actualizado 2026)

Este formulario condensa las fórmulas y relaciones matemáticas principales siguiendo estrictamente el orden del temario de la asignatura para facilitar el estudio y la resolución de problemas.

---

## 1.1. Polarización y Recta de Carga

### Ecuación de Shockley (Diodo Real)
$$I_D = I_S \left( e^{V_D / nV_T} - 1 \right)$$
*   **Voltaje térmico ($V_T$):** $V_T = \frac{kT}{q} \approx 25.86 \text{ mV a 25°C (300 K } \approx \text{ 26 mV)}$

### Recta de Carga (Análisis Gráfico)
Aplicando LVK en la malla de entrada ($E, R, D$):
$$V_D = E - I_D \cdot R \implies I_D = -\frac{1}{R}V_D + \frac{E}{R}$$
*   **Punto de Q (Operación):** Intersección entre la curva del diodo y la recta.
*   **Saturación ($V_D = 0$):** $I_{D_{max}} = E/R$
*   **Corte ($I_D = 0$):** $V_{D_{max}} = E$

### Resistencias del Diodo
*   **Resistencia estática (DC):** $R_{CD} = \frac{V_{D_Q}}{I_{D_Q}}$
*   **Resistencia dinámica (AC):** $r_d = \frac{n V_T}{I_{D_Q}}$

---

## 1.2. Circuitos Serie, Paralelo y Serie–Paralelo en DC

### Configuración Serie
*   **Condición de encendido:** $E > V_K$
*   **Corriente:** $I_D = I_R = \frac{E - V_K}{R}$

### Configuración Paralelo
*   **Voltaje:** $V_{D1} = V_{D2} = V_K$
*   **Corriente Total:** $I_T = \frac{E - V_K}{R}$
*   **Distribución (Diodos iguales):** $I_{D1} = I_{D2} = \frac{I_T}{2}$

---

## 1.3. Circuitos de Aplicación (AC)

### 1.3.1. Rectificación y Filtrado

#### Parámetros Generales
*   **Relación de transformación:** $a = \frac{N_1}{N_2} = \frac{V_{pri,rms}}{V_{sec,rms}}$
*   **Voltaje pico del secundario (Total):** $V_m = V_{sec,rms} \cdot \sqrt{2}$
*   **Potencia DC (útil):** $P_{DC} = V_{DC} \cdot I_{DC} = I_{DC}^2 \cdot R_L$
*   **Potencia AC (total):** $P_{AC} = V_{rms} \cdot I_{rms} = I_{rms}^2 \cdot R_L$

#### Tabla Comparativa de Rectificadores
| Parámetro | Media Onda | Onda Completa (Puente) | O. C. (Deriv. Central) |
| :--- | :--- | :--- | :--- |
| **$V_{peak, out}$ ($V_{o,m}$)** | $V_m - V_K$ | $V_m - 2V_K$ | $V_m/2 - V_K$ |
| **Voltaje promedio ($V_{DC}$)** | $\frac{V_{o,m}}{\pi}$ | $\frac{2V_{o,m}}{\pi}$ | $\frac{2V_{o,m}}{\pi}$ |
| **Voltaje RMS ($V_{rms}$)** | $\frac{V_{o,m}}{2}$ | $\frac{V_{o,m}}{\sqrt{2}}$ | $\frac{V_{o,m}}{\sqrt{2}}$ |
| **Voltaje Inverso (PIV)** | $V_m$ | $V_m - V_K$ | $V_m - V_K$ |
| **Frecuencia rizado ($f_r$)** | $f_{in}$ | $2f_{in}$ | $2f_{in}$ |
| **Corriente RMS diodo** | $I_{rms}$ | $I_{rms}/\sqrt{2}$ | $I_{rms}/\sqrt{2}$ |

#### Métricas de Calidad
*   **Factor de forma:** $FF = \frac{V_{rms}}{V_{DC}}$ ($1.11$ para onda completa)
*   **Voltaje de rizo RMS:** $V_{r(rms)} = \sqrt{V_{rms}^2 - V_{DC}^2}$
*   **Factor de rizo:** $r = \frac{V_{r(rms)}}{V_{DC}} = \sqrt{FF^2 - 1}$ ($0.482$ para onda completa)
*   **Eficiencia:** $\eta = \frac{P_{DC}}{P_{AC}} = \frac{1}{FF^2}$ (Máx. $81.06\%$ para onda completa)

#### Análisis de Fourier (Onda Completa)
*   **Serie de Fourier:** $v_o(t) = V_{DC} - \sum_{n=1}^{\infty} \frac{4V_{o,m}}{\pi(4n^2 - 1)} \cos(2n\omega t)$
*   **Armónico dominante ($120\text{ Hz}$):** $|C_1| = \frac{4V_{o,m}}{3\pi}$

#### Filtrado de Suavizado
**A. Filtro Capacitivo (Paralelo C):**
*   **Voltaje de rizo (p-p):** $V_r \approx \frac{V_{o,m}}{f_{rizado} \cdot R_L \cdot C}$ (Válido si $RC \gg T$)
*   **Voltaje DC final:** $V_{DC} = V_{o,m} - \frac{V_r}{2}$
*   **Capacitor mínimo ($C_{min}$):** $C_{min} = \frac{1}{x \cdot f_{rizado} \cdot R_L}$, con $x = \frac{2\sqrt{3} \cdot r_{obj}}{1 + \sqrt{3} \cdot r_{obj}}$

**B. Filtro Inductivo (Serie R-L):**
*   **Impedancia armónica:** $Z_n = \sqrt{(R_L+R_{dev})^2 + (n \cdot \omega_{rizado} \cdot L)^2}$
*   **Factor de rizo de corriente:** $r_i = \frac{|C_1|}{\sqrt{2} \cdot Z_1 \cdot I_{DC}}$

---

## 1.3.2. Recortadores (Clippers)
*   **Nivel de recorte (Paralelo):** $V_{recorte} = V_{ref} \pm V_K$
*   **Recortador Serie:** $V_o = V_{in} - V_{ref} - V_K$ (cuando conduce).
*   **Condición:** Si $V_{in}$ supera el umbral de la rama, el diodo conduce y define el voltaje de salida.

---

## 1.3.3. Sujetadores (Clampers)
*   **Regla de Diseño:** $\tau = R \cdot C \gg T/2$ (Usualmente $5\tau > 10 \cdot \frac{T}{2}$)
*   **Voltaje de salida:** $V_o(t) = V_{in}(t) + V_C$
*   **Carga del Capacitor ($V_C$):** $V_C \approx V_{in,peak} - V_K$ (en el semiciclo de conducción).
*   **Sujetador Positivo:** Desplaza la señal hacia arriba ($V_o \ge 0$ si no hay bias).
*   **Sujetador Negativo:** Desplaza la señal hacia abajo ($V_o \le 0$ si no hay bias).

---

## 1.3.4. Multiplicadores de Voltaje
*   **Duplicador:** $V_o \approx 2V_m$
*   **Triplicador:** $V_o \approx 3V_m$
*   **n-uplicador:** $V_o \approx n \cdot V_m$ (donde $n$ es el número de etapas).
*   *Nota:* Cada etapa consta de 1 diodo y 1 capacitor. El PIV por diodo es $2V_m$.

---

## 1.4. Diodo Zener y Regulación

### 1.4.1. Circuitos Reguladores
**Modelo del Zener:** $V_Z = V_{z0} + I_Z \cdot r_z$

**Análisis con $R_L$ fija:**
1. **Estado del Zener:** Se retira el Zener y se calcula $V = \frac{R_L \cdot V_i}{R_L + R_S}$.
   *   Si $V \ge V_Z$: El Zener está en zona de ruptura (regula). $V_o = V_Z$.
   *   Si $V < V_Z$: El Zener está apagado. $V_o = V$.
2. **Corriente Zener:** $I_Z = I_S - I_L = \frac{V_i - V_Z}{R_S} - \frac{V_Z}{R_L}$

**Diseño de la resistencia limitadora ($R_S$):**
$$R_{S,max} = \frac{V_{i,min} - V_Z}{I_{L,max} + I_{Z,min}}$$
$$R_{S,min} = \frac{V_{i,max} - V_Z}{I_{L,min} + I_{Z,max}}$$
*   *Regla práctica:* $I_{Z,min} \approx 0.1 \cdot I_{Z,max}$ o según hoja de datos ($I_{ZK}$).

**Potencia Máxima:** $P_{Z,max} = V_Z \cdot I_{Z,max}$ (Ocurre cuando $V_i = V_{i,max}$ y $I_L = 0$).

---

## 1.5. Otros Diodos

| Diodo | Característica / Parámetro Clave | Aplicación Principal |
| :--- | :--- | :--- |
| **Schottky** | Baja $V_K$ (0.2-0.3 V), conmutación rápida ($t_{rr}$ bajo) | Fuentes conmutadas, RF, lógica rápida |
| **Varactor** | Capacidad variable con $V_R$: $C_j = \frac{C_{j0}}{(1 + V_R/V_0)^n}$ | Sintonizadores electrónicos, VCO |
| **LED** | $V_K$ alto (1.8 - 3.6 V), emisión de fotones | Indicadores, iluminación, optoacopladores |
| **Fotodiodo** | Sensible a la luz (genera $I_\lambda$ en inversa) | Sensores de luz, receptores ópticos |
| **PIN** | Resistencia variable con $I_F$ en alta frecuencia | Conmutadores RF, atenuadores |
| **Túnel** | Resistencia negativa en zona directa | Osciladores de alta frecuencia |
| **Avalancha** | Ruptura controlada para protección | Supresión de transitorios (TVS) |

### Constantes Físicas
*   **$q$ (Carga):** $1.602 \times 10^{-19}$ C
*   **$k$ (Boltzmann):** $1.38 \times 10^{-23}$ J/K
*   **$n$ (Factor de idealidad):** 1 para Ge, $\approx 2$ para Si (o según fabricante)
