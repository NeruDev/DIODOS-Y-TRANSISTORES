<!--
::METADATA::
type: reference
topic_id: dio-formulario
file_id: DIO-Formulario
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 01](../00-Index.md) | [📋 Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# 📐 Formulario — Módulo 01: Circuitos de Aplicación con Diodos

---

## 1.1 Polarización y Recta de Carga

### Ecuación de Shockley

$$I_D = I_S\left(e^{V_D / nV_T} - 1\right)$$

| Símbolo | Descripción | Valor típico |
|---------|-------------|-------------|
| $I_S$ | Corriente de saturación inversa | $10^{-12}$ A (Si), $10^{-6}$ A (Ge) |
| $n$ | Factor de idealidad | 1 (Ge), 1–2 (Si) |
| $V_T$ | Voltaje térmico ($kT/q$) | 25.86 mV @ 25°C |
| $V_K$ | Voltaje de umbral | 0.7 V (Si), 0.3 V (Ge) |

### Voltaje térmico

$$V_T = \frac{kT}{q}$$

| Constante | Valor |
|-----------|-------|
| $k$ (Boltzmann) | $1.381 \times 10^{-23}$ J/K |
| $q$ (carga electrón) | $1.602 \times 10^{-19}$ C |

### Resistencia dinámica del diodo

$$r_d = \frac{nV_T}{I_D} \approx \frac{26 \text{ mV}}{I_D}$$

### Recta de carga (circuito serie R-diodo)

$$V_{CC} = V_D + I_D \cdot R$$

Puntos de intersección:
- Eje $V$: $V_D = V_{CC}$, $I_D = 0$
- Eje $I$: $V_D = 0$, $I_D = V_{CC}/R$

### Modelos del diodo

| Modelo | Directa | Inversa |
|--------|---------|---------|
| Ideal | Cortocircuito ($V_D = 0$) | Circuito abierto ($I_D = 0$) |
| Aproximado | $V_D = V_K$ | Circuito abierto |
| Completo | $V_D = V_K + I_D \cdot r_d$ | $I_D = -I_S$ |

### Efecto de la temperatura

| Parámetro | Comportamiento con ↑T |
|-----------|-----------------------|
| $V_K$ | Disminuye ~2.5 mV/°C |
| $I_S$ | Se duplica cada ~10°C |
| $r_d$ | Disminuye (más corriente) |

---

## 1.2 Circuitos Serie, Paralelo, Serie-Paralelo en DC

### Diodos en serie (polarización directa)

$$V_{total} = V_{K1} + V_{K2} + \cdots + V_{Kn}$$

$$I_D = \frac{V_{CC} - (V_{K1} + V_{K2} + \cdots)}{R}$$

### Diodos en paralelo (ideales idénticos)

$$I_{total} = I_{D1} + I_{D2} + \cdots$$

> **Nota práctica:** En la realidad, los diodos nunca son perfectamente idénticos. Se usan resistencias de ecualización para distribuir la corriente.

### Análisis de circuitos con múltiples diodos

**Procedimiento:**
1. Asumir estado de cada diodo (ON/OFF).
2. Sustituir modelo (corto/$V_K$/abierto).
3. Resolver el circuito resultante.
4. Verificar consistencia (corriente positiva en directa, voltaje negativo en inversa).
5. Si no es consistente, cambiar la suposición y repetir.

---

## 1.3.1 Rectificación y Filtrado

### Rectificador de media onda

| Parámetro | Fórmula |
|-----------|---------|
| $V_{DC}$ (sin filtro) | $V_{DC} = \frac{V_p}{\pi} \approx 0.318 \, V_p$ |
| $V_{DC}$ (con $V_K$) | $V_{DC} = \frac{V_p - V_K}{\pi}$ |
| PIV (voltaje inverso pico) | $V_{PIV} = V_p$ |
| Frecuencia de rizado | $f_r = f_{entrada}$ |
| Rizado (con filtro C) | $V_{r(pp)} \approx \frac{V_p}{f R_L C}$ |
| $V_{DC}$ (con filtro C) | $V_{DC} \approx V_p - \frac{V_{r(pp)}}{2}$ |

### Rectificador de onda completa (tap central)

| Parámetro | Fórmula |
|-----------|---------|
| $V_{DC}$ (sin filtro) | $V_{DC} = \frac{2V_p}{\pi} \approx 0.636 \, V_p$ |
| PIV | $V_{PIV} = 2V_p - V_K$ |
| Frecuencia de rizado | $f_r = 2f_{entrada}$ |
| Rizado (con filtro C) | $V_{r(pp)} \approx \frac{V_p}{2 f R_L C}$ |

### Rectificador puente (4 diodos)

| Parámetro | Fórmula |
|-----------|---------|
| $V_{DC}$ (sin filtro) | $V_{DC} = \frac{2(V_p - 2V_K)}{\pi}$ |
| PIV por diodo | $V_{PIV} = V_p - V_K$ |
| Frecuencia de rizado | $f_r = 2f_{entrada}$ |
| Rizado (con filtro C) | $V_{r(pp)} \approx \frac{V_p - 2V_K}{2 f R_L C}$ |

### Factor de rizado

$$r = \frac{V_{r(rms)}}{V_{DC}} \times 100\%$$

### Valores típicos estándar de capacitores de filtro

| Aplicación | Capacitor típico | Rizado resultante |
|------------|-----------------|-------------------|
| Fuente baja potencia (< 100 mA) | 100–470 μF | < 5% |
| Fuente media potencia (100 mA–1 A) | 1000–4700 μF | < 2% |
| Fuente alta potencia (> 1 A) | 4700–10000 μF | < 1% |

---

## 1.3.2 Recortadores

### Recortador serie

| Configuración | Salida cuando diodo ON | Salida cuando diodo OFF |
|---------------|----------------------|------------------------|
| Ánodo a entrada, sin bias | $V_o = V_i - V_K$ (Si) | $V_o = 0$ |
| Con fuente de bias $V_R$ | $V_o = V_i - V_K$ cuando $V_i > V_R + V_K$ | $V_o = 0$ |

### Recortador paralelo (shunt)

| Configuración | Nivel de recorte | Salida recortada |
|---------------|-----------------|------------------|
| Sin bias, diodo a tierra | $V_K$ (diodo Si) | $V_o \approx V_K$ |
| Con bias $+V_R$ | $V_R + V_K$ | $V_o \approx V_R + V_K$ |
| Con bias $-V_R$ | $-V_R + V_K$ | $V_o \approx V_K - V_R$ |
| Diodo invertido, sin bias | $-V_K$ | $V_o \approx -V_K$ |

---

## 1.3.3 Sujetadores

### Reglas de análisis

1. El capacitor se carga al valor pico durante el primer semiciclo (diodo ON).
2. Una vez cargado, el capacitor no se descarga (asumiendo $RC \gg T$).
3. La tensión del capacitor se suma/resta a la señal de entrada.

### Sujetador positivo (desplaza hacia arriba)

$$V_o(t) = V_i(t) + V_C$$

| Tipo | $V_C$ (carga del capacitor) | Rango de salida |
|------|---------------------------|-----------------|
| Sin bias | $V_p - V_K$ | $0$ a $2V_p - V_K$ |
| Con bias $+V_R$ | $V_p + V_R - V_K$ | $V_R$ a $2V_p + V_R - V_K$ |

### Sujetador negativo (desplaza hacia abajo)

| Tipo | Rango de salida |
|------|-----------------|
| Sin bias | $-(2V_p - V_K)$ a $0$ |
| Con bias $+V_R$ | $-(2V_p - V_K) + V_R$ a $V_R$ |

---

## 1.3.4 Multiplicadores de Voltaje

| Tipo | $V_{out}$ (ideal) | Diodos | Capacitores |
|------|-------------------|--------|-------------|
| Doblador media onda | $2V_p$ | 2 | 2 |
| Doblador onda completa | $2V_p$ | 2 | 2 |
| Triplicador | $3V_p$ | 3 | 3 |
| Cuadruplicador | $4V_p$ | 4 | 4 |
| Multiplicador ×N | $N \cdot V_p$ | N | N |

> **Nota:** La regulación de carga empeora con factores de multiplicación altos. La corriente disponible disminuye.

---

## 1.4 Diodo Zener y Circuitos Reguladores

### Parámetros del diodo Zener

| Parámetro | Símbolo | Descripción |
|-----------|---------|-------------|
| Voltaje Zener | $V_Z$ | Voltaje de ruptura nominal |
| Corriente mínima | $I_{Z(min)}$ o $I_{ZK}$ | Corriente mínima para mantener regulación |
| Corriente máxima | $I_{Z(max)}$ o $I_{ZM}$ | Limitada por $P_{Z(max)} / V_Z$ |
| Potencia máxima | $P_{Z(max)}$ | $P_Z = V_Z \cdot I_Z$ |
| Resistencia dinámica | $r_Z$ | Pendiente en zona de ruptura (2–20 Ω típico) |

### Regulador Zener básico

$$R_S = \frac{V_i - V_Z}{I_Z + I_L}$$

$$I_L = \frac{V_Z}{R_L}$$

$$I_Z = I_S - I_L = \frac{V_i - V_Z}{R_S} - \frac{V_Z}{R_L}$$

**Condiciones de regulación:**
- $I_{Z(min)} \leq I_Z \leq I_{Z(max)}$  
- $V_i > V_Z + I_{Z(min)} \cdot R_S$

### Valores comerciales típicos Zener

| $V_Z$ (V) | $P_{Z(max)}$ | $I_{Z(max)}$ | Aplicación típica |
|-----------|--------------|-------------|-------------------|
| 3.3 | 0.5 W | 152 mA | Referencia lógica 3.3V |
| 5.1 | 0.5 W | 98 mA | Referencia lógica 5V |
| 6.2 | 0.5 W | 81 mA | Mejor coef. temp. (~0) |
| 9.1 | 1 W | 110 mA | Regulación intermedia |
| 12 | 1 W | 83 mA | Circuitos analógicos |
| 15 | 1 W | 67 mA | Alimentación sensores |
| 24 | 1 W | 42 mA | Protección circuitos |

---

## 1.5 Otros Diodos — Valores Típicos

| Diodo | $V_K$ | Parámetro clave | Aplicación principal |
|-------|-------|-----------------|---------------------|
| Si estándar (1N4148) | 0.7 V | $I_F = 200$ mA, $t_{rr} = 4$ ns | Propósito general, señal |
| Si potencia (1N400x) | 0.7 V | $I_F = 1$ A, PIV = 50–1000 V | Rectificación |
| Ge (1N34A) | 0.3 V | $I_F = 50$ mA | Detectores RF |
| Schottky (1N5817) | 0.2–0.3 V | $I_F = 1$ A, $t_{rr} < 1$ ns | Fuentes conmutadas, RF |
| Zener (1N47xx) | — | $V_Z = 2.4$–75 V | Regulación de voltaje |
| Varactor (BB109) | — | $C_j = 2$–22 pF | Sintonización, VCO |
| PIN (BAP64) | 0.6 V | $R_{ON} = 1$ Ω, $C_T = 0.3$ pF | Conmutación RF |
| Túnel (1N3712) | ≈ 0.1 V | $I_P / I_V \approx 10$ | Oscilador microondas |
| LED rojo | 1.8 V | $I_F = 20$ mA | Indicadores |
| LED verde | 2.1 V | $I_F = 20$ mA | Indicadores |
| LED azul/blanco | 3.0–3.6 V | $I_F = 20$ mA | Iluminación |
| LASER (diodo) | 1.5–2.0 V | Potencia mW–W | Telecomunicaciones |

### Constantes físicas de referencia

| Constante | Símbolo | Valor |
|-----------|---------|-------|
| Carga del electrón | $q$ | $1.602 \times 10^{-19}$ C |
| Constante de Boltzmann | $k$ | $1.381 \times 10^{-23}$ J/K |
| Voltaje térmico (25°C) | $V_T$ | 25.86 mV |
| Barrera Si | $V_0$ | ≈ 0.7 V |
| Barrera Ge | $V_0$ | ≈ 0.3 V |
| Ancho de banda prohibida Si | $E_g$ | 1.12 eV |
| Ancho de banda prohibida Ge | $E_g$ | 0.67 eV |
