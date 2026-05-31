<!--
::METADATA::
type: cheatsheet
topic_id: BJT-02
file_id: tema_2-nota_1
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos del Transistor BJT: Configuraciones de Base Común y Emisor Común

Este documento recopila y estructura las relaciones matemáticas y los modelos físicos de las configuraciones de base común (B-com) y emisor común (E-com) del transistor de unión bipolar (BJT) presentadas en la Nota 1. Incluye las ecuaciones fundamentales de corrientes, los factores de ganancia de corriente ($\alpha$ y $\beta$), el modelado de corrientes de fuga, los límites de las regiones de operación y el análisis físico del Efecto Early.

---

## 1. Ecuación General de Corrientes del Transistor BJT

El transistor de unión bipolar opera como un dispositivo de tres terminales donde la suma de las corrientes que entran debe ser estrictamente igual a la suma de las que salen, de acuerdo con la Ley de Corrientes de Kirchhoff (LKC).

### 1.1 Relación de Corrientes de Terminales
Ecuación fundamental que establece que la corriente de emisor es la suma de las corrientes de colector y base (válida tanto para transistores NPN como PNP).

$$
I_E = I_C + I_B
$$

* **Nomenclatura:**
  * $I_E$: Corriente continua en la terminal del emisor (A).
  * $I_C$: Corriente continua en la terminal del colector (A).
  * $I_B$: Corriente continua en la terminal de la base (A).
* **Valores típicos de distribución:**
  * La corriente de base es extremadamente pequeña, típicamente del $0.2\%$ al $2\%$ de la corriente total de emisor.
  * La corriente de colector transporta entre el $98\%$ y el $99.8\%$ de la corriente de emisor en la región activa.

---

## 2. Configuración en Base Común (Base Común - B-com)

En la configuración de base común, la terminal de la base es compartida por la entrada (emisor) y la salida (colector), y suele estar acoplada a la referencia común o tierra.

### 2.1 Ganancia de Corriente en Base Común o Factor Alfa ($\alpha$)
Relación de amplificación de corriente directa en base común. Expresa qué fracción de la corriente de emisor logra cruzar la base y llegar al colector.

$$
\alpha = \frac{I_C}{I_E}
$$

### 2.2 Corriente de Colector Completa en Región Activa
Modelado físico de la corriente de colector que incorpora la componente de portadores inyectados desde el emisor y la corriente de fuga inversa residual de la unión colector-base polarizada en inversa.

$$
I_C = \alpha I_E + I_{CBO}
$$

* **Nomenclatura:**
  * $\alpha$: Ganancia de corriente continua en base común (adimensional). Su valor es siempre menor a la unidad.
  * $I_{CBO}$: Corriente de fuga colector-base con el emisor abierto (A).
* **Valores típicos en base común:**
  * $\alpha$: Típicamente entre $0.980$ y $0.998$.
  * $I_{CBO}$: Corriente extremadamente pequeña en condiciones de temperatura normal, típicamente en el orden de los nanoamperios ($10^{-9}\text{ A}$) para silicio.
  * *Comportamiento de Impedancias:* Posee una resistencia de entrada muy baja (debido a la unión Base-Emisor en directa) y una resistencia de salida muy alta (debido a la unión Colector-Base en inversa).

---

## 3. Configuración en Emisor Común (Emisor Común - E-com)

En la configuración de emisor común, la terminal del emisor es la referencia para la entrada (base) y la salida (colector). Es la topología más ampliamente utilizada para amplificación de voltaje y corriente.

### 3.1 Ganancia de Corriente en Emisor Común o Factor Beta ($\beta$)
Parámetro de ganancia o factor de amplificación de corriente del transistor. Expresa la capacidad de control de la corriente de base ($I_B$) sobre la corriente de colector ($I_C$).

$$
\beta = \frac{I_C}{I_B}
$$

### 3.2 Relación Analítica entre Factores Alfa ($\alpha$) y Beta ($\beta$)
Expresiones de conversión mutua para los dos factores de ganancia del BJT.

$$
\alpha = \frac{\beta}{\beta + 1}
$$

$$
\beta = \frac{\alpha}{1 - \alpha}
$$

### 3.3 Corriente de Colector Completa en Emisor Común
Modelado de la corriente de colector controlada por base en emisor común, incorporando la corriente de fuga inversa amplificada.

$$
I_C = \beta I_B + I_{CEO}
$$

### 3.4 Corriente de Fuga Colector-Emisor ($I_{CEO}$)
Corriente residual en inversa que fluye entre colector y emisor cuando la base se encuentra en circuito abierto ($I_B = 0$). Se relaciona directamente con la corriente de fuga de base común $I_{CBO}$ amplificada por el factor del transistor.

$$
I_{CEO} = (\beta + 1) I_{CBO}
$$

* **Nomenclatura:**
  * $\beta$: Ganancia de corriente en continua en emisor común o parámetro $h_{FE}$ (adimensional).
  * $I_{CEO}$: Corriente de fuga colector-emisor con la base abierta (A).
* **Valores típicos en emisor común:**
  * $\beta$: Típicamente varía en un amplio rango comercial desde $50$ hasta más de $400$.
  * $I_{CEO}$: Aunque es proporcional a $I_{CBO}$, sigue siendo pequeña, típicamente en el rango de los microamperios ($\mu\text{A}$).
  * *Comportamiento de Impedancias:* Posee una impedancia de entrada moderada (típicamente $1\text{ k}\Omega - 10\text{ k}\Omega$) y una impedancia de salida alta, lo que la hace idónea para etapas amplificadoras acopladas.

---

## 4. Regiones de Operación y Criterios Físicos

El transistor de unión bipolar posee tres regiones fundamentales de operación controladas por la polarización de sus dos uniones PN: la unión Base-Emisor (B-E) y la unión Colector-Base (C-B).

### 4.1 Criterios de Polarización por Región

| Región de Operación | Unión Base-Emisor (B-E) | Unión Colector-Base (C-B) | Comportamiento en el Circuito |
|---------------------|------------------------|--------------------------|---------------------------------|
| **Región Activa** | Polarización Directa | Polarización Inversa | Amplificador lineal de corriente ($I_C \approx \beta I_B$). |
| **Saturación** | Polarización Directa | Polarización Directa | Interruptor cerrado ($V_{CE(\text{sat})} \approx 0.2\text{ V}$). |
| **Corte** | Polarización Inversa | Polarización Inversa | Interruptor abierto ($I_C \approx I_{CEO} \approx 0\text{ A}$). |

* **Condición de Región Activa (NPN):**
  Para asegurar el estado activo en emisor común, el voltaje en la terminal del colector debe mantenerse estrictamente mayor que el de la base:
  $$
  V_C > V_B \implies V_{CB} > 0
  $$

### 4.2 Modelo Físico del Efecto Early
Fenómeno de modulación del ancho de la base neutral. Al aumentar la polarización inversa colector-base ($V_{CB}$), la región de depleción de la unión C-B se ensancha hacia el interior de la base debido a su bajo dopaje.

* **Efecto en la Base:**
  $$
  W_{\text{base, efectivo}} = W_{\text{base, metalúrgico}} - W_{\text{depleción}}
  $$
* **Impacto en el Dispositivo:**
  La reducción del ancho efectivo de la base neutral ($W_{\text{base, efectivo}}$) incrementa el gradiente de concentración de portadores inyectados. Esto causa:
  1. Un incremento sutil en las corrientes $I_E$ e $I_C$ para un voltaje $V_{BE}$ constante en las curvas de entrada.
  2. Una pendiente no nula (ligera inclinación ascendente) en las curvas de características de salida, reduciendo levemente la resistencia de salida del dispositivo.

* **Nomenclatura:**
  * $W_{\text{base, efectivo}}$: Ancho real de la base neutral donde ocurre la difusión de portadores (m).
  * $W_{\text{base, metalúrgico}}$: Distancia física de separación de las fronteras dopadas de la base (m).
  * $W_{\text{depleción}}$: Ancho de la zona de carga de espacio de la unión colector-base (m).

---

## 5. Glosario de Términos Técnicos

* **Transistor BJT (Bipolar Junction Transistor):** Dispositivo semiconductor de tres terminales formado por dos uniones PN muy cercanas, cuyo funcionamiento depende del flujo de portadores tanto mayoritarios como minoritarios (bipolar).
* **Configuración en Base Común:** Disposición circuital donde la terminal de la base actúa como nodo común de referencia a tierra, inyectando corriente por el emisor y extrayendo corriente por el colector.
* **Configuración en Emisor Común:** Disposición circuital comercialmente dominante en la cual el emisor se acopla a tierra, permitiendo controlar una corriente elevada de colector a partir de una corriente pequeña de base.
* **Ganancia Alfa ($\alpha$):** Parámetro fraccionario que describe la eficiencia de transporte de portadores a través de la base en configuración de base común.
* **Ganancia Beta ($\beta$):** Parámetro multiplicador que cuantifica la ganancia de corriente de un transistor en emisor común, equivalente al parámetro híbrido de señal $h_{FE}$.
* **Corriente de Fuga colector-base ($I_{CBO}$):** Corriente inversa minoritaria que circula por la unión colector-base cuando el emisor se mantiene en circuito abierto.
* **Corriente de Fuga colector-emisor ($I_{CEO}$):** Corriente inversa que fluye de colector a emisor con la base abierta, la cual es mayor que $I_{CBO}$ debido a que la corriente residual se amplifica por el efecto transistor del componente.
* **Efecto Early:** Fenómeno físico de reducción del ancho efectivo de la base activa a causa del ensanchamiento de la zona de deplexión del colector bajo polarización inversa creciente.
* **Región Activa:** Zona de operación lineal donde la unión de entrada está en directa y la de salida en inversa, permitiendo la amplificación de señales eléctricas.
* **Región de Saturación:** Zona de operación donde ambas uniones PN están en directa, provocando que el transistor actúe como un cortocircuito virtual con mínima caída de voltaje.
* **Región de Corte:** Zona de operación donde ambas uniones PN se polarizan en inversa, interrumpiendo el flujo de corrientes y emulando un circuito abierto.
