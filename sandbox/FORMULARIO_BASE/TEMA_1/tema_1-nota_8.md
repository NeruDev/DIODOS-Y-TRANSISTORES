<!--
::METADATA::
type: cheatsheet
topic_id: DIO-01
file_id: tema_1-nota_8
status: stable
audience: student
last_updated: 2026-05-31
-->

# Formulario y Modelos para Recortadores (Limitadores) de Voltaje

Este documento recopila y estructura las ecuaciones y modelos matemáticos de los recortadores (también llamados circuitos limitadores o *clippers*) presentados en la Nota 8. Incluye el análisis de recortadores en paralelo (simples y polarizados) y recortadores en serie (polarizados con diodo directo y con diodo invertido), detallando las condiciones de umbral, tensiones límites, corrientes de conducción, voltajes de bloqueo y ángulos de conmutación.

---

## 1. Recortador Paralelo Simple y Polarizado (Biased Parallel Clipper)

En esta topología, la rama del diodo se conecta en paralelo con los terminales de salida del circuito. Su función es "fijar" la salida al voltaje umbral del diodo, absorbiendo el excedente de la tensión de entrada a través de una resistencia en serie.

### 1.1 Ecuación de la Señal de Entrada
Tensión alterna periódica sinusoidal de excitación aplicada al circuito limitador.

$$
v_s(t) = V_m \sin(\omega t)
$$

### 1.2 Condición de Polarización Directa (Conducción)
Umbral de tensión en el cual el diodo paralelo entra en estado activo, estableciendo una caída fija en la salida.

* **Caso Simple (Sin polarización externa):**
  $$
  v_s > V_K
  $$
* **Caso Polarizado (Con fuente DC en serie con el diodo):**
  $$
  v_s > V_{DC} + V_K
  $$

### 1.3 Comportamiento Dinámico del Voltaje de Salida
Voltaje transitorio en bornes de la carga en función de la tensión instantánea de entrada.

* **Caso Polarizado Positivo:**
  $$
  v_o(t) = \begin{cases} V_{DC} + V_K & \text{si } v_s(t) > V_{DC} + V_K \\ v_s(t) & \text{si } v_s(t) \leq V_{DC} + V_K \end{cases}
  $$

### 1.4 Parámetros Límites del Recortador Paralelo Polarizado
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Nivel superior de recorte fijado.
  $$
  v_{o,\max} = V_{DC} + V_K
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Semiciclo negativo que atraviesa íntegramente al diodo en bloqueo.
  $$
  v_{o,\min} = -V_m
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Voltaje máximo de bloqueo soportado cuando la entrada alcanza su mínimo negativo.
  $$
  \text{PIV} = V_m + V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Circula en el instante en que la señal de entrada alcanza su amplitud máxima positiva ($v_s = V_m$).
  $$
  I_{D,\max} = \frac{V_m - (V_{DC} + V_K)}{R}
  $$

* **Nomenclatura:**
  * $v_s(t), v_o(t)$: Voltajes transitorios instantáneos de entrada y de salida (V).
  * $V_m$: Voltaje de amplitud pico de la fuente de alterna (V).
  * $V_K$: Voltaje de umbral en directa del diodo (V). Típicamente $0.7\text{ V}$ para silicio.
  * $V_{DC}$: Voltaje de la fuente continua de polarización serie en la rama (V).
  * $R$: Resistencia limitadora de corriente en serie ($\Omega$).
  * $\text{PIV}$: Voltaje inverso de pico soportado por el semiconductor (V).
  * $I_{D,\max}$: Corriente máxima de conducción en directa a través del diodo (A).

---

## 2. Recortador Serie Polarizado (Diodo Directo)

En la configuración serie, la rama del diodo y la fuente de polarización están en serie con la carga. Su propósito es eliminar por completo la porción inferior de la señal, permitiendo el paso únicamente cuando la entrada supera el umbral establecido.

### 2.1 Ecuación Dinámica del Voltaje de Salida
La salida $v_o(t)$ se mide a través de la resistencia de carga de salida $R$.

$$
v_o(t) = \begin{cases} v_s(t) - V_{DC} - V_K & \text{si } v_s(t) > V_{DC} + V_K \\ 0 & \text{si } v_s(t) \leq V_{DC} + V_K \end{cases}
$$

### 2.2 Parámetros Límites del Recortador Serie
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Voltaje pico alcanzado en la carga.
  $$
  v_{o,\max} = V_{m} - V_{DC} - V_K
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Salida nula en el semiciclo de corte.
  $$
  v_{o,\min} = 0\text{ V}
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Tensión de bloqueo en el pico negativo de entrada.
  $$
  \text{PIV} = V_m + V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Ocurre en el pico positivo de la señal de entrada.
  $$
  I_{D,\max} = \frac{V_m - V_{DC} - V_K}{R}
  $$

### 2.3 Ángulo de Inicio de Conducción ($\theta_{\text{on}}$)
Ángulo eléctrico en el cual el diodo inicia la conducción durante la pendiente ascendente del semiciclo positivo.

$$
\theta_{\text{on}} = \arcsin\left(\frac{V_{DC} + V_K}{V_m}\right)
$$

* **Nomenclatura:**
  * $\theta_{\text{on}}$: Ángulo de conmutación de encendido (rad o grados).

---

## 3. Recortador Serie Polarizado (Diodo Invertido)

Al invertir el diodo (ánodo conectado a la fuente continua $V_{DC}$ y cátodo al nodo de salida), el circuito modifica su lógica: en lugar de anular la salida, fija un nivel de voltaje mínimo de recorte, impidiendo que la señal descienda por debajo de él.

### 3.1 Condición de Polarización Directa (Conducción)
El diodo invertido se polariza directamente cuando la entrada desciende por debajo del umbral diferencial.

$$
v_s < V_{DC} - V_K
$$

### 3.2 Ecuación Dinámica del Voltaje de Salida
El voltaje se mide en el cátodo del diodo (nodo de salida en la resistencia).

$$
v_o(t) = \begin{cases} v_s(t) & \text{si } v_s(t) \geq V_{DC} - V_K \\ V_{DC} - V_K & \text{si } v_s(t) < V_{DC} - V_K \end{cases}
$$

### 3.3 Parámetros Límites del Diodo Invertido
* **Voltaje Máximo de Salida ($v_{o,\max}$):** Amplitud máxima positiva, la cual pasa sin alteración.
  $$
  v_{o,\max} = V_{m}
  $$
* **Voltaje Mínimo de Salida ($v_{o,\min}$):** Nivel inferior de recorte fijado.
  $$
  v_{o,\min} = V_{DC} - V_K
  $$
* **Tensión Inversa de Pico del Diodo (PIV):** Voltaje máximo de bloqueo soportado, que ocurre en el pico positivo de la entrada ($v_s = V_m$).
  $$
  \text{PIV} = V_m - V_{DC}
  $$
* **Corriente Máxima por el Diodo ($I_{D,\max}$):** Circula cuando la entrada alcanza su mínimo absoluto en el semiciclo negativo ($v_s = -V_m$).
  $$
  I_{D,\max} = \frac{V_{DC} - V_K + V_m}{R}
  $$

### 3.4 Ángulo de Corte de Conducción ($\theta_{\text{off}}$)
Ángulo eléctrico en el cual la señal cruza el límite de umbral y el diodo apaga.

$$
\theta_{\text{off}} = \arcsin\left(\frac{V_{DC} - V_K}{V_m}\right)
$$

* **Nomenclatura:**
  * $\theta_{\text{off}}$: Ángulo de conmutación de apagado (rad o grados).

> [!WARNING]
> **Tensión Inversa de Pico (PIV) en Recortadores**: La adición de una fuente DC de polarización modifica severamente el voltaje de bloqueo inverso. En recortadores paralelo y serie directos, el PIV es la suma de voltajes ($\text{PIV} = V_m + V_{DC}$). Si $V_{DC}$ es elevado, el diodo puede entrar fácilmente en ruptura inversa en el semiciclo opuesto. El diodo seleccionado debe cumplir con holgura la condición $V_{BR} > V_m + V_{DC}$.

> [!IMPORTANT]
> **Diferencia Fundamental entre Serie y Paralelo**: 
> * El **recortador paralelo** preserva la forma de onda original de la señal en bornes de la carga y únicamente "corta" o recorta los picos que exceden el umbral establecido.
> * El **recortador serie** tradicional (diodo directo) **elimina** por completo la señal que se encuentra por debajo del umbral, provocando que la salida sea nula ($0\text{ V}$) durante los intervalos de corte.

---

## 4. Glosario de Términos Técnicos

* **Recortador (Limitador):** Red no lineal de diodos diseñada para limitar o recortar la amplitud máxima o mínima instantánea de una señal de entrada variable a un nivel preestablecido.
* **Recortador Paralelo:** Configuración en la cual el diodo se conecta en paralelo con la carga, fijando el potencial de salida y forzando la disipación del excedente sobre una resistencia en serie.
* **Recortador Serie:** Configuración en la cual el diodo está en línea con la trayectoria de corriente de la carga, actuando como un interruptor de umbral que interrumpe o desplaza la transmisión de la señal.
* **Recortador Polarizado:** Circuito limitador que integra una fuente de tensión continua (DC) en serie con el diodo, permitiendo elevar o desplazar el nivel de recorte a cualquier valor deseado.
* **Ángulo de Conducción ($\theta_{\text{on}}$):** Instante medido en grados o radianes de la fase angular de entrada en el cual el diodo supera su umbral de polarización y comienza a conducir corriente activa.
* **Diodo Invertido:** Variante de conexión en la cual el cátodo se orienta hacia la carga y el ánodo a la fuente DC, invirtiendo el sentido de conducción para establecer una fijación de voltaje mínimo de salida.
* **Nivel de Recorte:** Voltaje umbral de salida del recortador ($V_{DC} \pm V_K$), determinado por la combinación algebraica del voltaje de la fuente continua y la caída intrínseca de silicio.
