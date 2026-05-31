<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_2
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para el Ajuste de Parámetros y Resistencias en Diodos

Este documento recopila y estructura las ecuaciones para el análisis avanzado de diodos en corriente continua (DC) y corriente alterna (AC) presentadas en la Nota 2. Se incluyen las fórmulas de variación instantánea por señal mixta, la metodología para la extracción de parámetros de Shockley a partir de mediciones experimentales y la diferenciación analítica entre resistencia estática (DC) y dinámica (AC).

---

## 1. Recta de Carga y Límites Instantáneos bajo Señal Mixta (DC + AC)

Cuando una fuente alterna está acoplada en serie con una fuente continua (señal mixta), la recta de carga sufre un desplazamiento dinámico paralelo que desplaza el punto de operación instantáneo entre límites extremos.

### 1.1 Ecuación de la Malla en CD
Planteamiento de tensiones estático que define la recta de carga nominal en corriente continua.

$$
R I_D + V_D = E
$$

### 1.2 Límites de Voltaje Efectivo Instantáneo
Amplitudes extremas que alcanza la tensión efectiva total en la malla debido a la adición de una señal AC superpuesta de la forma $v_s(t) = V_m \sin(\omega t)$.

$$
E_{\max} = E + V_m
$$

$$
E_{\min} = E - V_m
$$

### 1.3 Límites Teóricos de Corriente Instantánea
Aproximación ideal de corriente máxima y mínima en la malla, asumiendo un cortocircuito ideal en el diodo ($V_D \approx 0$).

$$
I_{D,\max} \approx \frac{E_{\max}}{R} = \frac{E + V_m}{R}
$$

$$
I_{D,\min} \approx \frac{E_{\min}}{R} = \frac{E - V_m}{R}
$$

### 1.4 Ajuste de Tensión de Fuente para Q Objetivo
Ecuación empleada para calcular la tensión continua de fuente ($E$) necesaria para posicionar un punto Q de operación deseado $(I_D, V_D)$ con una resistencia de malla $R$ dada.

$$
E = R I_D + V_D
$$

* **Nomenclatura:**
  * $E$: Tensión de polarización en corriente continua (V).
  * $V_m$: Amplitud pico de la señal de entrada alterna (V).
  * $R$: Resistencia limitadora en serie ($\Omega$).
  * $I_D$: Corriente instantánea en el diodo (A).
  * $V_D$: Caída de tensión instantánea en el diodo (V).
  * $E_{\max}, E_{\min}$: Tensiones instantáneas máxima y mínima del generador de señal mixta (V).
  * $I_{D,\max}, I_{D,\min}$: Corrientes instantáneas límites estimadas en el diodo (A).

---

## 2. Ajuste de Parámetros del Modelo de Shockley

Para obtener alta precisión en modelos no lineales, los parámetros intrínsecos de la ecuación exponencial del diodo se extraen analíticamente empleando dos puntos de operación conocidos bajo conducción directa directa ($(V_1, I_1)$ y $(V_2, I_2)$ donde $I \gg I_S$).

### 2.1 Ecuación del Factor de Idealidad ($n$)
Deducción analítica obtenida al relacionar los cocientes de corriente directa para anular la corriente de saturación inversa $I_S$.

$$
n = \frac{V_2 - V_1}{V_T \ln\left(\frac{I_2}{I_1}\right)}
$$

### 2.2 Ecuación de la Corriente de Saturación Inversa ($I_S$)
Cálculo de la corriente de fuga inversa del dispositivo sustituyendo el factor de idealidad ($n$) determinado en cualquiera de los puntos conocidos.

$$
I_S = \frac{I_1}{e^{\frac{V_1}{n V_T}} - 1}
$$

* **Nomenclatura:**
  * $V_1, V_2$: Tensiones continuas en terminales del diodo medidas en dos condiciones distintas (V).
  * $I_1, I_2$: Corrientes continuas a través del diodo medidas en las dos condiciones asociadas (A).
  * $V_T$: Voltaje térmico del semiconductor (V). Típicamente $\approx 26\text{ mV}$ a $25^\circ\text{C}$.
  * $n$: Factor de idealidad ajustado del diodo (adimensional).
  * $I_S$: Corriente de saturación inversa calculada para el componente (A).

---

## 3. Resistencias en Corriente Directa (DC) y Dinámica (AC)

La resistencia de un diodo semiconductor varía según el régimen de excitación. Es crítico distinguir entre la resistencia estática absoluta y la resistencia dinámica diferencial.

### 3.1 Resistencia Estática o en CD ($R_{\text{CD}}$)
Representa la oposición total al paso de la corriente continua. Gráficamente equivale a la inversa de la pendiente de la recta secante que conecta el origen del plano cartesiano $(0,0)$ con el punto de operación $Q(V_{DQ}, I_{DQ})$.

$$
R_{\text{CD}} = \frac{V_{D_Q}}{I_{D_Q}}
$$

### 3.2 Resistencia Dinámica o de AC Diferencial Analítica ($r_d$)
Es la resistencia equivalente ante perturbaciones infinitesimales de pequeña señal. Gráficamente es la recíproca de la recta tangente local a la curva exponencial evaluada en el punto $Q$.

$$
r_d = \frac{n V_T}{I_{D_Q}}
$$

### 3.3 Resistencia Dinámica Promedio Gráfica (Secante)
Aproximación de la resistencia de pequeña señal para variaciones finitas medibles ($\Delta V_D$ y $\Delta I_D$) alrededor de $Q$.

$$
r_d \approx \frac{\Delta V_D}{\Delta I_D} = \frac{V_{D,\max} - V_{D,\min}}{I_{D,\max} - I_{D,\min}}
$$

* **Nomenclatura:**
  * $R_{\text{CD}}$: Resistencia estática en corriente continua ($\Omega$).
  * $r_d$: Resistencia dinámica diferencial teórica ($\Omega$).
  * $V_{D_Q}, I_{D_Q}$: Coordenadas del punto $Q$ en continua (V, A).
  * $\Delta V_D, \Delta I_D$: Variaciones finitas en terminales del diodo entre sus límites de AC (V, A).
  * $V_{D,\max}, V_{D,\min}$: Caídas de tensión máxima y mínima reales en el diodo ante el swing de AC (V).
  * $I_{D,\max}, I_{D,\min}$: Corrientes máxima y mínima reales en el diodo ante el swing de AC (A).

> [!WARNING]
> **Diferencia entre $R_{\text{CD}}$ y $r_d$**: En la zona de conducción del diodo, la resistencia estática es significativamente mayor que la dinámica ($R_{\text{CD}} \gg r_d$). Esto ocurre porque $R_{\text{CD}}$ incorpora el voltaje umbral o de rodilla necesario para iniciar la conducción ($V_K \approx 0.6\text{ V}$), el cual no genera incrementos de corriente. La resistencia dinámica $r_d$ representa únicamente la pendiente de la curva en el punto de operación directa, donde el diodo presenta una resistencia incremental muy baja.

> [!IMPORTANT]
> **Desviación del Modelo Lineal**: La resistencia dinámica promedio gráfica ($\Delta V_D / \Delta I_D$) sobre una variación finita difiere ligeramente de la resistencia analítica instantánea en $Q$. Esto ocurre porque el swing alterno real no es infinitesimal y recorre un arco curvo de la exponencial en lugar de la recta tangente teórica. Además, emplear un modelo lineal simplificado por tramos suele sobreestimar severamente el valor de $r_d$ en comparación con el modelo exponencial de Shockley, debido a que asume pendientes promedio constantes de bajo gradiente.

---

## 4. Glosario de Términos Técnicos

* **Resistencia Estática ($R_{\text{CD}}$):** Cociente de la caída de tensión total en corriente continua dividida entre la corriente total a través del diodo en el punto de operación.
* **Resistencia Dinámica ($r_d$):** Oposición diferencial al flujo de corriente alterna de pequeña amplitud calculada como la inversa de la derivada matemática en el punto $Q$.
* **Señal Mixta (AC + CD):** Régimen de excitación donde un circuito posee componentes constantes de polarización en DC combinados con componentes periódicos variables en AC.
* **Ajuste del Modelo:** Metodología matemática para calcular las constantes físicas intrínsecas del diodo ($I_S$ y $n$) a partir de pares de datos experimentales de tensión y corriente.
* **Límites Instantáneos:** Puntos de operación extremos alcanzados periódicamente por el circuito debido a las amplitudes máximas y mínimas de la componente variable AC.
* **Pendiente Tangencial:** Gradiente local en la curva característica exponencial que define el modelo de resistencia dinámica infinitesimal en pequeña señal.
