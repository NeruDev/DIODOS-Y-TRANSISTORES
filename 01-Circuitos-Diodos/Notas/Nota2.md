# Recta de carga (análisis en CD)

La **recta de carga** se construye con base en el análisis de corriente directa (CD).  
Retomando el circuito de CD visto previamente, se tiene una batería conectada a una resistencia en su terminal positiva; la resistencia se conecta en serie con un diodo y este cierra el circuito hacia la terminal negativa de la batería.

La corriente convencional $I_D$ circula desde la terminal positiva de la batería, atraviesa la resistencia, pasa por el diodo y regresa a la terminal negativa; en el esquema se representa en **sentido horario**.

Además, se incluye una leyenda con líneas que delimitan la rama del diodo para definir $V_D$, que representa el voltaje en el diodo.

## Esquema del circuito base

![Circuito base para recta de carga](../media/generated/dio-recta-carga-circuito-vd.png)

## Ecuación de la recta de carga

Aplicando LKV en la malla:

$$
R I_D + V_D = E
$$

Despejando corriente:

$$
I_D = \frac{E - V_D}{R}
$$

Por lo tanto, para construir la recta, la ecuación se evalúa en los puntos extremos tal y como sigue (gráfica de la corriente en el eje **Y** y el voltaje en el eje **X**):

- Si $V_D = 0$ entonces $I_D = \dfrac{E}{R}$.
- Si $I_D = 0$ entonces $V_D = E$.

![Recta de carga por extremos](../media/generated/dio-recta-carga-extremos.png)

La intersección entre esta recta y la curva característica $I$–$V$ del diodo determina el **punto de operación** o **punto Q**.

## Punto de operación para pequeña señal (caso con excitación AC+CD)

Retomando los valores del ejemplo anterior, se dibuja la recta de carga de CD y la curva característica del diodo para encontrar el punto de operación que se usa en el análisis de pequeña señal.

Dado el circuito: batería de $6\,V$ conectada en su terminal positivo a una fuente de voltaje alterno, esta fuente conectada a una resistencia de $270\,\Omega$, seguida por un diodo, y con la leyenda de $V_D$ para indicar el voltaje en el diodo; la fuente alterna se expresa como:

$$
v_s(t)=2\,\mathrm{sen}(\omega t)
$$

![Circuito AC+CD para punto de operación](../media/generated/dio-circuito-ac-cd-6v-270ohm-vd.png)

Para el punto de operación en CD se usa la fuente continua $E=6\,V$ y la resistencia $R=270\,\Omega$:

Primero se plantea la recta de carga:

$$
R I_D + V_D = E
$$

Ahora se realizan los cálculos en los extremos:

1. Para $V_D=0$:

$$
R I_D + 0 = E \Rightarrow I_D = \frac{E}{R} = \frac{6}{270}=0.02222\,A=22.22\,mA
$$

2. Para $I_D=0$:

$$
R(0)+V_D=E \Rightarrow V_D=E=6\,V
$$

Con estos resultados, los puntos de la recta son:

- $(V_D, I_D) = (0\,V,\;22.22\,mA)$
- $(V_D, I_D) = (6\,V,\;0\,mA)$

Después se crea la gráfica colocando:

- Eje **Y**: corriente $I_D$ en **mA**.
- Eje **X**: voltaje $V_D$ en **V**.

La intersección entre esta recta y la curva $I$–$V$ del diodo entrega el punto $Q$ de polarización.

![Recta de carga CD y curva del diodo (punto Q)](../media/generated/dio-recta-carga-q-6v-270ohm.png)

### Diferencia entre valores en CD y valores máximos instantáneos

Los cálculos anteriores corresponden a la **recta de carga en CD** (polarización base para el punto $Q$), usando solo $E=6\,V$.

Si además se consideran los extremos instantáneos de la fuente alterna $v_s(t)=2\,\mathrm{sen}(\omega t)$, el voltaje efectivo en la malla varía entre:

$$
E_{\max}=6+2=8\,V, \qquad E_{\min}=6-2=4\,V
$$

Tomando aproximación ideal en el intercepto de corriente ($V_D\approx 0$):

$$
I_{D,\max}\approx \frac{8}{270}=29.63\,mA, \qquad
I_{D,\min}\approx \frac{4}{270}=14.81\,mA
$$

Por ello, en la gráfica se muestran:

- Recta de carga **CD** (la que fija el punto $Q$).
- Recta límite para **$E_{\max}$**.
- Recta límite para **$E_{\min}$**.

### Ejemplo adicional: ajuste de la recta y nueva $Q$ objetivo

Si inicialmente se propone el punto:

$$
Q=(I_D, V_D)=(19\,mA,\;1.5\,V)
$$

y se mantiene la resistencia del ejemplo actual $R=270\,\Omega$, entonces la fuente equivalente debe cumplir:

$$
E = R I_D + V_D
$$

Sustituyendo:

$$
E = 270(0.019)+1.5 = 6.63\,V
$$

Por lo tanto, el ajuste en los datos actuales es:

$$
\Delta E = 6.63 - 6.00 = +0.63\,V
$$

Con ese ajuste, la recta de carga queda en:

$$
I_D = \frac{6.63 - V_D}{270}
$$

y la **nueva $Q$ objetivo real** se toma como la intersección de esa recta con la curva $I$–$V$ del diodo (modelo usado en la gráfica), resultando aproximadamente:

$$
Q^* \approx (V_D\approx 0.62\,V,\; I_D\approx 22.3\,mA)
$$

En el caso con excitación AC+CD:

$$
E(t)=6+2\,\mathrm{sen}(\omega t)
$$

esa condición se cumple cuando:

$$
6+2\,\mathrm{sen}(\omega t)=6.63
\Rightarrow \mathrm{sen}(\omega t)=0.315
$$

Esto significa que el punto $(19\,mA,\;1.5\,V)$ sirve como referencia de ajuste de recta, pero la intersección física con la curva del diodo (y por tanto el punto de operación consistente del modelo) es la $Q^*$ calculada arriba.

![Recta de carga para el ejemplo objetivo Q*](../media/generated/dio-recta-carga-q-objetivo-19ma-1v5.png)

