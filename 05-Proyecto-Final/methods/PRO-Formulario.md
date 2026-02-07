<!--
::METADATA::
type: reference
topic_id: pro-formulario
file_id: PRO-Formulario
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 05](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 📐 Formulario — Módulo 05: Proyecto Final — Fuente de Alimentación Regulada

---

## Diagrama de bloques general

```
AC ─→ [Transformador] ─→ [Rectificador] ─→ [Filtro] ─→ [Regulador] ─→ DC regulada
         ↓                    ↓                ↓              ↓
       V_sec             V_pico - nV_K     V_DC ± V_r      V_o = cte
```

---

## Etapa 1: Transformador

$$V_{sec(pico)} = V_{sec(rms)} \times \sqrt{2}$$

$$\text{Relación de vueltas:} \quad \frac{V_{pri}}{V_{sec}} = \frac{N_1}{N_2}$$

### Valores comerciales típicos de transformadores

| $V_{sec}$ (RMS) | $V_{sec}$ (pico) | Corriente | Uso típico |
|-----------------|------------------|-----------|------------|
| 6 V | 8.49 V | 0.5–2 A | Fuentes 3.3–5 V |
| 9 V | 12.73 V | 0.5–2 A | Fuentes 5–7 V |
| 12 V | 16.97 V | 0.5–3 A | Fuentes 9–12 V |
| 15 V | 21.21 V | 0.5–2 A | Fuentes 12–15 V |
| 18 V | 25.46 V | 0.5–2 A | Fuentes 15–18 V |
| 24 V | 33.94 V | 0.5–2 A | Fuentes 18–24 V |

> $V_{sec}$ con tap central: cada mitad = $V_{sec}/2$.

---

## Etapa 2: Rectificación

### Comparativa de rectificadores

| Topología | Diodos | $V_{DC}$ (sin filtro) | PIV por diodo | Rizado $f$ |
|-----------|--------|----------------------|---------------|-----------|
| Media onda | 1 | $0.318 V_p$ | $V_p$ | $f$ |
| Onda completa (tap) | 2 | $0.636 V_p$ | $2V_p$ | $2f$ |
| Puente | 4 | $0.636(V_p - 2V_K)$ | $V_p - V_K$ | $2f$ |

### Diodos rectificadores comunes

| Diodo | $V_{RRM}$ | $I_F$ (avg) | $V_F$ | Encapsulado |
|-------|----------|------------|-------|-------------|
| 1N4001 | 50 V | 1 A | 1.0 V | DO-41 |
| 1N4004 | 400 V | 1 A | 1.0 V | DO-41 |
| 1N4007 | 1000 V | 1 A | 1.0 V | DO-41 |
| 1N5401 | 100 V | 3 A | 1.0 V | DO-201AD |
| 1N5408 | 1000 V | 3 A | 1.0 V | DO-201AD |
| 6A10 | 1000 V | 6 A | 1.0 V | R-6 |
| KBP206 (puente) | 600 V | 2 A | 1.0 V | KBP |
| KBPC3510 (puente) | 1000 V | 35 A | 1.1 V | KBPC |

---

## Etapa 3: Filtrado

### Capacitor de filtro

$$V_{r(pp)} \approx \frac{I_L}{f_r \cdot C}$$

$$V_{DC} \approx V_p - V_{diodo} - \frac{V_{r(pp)}}{2}$$

### Diseño del capacitor

$$C = \frac{I_L}{f_r \cdot V_{r(pp)}}$$

> Donde $f_r = f$ (media onda) o $f_r = 2f$ (onda completa).

### Valores comerciales electrolíticos (aluminio)

| Capacitancia | Voltaje | ESR típico | Uso |
|-------------|---------|-----------|-----|
| 100 μF | 25–50 V | 0.5–2 Ω | Filtro señal |
| 470 μF | 25–50 V | 0.2–1 Ω | Filtro baja potencia |
| 1000 μF | 25–50 V | 0.1–0.5 Ω | Filtro media potencia |
| 2200 μF | 25–50 V | 0.05–0.3 Ω | Filtro media-alta |
| 4700 μF | 25–63 V | 0.03–0.2 Ω | Filtro alta potencia |
| 10000 μF | 25–50 V | 0.02–0.1 Ω | Fuentes de potencia |

---

## Etapa 4a: Regulador Transistorizado (5.1.1)

### Regulador serie con Zener (circuito básico)

```
Vi ──[Rs]──┬── Base(Q1) ── C → Vo
           │              E ↓
          [Dz]            [RL]
           │               │
          GND             GND
```

$$V_o = V_Z - V_{BE} \approx V_Z - 0.7\text{ V}$$

$$I_L = \frac{V_o}{R_L}$$

$$I_C \approx I_E = I_L + I_{bias}$$

$$I_{R_S} = I_Z + I_B = I_Z + \frac{I_C}{\beta}$$

### Regulador serie con amplificador de error

```
Vi ──── Q1(paso) ──── Vo
         │B
    [Amplificador] ← V_ref (Zener)
    [  de error  ] ← V_muestra (divisor R1/R2)
```

$$V_o = V_Z \left(1 + \frac{R_1}{R_2}\right)$$

### Regulación de línea

$$\%Reg_{línea} = \frac{\Delta V_o}{\Delta V_i} \times 100\%$$

### Regulación de carga

$$\%Reg_{carga} = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\%$$

> Donde $V_{NL}$ = voltaje sin carga, $V_{FL}$ = voltaje a plena carga.

### Protección contra cortocircuito (limitación de corriente)

$$R_{SC} = \frac{V_{BE(Q2)}}{I_{L(max)}} \approx \frac{0.7\text{ V}}{I_{L(max)}}$$

---

## Etapa 4b: Regulador con Circuito Integrado (5.1.2)

### Familia 78xx / 79xx (reguladores fijos)

| Regulador | $V_o$ | Polaridad | $I_o$ máx | $V_{dropout}$ | $V_i$ rango |
|-----------|------|-----------|----------|--------------|-------------|
| 7805 | +5 V | Positiva | 1.5 A | 2 V | 7–25 V |
| 7809 | +9 V | Positiva | 1.5 A | 2 V | 11–25 V |
| 7812 | +12 V | Positiva | 1.5 A | 2 V | 14–30 V |
| 7815 | +15 V | Positiva | 1.5 A | 2 V | 17–30 V |
| 7905 | −5 V | Negativa | 1.5 A | 2 V | −7 a −25 V |
| 7912 | −12 V | Negativa | 1.5 A | 2 V | −14 a −30 V |

**Condición de operación:**

$$V_i \geq V_o + V_{dropout}$$

> **Ejemplo:** Para 7805: $V_i \geq 5 + 2 = 7\text{ V mínimo}$.

### Capacitores recomendados (datasheet)

| Ubicación | Valor | Propósito |
|-----------|-------|-----------|
| $C_i$ (entrada) | 0.33 μF (cerámico) | Prevenir oscilaciones si lejos del filtro |
| $C_o$ (salida) | 0.1 μF (cerámico) | Mejorar respuesta transitoria |
| $C_{grande}$ (entrada) | 1000–4700 μF (electrolítico) | Filtro principal |

### Reguladores ajustables

| Regulador | $V_o$ rango | Polaridad | $I_o$ máx | $V_{ref}$ |
|-----------|------------|-----------|----------|----------|
| LM317 | +1.25 a +37 V | Positiva | 1.5 A | 1.25 V |
| LM337 | −1.25 a −37 V | Negativa | 1.5 A | −1.25 V |
| LM350 | +1.25 a +33 V | Positiva | 3 A | 1.25 V |

### Fórmula del LM317

$$V_o = V_{ref}\left(1 + \frac{R_2}{R_1}\right) + I_{adj} \cdot R_2$$

Donde $V_{ref} = 1.25\text{ V}$ e $I_{adj} \approx 50\text{ μA}$ (despreciable si $R_2$ no es muy grande).

**Simplificado:**

$$V_o \approx 1.25\left(1 + \frac{R_2}{R_1}\right)$$

**Valor estándar:** $R_1 = 240\text{ Ω}$ (recomendado por datasheet para $I_{adj}$ mínimo de 3.5 mA).

### Tabla de diseño rápido LM317 ($R_1 = 240$ Ω)

| $V_o$ deseado | $R_2$ calculado | $R_2$ comercial |
|--------------|----------------|----------------|
| 1.25 V | 0 Ω | 0 (puente) |
| 3.3 V | 394 Ω | 390 Ω |
| 5 V | 720 Ω | 680 Ω |
| 9 V | 1488 Ω | 1.5 kΩ |
| 12 V | 2064 Ω | 2 kΩ |
| 15 V | 2640 Ω | 2.7 kΩ |
| 24 V | 4368 Ω | 4.3 kΩ |

---

## Diseño completo — Lista de verificación

| Etapa | Parámetro a definir | Fórmula / criterio |
|-------|--------------------|--------------------|
| 1. Transformador | $V_{sec}$ | $V_{sec(pico)} > V_o + V_{dropout} + V_{rizado}/2 + V_{diodo}$ |
| 2. Rectificador | Tipo, PIV diodos | PIV > $V_{pico}$ con margen 50% |
| 3. Filtro | Capacitor $C$ | $C = I_L / (f_r \cdot V_{r(pp)})$ |
| 4. Regulador | Tipo, disipación | $P_D = (V_i - V_o) \cdot I_o$ |
| 5. Disipador | $R_{θ(sa)}$ | $R_{θ(ja)} = (T_{j(max)} - T_a) / P_D$ |
| 6. Protección | Fusible, $R_{SC}$ | $I_{fusible} > 1.5 \times I_{L(max)}$ |

### Disipación térmica del regulador

$$P_D = (V_{in} - V_{out}) \times I_{out}$$

$$T_j = T_a + P_D \times R_{\theta(ja)}$$

> $T_{j(max)}$ = 125°C (típico para 78xx). Si $P_D > 1\text{ W}$, usar disipador.

### Resistencias térmicas típicas (TO-220)

| Condición | $R_{\theta}$ |
|-----------|-------------|
| Unión a cápsula ($R_{θ(jc)}$) | 3–5 °C/W |
| Cápsula a disipador ($R_{θ(cs)}$) | 0.5–1 °C/W (con pasta) |
| Disipador a ambiente ($R_{θ(sa)}$) | Depende del disipador |
| Sin disipador ($R_{θ(ja)}$) | 50–65 °C/W |
