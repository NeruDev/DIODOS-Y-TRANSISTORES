<!--
::METADATA::
type: cheatsheet
topic_id: BJT-02
file_id: tema_2-nota_2
status: stable
audience: student
last_updated: 2026-05-31
-->

# Guía de Convenciones y Diseño Esquemático de Circuitos BJT en Lcapy

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

## 4. Glosario de Términos Técnicos

* **Lcapy:** Biblioteca de Python especializada en el modelado, análisis matemático de funciones de transferencia y generación automatizada de diagramas esquemáticos de circuitos lineales.
* **Auto-layout:** Algoritmo de distribución espacial automático que calcula las coordenadas físicas ideales de los componentes de un circuito a partir de las conexiones lógicas descritas en su netlist.
* **Solapamiento (Overlap):** Error visual de renderizado en el cual símbolos de componentes, líneas de conexión o textos se sobreponen físicamente en el mismo espacio debido a la ausencia de restricciones horizontales en el netlist.
* **Nodo de Tierra Indexado:** Técnica de etiquetado lógico (`0_1`, `0_2`) empleada para separar físicamente los puntos de retorno comunes en el diagrama, manteniendo su interconexión eléctrica real.
* **Cable de Separación (Tramo W):** Elemento esquemático no resistivo de longitud fija utilizado para forzar un desplazamiento cartesiano (horizontal o vertical) en el motor de trazado.
* **Seguidor de Emisor:** Configuración de colector común caracterizada por poseer una ganancia de voltaje cercana a la unidad ($A_v \approx 1$), una alta impedancia de entrada y una muy baja impedancia de salida, ideal para el acoplamiento de etapas de potencia.
