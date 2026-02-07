<!--
::METADATA::
type: reference
topic_id: bjt-formulario
file_id: BJT-Formulario
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 02](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 📐 Formulario — Módulo 02: Transistor Bipolar (BJT)

---

## 2.1 Características, Parámetros y Punto de Operación

### Relaciones fundamentales de corriente

$$I_E = I_C + I_B$$

$$I_C = \beta \, I_B = \alpha \, I_E$$

$$\alpha = \frac{\beta}{1 + \beta} \qquad \beta = \frac{\alpha}{1 - \alpha}$$

### Parámetros típicos

| Parámetro | Símbolo | NPN típico | PNP típico |
|-----------|---------|-----------|-----------|
| Ganancia de corriente DC | $\beta$ / $h_{FE}$ | 50–300 | 50–300 |
| Voltaje umbral B-E | $V_{BE(on)}$ | 0.7 V (Si) | −0.7 V (Si) |
| Voltaje de saturación C-E | $V_{CE(sat)}$ | 0.1–0.3 V | −0.1 a −0.3 V |
| Voltaje de saturación B-E | $V_{BE(sat)}$ | 0.8 V | −0.8 V |
| Corriente de fuga | $I_{CEO}$ | nA–μA | nA–μA |

### Recta de carga DC

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

**Puntos de intersección:**
- Eje $V_{CE}$: $I_C = 0 \Rightarrow V_{CE} = V_{CC}$
- Eje $I_C$: $V_{CE} = 0 \Rightarrow I_C = \frac{V_{CC}}{R_C + R_E}$

### Transistores BJT comunes

| Transistor | Tipo | $\beta$ típico | $I_C$ máx | $V_{CEO}$ máx | $P_D$ máx | Uso |
|-----------|------|-------------|----------|-------------|----------|-----|
| 2N2222A | NPN | 100–300 | 800 mA | 40 V | 500 mW | Propósito general |
| 2N3904 | NPN | 100–300 | 200 mA | 40 V | 625 mW | Señal pequeña |
| 2N3906 | PNP | 100–300 | 200 mA | 40 V | 625 mW | Complemento 2N3904 |
| BC547 | NPN | 110–800 | 100 mA | 45 V | 500 mW | Señal/audio |
| BC557 | PNP | 110–800 | 100 mA | 45 V | 500 mW | Complemento BC547 |
| TIP31C | NPN | 10–50 | 3 A | 100 V | 40 W | Potencia media |
| TIP32C | PNP | 10–50 | 3 A | 100 V | 40 W | Complemento TIP31C |
| 2N3055 | NPN | 20–70 | 15 A | 60 V | 115 W | Potencia alta |

---

## 2.2.1 Polarización en Emisor Común

### Polarización fija

$$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$

$$I_C = \beta \, I_B$$

$$V_{CE} = V_{CC} - I_C R_C$$

> **Estabilidad:** MUY dependiente de $\beta$. $S(\beta) = I_{C1}/\beta_1$ (el peor caso).

### Polarización de emisor (con $R_E$)

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$

$$I_C = \beta \, I_B$$

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

> **Estabilidad:** Moderada. La realimentación por $R_E$ mejora la estabilidad.

### Polarización por divisor de voltaje (la más estable)

**Método exacto (Thévenin):**

$$R_{th} = R_1 \| R_2 = \frac{R_1 R_2}{R_1 + R_2}$$

$$V_{th} = V_{CC} \frac{R_2}{R_1 + R_2}$$

$$I_B = \frac{V_{th} - V_{BE}}{R_{th} + (\beta + 1)R_E}$$

**Método aproximado** (válido si $\beta R_E \gg 10 R_2$ o $R_{th} \ll \beta R_E$):

$$V_B \approx V_{CC} \frac{R_2}{R_1 + R_2}$$

$$I_E \approx \frac{V_B - V_{BE}}{R_E}$$

$$I_C \approx I_E$$

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

### Polarización por realimentación de colector

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)}$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C R_C - I_B R_B \approx V_{CC} - I_C(R_C + R_E)$$

---

## 2.2.2 Polarización en Base Común

$$I_E = \frac{V_{EE} - V_{BE}}{R_E}$$

$$I_C = \alpha \, I_E$$

$$V_{CB} = V_{CC} - I_C R_C$$

| Parámetro | Valor típico |
|-----------|-------------|
| $A_v$ | Alto (sin inversión) |
| $Z_i$ | Baja (~$r_e$) |
| $Z_o$ | Alta |
| Uso | Alta frecuencia, RF |

---

## 2.2.3 Polarización en Colector Común (seguidor de emisor)

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$

$$V_E = I_E R_E \approx V_B - V_{BE}$$

$$V_{CE} = V_{CC} - I_E R_E$$

| Parámetro | Valor típico |
|-----------|-------------|
| $A_v$ | ≈ 1 (sin inversión) |
| $Z_i$ | Alta ($\beta R_E$) |
| $Z_o$ | Baja ($r_e + R_B/\beta$) |
| Uso | Buffer, acoplamiento de impedancias |

---

## 2.3 Conmutación

### Condiciones de operación

| Estado | Región | $V_{BE}$ | $I_C$ | $V_{CE}$ |
|--------|--------|---------|-------|---------|
| OFF (corte) | Corte | $< 0.5$ V | ≈ 0 | $\approx V_{CC}$ |
| ON (saturación) | Saturación | ≈ 0.8 V | $V_{CC}/(R_C + R_E)$ | $V_{CE(sat)} \approx 0.2$ V |

### Resistencia mínima de base para saturación

$$I_{B(sat)} = \frac{I_{C(sat)}}{\beta} = \frac{V_{CC} - V_{CE(sat)}}{\beta(R_C + R_E)}$$

$$R_{B(max)} = \frac{V_{CC} - V_{BE(sat)}}{I_{B(sat)}}$$

> **En diseño práctico,** se usa un factor de sobredimensionamiento: $I_B = (2\text{–}5) \times I_{B(sat)}$ para asegurar saturación.

### Tiempos de conmutación

| Parámetro | Símbolo | Valor típico (2N2222) |
|-----------|---------|----------------------|
| Tiempo de retardo | $t_d$ | 10 ns |
| Tiempo de subida | $t_r$ | 25 ns |
| Tiempo de almacenamiento | $t_s$ | 225 ns |
| Tiempo de bajada | $t_f$ | 60 ns |
| Tiempo de encendido | $t_{on} = t_d + t_r$ | 35 ns |
| Tiempo de apagado | $t_{off} = t_s + t_f$ | 285 ns |

---

## 2.4 Estabilidad

### Factores de estabilidad

$$S(I_{CO}) = \frac{\partial I_C}{\partial I_{CO}}$$

$$S(\beta) = \frac{\partial I_C}{\partial \beta}$$

$$S(V_{BE}) = \frac{\partial I_C}{\partial V_{BE}}$$

### Variación total de $I_C$

$$\Delta I_C = S(I_{CO})\Delta I_{CO} + S(\beta)\Delta\beta + S(V_{BE})\Delta V_{BE}$$

### Factores de estabilidad por configuración

| Configuración | $S(I_{CO})$ | $S(\beta)$ | $S(V_{BE})$ | Estabilidad |
|---------------|------------|-----------|------------|-------------|
| Polarización fija | $\beta + 1$ | $I_{C1}/\beta_1$ | $-\beta/R_B$ | ❌ Mala |
| Con $R_E$ | $\frac{\beta+1}{1+\beta R_E/(R_B+R_E)}$ | — | — | ⚠️ Regular |
| Divisor de voltaje | $\frac{(\beta+1)(1+R_{th}/R_E)}{(\beta+1)+R_{th}/R_E}$ | $\frac{I_{C1}(\beta_2-\beta_1)}{\beta_2(\beta_1+\frac{R_{th}}{R_E}+1)}$ | $\frac{-\beta}{R_{th}+(\beta+1)R_E}$ | ✅ Buena |
| Realimentación colector | $\frac{\beta+1}{1+\beta R_C/R_B}$ | — | — | ⚠️ Regular |

> **Regla práctica:** $S(I_{CO})$ ideal = 1 (inalcanzable). Valores $< 10$ se consideran aceptables.

### Variaciones con temperatura

| Parámetro | Comportamiento |
|-----------|---------------|
| $\beta$ | ↑ con temperatura (≈ +1%/°C) |
| $V_{BE}$ | ↓ con temperatura (−2.5 mV/°C) |
| $I_{CO}$ | Se duplica cada ~10°C |
