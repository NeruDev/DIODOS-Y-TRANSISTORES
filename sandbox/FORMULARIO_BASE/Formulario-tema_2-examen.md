# Formulario de Examen: Tema 2 (Transistores BJT)

> Documento simplificado para consulta rápida en exámenes. Contiene exclusivamente fórmulas, modelos ideales/prácticos y aproximaciones estandarizadas.

---

## 1. Relaciones Fundamentales del BJT

### 1.1 Corrientes y Ganancias (DC)
* **Ley de Nodos en Transistor:**
  $$ I_E = I_C + I_B $$
* **Relaciones de Corriente Directa (Aproximación $I_{CEO} \ll \beta I_B$):**
  $$ I_C \approx \beta I_B \quad ; \quad I_C \approx \alpha I_E $$
* **Factores de Ganancia:**
  $$ \alpha = \frac{\beta}{\beta + 1} \quad ; \quad \beta = \frac{\alpha}{1 - \alpha} $$

### 1.2 Ecuaciones Exactas con Fuga (Alta Temp / Ge)
* **Emisor Común:**
  $$ I_C = \beta I_B + I_{CEO} $$
* **Base Común:**
  $$ I_C = \alpha I_E + I_{CBO} $$
* **Relación de Fugas:**
  $$ I_{CEO} = (\beta + 1) I_{CBO} $$

### 1.3 Regiones de Operación (Criterio Visual Teórico)
| Región | Unión BE | Unión BC |
|---|---|---|
| **Corte** | Inversa | Inversa |
| **Activa** | Directa | Inversa |
| **Saturación**| Directa | Directa |

---

## 2. Modelos Físicos y Pequeña Señal

### 2.1 Ecuación de Shockley y Efecto Early
* **Corriente de Colector (Básica):**
  $$ I_C = I_S e^{\frac{V_{BE}}{V_T}} $$
* **Efecto Early (Dependencia de $V_{CE}$):**
  $$ I_C = \beta I_B \left( 1 + \frac{V_{CE}}{V_A} \right) $$
  *(Donde $V_A$ es el Voltaje Early)*

### 2.2 Parámetros de Pequeña Señal
* **Transconductancia ($g_m$):**
  $$ g_m = \frac{I_C}{V_T} $$
* **Resistencia Dinámica de Emisor ($r_e$):**
  $$ r_e = \frac{V_T}{I_E} \approx \frac{V_T}{I_C} \approx \frac{26\text{ mV}}{I_{CQ}} $$

### 2.3 Desempeño por Configuraciones (Pequeña Señal)
| Parámetro | Emisor Común (E-com) | Base Común (B-com) | Colector Común (Seguidor) |
|-----------|----------------------|--------------------|---------------------------|
| **Desfase** | **180°** | **0°** | **0°** |
| **$A_v$** | Alta ($-R_C/r_e$)* | Alta | $\approx 1$ |
| **$A_i$** | Alta ($\beta$) | $\approx \alpha < 1$ | Alta ($\beta+1$) |
| **$Z_{in}$**| Media ($\beta r_e$) | Muy Baja | Alta |
| **$Z_{out}$**| Alta | Muy Alta | Baja |

> [!NOTE]
> *Aproximación simplificada para Emisor Común sin degeneración. Para circuitos reales con carga y emisor no puenteado: $A_v \approx -\frac{R_C \parallel R_L}{r_e + R_E}$.

---

## 3. Topologías de Polarización DC

### 3.1 Polarización Simple (Fija)
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B} $$

### 3.2 Polarización Estabilizada en Emisor
$$ I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1) R_E} $$

### 3.3 Polarización por Divisor de Tensión (Thévenin)
Es la topología más estable térmicamente.
1. **Voltaje y Resistencia Thévenin:**
   $$ V_{TH} = V_{CC} \frac{R_2}{R_1 + R_2} \quad ; \quad R_{TH} = R_1 \parallel R_2 = \frac{R_1 R_2}{R_1 + R_2} $$
2. **Corriente de Base (Malla Entrada):**
   $$ I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1) R_E} $$
3. **Voltaje Colector-Emisor (Malla Salida Exacta):**
   $$ V_{CE} = V_{CC} - I_C R_C - I_E R_E $$
   *(Aproximación válida si $\beta \gg 1$: $V_{CE} \approx V_{CC} - I_C(R_C + R_E)$)*

### 3.4 Polarización por Realimentación de Colector
Proporciona estabilidad contra variaciones de $\beta$ al conectar $R_B$ directamente al colector.
* **Corriente de Base:**
  $$ I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)} $$
* **Voltaje Colector-Emisor:**
  $$ V_{CE} = V_{CC} - I_C(R_C + R_E) $$

### 3.5 Base Común en DC
Normalmente utiliza dos fuentes de alimentación ($V_{EE}$ y $V_{CC}$).
* **Corriente de Emisor (Malla de entrada):**
  $$ I_E = \frac{V_{EE} - V_{BE}}{R_E} $$
* **Voltaje Colector-Base (Malla de salida):**
  $$ V_{CB} = V_{CC} - I_C R_C $$

### 3.6 Colector Común en DC / Seguidor de Emisor
No lleva resistencia de colector ($R_C = 0$). El colector va directo a $V_{CC}$.
* **Corriente de Base:**
  $$ I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1) R_E} $$
* **Voltaje Colector-Emisor:**
  $$ V_{CE} = V_{CC} - I_E R_E $$

### 3.7 Análisis Rápido sin $\beta$ (Aproximación Práctica)
Si el divisor es rígido, la corriente por la base se puede ignorar para un cálculo rapidísimo:
$$ V_B \approx V_{TH} \implies V_E \approx V_B - 0.7\text{ V} \implies I_E \approx \frac{V_E}{R_E} \approx I_C $$

### 3.8 Diseño Óptimo (Excursión Simétrica Máxima)
Para un diseño óptimo de amplificador lineal (Punto Q central):
$$ V_{CEQ} \approx \frac{V_{CC}}{2} $$

---

## 4. BJT como Interruptor (Conmutación Digital)

### 4.1 Corrientes de Conmutación
* **Corriente Máxima de Saturación:**
  $$ I_{C(\text{sat})} = \frac{V_{CC} - V_{CE(\text{sat})}}{R_C} \approx \frac{V_{CC}}{R_C} $$
* **Corriente Mínima Teórica de Base:**
  $$ I_{B(\text{sat},\min)} = \frac{I_{C(\text{sat})}}{\beta} $$

### 4.2 Criterio de Sobrediseño (Garantía de Saturación)
Se fuerza el estado ON asumiendo una ganancia degradada para evitar fallos térmicos:
$$ I_B \ge \frac{I_{C(\text{sat})}}{\beta_{\text{forzado}}} \quad \text{donde} \quad \beta_{\text{forzado}} \approx \frac{\beta}{5} \text{ o } 10 $$

---

## 5. Estabilidad Térmica ($S$)

> Mide la sensibilidad de la corriente de colector ($I_C$) ante variaciones de temperatura (específicamente por cambios en la corriente de fuga $I_{CBO}$). Un $S$ menor indica un circuito más estable.

* **Fórmula General de Estabilidad:**
  $$ S = \frac{\beta + 1}{1 - \beta \left( \frac{\partial I_B}{\partial I_C} \right)} $$

* **Comparativa de Estabilidad por Topología:**
| Topología | Factor $S$ (Aproximado) | Nivel de Estabilidad |
| --- | --- | --- |
| **Polarización Fija** | $S \approx \beta + 1$ | **Pésima** (Altamente inestable) |
| **Realimentación de Colector** | $S \approx \frac{\beta + 1}{1 + \beta \left( \frac{R_C}{R_C + R_B} \right)}$ | **Media** |
| **Divisor de Tensión (Thévenin)** | $S \approx \frac{\beta + 1}{1 + \beta \frac{R_E}{R_{TH} + R_E}} \approx 1 + \frac{R_{TH}}{R_E}$ | **Excelente** (Si $R_{TH} \ll R_E$) |

---

## 6. Método de Análisis Rápido y Examen

### 6.1 Método Universal (4 Pasos)
1. **Asume** $V_{BE} \approx 0.7\text{ V}$.
2. **Calcula** $I_B$ en malla de entrada $\implies$ **Calcula** $I_C = \beta I_B$.
3. **Calcula** $V_{CE}$ en malla de salida.
4. **Verifica Zona:**
   * $V_{BE} < 0.7\text{ V} \implies$ **CORTE** ($I_C = 0$).
   * $V_C > V_B$ (Físicamente $V_{CB} > 0$) $\implies$ **ACTIVA**.
   * $V_C \le V_B \implies$ **SATURACIÓN** (Recalcula con $V_{CE} = 0.2\text{ V}$ y $V_{BE} = 0.8\text{ V}$).

### 6.2 Trazado Rápido de Recta de Carga
* **Punto 1 (Eje Y):** Haz $V_{CE} = 0 \implies I_C = \frac{V_{CC}}{R_C + R_E}$ (Saturación)
* **Punto 2 (Eje X):** Haz $I_C = 0 \implies V_{CE} = V_{CC}$ (Corte)
* **Punto Q:** Sitúa $(V_{CEQ}, I_{CQ})$ obtenido del método universal sobre la línea.

### 6.3 Tabla Visual de Conmutación
| Estado | $I_B$ | $I_C$ | $V_{CE}$ | Comportamiento |
|--------|-------|-------|----------|----------------|
| **Corte** | $0$ | $0$ | $V_{CC}$ | Switch ABIERTO |
| **Activa** | Media | $\beta I_B$ | $V_{CC} - I_C R$ | Amplificador Lineal |
| **Sat.** | Alta | $I_{C(\text{sat})}$ | $0.2\text{ V}$ | Switch CERRADO |

---

## Glosario de Variables

| Símbolo | Nombre y Descripción |
|---------|----------------------|
| **$A_i$** | Ganancia de corriente en pequeña señal (adimensional o A/A). |
| **$A_v$** | Ganancia de voltaje en pequeña señal (adimensional o V/V). |
| **$BV_{CEO}$** | Voltaje de ruptura colector-emisor con base en circuito abierto (V). |
| **$I_B$** | Corriente continua de entrada de la base (A). |
| **$I_C$** | Corriente continua de salida del colector (A). |
| **$I_{C(\text{sat})}$** | Corriente de colector en saturación profunda (A). |
| **$I_{CBO}$** | Corriente de fuga inversa colector-base con el emisor en circuito abierto (A). |
| **$I_{CEO}$** | Corriente de fuga inversa colector-emisor con base en circuito abierto (A). |
| **$I_E$** | Corriente continua total del emisor (A). |
| **$I_S$** | Corriente de saturación inversa intrínseca de la unión base-emisor (A). |
| **$R_1$** | Resistencia de polarización superior del divisor ($\Omega$). |
| **$R_2$** | Resistencia de polarización inferior del divisor ($\Omega$). |
| **$R_B$** | Resistencia de limitación conectada en serie con la base para control digital ($\Omega$). |
| **$R_C, R_E$** | Resistencias de colector y de emisor respectivamente ($\Omega$). |
| **$R_{TH}$** | Resistencia equivalente de Thévenin en la base ($\Omega$). |
| **$S$** | Factor de estabilidad térmica (adimensional). |
| **$V_A$** | Voltaje de Early, proyecta la convergencia de las curvas de salida en la región activa (V). |
| **$V_B, V_C, V_E$** | Tensiones absolutas en bornes de base, colector y emisor (V). |
| **$V_{BE(\text{sat})}$** | Voltaje de saturación base-emisor, requerido para forzar la conducción plena (V). |
| **$V_{BE}$** | Caída de tensión directa base-emisor (V). Típicamente $0.7\text{ V}$ para silicio. |
| **$V_{CC}$** | Fuente única de alimentación en corriente continua (V). |
| **$V_{CE(\text{sat})}$** | Voltaje de saturación de conmutación del transistor en directa (V). Típicamente $0.2\text{ V}$. |
| **$V_{CE}$** | Diferencia de potencial colector-emisor (V). |
| **$V_{HI}$** | Voltaje lógico de nivel alto entregado por la etapa de control de entrada (V). |
| **$V_{TH}$** | Voltaje equivalente de Thévenin en la base (V). |
| **$W_{\text{base, efectivo}}$** | Ancho real de la base neutral donde ocurre la difusión de portadores (m). |
| **$W_{\text{base, metalúrgico}}$** | Distancia física de separación de las fronteras dopadas de la base (m). |
| **$W_{\text{depleción}}$** | Ancho de la zona de carga de espacio de la unión colector-base (m). |
| **$Z_{in(\text{base})}$** | Impedancia de entrada vista desde el terminal de base ($\Omega$). |
| **$\alpha$** | Ganancia de corriente en base común (adimensional). |
| **$\beta$** | Ganancia de corriente del transistor en continua ($h_{FE}$, adimensional). |
| **$\beta_{\text{forzado}}$** | Ganancia de corriente degradada o asumida forzosamente para asegurar saturación en diseño de switch (adimensional). |
