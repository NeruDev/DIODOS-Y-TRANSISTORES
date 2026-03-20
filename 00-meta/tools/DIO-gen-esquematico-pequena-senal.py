"""
DIO-gen-esquematico-pequena-senal.py
───────────────────
Genera diagramas esquemáticos para el análisis de pequeña señal del diodo:
  1. Circuito DC original — malla cerrada (V_in + R + Diodo)
  2. Modelo equivalente de pequeña señal — malla cerrada (v_s + R + r_d)
  3. Circuito completo con señal AC superpuesta a DC — malla cerrada
  4. Gráfica de recta de carga con curva I-V y punto Q
  5. Gráfica de linealización alrededor del punto Q (pequeña señal)
  6. Formas de onda temporales: v_s(t), i_D(t) y v_D(t)

::SCRIPT_METADATA::
script_id: DIO-gen-esquematico-pequena-senal
module: DIO
generates:
  - circuito_dc_diodo.png
  - modelo_pequena_senal.png
  - circuito_ac_superpuesto.png
  - recta_de_carga_punto_q.png
  - diodo_pequena_senal.png
  - formas_de_onda_temporal.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota1.md
last_updated: 2026-02-13

Todos los circuitos se dibujan como mallas cerradas (lazos rectangulares)
para que el camino de la corriente sea claro y didáctico.
No se usa tierra porque son circuitos serie de una sola malla.

Salida:
  - topics/01-circuitos-diodos/assets/circuito_dc_diodo.png
  - topics/01-circuitos-diodos/assets/modelo_pequena_senal.png
  - topics/01-circuitos-diodos/assets/circuito_ac_superpuesto.png
  - topics/01-circuitos-diodos/assets/recta_de_carga_punto_q.png
  - topics/01-circuitos-diodos/assets/diodo_pequena_senal.png
  - topics/01-circuitos-diodos/assets/formas_de_onda_temporal.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-esquematico-pequena-senal.py
"""

import schemdraw
import schemdraw.elements as elm
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os

# Directorio de salida
OUTPUT_DIR = os.path.join("topics", "01-circuitos-diodos", "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# FIGURA 1: Circuito DC — Malla cerrada rectangular
#   V_in → R → Diodo → regreso a V_in
#   Labels con offsets para evitar superposición con símbolos
# ============================================================
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'circuito_dc_diodo.png'),
                       show=False, dpi=150) as d:
    d.config(fontsize=14)
    # Rama izquierda: fuente DC (de abajo hacia arriba)
    d += (V := elm.SourceV().up().label('$V_{in}$', loc='left', ofst=0.3))
    # Rama superior: resistencia (de izquierda a derecha)
    d += elm.Line().right(1)
    d += (R := elm.Resistor().right().label('$R$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(R).label('$I_D$', loc='top', ofst=0.6)
    d += elm.Line().right(1)
    # Rama derecha: diodo (de arriba hacia abajo)
    d += (D := elm.Diode().down().label('$D$', loc='right', ofst=0.3))
    # Rama inferior: cierre de malla (de derecha a izquierda)
    d += elm.Line().left().tox(V.start)
    # Indicadores de voltaje V_D (terminales abiertas a la derecha del diodo)
    d += elm.Line().right(1.8).at(D.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$V_D$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

print("✅ Generada: circuito_dc_diodo.png")


# ============================================================
# FIGURA 2: Modelo equivalente de pequeña señal — Malla cerrada
#   v_s(t) → R → r_d → regreso a v_s
#   El diodo se reemplaza por la resistencia dinámica r_d
# ============================================================
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'modelo_pequena_senal.png'),
                       show=False, dpi=150) as d:
    d.config(fontsize=14)
    # Rama izquierda: fuente AC (de abajo hacia arriba)
    d += (Vs := elm.SourceSin().up().label('$v_s$', loc='left', ofst=0.3))
    # Rama superior: resistencia R
    d += elm.Line().right(1)
    d += (R := elm.Resistor().right().label('$R$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(R).label('$i_d$', loc='top', ofst=0.6)
    d += elm.Line().right(1)
    # Rama derecha: resistencia dinámica r_d (de arriba hacia abajo)
    d += (Rd := elm.Resistor().down().label('$r_d$', loc='right', ofst=0.3))
    # Rama inferior: cierre de malla
    d += elm.Line().left().tox(Vs.start)
    # Indicadores de voltaje v_d
    d += elm.Line().right(1.8).at(Rd.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$v_d$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

print("✅ Generada: modelo_pequena_senal.png")


# ============================================================
# FIGURA 3: Circuito completo DC + AC superpuesta — Malla cerrada
#   V_DC + v_s(t) en serie → R → Diodo → regreso
# ============================================================
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'circuito_ac_superpuesto.png'),
                       show=False, dpi=150) as d:
    d.config(fontsize=14)
    # Rama izquierda: fuente DC + fuente AC en serie (de abajo hacia arriba)
    d += (Vdc := elm.SourceV().up().label('$V_{DC}$', loc='left', ofst=0.3))
    d += (Vac := elm.SourceSin().up().label('$v_s(t)$', loc='left', ofst=0.3))
    # Rama superior: resistencia
    d += elm.Line().right(1)
    d += (R := elm.Resistor().right().label('$R$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(R).label('$i_D(t)$', loc='top', ofst=0.6)
    d += elm.Line().right(1)
    # Rama derecha: diodo (de arriba hacia abajo)
    d += (D := elm.Diode().down().label('$D$', loc='right', ofst=0.3))
    # Rama inferior: cierre de malla
    d += elm.Line().down().toy(Vdc.start)
    d += elm.Line().left().tox(Vdc.start)
    # Indicadores de voltaje v_D(t)
    d += elm.Line().right(1.8).at(D.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$v_D(t)$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

print("✅ Generada: circuito_ac_superpuesto.png")


# ============================================================
# PARÁMETROS COMUNES para las gráficas
# ============================================================
Is = 1e-12      # Corriente de saturación inversa
n = 1.0         # Factor de idealidad
Vt = 0.026      # Voltaje térmico (26 mV a 300 K)

# Valores del circuito de ejemplo
V_in = 5.0      # Tensión de la fuente (V)
R_val = 1000    # Resistencia (Ω)

# Punto de operación Q (intersección numérica)
def sistema(V_D):
    """Ecuación: corriente del diodo = corriente de la recta de carga"""
    return Is * (np.exp(V_D / (n * Vt)) - 1) - (V_in - V_D) / R_val

V_Q = float(fsolve(sistema, 0.6)[0])
I_Q = (V_in - V_Q) / R_val

# Resistencia dinámica en Q
rd = (n * Vt) / I_Q


# ============================================================
# FIGURA 4: RECTA DE CARGA con curva I-V y punto Q
# ============================================================
fig, ax = plt.subplots(figsize=(10, 7))

# Curva I-V del diodo (Shockley) — solo zona directa
Vd_iv = np.linspace(-0.5, 1.0, 2000)
Id_iv = Is * (np.exp(Vd_iv / (n * Vt)) - 1)

# Recta de carga: I_D = (V_in - V_D) / R
Vd_rc = np.linspace(0, V_in, 100)
Id_rc = (V_in - Vd_rc) / R_val

# Curva I-V del diodo
ax.plot(Vd_iv, Id_iv * 1e3, 'b-', linewidth=2.5,
        label='Curva I-V del Diodo (Shockley)', zorder=3)

# Recta de carga
ax.plot(Vd_rc, Id_rc * 1e3, 'r-', linewidth=2.5,
        label=f'Recta de carga ($V_{{in}}$={V_in} V, R={R_val} Ω)', zorder=3)

# Punto Q
ax.plot(V_Q, I_Q * 1e3, 'ko', markersize=12, zorder=5)
ax.annotate(f'Punto Q\n$V_{{DQ}}$ = {V_Q:.3f} V\n$I_{{DQ}}$ = {I_Q*1e3:.2f} mA',
            xy=(V_Q, I_Q * 1e3),
            xytext=(V_Q + 1.0, I_Q * 1e3 + 0.8),
            fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='black', lw=2),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow',
                      edgecolor='black'))

# Puntos extremos de la recta
ax.plot(0, V_in / R_val * 1e3, 'rs', markersize=8, zorder=5)
ax.annotate(f'$(0,\\; V_{{in}}/R)$\n= (0, {V_in/R_val*1e3:.1f} mA)',
            xy=(0, V_in / R_val * 1e3),
            xytext=(0.3, V_in / R_val * 1e3 - 0.3),
            fontsize=10, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

ax.plot(V_in, 0, 'rs', markersize=8, zorder=5)
ax.annotate(f'$(V_{{in}},\\; 0)$\n= ({V_in} V, 0)',
            xy=(V_in, 0),
            xytext=(V_in - 1.5, 0.6),
            fontsize=10, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# Líneas punteadas del punto Q a los ejes
ax.plot([V_Q, V_Q], [0, I_Q * 1e3], 'k:', alpha=0.4)
ax.plot([0, V_Q], [I_Q * 1e3, I_Q * 1e3], 'k:', alpha=0.4)

# Anotaciones de ejes
ax.annotate('$V_{DQ}$', xy=(V_Q, 0), xytext=(V_Q, -0.3),
            fontsize=11, ha='center', color='black')
ax.annotate('$I_{DQ}$', xy=(0, I_Q * 1e3), xytext=(-0.35, I_Q * 1e3),
            fontsize=11, ha='center', va='center', color='black')

# Configuración
ax.set_xlabel('Voltaje del Diodo $V_D$ (V)', fontsize=13)
ax.set_ylabel('Corriente del Diodo $I_D$ (mA)', fontsize=13)
ax.set_title('Recta de Carga y Punto de Operación Q', fontsize=14)
ax.set_xlim(-0.5, V_in + 0.5)
ax.set_ylim(-0.5, V_in / R_val * 1e3 + 1)
ax.legend(loc='upper right', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'recta_de_carga_punto_q.png'), dpi=150)
plt.close()

print("✅ Generada: recta_de_carga_punto_q.png")


# ============================================================
# FIGURA 5: Gráfica de linealización — Pequeña señal
# ============================================================
# Recta tangente en Q (modelo lineal de pequeña señal)
pendiente = 1 / rd  # dI/dV|_Q
Vd_tangente = np.linspace(V_Q - 0.12, V_Q + 0.12, 100)
Id_tangente = I_Q + pendiente * (Vd_tangente - V_Q)

# Amplitud de la señal AC superpuesta
delta_v = 0.05  # ±50 mV

fig, ax = plt.subplots(figsize=(10, 7))

# Curva I-V del diodo
Vd_ps = np.linspace(-0.2, 0.85, 1000)
Id_ps = Is * (np.exp(Vd_ps / (n * Vt)) - 1)
ax.plot(Vd_ps, Id_ps * 1e3, 'b-', linewidth=2.5,
        label='Curva I-V del Diodo', zorder=3)

# Recta tangente (modelo pequeña señal)
ax.plot(Vd_tangente, Id_tangente * 1e3, 'r--', linewidth=2,
        label='Modelo lineal (pendiente = $1/r_d$)', zorder=4)

# Punto Q
ax.plot(V_Q, I_Q * 1e3, 'ko', markersize=10, zorder=5)
ax.annotate(f'Punto Q\n($V_{{DQ}}$={V_Q:.3f} V, $I_{{DQ}}$={I_Q*1e3:.2f} mA)',
            xy=(V_Q, I_Q * 1e3),
            xytext=(V_Q - 0.30, I_Q * 1e3 + 4),
            fontsize=11, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='black', lw=2),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                      edgecolor='black'))

# Zona de pequeña señal (sombreado verde)
ax.axvspan(V_Q - delta_v, V_Q + delta_v, alpha=0.15, color='green',
           label=f'Zona de pequeña señal (±{delta_v*1e3:.0f} mV)', zorder=1)

# Líneas punteadas auxiliares del punto Q
ax.axhline(I_Q * 1e3, color='gray', linestyle=':', alpha=0.5)
ax.axvline(V_Q, color='gray', linestyle=':', alpha=0.5)

# Anotación del valor de r_d
ax.annotate(f'$r_d = \\frac{{nV_T}}{{I_{{DQ}}}} \\approx {rd:.1f}\\,\\Omega$',
            xy=(V_Q + 0.06, (I_Q + pendiente * 0.06) * 1e3),
            fontsize=12, color='red',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='mistyrose',
                      edgecolor='red'))

# Flechas indicando la amplitud de señal AC
ax.annotate('', xy=(V_Q + delta_v, I_Q * 1e3),
            xytext=(V_Q - delta_v, I_Q * 1e3),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax.text(V_Q, I_Q * 1e3 - 1.8, '$v_d(t)$', ha='center', fontsize=11,
        color='darkgreen', fontweight='bold')

# Configuración
ax.set_xlabel('Voltaje del Diodo $V_D$ (V)', fontsize=13)
ax.set_ylabel('Corriente del Diodo $I_D$ (mA)', fontsize=13)
ax.set_title('Análisis de Pequeña Señal — Linealización alrededor del Punto Q',
             fontsize=14)
ax.set_xlim(-0.1, 0.85)
ax.set_ylim(-1, I_Q * 1e3 + 8)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'diodo_pequena_senal.png'), dpi=150)
plt.close()

print("✅ Generada: diodo_pequena_senal.png")


# ============================================================
# FIGURA 6: Formas de onda temporales — v_s(t), i_D(t), v_D(t)
#   Muestra las señales en el dominio del tiempo para visualizar
#   cómo la componente AC se superpone a la componente DC.
#
#   Panel superior: Señal de entrada v_s(t)
#   Panel central:  Corriente total i_D(t) = I_DQ + i_d(t)
#   Panel inferior: Voltaje en el diodo v_D(t) = V_DQ + v_d(t)
# ============================================================

# Parámetros de la señal AC
f_ac = 1000         # Frecuencia de la señal AC (Hz)
Vm = 0.1            # Amplitud pico de la fuente AC (V) — pequeña vs V_in
T = 1 / f_ac        # Período (s)
t = np.linspace(0, 3 * T, 1000)  # 3 períodos completos

# Señal de entrada AC
vs_t = Vm * np.sin(2 * np.pi * f_ac * t)

# Componentes de pequeña señal (modelo lineal)
# Del divisor de voltaje:  v_d = v_s * r_d / (R + r_d)
#                          i_d = v_s / (R + r_d)
vd_t = vs_t * rd / (R_val + rd)        # voltaje AC en el diodo
id_t = vs_t / (R_val + rd)              # corriente AC

# Señales totales (DC + AC)
iD_t = I_Q + id_t                        # corriente total
vD_t = V_Q + vd_t                        # voltaje total en el diodo

# Voltaje de salida = voltaje en el diodo (para este circuito)
vR_t = (V_in - V_Q) + (vs_t - vd_t)     # voltaje en R  (complemento)

# Amplitudes para anotaciones
id_amp = Vm / (R_val + rd)              # amplitud pico de i_d
vd_amp = Vm * rd / (R_val + rd)         # amplitud pico de v_d

# Convertir tiempo a milisegundos para visualización
t_ms = t * 1e3

fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# --- Panel 1: Señal de entrada v_s(t) ---
ax1 = axes[0]
ax1.plot(t_ms, vs_t * 1e3, 'b-', linewidth=2, label='$v_s(t)$')
ax1.axhline(0, color='gray', linestyle='-', alpha=0.3)
ax1.set_ylabel('$v_s(t)$ (mV)', fontsize=12)
ax1.set_title('Formas de Onda en el Dominio del Tiempo — Análisis de Pequeña Señal',
              fontsize=14)
ax1.legend(loc='upper right', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.4)
ax1.annotate(f'$V_m$ = {Vm*1e3:.0f} mV\nf = {f_ac} Hz',
             xy=(0.02, 0.95), xycoords='axes fraction',
             fontsize=10, va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                       edgecolor='gray'))

# --- Panel 2: Corriente total i_D(t) = I_DQ + i_d(t) ---
ax2 = axes[1]
ax2.plot(t_ms, iD_t * 1e3, 'r-', linewidth=2, label='$i_D(t) = I_{DQ} + i_d(t)$')
ax2.axhline(I_Q * 1e3, color='darkred', linestyle='--', linewidth=1.5,
            alpha=0.7, label=f'$I_{{DQ}}$ = {I_Q*1e3:.2f} mA')
ax2.set_ylabel('$i_D(t)$ (mA)', fontsize=12)
ax2.legend(loc='upper right', fontsize=11)
ax2.grid(True, linestyle='--', alpha=0.4)

# Mostrar amplitud de la componente AC de corriente
ax2.annotate('', xy=(2.5 * T * 1e3, (I_Q + id_amp) * 1e3),
             xytext=(2.5 * T * 1e3, I_Q * 1e3),
             arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax2.annotate(f'$i_d$ = {id_amp*1e3:.3f} mA',
             xy=(2.5 * T * 1e3, (I_Q + id_amp / 2) * 1e3),
             xytext=(2.55 * T * 1e3, (I_Q + id_amp * 1.5) * 1e3),
             fontsize=10, color='green', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# --- Panel 3: Voltaje en el diodo v_D(t) = V_DQ + v_d(t) ---
ax3 = axes[2]
ax3.plot(t_ms, vD_t * 1e3, color='purple', linewidth=2,
         label='$v_D(t) = V_{DQ} + v_d(t)$')
ax3.axhline(V_Q * 1e3, color='indigo', linestyle='--', linewidth=1.5,
            alpha=0.7, label=f'$V_{{DQ}}$ = {V_Q*1e3:.1f} mV')
ax3.set_ylabel('$v_D(t)$ (mV)', fontsize=12)
ax3.set_xlabel('Tiempo (ms)', fontsize=12)
ax3.legend(loc='upper right', fontsize=11)
ax3.grid(True, linestyle='--', alpha=0.4)

# Mostrar amplitud de la componente AC de voltaje
ax3.annotate('', xy=(2.25 * T * 1e3, (V_Q + vd_amp) * 1e3),
             xytext=(2.25 * T * 1e3, V_Q * 1e3),
             arrowprops=dict(arrowstyle='<->', color='green', lw=2))
ax3.annotate(f'$v_d$ = {vd_amp*1e6:.1f} µV',
             xy=(2.25 * T * 1e3, (V_Q + vd_amp / 2) * 1e3),
             xytext=(2.35 * T * 1e3, (V_Q + vd_amp * 3) * 1e3),
             fontsize=10, color='green', fontweight='bold',
             arrowprops=dict(arrowstyle='->', color='green', lw=1.5))

# Anotación informativa en el panel inferior
ax3.annotate(f'$r_d$ ≈ {rd:.1f} Ω — R = {R_val} Ω\n'
             f'$v_d/v_s$ = $r_d/(R+r_d)$ ≈ {rd/(R_val+rd):.5f}',
             xy=(0.02, 0.05), xycoords='axes fraction',
             fontsize=10, va='bottom',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lavender',
                       edgecolor='purple'))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'formas_de_onda_temporal.png'), dpi=150)
plt.close()

print("✅ Generada: formas_de_onda_temporal.png")


# ============================================================
# FIGURAS 7 y 8: Ejemplo aplicado
#   E = 6 V (DC), e(t) = 2 sin(ωt) V, R = 270 Ω
#   Diodo de silicio: V_K = 0.7 V, r_d = 0.1 Ω
#
#   Fig 7: Esquemático del circuito (malla cerrada)
#   Fig 8: Formas de onda temporales i_D(t), v_D(t), v_R(t)
# ============================================================

# --- FIGURA 7: Esquemático del ejemplo ---
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'ejemplo_circuito_ps.png'),
                       show=False, dpi=150) as d:
    d.config(fontsize=14)
    # Rama izquierda: batería + fuente AC en serie (de abajo hacia arriba)
    d += (Edc := elm.SourceV().up().label('$E = 6\\,V$', loc='left', ofst=0.3))
    d += (eac := elm.SourceSin().up().label('$e = 2\\sin(\\omega t)$', loc='left', ofst=0.3))
    # Rama superior: resistencia R = 270 Ω
    d += elm.Line().right(1)
    d += (Rext := elm.Resistor().right().label('$R = 270\\,\\Omega$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(Rext).label('$i_D$', loc='top', ofst=0.6)
    d += elm.Line().right(1)
    # Rama derecha: diodo (de arriba hacia abajo)
    d += (D := elm.Diode().down().label('$D$ (Si)', loc='right', ofst=0.3))
    # Rama inferior: cierre de malla
    d += elm.Line().down().toy(Edc.start)
    d += elm.Line().left().tox(Edc.start)
    # Indicadores de voltaje v_D
    d += elm.Line().right(1.8).at(D.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$v_D$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

print("✅ Generada: ejemplo_circuito_ps.png")

# --- FIGURA 8: Formas de onda del ejemplo ---
# Parámetros del ejemplo
E_ej = 6.0          # Tensión DC (V)
Vm_ej = 2.0         # Amplitud pico de la señal AC (V)
R_ej = 270.0        # Resistencia (Ω)
Vk_ej = 0.7         # Tensión de rodilla (Si)
rd_ej = 0.1         # Resistencia interna del diodo (Ω)

# Análisis DC: punto de operación
I_DQ_ej = (E_ej - Vk_ej) / (R_ej + rd_ej)  # corriente DC
V_DQ_ej = Vk_ej + I_DQ_ej * rd_ej           # voltaje DC en el diodo

# Análisis AC: pequeña señal
# Amplitudes pico de las componentes AC
id_amp_ej = Vm_ej / (R_ej + rd_ej)          # amplitud pico de i_d
vd_amp_ej = Vm_ej * rd_ej / (R_ej + rd_ej)  # amplitud pico de v_d
vR_amp_ej = Vm_ej * R_ej / (R_ej + rd_ej)   # amplitud pico de v_R (AC)

# Señales temporales
f_ej = 1000         # Frecuencia de ejemplo (Hz)
T_ej = 1 / f_ej
t_ej = np.linspace(0, 3 * T_ej, 1500)

# Señal de entrada AC
e_t = Vm_ej * np.sin(2 * np.pi * f_ej * t_ej)

# Señales totales
iD_t_ej = I_DQ_ej + e_t / (R_ej + rd_ej)
vD_t_ej = V_DQ_ej + e_t * rd_ej / (R_ej + rd_ej)
vR_t_ej = I_DQ_ej * R_ej + e_t * R_ej / (R_ej + rd_ej)

t_ej_ms = t_ej * 1e3

fig, axes = plt.subplots(3, 1, figsize=(12, 11), sharex=True)

# --- Panel 1: Corriente total i_D(t) ---
ax1 = axes[0]
ax1.plot(t_ej_ms, iD_t_ej * 1e3, 'r-', linewidth=2,
         label='$i_D(t) = I_{DQ} + i_d(t)$')
ax1.axhline(I_DQ_ej * 1e3, color='darkred', linestyle='--', linewidth=1.5,
            alpha=0.7, label=f'$I_{{DQ}}$ = {I_DQ_ej*1e3:.2f} mA')
ax1.fill_between(t_ej_ms, I_DQ_ej * 1e3, iD_t_ej * 1e3, alpha=0.15, color='red')
ax1.set_ylabel('$i_D(t)$ (mA)', fontsize=12)
ax1.set_title(f'Ejemplo: $E$ = {E_ej} V, $e$ = {Vm_ej} sin(ωt) V, '
              f'$R$ = {R_ej:.0f} Ω, $r_d$ = {rd_ej} Ω (Si)',
              fontsize=13)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.4)

# Anotación de valores
ax1.annotate(f'$I_{{DQ}}$ = {I_DQ_ej*1e3:.2f} mA\n'
             f'$\\hat{{i}}_d$ = ±{id_amp_ej*1e3:.2f} mA\n'
             f'$i_{{D,max}}$ = {(I_DQ_ej+id_amp_ej)*1e3:.2f} mA\n'
             f'$i_{{D,min}}$ = {(I_DQ_ej-id_amp_ej)*1e3:.2f} mA',
             xy=(0.02, 0.95), xycoords='axes fraction',
             fontsize=10, va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='mistyrose',
                       edgecolor='red'))

# --- Panel 2: Voltaje en el diodo v_D(t) ---
ax2 = axes[1]
ax2.plot(t_ej_ms, vD_t_ej * 1e3, color='purple', linewidth=2,
         label='$v_D(t) = V_{DQ} + v_d(t)$')
ax2.axhline(V_DQ_ej * 1e3, color='indigo', linestyle='--', linewidth=1.5,
            alpha=0.7, label=f'$V_{{DQ}}$ = {V_DQ_ej*1e3:.2f} mV')
ax2.fill_between(t_ej_ms, V_DQ_ej * 1e3, vD_t_ej * 1e3, alpha=0.15, color='purple')
ax2.set_ylabel('$v_D(t)$ (mV)', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.4)

ax2.annotate(f'$V_{{DQ}}$ = {V_DQ_ej*1e3:.2f} mV\n'
             f'$\\hat{{v}}_d$ = ±{vd_amp_ej*1e3:.4f} mV\n'
             f'$v_{{D,max}}$ = {(V_DQ_ej+vd_amp_ej)*1e3:.2f} mV\n'
             f'$v_{{D,min}}$ = {(V_DQ_ej-vd_amp_ej)*1e3:.2f} mV',
             xy=(0.02, 0.95), xycoords='axes fraction',
             fontsize=10, va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='lavender',
                       edgecolor='purple'))

# --- Panel 3: Voltaje en la resistencia v_R(t) ---
ax3 = axes[2]
ax3.plot(t_ej_ms, vR_t_ej, color='teal', linewidth=2,
         label='$v_R(t) = I_{DQ} R + i_d(t) R$')
ax3.axhline(I_DQ_ej * R_ej, color='darkcyan', linestyle='--', linewidth=1.5,
            alpha=0.7, label=f'$I_{{DQ}} \\cdot R$ = {I_DQ_ej*R_ej:.2f} V')
ax3.fill_between(t_ej_ms, I_DQ_ej * R_ej, vR_t_ej, alpha=0.15, color='teal')
ax3.set_ylabel('$v_R(t)$ (V)', fontsize=12)
ax3.set_xlabel('Tiempo (ms)', fontsize=12)
ax3.legend(loc='upper right', fontsize=10)
ax3.grid(True, linestyle='--', alpha=0.4)

ax3.annotate(f'$V_{{R,DC}}$ = {I_DQ_ej*R_ej:.2f} V\n'
             f'$\\hat{{v}}_R$ = ±{vR_amp_ej:.4f} V\n'
             f'$v_{{R,max}}$ = {I_DQ_ej*R_ej+vR_amp_ej:.2f} V\n'
             f'$v_{{R,min}}$ = {I_DQ_ej*R_ej-vR_amp_ej:.2f} V',
             xy=(0.02, 0.95), xycoords='axes fraction',
             fontsize=10, va='top',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='honeydew',
                       edgecolor='teal'))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'ejemplo_formas_onda_ps.png'), dpi=150)
plt.close()

print("✅ Generada: ejemplo_formas_onda_ps.png")
print(f"\n📋 Resumen: 8 imágenes en {OUTPUT_DIR}/")
