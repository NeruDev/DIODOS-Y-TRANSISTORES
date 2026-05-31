<!--
::METADATA::
type: cheatsheet
topic_id: BJT-02
file_id: tema_2-nota_3
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Deducción de Corrientes del Transistor BJT en Emisor Común

Este documento presenta de forma analítica y estructurada la deducción matemática de las corrientes en configuración de emisor común (E-com) del transistor de unión bipolar (BJT) a partir de la Nota 3. Contempla la relación matemática exacta entre los factores de ganancia de base común y emisor común, la deducción y amplificación de la corriente de fuga inversa colector-emisor ($I_{CEO}$), el análisis de la modulación de corriente de base por el Efecto Early y la caracterización de las regiones de operación junto con la tensión de ruptura ($BV_{CEO}$).

---

## 1. Deducción Analítica de la Corriente de Colector en Emisor Común

La configuración de emisor común describe la corriente de salida ($I_C$) en función de la corriente de entrada de control ($I_B$). Se parte de las dos relaciones físicas fundamentales del BJT:

1. **Ecuación de Colector en Base Común:**
   $$
   I_C = \alpha I_E + I_{CBO}
   $$
2. **Relación de Corrientes de Kirchhoff en Terminales:**
   $$
   I_E = I_C + I_B
   $$

### 1.1 Sustitución y Agrupamiento
Sustituyendo la corriente de emisor $I_E$ en la ecuación de colector:

$$
I_C = \alpha (I_C + I_B) + I_{CBO} \implies I_C = \alpha I_C + \alpha I_B + I_{CBO}
$$

Agrupando los términos que contienen la corriente de colector ($I_C$) en el miembro izquierdo de la igualdad:

$$
I_C - \alpha I_C = \alpha I_B + I_{CBO}
$$

### 1.2 Factorización y Despeje General
Factorizando la corriente de colector ($I_C$) e implementando el despeje algebraico final:

$$
I_C (1 - \alpha) = \alpha I_B + I_{CBO}
$$

$$
I_C = \frac{\alpha}{1 - \alpha} I_B + \frac{I_{CBO}}{1 - \alpha}
$$

* **Nomenclatura:**
  * $I_C$: Corriente continua de salida del colector (A).
  * $I_B$: Corriente continua de entrada de la base (A).
  * $I_E$: Corriente continua total del emisor (A).
  * $\alpha$: Ganancia de corriente en base común (adimensional).
  * $I_{CBO}$: Corriente de fuga inversa colector-base con el emisor en circuito abierto (A).

---

## 2. Factores de Ganancia y Amplificación de Fuga en Emisor Común

Para simplificar la ecuación general obtenida en la deducción, se implementa el cambio de variables físicas asociadas a la topología de emisor común.

### 2.1 Ganancia de Corriente Directa en Emisor Común ($\beta$ o $h_{FE}$)
Relación analítica de conversión entre los factores de ganancia de base común y emisor común.

$$
\beta = \frac{\alpha}{1 - \alpha}
$$

### 2.2 Corriente de Fuga Colector-Emisor con Base Abierta ($I_{CEO}$)
Es la corriente residual inversa de colector que circula cuando la base se encuentra en vacío ($I_B = 0$). Sufre una severa amplificación debido a la modulación de portadores minoritarios.

$$
I_{CEO} = \frac{I_{CBO}}{1 - \alpha} = (\beta + 1) I_{CBO}
$$

### 2.3 Ecuación Completa de Corriente de Colector
Expresión formal de salida para el transistor en configuración de emisor común.

$$
I_C = \beta I_B + I_{CEO}
$$

### 2.4 Ecuación Simplificada en Región Activa
En la práctica de polarización y diseño, la corriente de control amplificada es órdenes de magnitud mayor que la corriente de fuga inversa ($\beta I_B \gg I_{CEO}$), permitiendo despreciarla.

$$
I_C \approx \beta I_B
$$

* **Nomenclatura:**
  * $\beta$: Ganancia de corriente continua en emisor común o parámetro $h_{FE}$ (adimensional).
  * $I_{CEO}$: Corriente de fuga inversa colector-emisor con base en circuito abierto (A).
* **Parámetros típicos:**
  * Dado que $\alpha \to 1$ (e.g. $0.98 - 0.998$), el denominador $(1-\alpha)$ es extremadamente pequeño ($0.02 - 0.002$), disparando el valor de $\beta$ a magnitudes grandes (e.g. $50 - 500$).
  * En hojas de datos comerciales, $h_{FE}$ denota la ganancia en continua y $h_{fe}$ la ganancia diferencial de pequeña señal en alterna.

---

## 3. Características de Entrada y Modulación por Efecto Early

Al ser polarizada en directa la unión base-emisor, la entrada del circuito presenta un comportamiento de curva exponencial similar al de un diodo directo ($I_B$ en función de $V_{BE}$).

### 3.1 Modulación de la Corriente de Base por $V_{CE}$
Para una tensión de entrada $V_{BE}$ constante, la corriente de base ($I_B$) se reduce sistemáticamente a medida que el voltaje colector-emisor ($V_{CE}$) aumenta.

$$
I_B \downarrow \quad \text{si} \quad V_{CE} \uparrow \quad (\text{para } V_{BE} = \text{constante})
$$

### 3.2 Explicación Física (Modulación de Ancho de Base)
1. Un incremento en $V_{CE}$ eleva la polarización inversa de la unión colector-base ($V_{CB}$), ensanchando la zona de deplexión C-B hacia el interior de la base.
2. Al estrecharse el ancho de la base neutral activa, la probabilidad de que los portadores minoritarios inyectados desde el emisor se recombinen con los portadores mayoritarios en la base disminuye drásticamente.
3. Al caer la tasa de recombinación de base, la corriente de base externa requerida para reponer dichos portadores ($I_B$) disminuye.
4. Por el contrario, un voltaje $V_{CE}$ bajo ensancha la base neutral activa, incrementando la recombinación y aumentando la corriente de base ($I_B$) para un $V_{BE}$ dado.

---

## 4. Regiones de Operación y Tensión de Ruptura

La familia de curvas de salida ($I_C$ frente a $V_{CE}$ para distintas $I_B$) delimita las zonas físicas de operación del dispositivo.

### 4.1 Criterios de Límite de las Regiones
*   **Región de Corte:**
    Se define por la curva de entrada nula:
    $$
    I_B = 0 \implies I_C \approx I_{CEO} \approx 0\text{ A}
    $$
*   **Región Activa:**
    La corriente de salida es lineal e independiente de $V_{CE}$, gobernada por:
    $$
    I_C = \beta I_B
    $$
    La ligera pendiente ascendente en esta región se debe al incremento de gradiente por modulación de base (Efecto Early).
*   **Región de Saturación:**
    Ocurre cuando la caída colector-emisor desciende por debajo de la tensión de saturación de rodilla del silicio. La corriente de colector queda restringida por la malla externa del circuito.
    $$
    V_{CE} < V_{CE(\text{sat})} \approx 0.2\text{ V}
    $$

### 4.2 Tensión de Ruptura Colector-Emisor ($BV_{CEO}$)
Es el límite máximo absoluto de tensión inversa que puede soportar la unión colector-base con la base abierta antes de sufrir una avalancha de portadores.

$$
V_{CE} < BV_{CEO}
$$

* **Nomenclatura:**
  * $V_{CE(\text{sat})}$: Voltaje de saturación colector-emisor típico en conducción plena (V).
  * $BV_{CEO}$: Voltaje de ruptura colector-emisor con base en circuito abierto (V).
* *Peligro de Diseño:* Operar en la vecindad de $BV_{CEO}$ incrementa exponencialmente la corriente de colector por ionización por impacto, provocando la destrucción del dispositivo por avalancha térmica.

---

## 5. Glosario de Términos Técnicos

* **Corriente de Fuga Amplificada ($I_{CEO}$):** Corriente inversa que fluye entre colector y emisor en base abierta, cuyo valor es sustancialmente mayor que la corriente de base común ($I_{CBO}$) debido al factor multiplicador $(\beta + 1)$.
* **Ganancia $h_{FE}$:** Parámetro híbrido que designa la ganancia de corriente continua ($I_C / I_B$) en emisor común en hojas de especificaciones comerciales.
* **Ganancia $h_{fe}$:** Parámetro híbrido que cuantifica la ganancia de corriente de pequeña señal alterna ($\Delta I_C / \Delta I_B$) en el modelo equivalente de pequeña señal.
* **Voltaje de Saturación ($V_{CE(\text{sat})}$):** Mínima caída de tensión entre colector y emisor alcanzada cuando el transistor está conduciendo al máximo (saturado), típicamente de $0.2\text{ V}$ para silicio.
* **Voltaje de Ruptura ($BV_{CEO}$):** Máxima tensión inversa que tolera la estructura colector-emisor con la terminal de base abierta antes de entrar en régimen de avalancha eléctrica.
* **Recombinación de Portadores:** Proceso físico en el cual los electrones inyectados en la base (para transistores NPN) se combinan con los huecos mayoritarios de la base, desapareciendo como portadores libres y dando origen a la corriente de base externa $I_B$.
* **Modulación del Ancho de Base:** Variación de la anchura de la base neutral activa debido al ensanchamiento de las zonas de depleción bajo tensiones inversas de colector-base variables.
