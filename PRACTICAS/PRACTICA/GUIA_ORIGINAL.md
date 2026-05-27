# INSTITUTO TECNOLOGICO DE TOLUCA

## Diodos y Transistores
### Examen Práctico UNIDAD-IV

**Objetivo.** — La presente práctica tiene como objetivo el aplicar un transistor como amplificador de señal configurado en emisor común, en donde para esto se determinarán los parámetros de pequeña señal y valores de ganancia.

### ➢ Material:

1. Transistor BC-548-B
2. Resistencias según diseño
3. Capacitores: $C_1 = 47 \, \mu\text{F}$, $C_2 = 100 \, \mu\text{F}$ y $C_3 = 10 \, \mu\text{F}$

### ➢ Equipo:

1. Multímetro digital
2. Fuente de Alimentación
3. Generador de Señales
4. Osciloscopio

### Procedimiento:

1. Diseñe un amplificador de señal con base al transistor BC 548B en configuración de emisor común, utilizando la $\beta$ mínima, $I_C = 50 \, \text{mA}$, $V_{CC} = 15 \, \text{V}$, $V_{BE} = 0.7 \, \text{V}$, $R_S = 50 \, \Omega$, $V_s = 100 \, \text{mV}$, en donde la ganancia requerida en lazo abierto es de:

$$
|A_{vo}| \ge 40
$$

2. Aplique el procedimiento visto en clase para calcular los parámetros de pequeña señal y sus ganancias.
3. Mida la ganancia de voltaje en el osciloscopio:

$$
A_v = \frac{V_o}{V_s}
$$

4. Elimine $R_{E1}$ y cambie a $R_E$ y nuevamente verifique la ganancia en voltaje total; $A_v$
5. Varíe la frecuencia del generador y observe el cambio que existe en amplitud y fase con respecto a las señales de entrada y salida.

> **[Diagrama de Circuito]:** En el fondo del documento se aprecia una marca de agua tenue que muestra el esquema de un amplificador emisor común con polarización por divisor de tensión. El circuito consta de una fuente de alimentación $V_{CC}$ de $15 \, \text{V}$, resistencias de polarización en la base ($R_1$ y $R_2$), resistencia de colector ($R_C$) y una red de emisor con resistencias de estabilización ($R_{E1}$ y $R_{E2}$ o $R_E$). Cuenta con capacitores de acoplamiento de entrada ($C_1$), de salida ($C_2$) y un capacitor de desacoplo de emisor ($C_3$).


# Netlist de SPICE — Amplificador Emisor Común

A continuación se presenta la conversión del circuito electrónico de la segunda imagen a formato de netlist compatible con simuladores tipo SPICE (LTspice, PSpice, Ngspice). 

Dado que los valores de las resistencias de polarización ($R_1$, $R_2$, $R_C$ y $R_E$) se especifican "según diseño" en la guía de la práctica, se han declarado utilizando la directiva `.param` con valores comerciales típicos a modo de marcador de posición (*placeholder*) para que la netlist sea completamente funcional desde el inicio.

```spice
* Amplificador Emisor Común - Transistor BC548B
* Conversión automatizada por MarkLaTeX

* =================================================================
* PARÁMETROS DE DISEÑO (Modificar valores según cálculos de la práctica)
* =================================================================
.param r1_val = 22k      ; Resistencia de polarización superior
.param r2_val = 4.7k     ; Resistencia de polarización inferior
.param rc_val = 1.2k     ; Resistencia de colector
.param re_val = 150      ; Resistencia de emisor (RE total)

* =================================================================
* FUENTES DE ALIMENTACIÓN Y SEÑAL
* =================================================================
* Fuente de alimentación de CD (15V)
Vcc VCC 0 DC 15V

* Generador de señales (VOFF=0, VAMPL=1mV, FREQ=1kHz)
V2 N_source 0 SIN(0 1mV 1k) AC 1mV

* =================================================================
* COMPONENTES DEL CIRCUITO
* =================================================================
* Red de entrada y acoplamiento
R5 N_source N_in 50
C1 N_in N_B 47uF

* Red de polarización y carga del transistor
R1 VCC N_B {r1_val}
R2 N_B 0 {r2_val}
RC VCC N_C {rc_val}
RE N_E 0 {re_val}
C3 N_E 0 100uF

* Transistor BJT (Conexión: Colector Base Emisor)
Q1 N_C N_B N_E BC548B

* Red de salida y carga
C2 N_C N_out 10uF
R6 N_out 0 1k

* =================================================================
* MODELO DEL TRANSISTOR Y COMANDOS DE SIMULACIÓN
* =================================================================
* Modelo estándar para el transistor NPN BC548B
.model BC548B NPN(Is=14.17f Xti=3 Eg=1.11 Vaf=100 Bf=300 Ne=1.428 Ise=14.17f 
+ Ikf=99.27m Xtb=1.5 Br=4.444 Nc=2 Isc=0 Ikr=0 Rc=1 Cjc=9.377p Mjc=.3526 
+ Vjc=.5 Fc=.5 Cje=13p Mje=.3347 Vje=.5 Tr=474.3n Tf=411.1p Itf=.17 Vtf=5 Xtf=8 Rb=10)

* Análisis propuestos:
.tran 10u 5m             ; Análisis transitorio para observar la señal en el tiempo
.ac dec 20 10 100meg     ; Respuesta en frecuencia (Amplitud y Fase)

.end