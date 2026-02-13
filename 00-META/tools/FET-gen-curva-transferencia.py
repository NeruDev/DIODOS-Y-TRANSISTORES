"""
FET-gen-curva-transferencia.py
──────────────────────────────
Genera las curvas características del transistor FET:
  1. Curva de transferencia ID vs VGS (ecuación de Shockley para FET)
  2. Curvas de salida ID vs VDS (familia de curvas)
  3. Solución gráfica de autopolarización
  4. Comparativa JFET / MOSFET deplexión / MOSFET enriquecimiento

::SCRIPT_METADATA::
script_id: FET-gen-curva-transferencia
module: FET
generates:
  - fet_curva_transferencia.png
  - fet_familia_curvas_id_vds.png
  - fet_autopolarizacion_grafica.png
referenced_by: []
last_updated: 2026-02-13

Dependencias: numpy, matplotlib
Salida: 03-Transistor-FET/media/generated/

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/FET-gen-curva-transferencia.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join("03-Transistor-FET", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Parámetros JFET canal N (tipo 2N5459) ──
IDSS = 9e-3    # 9 mA
VP = -4.0      # Voltaje de pinch-off (V)

def jfet_transfer(VGS, IDSS, VP):
    """Ecuación de Shockley para FET: ID = IDSS*(1 - VGS/VP)^2"""
    ID = np.where(VGS <= VP, 0, IDSS * (1 - VGS / VP)**2)
    return np.clip(ID, 0, None)

def jfet_output(VDS, VGS, IDSS, VP):
    """Curva de salida simplificada con región óhmica y saturación."""
    VP_eff = VGS - VP  # VP_eff = VGS - VP (positivo cuando conduce)
    ID_sat = IDSS * (1 - VGS / VP)**2
    
    ID = np.where(
        VDS < VP_eff,
        # Región óhmica: aproximación cuadrática
        ID_sat * (2 * VDS / VP_eff - (VDS / VP_eff)**2),
        # Región de saturación
        ID_sat * np.ones_like(VDS)
    )
    return np.clip(ID, 0, None)

# ═══════════════ GRÁFICA 1: CURVA DE TRANSFERENCIA ═══════════════
VGS = np.linspace(VP, 0.5, 500)
ID = jfet_transfer(VGS, IDSS, VP)

fig, ax = plt.subplots(figsize=(8, 7))
ax.plot(VGS, ID * 1000, 'b-', linewidth=2.5, label='$I_D = I_{DSS}(1 - V_{GS}/V_P)^2$')

# Puntos notables
ax.plot(0, IDSS * 1000, 'ro', markersize=10, zorder=5)
ax.annotate(f'$I_{{DSS}} = {IDSS*1000:.0f}$ mA', xy=(0, IDSS*1000),
            xytext=(0.3, IDSS*1000 - 0.5), fontsize=11, color='red',
            arrowprops=dict(arrowstyle='->', color='red'))

ax.plot(VP, 0, 'go', markersize=10, zorder=5)
ax.annotate(f'$V_P = {VP:.0f}$ V', xy=(VP, 0),
            xytext=(VP + 0.3, 0.8), fontsize=11, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

# Punto medio
VGS_mid = VP / 2
ID_mid = IDSS * (1 - VGS_mid / VP)**2
ax.plot(VGS_mid, ID_mid * 1000, 'ms', markersize=8, zorder=5)
ax.annotate(f'$V_{{GS}} = V_P/2$\n$I_D = I_{{DSS}}/4$\n= {ID_mid*1000:.2f} mA',
            xy=(VGS_mid, ID_mid * 1000), xytext=(VGS_mid + 0.5, ID_mid * 1000 + 1),
            fontsize=9, color='purple',
            arrowprops=dict(arrowstyle='->', color='purple'))

# Tabla normalizada como marcadores
fractions = [0.25, 0.5, 0.75]
for frac in fractions:
    vgs_f = VP * frac
    id_f = IDSS * (1 - frac)**2
    ax.plot(vgs_f, id_f * 1000, 'k.', markersize=6)

ax.set_title('Curva de Transferencia JFET Canal N', fontsize=14)
ax.set_xlabel('$V_{GS}$ [V]', fontsize=12)
ax.set_ylabel('$I_D$ [mA]', fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(fontsize=11, loc='upper left')
ax.set_xlim(VP - 0.5, 1)
ax.set_ylim(-0.3, IDSS * 1000 * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fet_curva_transferencia.png'), dpi=120)
print("Generada: fet_curva_transferencia.png")

# ═══════════════ GRÁFICA 2: FAMILIA DE CURVAS ID vs VDS ═══════════════
VDS = np.linspace(0, 12, 500)
VGS_values = [0, -1, -2, -3, -3.5]
colors = ['#d62728', '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd']

fig, ax = plt.subplots(figsize=(10, 7))

for vgs, color in zip(VGS_values, colors):
    if vgs <= VP:
        continue
    ID = jfet_output(VDS, vgs, IDSS, VP)
    ax.plot(VDS, ID * 1000, color=color, linewidth=2,
            label=f'$V_{{GS}} = {vgs:.0f}$ V')

# Curva de pinch-off (locus)
VDS_pinch = np.linspace(0, 12, 200)
VGS_pinch = VP + VDS_pinch  # VDS = VGS - VP
ID_pinch = jfet_transfer(VGS_pinch, IDSS, VP)
mask = (VGS_pinch <= 0) & (VDS_pinch >= 0)
ax.plot(VDS_pinch[mask], ID_pinch[mask] * 1000, 'k--', linewidth=1.5,
        alpha=0.6, label='Frontera pinch-off')

ax.text(2, 7, 'Región\nÓhmica', fontsize=11, color='gray', ha='center', style='italic')
ax.text(8, 5, 'Región de\nSaturación', fontsize=11, color='darkgreen', ha='center', style='italic')

ax.set_title('Familia de Curvas de Salida — JFET Canal N', fontsize=14)
ax.set_xlabel('$V_{DS}$ [V]', fontsize=12)
ax.set_ylabel('$I_D$ [mA]', fontsize=12)
ax.set_xlim(0, 12)
ax.set_ylim(0, IDSS * 1000 * 1.1)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fet_familia_curvas_id_vds.png'), dpi=120)
print("Generada: fet_familia_curvas_id_vds.png")

# ═══════════════ GRÁFICA 3: AUTOPOLARIZACIÓN (solución gráfica) ═══════════════
RS = 500  # Ω

fig, ax = plt.subplots(figsize=(8, 7))

# Curva de transferencia
VGS_t = np.linspace(VP, 0.5, 500)
ID_t = jfet_transfer(VGS_t, IDSS, VP)
ax.plot(VGS_t, ID_t * 1000, 'b-', linewidth=2.5, label='Curva de transferencia')

# Recta de polarización: VGS = -ID*RS → ID = -VGS/RS
VGS_line = np.linspace(VP, 0, 200)
ID_line = -VGS_line / RS
ax.plot(VGS_line, ID_line * 1000, 'r-', linewidth=2.5,
        label=f'Recta: $V_{{GS}} = -I_D R_S$ ($R_S = {RS}Ω$)')

# Punto Q (intersección numérica)
# Resolver: IDSS*(1 - VGS/VP)^2 = -VGS/RS
# con VGS = -ID*RS
from scipy.optimize import fsolve

def eq_autopolarizacion(ID_val):
    VGS_val = -ID_val * RS
    return IDSS * (1 - VGS_val / VP)**2 - ID_val

try:
    ID_Q = fsolve(eq_autopolarizacion, IDSS/4)[0]
    VGS_Q = -ID_Q * RS
    ax.plot(VGS_Q, ID_Q * 1000, 'ko', markersize=12, zorder=5)
    ax.annotate(f'Punto Q\n$V_{{GS}} = {VGS_Q:.2f}V$\n$I_D = {ID_Q*1000:.2f}mA$',
                xy=(VGS_Q, ID_Q * 1000), xytext=(VGS_Q + 0.8, ID_Q * 1000 + 1.5),
                fontsize=10, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black', linewidth=2),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8))
except Exception:
    pass  # scipy no disponible, se omite el punto Q

ax.set_title('Solución Gráfica — Autopolarización JFET', fontsize=14)
ax.set_xlabel('$V_{GS}$ [V]', fontsize=12)
ax.set_ylabel('$I_D$ [mA]', fontsize=12)
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(fontsize=10, loc='upper left')
ax.set_xlim(VP - 0.5, 1)
ax.set_ylim(-0.3, IDSS * 1000 * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fet_autopolarizacion_grafica.png'), dpi=120)
print("Generada: fet_autopolarizacion_grafica.png")

print("\n✅ Todas las gráficas FET generadas en:", OUTPUT_DIR)
