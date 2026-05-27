# Formularios y Ecuaciones: JFET Canal-N

### Imagen 1

$$
V_{DS(sat)} = V_{GS} - V_P
$$

---

### Imagen 2

La ecuación para la Parábola es:

$$
I_D = I_{DSS} \left( \frac{V_{DS(sat)}}{V_P} \right)^2
$$

---

### Imagen 3

$$
I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2
$$

---

### Imagen 4

Para asegurar que el punto Q se encuentra en la región de estrangulamiento, se debe cumplir que:

$$
|V_{DS}| > |V_P| - |V_{GS}|
$$

---

### Imagen 5

$$
\begin{aligned}
I_D &= I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2 \quad - (1) \\
y \quad V_{GS} &= I_D R_S \quad - (2)
\end{aligned}
$$

Sustituyendo (2) en (1):

$$
\begin{aligned}
\Rightarrow I_D &= I_{DSS} \left[ 1 - \frac{I_D R_S}{V_P} \right]^2 \\
\therefore I_D &= I_{DSS} \left\{ 1 - 2\frac{I_D R_S}{V_P} + \left( \frac{R_S I_D}{V_P} \right)^2 \right\} \\
I_D &= \left( \frac{R_S}{V_P} \right)^2 I_{DSS} I_D^2 - 2\left( \frac{R_S}{V_P} \right) I_{DSS} I_D + I_{DSS} \\
\Rightarrow \left( \frac{R_S}{V_P} \right)^2 I_{DSS} I_D^2 &+ \left[ -2\left( \frac{R_S}{V_P} \right) I_{DSS} - 1 \right] I_D + I_{DSS} = 0
\end{aligned}
$$

---

### Imagen 6

Multiplicando la expresión anterior por: $(V_P)^2$:

$$
\Rightarrow R_S^2 I_{DSS} I_D^2 - \left[ 2 R_S V_P + \frac{V_P^2}{I_{DSS}} \right] I_{DSS} I_D + I_{DSS} V_P^2 = 0
$$

Factorizando $I_{DSS}$ y despejándola; Finalmente queda un polinomio de segundo orden, el cual se resuelve para $I_D$.

$$
\therefore R_S^2 I_D^2 - \left[ 2 R_S V_P + \frac{V_P^2}{I_{DSS}} \right] I_D + V_P^2 = 0
$$

Aplicando fórmula general:

---

### Imagen 7

$$
I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}
$$

donde:

$$
\begin{aligned}
A &= R_S^2 \\
B &= - \left[ 2 R_S |V_P| + \frac{V_P^2}{I_{DSS}} \right] \\
C &= V_P^2
\end{aligned}
$$

Finalmente:

$$
\begin{aligned}
|V_{DS}| &= |V_{DD}| - I_D(R_D + R_S) > 0 \quad \text{Para un canal - N} \\
|V_{GS}| &= I_D R_S < 0 \quad \text{Para un canal - N}
\end{aligned}
$$

---

### Imagen 8

$$
I_D = \frac{-B - \sqrt{B^2 - 4AC}}{2A}
$$

donde:

$$
\begin{aligned}
A &= R_S^2 \\
B &= - \left[ 2(|V_P| + |V_G|) R_S + \frac{V_P^2}{I_{DSS}} \right] \\
C &= (|V_P| + |V_G|)^2
\end{aligned}
$$

$$
\begin{aligned}
|V_G| &= \frac{R_2}{R_1 + R_2} |V_{DD}| \\
|V_{DS}| &= |V_{DD}| - I_D(R_D + R_S) \quad \text{; Positivo para un canal-N} \\
|V_{GS}| &= |V_G| - I_D R_S \quad \text{; Negativo para un canal - N}
\end{aligned}
$$

---

### Imagen 9

**Diseño de Autopolarización**

$$
R_S = \frac{-B - \sqrt{B^2 - 4AC}}{2A}
$$

donde:

$$
\begin{aligned}
A &= I_D^2 \\
B &= -2|V_P|I_D \\
C &= V_P^2 \left( 1 - \frac{I_D}{I_{DSS}} \right) \\
R_D &= \frac{|V_{DD}| - |V_{DS}| - I_D R_S}{I_D}
\end{aligned}
$$

---

### Imagen 10

**Diseño de Polarización Por divisor de voltaje.**
(JFET canal - N)

$$
|V_G| = \frac{I_{D1}(|V_{GS2}| - |V_{GS1}|)}{I_{D2} - I_{D1}} - |V_{GS1}|
$$

donde; $(V_{GS1}, I_{D1})$ y $(V_{GS2}, I_{D2})$ es el rango permitido del punto de operación de la curva de transferencia.

$$
R_S = \frac{-B - \sqrt{B^2 - 4AC}}{2A}
$$

donde:

$$
\begin{aligned}
A &= I_D^2 \\
B &= -2(|V_P| + |V_G|) I_D \\
C &= (|V_P| + |V_G|)^2 - V_P^2 \frac{I_D}{I_{DSS}} \\
R_D &= \frac{|V_{DD}| - |V_{DS}| - I_D R_S}{I_D}
\end{aligned}
$$

> **[Diagrama de Circuito]:** Esquema de polarización por divisor de voltaje para un transistor JFET (canal N). El terminal de drenaje (Drain) se conecta a la tensión $+V_{DD}$ mediante la resistencia $R_D$. El terminal de fuente (Source) se conecta a tierra mediante la resistencia $R_S$. La compuerta (Gate) está conectada al nodo intermedio de un divisor de tensión resistivo formado por $R_1$ (conectada a $+V_{DD}$) y $R_2$ (conectada a tierra). El diagrama indica el flujo de la corriente de drenaje $I_D$ hacia el transistor y la caída de tensión $V_{DS}$ entre el drenaje y la fuente.

---

### Imagen 11

Seleccionando $R_2$:

$$
\Rightarrow R_1 = \frac{R_2 (|V_{DD}| - |V_G|)}{|V_G|}
$$