# Formulario Tema 2

Este documento recopila y estructura las relaciones matemáticas y los modelos físicos de las configuraciones de base común (B-com) y emisor común (E-com) del transistor de unión bipolar (BJT) presentadas en la Nota 1. Incluye las ecuaciones fundamentales de corrientes, los factores de ganancia de corriente ($\alpha$ y $\beta$), el modelado de corrientes de fuga, los límites de las regiones de operación y el análisis físico del Efecto Early.

---

## 1. Ecuación General de Corrientes del Transistor BJT

El transistor de unión bipolar opera como un dispositivo de tres terminales donde la suma de las corrientes que entran debe ser estrictamente igual a la suma de las que salen, de acuerdo con la Ley de Corrientes de Kirchhoff (LKC).

### 1.1 Relación de Corrientes de Terminales
Ecuación fundamental que establece que la corriente de emisor es la suma de las corrientes de colector y base (válida tanto para transistores NPN como PNP).

$$
I_E = I_C + I_B
$$

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

---

## 4. Regiones de Operación y Criterios Físicos

El transistor de unión bipolar posee tres regiones fundamentales de operación controladas por la polarización de sus dos uniones PN: la unión Base-Emisor (B-E) y la unión Colector-Base (C-B).

### 4.1 Criterios de Polarización por Región

| Región de Operación | Unión Base-Emisor (B-E) | Unión Colector-Base (C-B) | Comportamiento en el Circuito |
|---------------------|------------------------|--------------------------|---------------------------------|
| **Región Activa** | Polarización Directa | Polarización Inversa | Amplificador lineal de corriente ($I_C \approx \beta I_B$, válido si $I_{CEO} \ll \beta I_B$). |
| **Saturación** | Polarización Directa | Polarización Directa | Interruptor cerrado ($V_{CE(\text{sat})} \approx 0.2\text{ V}$ y $V_{BE(\text{sat})} \approx 0.8\text{ V}$). |
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
  1. Un incremento sutil en las corrientes $I_E$ e $I_C$ para un voltaje $V_{BE}$ constante en las curvas de entrada. Matemáticamente: $I_C = \beta I_B \left(1 + \frac{V_{CE}}{V_A}\right)$ donde $V_A$ es el Voltaje Early.
  2. Una pendiente no nula (ligera inclinación ascendente) en las curvas de características de salida, reduciendo levemente la resistencia de salida del dispositivo.

---

---

Este documento recopila y estructura las directrices metodológicas de diseño, auto-layout y diagramación de circuitos con transistores bipolares (BJT) mediante la herramienta Lcapy descritas en la Nota 2. Incluye la definición estructural de las tres configuraciones básicas (Emisor Común, Colector Común y Base Común), las reglas prácticas para la prevención del colapso físico de elementos y el correcto direccionamiento de los nodos de referencia en el motor de renderizado.

---

## 1. Configuraciones de BJT en Lcapy (Definición Estructural)

Lcapy permite representar transistores BJT del tipo NPN y PNP asociando sus tres terminales a ramas específicas de un circuito mediante nodos lógicos. Las tres topologías se caracterizan por cuál de las terminales se define como punto común o de referencia para la entrada y la salida.

### 1.1 Emisor Común (E-com)
*   **Terminal de referencia:** Emisor ($E$).
*   **Entrada:** Base ($B$).
*   **Salida:** Colector ($C$).
*   **Implementación Lcapy:** El emisor se conecta directamente a un nodo de referencia de tierra. La base se alimenta lateralmente mediante un resistor de polarización ($R_B$) y el colector se acopla verticalmente a la fuente de alimentación ($V_{CC}$) mediante una resistencia limitadora ($R_C$).

### 1.2 Colector Común (C-com) o Seguidor de Emisor
*   **Terminal de referencia:** Colector ($C$).
*   **Entrada:** Base ($B$).
*   **Salida:** Emisor ($E$).
*   **Implementación Lcapy:** El colector se conecta de forma directa a la barra de alimentación DC ($V_{CC}$), la cual actúa como tierra de corriente alterna (AC). El voltaje de salida regulado se extrae en bornes de un resistor de emisor ($R_E$) acoplado a tierra.

### 1.3 Base Común (B-com)
*   **Terminal de referencia:** Base ($B$).
*   **Entrada:** Emisor ($E$).
*   **Salida:** Colector ($C$).
*   **Implementación Lcapy:** La base del transistor se conecta directamente a la tierra del circuito, sirviendo como blindaje electrostático entre el circuito de emisor y colector.

---

## 2. Reglas Prácticas para Evitar Solapamiento y Colapso de Layout

El motor de auto-layout de Lcapy distribuye los componentes basándose en ecuaciones de malla y nodos. Sin la inclusión de tramos direccionales explícitos, Lcapy tiende a colapsar múltiples ramas verticales en el mismo eje, provocando el encimado de labels y símbolos.

### 2.1 Regla 1: Inserción de Tramos de Separación Horizontal (Cables `W`)
Para separar colector, base y emisor en columnas independientes antes de acoplarlos a sus respectivas fuentes o cargas verticales, se deben añadir de forma obligatoria tramos de cable horizontal (`W`).

*   **Ecuación Conceptual de Columna:**
    $$
    x_{\text{componente}} = x_{\text{terminal}} \pm \Delta x_{\text{cable}}
    $$
*   **Sintaxis Lcapy de Separación:**
    `W [nodo_terminal] [nodo_auxiliar]; right` o `left`
*   *Efecto:* Desplaza horizontalmente el eje de conexión, creando una columna paralela que proporciona espacio físico para la colocación limpia de rótulos (labels).

### 2.2 Regla 2: Multiplicidad de Nodos de Tierra Independientes
El uso de un único identificador global de tierra (`0`) en todos los resistores y fuentes fuerza al motor de auto-layout a fusionar todos esos terminales en la misma coordenada $x$ o $y$, distorsionando el circuito.

*   **Conjunto de Referencias Lógicas de Tierra:**
    $$
    \text{GND} = \{0_1, \; 0_2, \; 0_3, \; \ldots, \; 0_k\}
    $$
*   *Regla de Implementación:* Asignar nombres indexados a cada tierra (`0_1` para la rama de base, `0_2` para la de emisor, `0_3` para colector). Lcapy los interpretará eléctricamente como el mismo nodo común (GND) pero los separará físicamente en el espacio cartesiano de renderizado.

### 2.3 Regla 3: Evitar Elementos Verticales en Serie Ininterrumpidos
La conexión consecutiva de dos o más elementos de dirección vertical en la misma malla (por ejemplo, una resistencia de emisor $R_E$ y una fuente de señal variable $V_{in}$ conectadas directamente hacia abajo en serie) incrementa la probabilidad de colapso de componentes.

*   **Criterio de Layout Seguro:** Interrumpir o desviar la rama en serie mediante un puente horizontal corto antes de realizar la transición hacia el siguiente componente vertical.
    $$
    \text{Ruta Segura} = \text{Elemento 1 (down)} \to \text{Cable W (right)} \to \text{Elemento 2 (down)}
    $$

---

## 3. Backends y Herramientas del Sistema para Renderizado

El procesamiento visual de los circuitos en el repositorio se realiza en formato digital a partir del código de netlist.

### 3.1 Backend de Procesamiento
Para la compilación y exportación de los diagramas vectoriales y de mapa de bits (PNG/SVG) se emplean herramientas del sistema en segundo plano:
*   **`pdflatex`**: Compila el código del circuito en código LaTeX (usando paquetes como `circuitikz`).
*   **`dvisvgm`**: Convierte la salida DVI/PDF a gráficos vectoriales SVG o imágenes rasterizadas PNG de alta resolución.

### 3.2 Espaciado de Rótulos (Labels)
Los símbolos "espaciados" en las bibliotecas de Lcapy extienden las terminales físicas del transistor. Esto incrementa la separación cartesiana por defecto entre la unión física del semiconductor y los nodos de soldadura del circuito, permitiendo el espaciado necesario para alojar la nomenclatura física de los componentes ($I_C, V_{CE}, I_B, V_{BE}$) sin generar colisiones tipográficas.

---

---

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
    La corriente de salida es casi lineal y depende ligeramente de $V_{CE}$ (Efecto Early), gobernada aproximadamente por:
    $$
    I_C \approx \beta I_B
    $$
    > [!NOTE]
    > **Aproximación**: Válido cuando $I_{CEO} \ll \beta I_B$. Rigurosamente $I_C = \beta I_B + I_{CEO}$.
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

---

---

Este documento presenta de forma estructurada y analítica las ecuaciones y modelos matemáticos de las principales configuraciones de polarización en corriente directa (DC) para transistores bipolares (BJT) en emisor común (E-com) descritos en la Nota 4. Contempla el análisis de polarización fija, estabilización por resistencia de emisor, y la técnica de divisor de voltaje mediante la simplificación de equivalentes de Thévenin.

---

## 1. Relaciones Generales de Voltaje y Corriente en la Malla

Para cualquier transistor BJT operando en su región activa bajo configuración de emisor común, se cumplen las siguientes relaciones fundamentales de corriente y voltaje.

### 1.1 Ecuación de Corriente de Emisor en Región Activa
Relación directa obtenida de la Ley de Corrientes de Kirchhoff (LKC) sustituyendo la ganancia de colector ($I_C = \beta I_B$).

$$
I_E = I_B + I_C \implies I_E = (\beta + 1) I_B
$$

### 1.2 Potenciales de Nodo Respecto a Tierra
Tensiones estáticas absolutas medidas en cada terminal física del semiconductor con referencia al común (GND).

* **Voltaje de Emisor ($V_E$):** Caída de tensión debida al flujo de corriente por la resistencia de emisor.
  $$
  V_E = I_E R_E
  $$
* **Voltaje de Base ($V_B$):** Potencial de control en la base.
  $$
  V_B = V_E + V_{BE}
  $$
* **Voltaje de Colector ($V_C$):** Potencial de salida en el colector.
  $$
  V_C = V_{CC} - I_C R_C
  $$

### 1.3 Voltajes entre Terminales
Diferencia de potencial diferencial entre bornes del semiconductor.

$$
V_{CE} = V_C - V_E
$$

$$
V_{BE} = V_B - V_E
$$

---

## 2. Polarización Fija (Simple, $R_E = 0\ \Omega$)

Es la topología más simple, donde el emisor se acopla directamente a la tierra de referencia. Presenta una alta sensibilidad ante variaciones de temperatura y ganancias $\beta$.

### 2.1 Ecuación de la Malla de Entrada (Corriente de Base $I_B$)
Deducción obtenida por la Ley de Voltajes de Kirchhoff (LVK) en el lazo base-emisor.

$$
I_B = \frac{V_{CC} - V_{BE}}{R_B}
$$

### 2.2 Ecuación de la Malla de Salida (Recta de Carga DC)
Relación lineal de salida que delimita las combinaciones de voltaje y corriente.

$$
V_{CE} = V_{CC} - R_C I_C
$$

* **Puntos Extremos de la Recta:**
  * **Corte (Límite de Apagado, $I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación (Límite de Conducción Máxima, $V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C} \quad \left( \text{Real: } I_{C(\text{sat})} \approx \frac{V_{CC} - V_{CE(\text{sat})}}{R_C} \right)
    $$

---

## 3. Polarización Estabilizada por Resistencia de Emisor ($R_E \neq 0\ \Omega$)

La adición de una resistencia en el emisor introduce un lazo de retroalimentación negativa que estabiliza el punto de operación $Q$ frente a derivas térmicas o cambios en $\beta$.

### 3.1 Mecanismo de Estabilización Térmica
Cualquier factor térmico que intente elevar la corriente de colector ($I_C \uparrow$) desencadena la siguiente secuencia de compensación:

$$
I_C \uparrow \;\implies\; I_E \uparrow \;\implies\; V_E \uparrow \text{ (pues } V_E = I_E R_E\text{)} \;\implies\; V_{BE} \downarrow \text{ (pues } V_{BE} = V_B - V_E\text{)} \;\implies\; I_B \downarrow \;\implies\; I_C \downarrow
$$

### 3.2 Ecuación de la Malla de Salida (Recta de Carga DC)
Planteamiento de tensiones en el lazo colector-emisor asumiendo la aproximación $I_E \approx I_C$.

$$
V_{CE} = V_{CC} - (R_C + R_E) I_C
$$

* **Puntos Extremos de la Recta:**
  * **Corte ($I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación Ideal ($V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C + R_E}
    $$

---

## 4. Polarización por Divisor de Voltaje

Es la configuración más robusta y estable. Utiliza un divisor de tensión en la base ($R_1$ y $R_2$) para fijar el voltaje de base de manera independiente del parámetro $\beta$ del transistor. Su análisis se simplifica mediante el Teorema de Thévenin.

### 4.1 Resistencia Equivalente de Thévenin ($R_{TH}$)
Resistencia vista desde la base hacia el divisor de voltaje con la fuente DC anulada.

$$
R_{TH} = R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}
$$

### 4.2 Voltaje Equivalente de Thévenin ($V_{TH}$)
Voltaje a circuito abierto en el nodo de base (desconectando el transistor).

$$
V_{TH} = V_{CC} \cdot \frac{R_2}{R_1 + R_2}
$$

### 4.3 Ecuación de la Corriente de Base ($I_B$)
Deducción obtenida por LVK en la malla de entrada simplificada por Thévenin, donde la resistencia de emisor ($R_E$) aparece multiplicada (reflejada) en la base por el factor $(\beta + 1)$.

$$
I_B = \frac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1) R_E}
$$

### 4.4 Malla de Salida y Recta de Carga DC
* **Ecuación de la Malla de Salida Exacta:**
  $$
  V_{CE} = V_{CC} - I_C R_C - I_E R_E = V_{CC} - I_B \left[ \beta R_C + (\beta + 1) R_E \right]
  $$
* **Ecuación de la Recta de Carga DC Aproximada ($I_E \approx I_C$):**
  $$
  V_{CE} = V_{CC} - (R_C + R_E) I_C
  $$
* **Puntos Extremos de la Recta:**
  * **Corte ($I_C = 0$):**
    $$
    V_{CE} = V_{CC}
    $$
  * **Saturación Ideal ($V_{CE} = 0$):**
    $$
    I_{C(\text{sat})} = \frac{V_{CC}}{R_C + R_E}
    $$

> [!IMPORTANT]
> **Resistencia de Emisor Reflejada**: La ecuación de entrada por Thévenin demuestra que la resistencia de emisor $R_E$ se ve multiplicada por $(\beta + 1)$ cuando se analiza desde el circuito de base. Esta multiplicación virtual incrementa significativamente la impedancia vista por la fuente, limitando las variaciones de corriente de base $I_B$ ante cambios bruscos del parámetro $\beta$ debido a variaciones térmicas o de lote del transistor.

> [!WARNING]
> **Criterio de Linealidad (Polarización Inversa Colector-Base)**: Para garantizar el funcionamiento en la región activa lineal, se debe verificar que el voltaje de colector sea mayor al de base. Si no se cumple, el transistor caerá en saturación profunda.
> $$
> V_C > V_B \implies V_{CC} - I_C R_C > V_B
> $$

---

---

Este documento recopila y estructura las metodologías analíticas, criterios prácticos y fórmulas de diseño electrónico para transistores bipolares (BJT) presentadas en la Nota 5. Contempla el diseño sistemático de la polarización por divisor de voltaje (caso de estudio del transistor 2N2222) y el dimensionamiento de componentes para la operación del transistor como interruptor (switch de lado bajo) en corte y saturación.

---

## 1. Diseño de Polarización por Divisor de Voltaje (Región Activa Lineal)

El diseño de una red de polarización por divisor de voltaje estable busca fijar un punto de operación Q ($I_C, V_{CEQ}$) robusto frente a variaciones severas en el factor de ganancia de corriente ($\beta$) del transistor.

### 1.1 Criterio de Reparto de Tensiones en Tercios
Regla práctica de ingeniería empleada para distribuir simétricamente el voltaje de la fuente única $V_{CC}$ entre las caídas de los resistores de malla y el transistor, maximizando la estabilidad térmica y la excursión simétrica de señal.

$$
V_E \approx \frac{V_{CC}}{3} \quad ; \quad V_{CEQ} \approx \frac{V_{CC}}{3} \quad ; \quad V_{RC} \approx \frac{V_{CC}}{3}
$$

### 1.2 Corrientes de Malla en el Peor Caso
Cálculo de la corriente de base máxima ($I_{B,\max}$) y la corriente de emisor ($I_E$) asociadas a la mínima ganancia comercial del componente ($\beta_{\min}$), asegurando que el transistor nunca abandone la región activa.

$$
I_{B,\max} = \frac{I_C}{\beta_{\min}}
$$

$$
I_E = \frac{I_C}{\alpha_{\min}} = I_C \left( 1 + \frac{1}{\beta_{\min}} \right) \quad \text{donde} \quad \alpha_{\min} = \frac{\beta_{\min}}{\beta_{\min} + 1}
$$

### 1.3 Dimensionamiento de las Resistencias de Colector y Emisor
Cálculo de los valores óhmicos de las resistencias principales y sus potencias térmicas de disipación disipadas nominales.

*   **Resistencia de Emisor ($R_E$):**
    $$
    R_E = \frac{V_E}{I_E} \quad \implies \quad P_{R_E} = I_E^2 \cdot R_E
    $$
*   **Resistencia de Colector ($R_C$):**
    $$
    R_C = \frac{V_{CC} - V_C}{I_C} = \frac{V_{RC}}{I_C} \quad \implies \quad P_{R_C} = I_C^2 \cdot R_C
    $$
    *(Nota: El potencial estático de colector es $V_C = V_E + V_{CEQ}$).*

### 1.4 Criterio de Rigidez del Divisor (Cálculo de $R_{TH}$)
Fórmula de diseño empleada para definir la resistencia máxima equivalente del divisor en la base ($R_{TH}$). Impone que la corriente que fluye por el divisor sea al menos 10 veces mayor que la corriente de base para independizar el voltaje de base de la carga.

$$
R_{TH} \approx \frac{(\beta_{\min} + 1) R_E}{10}
$$

### 1.5 Voltaje Equivalente de Thévenin Requerido ($V_{TH}$)
Tensión de base equivalente requerida que incorpora la caída del diodo directa ($V_{BE}$) y la caída en la resistencia de Thévenin.

$$
V_{TH} = V_E + V_{BE} + I_{B,\max} R_{TH}
$$

### 1.6 Determinación Directa de las Resistencias del Divisor ($R_1$ y $R_2$)
Cálculo analítico de los resistores superior ($R_1$) e inferior ($R_2$) a partir del voltaje y resistencia de Thévenin deseados.

$$
R_1 = \frac{V_{CC}}{V_{TH}} R_{TH}
$$

$$
R_2 = \frac{V_{CC}}{V_{CC} - V_{TH}} R_{TH}
$$

*   **Potencia disipada real en las resistencias del divisor (con carga):**
    $$
    P_{R_1} \approx \frac{(V_{CC} - V_B)^2}{R_1} \quad ; \quad P_{R_2} \approx \frac{V_B^2}{R_2} \quad \text{donde} \quad V_B = V_E + V_{BE}
    $$

### 1.7 Verificación de Sensibilidad frente a Variaciones de $\beta$
Ecuaciones de validación para calcular la deriva de las corrientes de emisor y colector ante cualquier fluctuación de $\beta$.

$$
I_E(\beta) = \frac{V_{TH} - V_{BE}}{R_E + \frac{R_{TH}}{\beta + 1}} \quad \implies \quad I_C(\beta) \approx \frac{\beta}{\beta + 1} I_E(\beta)
$$

---

## 2. Transistor BJT como Interruptor (Switch de Lado Bajo)

En aplicaciones de conmutación digital, el BJT opera de manera discreta alternando entre dos zonas extremas: Corte (estado OFF, circuito abierto) y Saturación (estado ON, cortocircuito virtual).

### 2.1 Corriente de Saturación de Colector Ideal ($I_{C(\text{sat})}$)
Corriente máxima posible en la carga, limitada únicamente por la resistencia externa en serie del colector.

$$
I_{C(\text{sat})} \approx \frac{V_{CC}}{R_C} \quad \left( \text{Real: } I_{C(\text{sat})} = \frac{V_{CC} - V_{CE(\text{sat})}}{R_C} \right)
$$

### 2.2 Corriente Mínima de Base de Conmutación ($I_{B(\text{sat},\min)}$)
Corriente de control mínima requerida en la base para forzar al transistor a entrar en la región de saturación profunda.

$$
I_{B(\text{sat},\min)} = \frac{I_{C(\text{sat})}}{\beta}
$$
Para asegurar una conmutación robusta en diseño real, se sobrediseña inyectando una corriente mayor utilizando un $\beta_{\text{forzado}}$ (ej. $\beta / 5$ o $\beta = 10$):
$$
I_B \ge \frac{I_{C(\text{sat})}}{\beta_{\text{forzado}}}
$$

### 2.3 Criterios de Diseño para la Resistencia de Base de Control ($R_B$)
Cuando el circuito de control (por ejemplo, un microcontrolador o compuerta lógica) entrega una tensión de nivel alto ($V_{HI}$), la resistencia de base ($R_B$) debe limitarse para inyectar suficiente corriente y garantizar el estado ON.

*   **Límite Óhmico de la Resistencia de Base ($R_B$):**
    $$
    R_B \le \frac{(V_{HI} - V_{BE}) \cdot \beta \cdot R_C}{V_{CC}}
    $$
*   **Límite de la Resistencia de Carga de Colector ($R_C$):**
    $$
    R_C \ge \frac{V_{CC} \cdot R_B}{\beta \cdot (V_{HI} - V_{BE})}
    $$

> [!IMPORTANT]
> **Estabilidad del Divisor de Tensión**: El criterio de rigidez del divisor ($R_{TH} \approx (\beta + 1)R_E / 10$) es el pilar de la polarización estable. Asegura que la corriente circulante por el divisor sea muy superior a la corriente de base consumida por el BJT. Esto independiza de forma efectiva la tensión $V_B$ del transistor, garantizando que el punto de operación Q se mantenga casi inmóvil ante amplias variaciones de $\beta$.

> [!WARNING]
> **Factor de Sobrediseño en Conmutación**: Para asegurar una saturación profunda y confiable en aplicaciones industriales, la corriente de base real inyectada en el diseño debe ser de 2 a 5 veces superior al mínimo teórico calculado ($I_B = k \cdot I_{B(\text{sat},\min)}$ donde $k \geq 2$). Esto protege al interruptor contra caídas imprevistas del factor $\beta$ debidas a bajas temperaturas.

---

---



---

## Tema Adicional: Modelos Físicos, Parámetros AC y Otras Configuraciones

### 1. Ecuación de Shockley del BJT
La ecuación exponencial fundamental que relaciona la corriente de colector con la tensión base-emisor:
$$
I_C = I_S e^{\frac{V_{BE}}{V_T}}
$$
Derivadas importantes para pequeña señal:
* **Transconductancia ($g_m$):**
  $$
  g_m = \frac{I_C}{V_T}
  $$
* **Resistencia dinámica de emisor ($r_e$):**
  $$
  r_e = \frac{V_T}{I_E} \approx \frac{V_T}{I_C}
  $$

### 2. Parámetros Básicos de Pequeña Señal (AC) en Emisor Común
* **Ganancia de voltaje ($A_v$):**
  $$
  A_v \approx -\frac{R_C}{r_e}
  $$
* **Ganancia de corriente ($A_i$):**
  $$
  A_i \approx \beta
  $$
* **Impedancia de entrada en la base ($Z_{in(\text{base})}$):**
  $$
  Z_{in(\text{base})} \approx \beta r_e
  $$

### 3. Características Clave por Configuración
* **Base Común (B-com):**
  * Ganancia de corriente: $A_i \approx \alpha < 1$
  * Ganancia de voltaje: Alta
  * Impedancia de entrada: Muy baja
  * Impedancia de salida: Alta
* **Colector Común (C-com) o Seguidor de Emisor:**
  * Ganancia de voltaje: $A_v \approx 1$
  * Ganancia de corriente: Alta ($\beta + 1$)
  * Impedancia de entrada: Alta
  * Impedancia de salida: Baja

### 4. Estabilidad Matemática Térmica
El factor de estabilidad evalúa cuánto se desvía la corriente de colector ante variaciones térmicas en la corriente de fuga.
$$
S = \frac{\partial I_C}{\partial I_{CBO}}
$$
> [!NOTE]
> **Deriva Térmica**: Si la temperatura sube ($T \uparrow$), entonces $V_{BE} \downarrow$ y las fugas $I_{CBO} \uparrow$, lo cual fuerza a $I_C \uparrow$. La resistencia de emisor ($R_E$) es fundamental porque introduce realimentación negativa para compensar y frenar este incremento.

---

## Método Rápido de Análisis (Estrategia Práctica para Exámenes)

Este compendio de métodos prácticos te permitirá sobrevivir al 90% de los ejercicios analíticos sin perder tiempo en derivaciones físicas.

### 1. Método Universal de Polarización DC
Sigue estos pasos en orden para resolver casi cualquier circuito BJT en activa:
1. **Paso 1:** Asume siempre $V_{BE} \approx 0.7\text{ V}$ para transistores de silicio.
2. **Paso 2:** Calcula $I_B$ resolviendo la malla de entrada. Luego calcula $I_C = \beta I_B$.
3. **Paso 3:** Calcula $V_{CE}$ resolviendo la malla de salida.
4. **Paso 4:** Verifica la región analizando los voltajes obtenidos:
   * **Corte:** $V_{BE} < 0.7\text{ V}$
   * **Activa:** $V_C > V_B$
   * **Saturación:** $V_C \le V_B$ o $V_{CE} \approx 0.2\text{ V}$

### 2. Método Rápido de Recta de Carga
El examen típico exige dibujar la recta y situar el punto Q.
1. **Punto de Corte (Eje X):** Haz $I_C = 0 \implies V_{CE} = V_{CC}$
2. **Punto de Saturación (Eje Y):** Haz $V_{CE} = 0 \implies I_C = \frac{V_{CC}}{R_C + R_E}$
3. **Punto Q:** Sitúa las coordenadas $(V_{CEQ}, I_{CQ})$ halladas en el Paso 3 del método universal sobre la línea recta.

### 3. Estados de Conmutación (Switching)
Memoriza esta tabla visual para circuitos digitales:

| Estado | $I_B$ | $I_C$ | $V_{CE}$ |
|--------|-------|-------|----------|
| **Corte** (OFF) | $0$ | $0$ | $V_{CC}$ |
| **Activa** (Amp) | Media | $\beta I_B$ | Intermedio |
| **Saturación** (ON) | Alta | Máxima | $\approx 0.2\text{ V}$ |

### 4. Memorización de Gráficas
Los profesores evalúan mucho el entendimiento visual:
* **Curva de Entrada ($I_B$ vs $V_{BE}$):** Es idéntica a la curva de un diodo polarizado en directa.
* **Curva de Salida ($I_C$ vs $V_{CE}$):** Es una "familia de curvas horizontales" separadas por escalones de $I_B$.
  * **Saturación:** La pared casi vertical a la izquierda ($V_{CE} < 0.2\text{ V}$).
  * **Activa:** Las líneas horizontales en el centro.
  * **Ruptura (Breakdown):** El quiebre abrupto hacia arriba a la derecha extrema.

---
## Glosario de Variables

* **$A_i$**: Ganancia de corriente en pequeña señal (adimensional o A/A).
* **$A_v$**: Ganancia de voltaje en pequeña señal (adimensional o V/V).
* **$BV_{CEO}$**: Voltaje de ruptura colector-emisor con base en circuito abierto (V).
* **$I_B$**: Corriente continua de entrada de la base (A).
* **$I_B, I_C, I_E$**: Corrientes continuas de base, colector y emisor (A).
* **$I_C$**: Corriente continua de salida del colector (A).
* **$I_E$**: Corriente continua total del emisor (A).
* **$I_S$**: Corriente de saturación inversa intrínseca de la unión base-emisor (A).
* **$I_{C(\text{sat})}$**: Corriente de colector en saturación profunda (A).
* **$I_{CBO}$**: Corriente de fuga inversa colector-base con el emisor en circuito abierto (A).
* **$I_{CEO}$**: Corriente de fuga inversa colector-emisor con base en circuito abierto (A).
* **$R_1$**: Resistencia de polarización superior del divisor ($\Omega$).
* **$R_2$**: Resistencia de polarización inferior del divisor ($\Omega$).
* **$R_B$**: Resistencia de limitación conectada en serie con la base para control digital ($\Omega$).
* **$R_C, R_E$**: Resistencias de colector y de emisor respectivamente ($\Omega$).
* **$R_{TH}$**: Resistencia equivalente de Thévenin en la base ($\Omega$).
* **$S$**: Factor de estabilidad térmica (adimensional).
* **$V_A$**: Voltaje de Early, proyecta la convergencia de las curvas de salida en la región activa (V).
* **$V_B, V_C, V_E$**: Tensiones absolutas en bornes de base, colector y emisor (V).
* **$V_{BE(\text{sat})}$**: Voltaje de saturación base-emisor, requerido para forzar la conducción plena (V).
* **$V_{BE}$**: Caída de tensión directa base-emisor (V). Típicamente $0.7\text{ V}$ para silicio.
* **$V_{CC}$**: Fuente única de alimentación en corriente continua (V).
* **$V_{CE(\text{sat})}$**: Voltaje de saturación de conmutación del transistor en directa (V). Típicamente $0.2\text{ V}$.
* **$V_{CE}$**: Diferencia de potencial colector-emisor (V).
* **$V_{HI}$**: Voltaje lógico de nivel alto entregado por la etapa de control de entrada (V).
* **$V_{TH}$**: Voltaje equivalente de Thévenin en la base (V).
* **$W_{\text{base, efectivo}}$**: Ancho real de la base neutral donde ocurre la difusión de portadores (m).
* **$W_{\text{base, metalúrgico}}$**: Distancia física de separación de las fronteras dopadas de la base (m).
* **$W_{\text{depleción}}$**: Ancho de la zona de carga de espacio de la unión colector-base (m).
* **$Z_{in(\text{base})}$**: Impedancia de entrada vista desde el terminal de base ($\Omega$).
* **$\alpha$**: Ganancia de corriente en base común (adimensional).
* **$\beta$**: Ganancia de corriente del transistor en continua ($h_{FE}$, adimensional).
* **$\beta_{\text{forzado}}$**: Ganancia de corriente degradada o asumida forzosamente para asegurar saturación en diseño de switch (adimensional).
* **$g_m$**: Transconductancia del transistor BJT (S o A/V).
* **$r_e$**: Resistencia dinámica diferencial de emisor en el modelo $\pi$ o T ($\Omega$).
