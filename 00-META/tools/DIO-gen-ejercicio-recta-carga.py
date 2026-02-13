"""
DIO-gen-ejercicio-recta-carga.py
───────────────────
Ejercicio: Circuito con batería 0.8 V + AC 0.15 sen(ωt), R=250 Ω.
Curva I-V ajustada al modelo de Shockley (exponencial) a partir de
los puntos dados: (0.4 V, 0 mA), (0.6 V, 1 mA), (0.64 V, 3 mA).

::SCRIPT_METADATA::
script_id: DIO-gen-ejercicio-recta-carga
module: DIO
generates:
  - dio-ejercicio-circuito-08v-250ohm.png
  - dio-ejercicio-recta-carga-08v-250ohm.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota2.md
last_updated: 2026-02-13

Salida:
  - 01-Circuitos-Diodos/media/generated/dio-ejercicio-circuito-08v-250ohm.png
  - 01-Circuitos-Diodos/media/generated/dio-ejercicio-recta-carga-08v-250ohm.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-ejercicio-recta-carga.py
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import schemdraw
import schemdraw.elements as elm

schemdraw.use('matplotlib')

OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

output_circuit = os.path.join(OUTPUT_DIR, "dio-ejercicio-circuito-08v-250ohm.png")
output_graph = os.path.join(OUTPUT_DIR, "dio-ejercicio-recta-carga-08v-250ohm.png")

# ============================================================
# Parámetros del circuito
# ============================================================
E_dc  = 0.8        # V  (batería)
v_ac  = 0.15       # V  (amplitud AC)
R     = 250.0      # Ω
E_max = E_dc + v_ac   # 0.95 V
E_min = E_dc - v_ac   # 0.65 V

# ============================================================
# Modelo de Shockley ajustado a los 3 puntos dados
# Puntos: (0.4V, 0mA), (0.6V, 1mA), (0.64V, 3mA)
# ============================================================
VT   = 0.026       # V  (voltaje térmico a ~300 K)
n    = 1.40        # factor de idealidad (ajustado)
I_S  = 7.24e-11    # A  (corriente de saturación ajustada)
nVT  = n * VT      # 0.0364 V

def I_diode(Vd):
    """Corriente del diodo (Shockley) en Amperios."""
    return I_S * (np.exp(np.clip(Vd / nVT, -50, 50)) - 1)

def find_Q(E_val):
    """Encuentra el punto Q por intersección recta-exponencial."""
    def eq(Vd):
        return (E_val - Vd) / R - I_diode(Vd)
    Vd_sol = fsolve(eq, 0.55, full_output=False)[0]
    Id_sol = I_diode(Vd_sol)
    return Vd_sol, Id_sol

# Puntos de referencia dados
pts_ref = [(0.4, 0.0), (0.6, 1.0), (0.64, 3.0)]

# Verificación del modelo
print("Modelo Shockley: Is = {:.2e} A, n = {:.2f}".format(I_S, n))
print("Verificación de puntos de referencia:")
for v, i_ref in pts_ref:
    i_calc = I_diode(v) * 1e3
    print("  V={:.2f} V -> I_modelo={:.4f} mA  (ref: {:.1f} mA)".format(v, i_calc, i_ref))

# Cálculo de los 3 puntos Q
Vd_Q, Id_Q     = find_Q(E_dc)
Vd_max, Id_max = find_Q(E_max)
Vd_min, Id_min = find_Q(E_min)

R_CD = Vd_Q / Id_Q
rd   = nVT / Id_Q

print("\n  Q_CD   = ({:.1f} mV, {:.3f} mA)".format(Vd_Q*1e3, Id_Q*1e3))
print("  Q_max  = ({:.1f} mV, {:.3f} mA)".format(Vd_max*1e3, Id_max*1e3))
print("  Q_min  = ({:.1f} mV, {:.3f} mA)".format(Vd_min*1e3, Id_min*1e3))
print("  R_CD   = {:.1f} ohm".format(R_CD))
print("  r_d    = {:.2f} ohm".format(rd))


# ============================================================
# 1) Esquemático del circuito
# ============================================================
with schemdraw.Drawing(file=output_circuit, show=False, dpi=150) as d:
    d.config(fontsize=14)

    # Rama izquierda: fuente DC + fuente AC en serie
    d += (src_dc := elm.SourceV().up().label(r'$E=0.8\,V$', loc='left', ofst=0.3))
    d += elm.SourceSin().up().label(r'$e=0.15\,\mathrm{sen}(\omega t)$', loc='left', ofst=0.3)

    # Rama superior: resistencia
    d += elm.Line().right(1)
    d += (rload := elm.Resistor().right().label(r'$R=250\,\Omega$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(rload).label('$I_D$', loc='top', ofst=0.6)
    d += elm.Line().right(1)

    # Rama derecha: diodo
    d += (diode := elm.Diode().down().label('$D$', loc='right', ofst=0.3))

    # Rama inferior: cierre
    d += elm.Line().down().toy(src_dc.start)
    d += elm.Line().left().tox(src_dc.start)

    # Leyenda V_D
    d += elm.Line().right(1.8).at(diode.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$V_D$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

print("\n✅ Generada: dio-ejercicio-circuito-08v-250ohm.png")


# ============================================================
# 2) Gráfica: curva I-V (Shockley) + rectas + puntos Q
# ============================================================

# Curva I-V exponencial
Vd_arr = np.linspace(0, 0.75, 500)
Id_arr = I_diode(Vd_arr) * 1e3  # mA

# Rectas de carga
Vd_recta = np.linspace(0, 1.0, 300)

def recta(E_val, Vd):
    return (E_val - Vd) / R * 1e3  # mA

fig, ax = plt.subplots(figsize=(9, 6))

# Curva I-V exponencial
ax.plot(Vd_arr, Id_arr, 'b-', linewidth=2.5, label=r'Curva $I$-$V$ (Shockley)')

# Puntos de referencia dados
for v, i_ref in pts_ref:
    ax.plot(v, i_ref, 'bs', markersize=8, zorder=5)
    ax.annotate(r'$({}, {})$'.format(v, i_ref),
                xy=(v, i_ref), xytext=(-55, 10),
                textcoords='offset points', fontsize=9, color='blue')

# Recta CD
r_cd = recta(E_dc, Vd_recta)
mask_cd = r_cd >= 0
ax.plot(Vd_recta[mask_cd], r_cd[mask_cd], 'k-', linewidth=2,
        label=r'Recta CD ($E={}$ V)'.format(E_dc))

# Recta E_max
r_max_line = recta(E_max, Vd_recta)
mask_max = r_max_line >= 0
ax.plot(Vd_recta[mask_max], r_max_line[mask_max], 'r--', linewidth=1.5,
        label=r'$E_{{\max}}={}$ V'.format(E_max))

# Recta E_min
r_min_line = recta(E_min, Vd_recta)
mask_min = r_min_line >= 0
ax.plot(Vd_recta[mask_min], r_min_line[mask_min], 'g--', linewidth=1.5,
        label=r'$E_{{\min}}={}$ V'.format(E_min))

# Punto Q CD
ax.plot(Vd_Q, Id_Q * 1e3, 'ko', markersize=10, zorder=6)
ax.annotate(r'$Q$ ({:.0f} mV, {:.2f} mA)'.format(Vd_Q*1e3, Id_Q*1e3),
            xy=(Vd_Q, Id_Q*1e3), xytext=(20, 15),
            textcoords='offset points', fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='black'))

# Punto Q max
ax.plot(Vd_max, Id_max * 1e3, 'r^', markersize=9, zorder=6)
ax.annotate(r'$Q_{{\max}}$ ({:.0f} mV, {:.2f} mA)'.format(Vd_max*1e3, Id_max*1e3),
            xy=(Vd_max, Id_max*1e3), xytext=(15, 12),
            textcoords='offset points', fontsize=9, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

# Punto Q min
ax.plot(Vd_min, Id_min * 1e3, 'gv', markersize=9, zorder=6)
ax.annotate(r'$Q_{{\min}}$ ({:.0f} mV, {:.2f} mA)'.format(Vd_min*1e3, Id_min*1e3),
            xy=(Vd_min, Id_min*1e3), xytext=(15, -20),
            textcoords='offset points', fontsize=9, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# Líneas punteadas de proyección para Q
ax.plot([Vd_Q, Vd_Q], [0, Id_Q*1e3], 'k:', linewidth=1.0, alpha=0.5)
ax.plot([0, Vd_Q], [Id_Q*1e3, Id_Q*1e3], 'k:', linewidth=1.0, alpha=0.5)

# Extremos de la recta CD
ax.plot(0, E_dc / R * 1e3, 'ks', markersize=6)
ax.annotate(r'$I_D={:.2f}\,mA$'.format(E_dc/R*1e3),
            xy=(0, E_dc/R*1e3), xytext=(0.03, E_dc/R*1e3 + 0.15), fontsize=9)
ax.plot(E_dc, 0, 'ks', markersize=6)
ax.annotate(r'$V_D={}\,V$'.format(E_dc),
            xy=(E_dc, 0), xytext=(E_dc - 0.12, -0.3), fontsize=9)

# Tabla de resultados dentro de la gráfica
tabla_txt = (
    r'$R_{{CD}} = V_{{DQ}}/I_{{DQ}} = {:.1f}\,\Omega$'.format(R_CD) + '\n'
    r'$r_d = nV_T/I_{{DQ}} = {:.1f}\,\Omega$'.format(rd) + '\n'
    r'$n = {:.2f}$,  $I_S = {:.2e}\,A$'.format(n, I_S)
)
ax.text(0.97, 0.55, tabla_txt, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow',
                  edgecolor='gray', alpha=0.9))

ax.set_xlabel(r'Voltaje del diodo $V_D$ (V)', fontsize=12)
ax.set_ylabel(r'Corriente del diodo $I_D$ (mA)', fontsize=12)
ax.set_title(r'Recta de carga + curva I-V (modelo Shockley)' + '\n'
             r'$E=0.8\,V$, $R=250\,\Omega$, $e=0.15\,\mathrm{sen}(\omega t)$',
             fontsize=13)
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 4.5)
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, linestyle='--', alpha=0.45)

plt.tight_layout()
plt.savefig(output_graph, dpi=150)
plt.close(fig)

print("✅ Generada: dio-ejercicio-recta-carga-08v-250ohm.png")
