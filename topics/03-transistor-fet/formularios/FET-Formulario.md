<!--
::METADATA::
type: reference
topic_id: fet-formulario
file_id: FET-Formulario
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 03](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md) | [📁 Formularios](./)

# 📐 Formulario — Módulo 03: Transistor Unipolar (FET, MOSFET)

---

## Ecuaciones Fundamentales del JFET

### Ecuación de transferencia (Shockley para FET)

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2$$

> Válida para la región de saturación (pinch-off): $V_{DS} > V_{GS} - V_P$

### Transconductancia

$$g_m = \frac{\partial I_D}{\partial V_{GS}} = g_{m0}\left(1 - \frac{V_{GS}}{V_P}\right)$$

$$g_{m0} = \frac{2 I_{DSS}}{|V_P|}$$

$$g_m = \frac{2}{|V_P|}\sqrt{I_{DSS} \cdot I_D}$$

### Relación entre $I_D$ y $V_{GS}$

| $V_{GS}/V_P$ | $I_D/I_{DSS}$ | $g_m/g_{m0}$ |
|--------------|--------------|-------------|
| 0.0 | 1.000 | 1.000 |
| −0.1 | 0.810 | 0.900 |
| −0.2 | 0.640 | 0.800 |
| −0.3 | 0.490 | 0.700 |
| −0.4 | 0.360 | 0.600 |
| −0.5 | 0.250 | 0.500 |
| −0.6 | 0.160 | 0.400 |
| −0.7 | 0.090 | 0.300 |
| −0.8 | 0.040 | 0.200 |
| −0.9 | 0.010 | 0.100 |
| −1.0 | 0.000 | 0.000 |

### Parámetros típicos JFET

| Dispositivo | Tipo | $I_{DSS}$ | $V_P$ ($V_{GS(off)}$) | $g_{m0}$ | Uso |
|------------|------|----------|----------------------|---------|-----|
| 2N5457 | N | 1–5 mA | −0.5 a −6 V | 1–5 mS | Propósito general |
| 2N5458 | N | 2–9 mA | −1 a −7 V | 1.5–5 mS | Amplificador |
| 2N5459 | N | 4–16 mA | −2 a −8 V | 2–6 mS | Amplificador |
| 2N3819 | N | 2–20 mA | −3 a −8 V | ≥ 2 mS | Propósito general |
| 2N5460 | P | 1–5 mA | +0.75 a +6 V | 1–5 mS | Audio, señal |
| J310 | N | 24–60 mA | −2 a −6.5 V | 8–20 mS | RF, VHF |

### Recta de carga DC del FET

$$V_{DS} = V_{DD} - I_D(R_D + R_S)$$

---

## 3.1.1 Polarización Fija

$$V_{GS} = -V_{GG}$$

$$I_D = I_{DSS}\left(1 + \frac{V_{GG}}{V_P}\right)^2$$

$$V_{DS} = V_{DD} - I_D R_D$$

> **Nota:** $I_G = 0$ siempre, por lo que no hay caída en $R_G$.

---

## 3.1.2 Autopolarización

$$V_{GS} = -I_D R_S$$

**Solución gráfica:** Intersección de la curva de transferencia con la recta $V_{GS} = -I_D R_S$.

**Solución analítica (sustitución):**

$$I_D = I_{DSS}\left(1 + \frac{I_D R_S}{V_P}\right)^2$$

> Se expande y resuelve como ecuación cuadrática en $I_D$.

### Selección de $R_S$

| $R_S$ | Efecto en punto Q |
|-------|-------------------|
| Pequeña | $I_D$ cercana a $I_{DSS}$, $V_{GS}$ cercano a 0 |
| Grande | $I_D$ baja, $V_{GS}$ más negativo |
| $|V_P|/I_{DSS}$ | $I_D \approx I_{DSS}/4$, $V_{GS} \approx V_P/2$ |

### Curva de polarización universal

Normalización: $m = |V_P|/(I_{DSS} \cdot R_S)$

Se grafica $I_D/I_{DSS}$ vs. $V_{GS}/V_P$ para distintos valores de $m$, y el punto Q se lee directamente.

---

## 3.2 Polarización por Divisor de Voltaje

$$V_G = V_{DD} \frac{R_2}{R_1 + R_2}$$

$$V_{GS} = V_G - I_D R_S$$

**Solución gráfica:** Intersección de la curva de transferencia con la recta $V_{GS} = V_G - I_D R_S$ (pendiente $-R_S$, intercepta eje $V_{GS}$ en $V_G$).

**Ecuaciones completas:**

$$I_D = I_{DSS}\left(1 - \frac{V_G - I_D R_S}{V_P}\right)^2$$

$$V_{DS} = V_{DD} - I_D(R_D + R_S)$$

> **Nota:** A diferencia del BJT, el divisor de voltaje en FET NO es necesariamente la configuración más estable, ya que $I_G = 0$ simplifica todas las configuraciones.

---

## 3.3 Configuración en Compuerta y Drenador Común

### Compuerta común (equivalente a base común)

$$V_{GS} = -I_D R_S + V_{entrada}$$

| Parámetro | Valor |
|-----------|-------|
| $A_v$ | $g_m R_D$ (sin inversión) |
| $Z_i$ | Baja: $R_S \| (1/g_m)$ |
| $Z_o$ | $R_D$ |

### Drenador común (seguidor de fuente)

$$V_{out} = I_D R_S$$

| Parámetro | Valor |
|-----------|-------|
| $A_v$ | $\frac{g_m R_S}{1 + g_m R_S} < 1$ |
| $Z_i$ | Muy alta (MΩ–GΩ) |
| $Z_o$ | Baja: $R_S \| (1/g_m)$ |
| Uso | Buffer de alta impedancia |

---

## 3.4 Polarización de MOSFET

### MOSFET de deplexión (Depletion — normalmente ON)

Mismas ecuaciones que el JFET:

$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2$$

> **Diferencia clave:** Puede operar con $V_{GS} > 0$ también (modo enriquecimiento).

### MOSFET de enriquecimiento (Enhancement — normalmente OFF)

$$I_D = k\left(V_{GS} - V_{T(th)}\right)^2 \quad \text{para } V_{GS} > V_{T(th)}$$

Donde $k = I_{D(on)} / (V_{GS(on)} - V_{T(th)})^2$

| Parámetro | Símbolo | Canal N típico | Canal P típico |
|-----------|---------|---------------|---------------|
| Voltaje umbral | $V_{T(th)}$ | +1 a +5 V | −1 a −5 V |
| $k$ | — | $0.1\text{–}10$ mA/V² | $0.1\text{–}10$ mA/V² |

### MOSFET comunes

| Dispositivo | Tipo | $V_{DS}$ máx | $I_D$ máx | $R_{DS(on)}$ | Uso |
|------------|------|-------------|----------|-------------|-----|
| 2N7000 | NMOS enh. | 60 V | 200 mA | 5 Ω | Señal, lógica |
| IRF540N | NMOS enh. | 100 V | 33 A | 44 mΩ | Potencia |
| IRF9540N | PMOS enh. | −100 V | −23 A | 117 mΩ | Potencia |
| BS170 | NMOS enh. | 60 V | 500 mA | 1.2 Ω | Conmutación señal |
| CD4007 | CMOS | ±7.5 V | 10 mA | — | Educativo/prototipo |

---

## 3.5 Redes Combinadas

### Circuitos con FET y BJT combinados

**Reglas de análisis:**
1. Iniciar por la etapa con parámetros más definidos (usualmente el FET, donde $I_G = 0$).
2. En cascada FET→BJT: la salida de la etapa FET ($V_{DS}$) fija el punto Q del BJT.
3. La alta $Z_i$ del FET lo hace ideal como primera etapa.

### Tabla resumen de comparación FET vs BJT

| Característica | BJT | JFET | MOSFET |
|---------------|-----|------|--------|
| Controlado por | Corriente ($I_B$) | Voltaje ($V_{GS}$) | Voltaje ($V_{GS}$) |
| $Z_i$ | Media (kΩ) | Alta (MΩ) | Muy alta (GΩ) |
| Ganancia | $\beta$ (50–300) | $g_m$ (1–20 mS) | $g_m$ (variable) |
| Ruido | Medio | Bajo | Bajo |
| Linealidad | Buena | Moderada | Moderada |
| Potencia | Alta | Baja–Media | Muy alta (potencia) |
