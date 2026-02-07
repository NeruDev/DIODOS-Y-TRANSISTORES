<!--
::METADATA::
type: reference
topic_id: amp-formulario
file_id: AMP-Formulario
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 04](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md) | [📁 Formularios](./)

# 📐 Formulario — Módulo 04: Amplificadores con BJT y FET

---

## 4.1 Introducción a los Amplificadores en Pequeña Señal

### Procedimiento general de análisis

1. **Análisis DC:** Determinar punto Q ($I_C$, $V_{CE}$ o $I_D$, $V_{DS}$).
2. **Calcular parámetros AC:**
   - BJT: $r_e = 26\text{ mV}/I_E$ (a 25°C)
   - FET: $g_m = g_{m0}(1 - V_{GS}/V_P)$
3. **Modelo de pequeña señal:** Reemplazar transistor por circuito equivalente AC.
4. **Análisis AC:** Calcular $A_v$, $Z_i$, $Z_o$, $A_i$.

### Convenciones AC

- Fuentes DC → cortocircuito (0V)
- Capacitores de acoplamiento/desacople → cortocircuito
- Terminales DC sin señal AC → tierra AC

### Parámetros de un amplificador

| Parámetro | Definición | Ideal (voltaje) |
|-----------|-----------|-----------------|
| $A_v = V_o/V_i$ | Ganancia de voltaje | $|A_v| \to \infty$ |
| $A_i = I_o/I_i$ | Ganancia de corriente | $|A_i| \to \infty$ |
| $Z_i$ | Impedancia de entrada | $Z_i \to \infty$ |
| $Z_o$ | Impedancia de salida | $Z_o \to 0$ |
| $A_{v_s} = A_v \cdot Z_i/(Z_i + R_s)$ | Ganancia total con fuente | — |

---

## 4.2 Amplificador con BJT

### 4.2.1 Modelo $r_e$

$$r_e = \frac{V_T}{I_E} = \frac{26 \text{ mV}}{I_E} \quad (\text{a } 25°C)$$

### Emisor común (EC) — Modelo $r_e$

| Parámetro | Sin $R_E$ bypass | Con $R_E$ (sin bypass) |
|-----------|-----------------|----------------------|
| $A_v$ | $-R_C \| R_L / r_e$ | $-R_C \| R_L / (r_e + R_E)$ |
| $Z_i$ | $R_1 \| R_2 \| \beta r_e$ | $R_1 \| R_2 \| \beta(r_e + R_E)$ |
| $Z_o$ | $R_C$ | $R_C$ |
| Fase | Inversión (180°) | Inversión (180°) |

### Base común (BC) — Modelo $r_e$

| Parámetro | Fórmula |
|-----------|---------|
| $A_v$ | $R_C \| R_L / r_e$ (sin inversión) |
| $Z_i$ | $R_E \| r_e$ |
| $Z_o$ | $R_C$ |
| Fase | Sin inversión (0°) |

### Colector común (CC / Seguidor de emisor) — Modelo $r_e$

| Parámetro | Fórmula |
|-----------|---------|
| $A_v$ | $R_E \| R_L / (r_e + R_E \| R_L) \approx 1$ |
| $Z_i$ | $R_1 \| R_2 \| \beta(r_e + R_E \| R_L)$ |
| $Z_o$ | $r_e + R_{th}/\beta$ (vista desde emisor) |
| Fase | Sin inversión (0°) |

### Resumen comparativo EC / BC / CC

| Parámetro | Emisor Común | Base Común | Colector Común |
|-----------|-------------|-----------|---------------|
| $A_v$ | Alto, negativo | Alto, positivo | ≈ 1 |
| $Z_i$ | Media | Baja ($r_e$) | Alta ($\beta R_E$) |
| $Z_o$ | Media ($R_C$) | Alta ($R_C$) | Baja ($r_e$) |
| $A_i$ | Alto ($\beta$) | ≈ 1 ($\alpha$) | Alto ($\beta + 1$) |
| Uso principal | Amplificación | RF, alta freq. | Buffer |

---

### 4.2.2 Parámetros de red de 2 puertos

$$V_1 = h_{11}I_1 + h_{12}V_2$$
$$I_2 = h_{21}I_1 + h_{22}V_2$$

| Parámetro | Fórmula | Condición |
|-----------|---------|-----------|
| $h_{11} = h_i$ | $V_1/I_1$ | $V_2 = 0$ (salida en cortocircuito AC) |
| $h_{12} = h_r$ | $V_1/V_2$ | $I_1 = 0$ (entrada abierta) |
| $h_{21} = h_f$ | $I_2/I_1$ | $V_2 = 0$ (salida en cortocircuito AC) |
| $h_{22} = h_o$ | $I_2/V_2$ | $I_1 = 0$ (entrada abierta) |

### 4.2.3 Modelo híbrido

### Fórmulas generales (modelo híbrido completo)

| Parámetro | Fórmula general |
|-----------|---------------|
| $A_v$ | $\frac{-h_f R_L}{h_i + (h_i h_o - h_f h_r)R_L}$ |
| $A_i$ | $\frac{h_f}{1 + h_o R_L}$ |
| $Z_i$ | $h_i - \frac{h_f h_r R_L}{1 + h_o R_L}$ |
| $Z_o$ | $\frac{h_i + R_s}{h_i h_o - h_f h_r + h_o R_s}$ |

### Fórmulas simplificadas (modelo híbrido aproximado: $h_r \approx 0$, $h_o \approx 0$)

| Parámetro | EC | BC | CC |
|-----------|-----|-----|-----|
| $A_v$ | $-h_{fe} R_L / h_{ie}$ | $h_{fb} R_L / h_{ib}$ | $\approx 1$ |
| $A_i$ | $h_{fe}$ | $-h_{fb} \approx -\alpha$ | $h_{fe} + 1$ |
| $Z_i$ | $h_{ie} \approx \beta r_e$ | $h_{ib} \approx r_e$ | $h_{ie} + (1+h_{fe})R_L$ |
| $Z_o$ | $1/h_{oe} \approx r_o$ | $1/h_{ob}$ | $h_{ie}/(1+h_{fe})$ |

### Valores típicos de parámetros h (emisor común, BJT de señal)

| Parámetro | Símbolo | Valor típico | Unidad |
|-----------|---------|-------------|--------|
| Impedancia de entrada | $h_{ie}$ | 1–5 kΩ | Ω |
| Fracción realimentación | $h_{re}$ | $10^{-4}$–$10^{-3}$ | — |
| Ganancia de corriente | $h_{fe}$ | 50–300 | — |
| Admitancia de salida | $h_{oe}$ | 5–50 μS | S |

### Conversión de parámetros h entre configuraciones

| De EC a: | $h_i$ | $h_r$ | $h_f$ | $h_o$ |
|---------|-------|-------|-------|-------|
| BC | $\frac{h_{ie}}{1+h_{fe}}$ | $\frac{h_{ie}h_{oe}}{1+h_{fe}} - h_{re}$ | $\frac{-h_{fe}}{1+h_{fe}}$ | $\frac{h_{oe}}{1+h_{fe}}$ |
| CC | $h_{ie}$ | $1 - h_{re}$ | $-(1+h_{fe})$ | $h_{oe}$ |

---

### 4.2.5 Efecto de $R_s$ y $R_L$

#### Ganancia total con resistencia de fuente

$$A_{v_s} = A_v \cdot \frac{Z_i}{Z_i + R_s}$$

#### Ganancia con carga

$$A_{v_L} = A_v \cdot \frac{R_L}{R_L + Z_o}$$

> **Regla práctica:** Para máxima transferencia de señal: $Z_i \gg R_s$ y $Z_o \ll R_L$.

---

## 4.3 Amplificador con JFET

### 4.3.1 Modelo del JFET en pequeña señal

Fuente de corriente controlada por voltaje:

$$i_d = g_m v_{gs}$$

Donde:

$$g_m = g_{m0}\left(1 - \frac{V_{GS}}{V_P}\right) = \frac{2}{|V_P|}\sqrt{I_{DSS} \cdot I_D}$$

$$g_{m0} = \frac{2I_{DSS}}{|V_P|}$$

### 4.3.2 Parámetros del amplificador JFET

### Fuente común (FC) — equivalente a emisor común

| Parámetro | Sin $R_S$ bypass | Con $R_S$ (sin bypass) |
|-----------|-----------------|----------------------|
| $A_v$ | $-g_m(R_D \| R_L)$ | $\frac{-g_m(R_D \| R_L)}{1 + g_m R_S}$ |
| $Z_i$ | $R_G$ (MΩ) | $R_G$ (MΩ) |
| $Z_o$ | $R_D$ | $R_D$ |
| Fase | Inversión (180°) | Inversión (180°) |

### Compuerta común (GC) — equivalente a base común

| Parámetro | Fórmula |
|-----------|---------|
| $A_v$ | $g_m(R_D \| R_L)$ (sin inversión) |
| $Z_i$ | $R_S \| (1/g_m)$ |
| $Z_o$ | $R_D$ |

### Drenador común (DC / Seguidor de fuente) — equivalente a colector común

| Parámetro | Fórmula |
|-----------|---------|
| $A_v$ | $\frac{g_m(R_S \| R_L)}{1 + g_m(R_S \| R_L)} < 1$ |
| $Z_i$ | $R_G$ (MΩ) |
| $Z_o$ | $R_S \| (1/g_m)$ |

### Resumen comparativo FC / GC / DC

| Parámetro | Fuente Común | Compuerta Común | Drenador Común |
|-----------|-------------|----------------|---------------|
| $A_v$ | Alto, negativo | Alto, positivo | ≈ 1 |
| $Z_i$ | Muy alta ($R_G$) | Baja ($1/g_m$) | Muy alta ($R_G$) |
| $Z_o$ | Media ($R_D$) | Alta ($R_D$) | Baja ($1/g_m$) |
| Uso principal | Amplificación | RF | Buffer |

---

### 4.3.3 Amplificador con MOSFET

#### MOSFET de deplexión

Mismas fórmulas que JFET (mismo modelo de pequeña señal).

#### MOSFET de enriquecimiento

$$g_m = 2k(V_{GS} - V_{T(th)}) = \frac{2I_D}{V_{GS} - V_{T(th)}}$$

Donde $k = I_{D(on)}/(V_{GS(on)} - V_{T(th)})^2$.

Las fórmulas de $A_v$, $Z_i$, $Z_o$ son idénticas a las del JFET, usando el valor de $g_m$ calculado.

---

## Valores de referencia rápida

| Parámetro | BJT (EC) | JFET (FC) | MOSFET (FC) |
|-----------|---------|----------|------------|
| $|A_v|$ típico | 50–200 | 5–20 | 5–20 |
| $Z_i$ | 1–5 kΩ | 1–10 MΩ | > 10⁹ Ω |
| $Z_o$ | 1–10 kΩ | 1–10 kΩ | 1–10 kΩ |
| Ruido | Medio | Bajo | Bajo |
| BW típico | 1–100 MHz | 1–500 MHz | 1 MHz–GHz |
