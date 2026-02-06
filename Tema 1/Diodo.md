<!-- 
METADATA DEL DOCUMENTO
----------------------
Última actualización: 06 de Febrero, 2026
Estado: Borrador Avanzado
Módulos implementados:
  - Definición teórica y Ecuación de Shockley.
  - Regiones de operación (Directa, Inversa, Ruptura).
  - Efectos de la temperatura (Coeficientes térmicos).
  - Galería de gráficos (Python generada): Curva Global + Zoom Inversa.
  - Ejemplo práctico de cálculo numérico (20°C vs 100°C).
Pendiente:
  - Añadir simulaciones de otros semiconductores.
  - Añadir circuito equivalente.
-->

# El Diodo

El diodo es un componente electrónico de dos terminales que permite la circulación de la corriente eléctrica a través de él en un solo sentido, bloqueando el paso si la corriente circula en sentido contrario.

## Curva Característica del Diodo

La relación entre la corriente ($I$) que atraviesa un diodo y el voltaje ($V$) en sus terminales no es lineal. Esta relación se describe mediante la **Ecuación de Shockley**:

$$ I = I_S (e^{V/n V_T} - 1) $$

Donde:
- $I_S$ es la corriente de saturación inversa.
- $V_T$ es el voltaje térmico (aprox. 26mV a temperatura ambiente).
- $n$ es el factor de idealidad.

---

### Conceptos Fundamentales en la Curva V-I

A continuación se definen los parámetros clave observados en la gráfica:

#### 1. Voltaje de Umbral ($V_K$ o $V_{th}$)
También conocido como voltaje de codo o de rodilla. Es el valor de voltaje en polarización directa a partir del cual la barrera de potencial de la unión PN es superada y la corriente comienza a incrementarse **exponencialmente**.
- Silicio (Si): $\approx 0.7V$
- Germanio (Ge): $\approx 0.3V$
- Arseniuro de Galio (GaAs): $\approx 1.2V$

#### 2. Corriente Inversa de Fuga ($I_S$)
Es la pequeña corriente que fluye a través del diodo cuando está polarizado inversamente (pero antes de llegar a la ruptura).
- Se debe fundamentalmente a los portadores minoritarios generados térmicamente.
- Es extremadamente pequeña (del orden de nanoamperios $nA$ o picoamperios $pA$), por lo que en muchas aplicaciones se considera cero idealmente. Sin embargo, **no es cero**, y varía con la temperatura.

#### 3. Voltaje Inverso Aplicado ($V_R$)
Es el rango de voltaje negativo aplicado a los terminales del diodo (ánodo negativo respecto al cátodo). En esta región, la barrera de potencial interna aumenta, impidiendo el flujo de portadores mayoritarios, resultando en la condición de "bloqueo".

#### 4. Voltaje de Rompimiento Inverso ($V_{BR}$ o $V_{Z}$)
Es el valor crítico de voltaje inverso donde el diodo entra en la región de ruptura. Al alcanzar este potencial negativo extenso:
- Ocurre el efecto **Avalancha** o **Zener**.
- La corriente inversa aumenta drásticamente.
- El voltaje a través del diodo se mantiene casi constante mientras la corriente varía ampliamente.

---

### Regiones de Operación

#### 1. Región Directa ($V > 0$)
Cuando se aplica un voltaje positivo en el ánodo respecto al cátodo (polarización directa):
- **Inicio de conducción:** El diodo comienza a conducir corriente de manera significativa una vez que se supera el **voltaje umbral** (o voltaje de rodilla, $V_K$).
- **Voltaje Típico:** Para diodos de silicio, este umbral es aproximadamente **0.7V**. Para germanio, es alrededor de **0.3V**.
- **Comportamiento:** La corriente aumenta exponencialmente con pequeños incrementos de voltaje por encima del umbral. El diodo actúa casi como un interruptor cerrado (resistencia muy baja).

#### 2. Región Inversa ($0 > V > V_{BR}$)
Cuando se aplica un voltaje negativo pero sin superar el límite de ruptura:
- **Bloqueo:** El diodo impide el paso de corriente significativa, actuando como un interruptor abierto.
- **Corriente de Fuga ($I_S$):** Existe una corriente minúscula y constante llamada corriente de saturación inversa ($I_S$), del orden de nano o pico amperios.

#### 3. Región de Ruptura ($V \le V_{BR}$)
Si el voltaje inverso se hace más negativo que el voltaje de ruptura ($V_{BR}$):
- **Avalancha Exponencial:** La corriente aumenta drásticamente en magnitud (sentido negativo). La curva adopta una forma casi vertical o exponencial negativa.
- **Mecanimso:** Ocurre por efecto Avalancha (multiplicación de portadores por impacto) o efecto Zener (efecto de campo eléctrico intenso).
- **Control:** En diodos _Zener_, esta región se usa para regulación de voltaje. En diodos rectificadores comunes, entrar en esta zona suele destruir el componente por exceso de potencia disipada ($P = V \cdot I$).

### Efectos de la Temperatura

La temperatura es un factor crítico que afecta el comportamiento del diodo tanto en polarización directa como inversa. Los semiconductores son muy sensibles a cambios térmicos porque el calor genera más portadores de carga libres (pares electrón-hueco).

#### 1. En Polarización Directa ($V_D$)
Al **aumentar** la temperatura, el voltaje necesario para producir una misma corriente disminuye.
- **Razón:** El incremento de energía térmica facilita que los portadores superen la barrera de potencial.
- **Coeficiente de Temperatura:** El voltaje de encendido ($V_D$) disminuye aproximadamente **2.5 mV por cada 1°C** de aumento en la temperatura.
  $$ \frac{\Delta V_D}{\Delta T} \approx -2.5 \ mV/^\circ C $$

  Para aplicaciones de precisión, el nuevo **Voltaje de Umbral ($V_{th}$)** debido al cambio térmico se calcula con la fórmula completa:
  $$ V_{th}(T_j) = V_{th}(T_o) + K_{TC} \cdot (T_j - T_o) $$

  Donde:
  - $V_{th}(T_j)$: Voltaje de umbral a la temperatura de la unión actual.
  - $V_{th}(T_o)$: Voltaje de umbral a la temperatura de referencia (usualmente $25^\circ C$ o $20^\circ C$).
  - $K_{TC}$: Coeficiente de temperatura del voltaje (típicamente $-2.5 \times 10^{-3} V/^\circ C$ para Silicio).
  - $T_j$: Temperatura de la unión actual.
  - $T_o$: Temperatura de referencia (ambiente).

- **Consecuencia:** Un diodo "caliente" conduce corriente más fácilmente que uno frío.

#### 2. En Polarización Inversa ($I_S$)
Al **aumentar** la temperatura, la corriente de fuga aumenta drásticamente.
- **Razón:** Se generan más portadores minoritarios debido a la agitación térmica en el material semiconductor.
- **Regla Empírica:** La corriente de saturación inversa ($I_S$) se **duplica por cada 10°C** de aumento en la temperatura.
  $$ I_S(T_2) \approx I_S(T_1) \ 2^{(T_2 - T_1) / 10} $$
- **Consecuencia:** El diodo se vuelve menos "ideal" como bloqueador de corriente a altas temperaturas.

#### 3. En la Región de Ruptura ($V_{Z}$)
El efecto de la temperatura depende del mecanismo físico predominante:
- **Efecto Zener ($V_Z < 5V$):** Coeficiente de temperatura negativo (el voltaje de ruptura disminuye al calentarse).
- **Efecto Avalancha ($V_Z > 5V$):** Coeficiente de temperatura positivo (el voltaje de ruptura aumenta al calentarse).

---

## Galería de Visualizaciones y Simulaciones

Esta sección contiene las gráficas generadas computacionalmente para ilustrar los conceptos teóricos.

### 1. Curva Característica Global
Muestra la curva completa del diodo, incluyendo las zonas de conducción ideal y ruptura.
![Curva Característica Global](curva_diodo_general.png)

### 2. Detalles de la Región Inversa (Zoom)
A menudo se simplifica diciendo que la corriente en inversa es cero. Sin embargo, al hacer un **zoom** a escala microscópica, observamos la **Corriente de Fuga ($I_S$)**.

Esta gráfica muestra específicamente la magnitud del desfase entre el eje cero (corriente nula) y la curva real de corriente de fuga:
![Zoom Región Inversa](curva_diodo_zoom_inversa.png)

> **Nota Técnica:** Las gráficas anteriores fueron generadas automáticamente utilizando el script `curva_diodo.py` ubicado en esta misma carpeta, el cual utiliza la ecuación teórica de Shockley para modelar el comportamiento.

---

### Ejemplos de Cálculo

#### Ejemplo 1: Ecuación de Shockley y Corriente

**Problema:**
Un diodo de silicio tiene una corriente de fuga ($I_S$) de 0.1 pA a 20°C.
1. Encontrar la corriente del diodo cuando se polariza directamente con 0.55V a 20°C.
2. Encontrar la corriente con el mismo diodo cuando la temperatura se incrementa a 100°C.

**Solución:**

**Parte A: Temperatura a 20°C**
Datos:
- $V = 0.55 V$
- $I_S = 0.1 pA = 1 \times 10^{-13} A$
- $T = 20^\circ C = 293 K$
- $n = 1$ (asumiremos comportamiento ideal)

Primero calculamos el voltaje térmico $V_T$:
$$ V_T = \frac{k T}{q} \approx \frac{293}{11600} \approx 0.02526 V $$

Usamos la ecuación de Shockley:
$$ I_D = I_S (e^{V / (n V_T)} - 1) $$
$$ I_D = 10^{-13} (e^{0.55 / 0.02526} - 1) $$
$$ I_D = 10^{-13} (e^{21.77} - 1) \approx 10^{-13} (2.85 \times 10^9) $$
$$ I_D \approx 0.285 \times 10^{-3} A = \mathbf{0.285 \ mA} $$

**Parte B: Temperatura a 100°C**
Datos nuevos:
- $T_{nuevo} = 100^\circ C$
- $\Delta T = 100 - 20 = 80^\circ C$

*Paso 1: Calcular la nueva $I_S$*
La corriente de fuga se duplica cada 10°C:
$$ Factor = 2^{(\Delta T / 10)} = 2^{(80 / 10)} = 2^8 = 256 $$
$$ I_S' = I_S \times 256 = 0.1 pA \times 256 = 25.6 pA = 2.56 \times 10^{-11} A $$

*Paso 2: Calcular el nuevo $V_T$*
$$ V_T' = \frac{k T'}{q} \approx \frac{273 + 100}{11600} \approx 0.03216 V $$

*Paso 3: Calcular la nueva corriente $I_D$*
$$ I_D' = I_S' (e^{V / (n V_T')} - 1) $$
$$ I_D' = 2.56 \times 10^{-11} (e^{0.55 / 0.03216} - 1) $$
$$ I_D' = 2.56 \times 10^{-11} (e^{17.1} - 1) $$
$$ I_D' \approx 2.56 \times 10^{-11} (2.67 \times 10^7) $$
$$ I_D' \approx 6.84 \times 10^{-4} A = \mathbf{0.684 \ mA} $$

**Conclusión:**
Al pasar de 20°C a 100°C, a pesar de que el término exponencial disminuye (debido al aumento de $V_T$), el aumento drástico de la corriente de fuga $I_S$ domina, haciendo que la corriente total del diodo aumente más del doble (de 0.285 mA a 0.684 mA) para el mismo voltaje aplicado.

---

#### Ejemplo 2: Variación del Voltaje de Umbral ($V_{th}$)

**Problema:**
El voltaje de umbral $V_{th}$ de un diodo de silicio es de 0.7V a 25°C. Determine el voltaje de umbral $V_{th}$ cuando la temperatura de la unión ($T_j$) aumenta a 100°C.

**Solución:**

Datos Generales:
- $V_{th}(T_o) = 0.7 V$
- $T_o = 25^\circ C$
- $K_{TC} = -2.5 \ mV/^\circ C = -0.0025 \ V/^\circ C$ (valor típico para Silicio)

**Inciso a) Para $T_j = 100^\circ C$**

1. Calculamos el cambio de temperatura:
   $$ \Delta T = 100^\circ C - 25^\circ C = 75^\circ C $$

2. Calculamos el cambio de voltaje:
   $$ \Delta V = K_{TC} \cdot \Delta T = (-0.0025 \ V/^\circ C) \cdot 75^\circ C = -0.1875 \ V $$

3. Calculamos el voltaje final:
   $$ V_{th}(100^\circ C) = 0.7 \ V - 0.1875 \ V = \mathbf{0.5125 \ V} $$

**Inciso b) Para $T_j = -100^\circ C$**

1. Calculamos el cambio de temperatura:
   $$ \Delta T = -100^\circ C - 25^\circ C = -125^\circ C $$

2. Calculamos el cambio de voltaje:
   $$ \Delta V = K_{TC} \cdot \Delta T = (-0.0025 \ V/^\circ C) \cdot (-125^\circ C) = +0.3125 \ V $$

3. Calculamos el voltaje final:
   $$ V_{th}(-100^\circ C) = 0.7 \ V + 0.3125 \ V = \mathbf{1.0125 \ V} $$

**Conclusión:**
- Al **calentar** el diodo a 100°C, el voltaje de umbral disminuye a **0.51 V** (es más fácil de encender).
- Al **enfriar** el diodo a -100°C, el voltaje de umbral aumenta a **1.01 V** (es más difícil de encender).

---

### Gráfica del Efecto de la Temperatura

A continuación se muestra una simulación gráfica de los tres casos calculados en el **Ejemplo 2**:
- **Línea Roja (100°C):** El diodo se "activa" mucho antes ($V_{th} \approx 0.51V$).
- **Línea Azul (25°C):** Comportamiento estándar ($V_{th} \approx 0.70V$).
- **Línea Verde (-100°C):** Se requiere mucho más voltaje para encender el diodo ($V_{th} \approx 1.01V$).

A continuación se presentan tres vistas detalladas de las regiones de operación:

### 1. Región Directa (Encendido)
Se aprecia claramente el desplazamiento del voltaje de umbral. A 100°C (Rojo), el diodo conduce significativamente antes.
![Región Directa](curva_temp_directa.png)

### 2. Región Inversa (Zoom - Corriente de Fuga)
En esta escala ampliada (picoamperios/nanoamperios), vemos que la corriente de fuga aumenta drásticamente con la temperatura, aunque sigue siendo muy pequeña para propósitos generales.
![Región Inversa](curva_temp_inversa.png)

### 3. Región de Ruptura
El voltaje de ruptura se mantiene relativamente estable (en este modelo $V_{BR} \approx -5V$), pero la pendiente de la avalancha es pronunciada.
![Región Ruptura](curva_temp_ruptura.png)
