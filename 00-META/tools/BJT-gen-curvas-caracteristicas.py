"""
BJT-gen-curvas-caracteristicas.py
─────────────────────────────────
Genera las curvas características del transistor BJT:
  1. Curvas de salida IC vs VCE (familia de curvas)
  2. Curva de transferencia IC vs IB
  3. Recta de carga DC con punto Q
  4. Regiones de operación (corte, activa, saturación)

::SCRIPT_METADATA::
script_id: BJT-gen-curvas-caracteristicas
module: BJT
generates:
  - bjt_familia_curvas_ic_vce.png
  - bjt_recta_carga_dc.png
  - bjt_regiones_operacion.png
referenced_by: []
last_updated: 2026-02-13

Dependencias: numpy, matplotlib
Salida: 02-Transistor-BJT/media/generated/

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/BJT-gen-curvas-caracteristicas.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join("02-Transistor-BJT", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Parámetros del BJT (modelo simplificado tipo 2N2222) ──
beta = 150
VCE_sat = 0.2  # V
VA = 100        # Voltaje Early (V) — efecto de modulación de base
IC_max = 0.3    # A (300 mA para visualización)

def bjt_ic(VCE, IB, beta=150, VA=100, VCE_sat=0.2):
    """Modelo simplificado: IC = beta*IB * (1 + VCE/VA) en zona activa."""
    IC = np.zeros_like(VCE)
    for idx, vce in enumerate(VCE):
        if vce < VCE_sat:
            # Región de saturación: crece linealmente
            IC[idx] = beta * IB * (vce / VCE_sat)
        else:
            # Región activa: casi constante con efecto Early
            IC[idx] = beta * IB * (1 + vce / VA)
    return np.clip(IC, 0, IC_max)

# ═══════════════ GRÁFICA 1: FAMILIA DE CURVAS IC vs VCE ═══════════════
VCE = np.linspace(0, 12, 500)
IB_values = [10e-6, 20e-6, 40e-6, 60e-6, 80e-6, 100e-6]  # μA
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(10, 7))

for IB, color in zip(IB_values, colors):
    IC = bjt_ic(VCE, IB, beta=beta)
    label = f'$I_B = {IB*1e6:.0f}$ μA'
    ax.plot(VCE, IC * 1000, color=color, linewidth=2, label=label)

# Línea de VCE_sat
ax.axvline(VCE_sat, color='gray', linestyle=':', alpha=0.7)
ax.text(VCE_sat + 0.1, IC_max * 1000 * 0.95, '$V_{CE(sat)}$', color='gray', fontsize=10)

# Regiones
ax.axvspan(0, VCE_sat, alpha=0.08, color='red', label='Saturación')
ax.text(0.05, IC_max * 1000 * 0.5, 'Saturación', rotation=90, fontsize=9, color='red', va='center')
ax.text(6, IC_max * 1000 * 0.85, 'Región Activa', fontsize=12, color='darkgreen',
        ha='center', style='italic')

ax.set_title('Familia de Curvas de Salida — BJT NPN ($\\beta = 150$)', fontsize=14)
ax.set_xlabel('$V_{CE}$ [V]', fontsize=12)
ax.set_ylabel('$I_C$ [mA]', fontsize=12)
ax.set_xlim(0, 12)
ax.set_ylim(0, IC_max * 1000 * 1.05)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='lower right', fontsize=9)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'bjt_familia_curvas_ic_vce.png'), dpi=120)
print("Generada: bjt_familia_curvas_ic_vce.png")

# ═══════════════ GRÁFICA 2: RECTA DE CARGA DC ═══════════════
VCC = 12     # V
RC = 2000    # Ω (2 kΩ)
RE = 500     # Ω

fig, ax = plt.subplots(figsize=(10, 7))

# Curvas de fondo
for IB, color in zip(IB_values, colors):
    IC = bjt_ic(VCE, IB, beta=beta)
    ax.plot(VCE, IC * 1000, color=color, linewidth=1.5, alpha=0.5,
            label=f'$I_B = {IB*1e6:.0f}$ μA')

# Recta de carga: VCE = VCC - IC*(RC + RE)
IC_eje = VCC / (RC + RE)  # Punto en eje IC
VCE_eje = VCC              # Punto en eje VCE

VCE_line = np.array([0, VCE_eje])
IC_line = np.array([IC_eje, 0])
ax.plot(VCE_line, IC_line * 1000, 'k-', linewidth=2.5, label='Recta de Carga DC')

# Punto Q (ejemplo: IB = 40 μA)
IB_Q = 40e-6
IC_Q = beta * IB_Q  # 6 mA
VCE_Q = VCC - IC_Q * (RC + RE)

ax.plot(VCE_Q, IC_Q * 1000, 'ro', markersize=12, zorder=5)
ax.annotate(f'Punto Q\n($V_{{CE}}={VCE_Q:.1f}V$, $I_C={IC_Q*1000:.1f}mA$)',
            xy=(VCE_Q, IC_Q * 1000), xytext=(VCE_Q + 1.5, IC_Q * 1000 + 0.8),
            fontsize=10, color='red', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='red', linewidth=1.5))

# Puntos de saturación y corte
ax.plot(0, IC_eje * 1000, 'bs', markersize=8, zorder=5)
ax.annotate(f'Saturación\n$I_C = {IC_eje*1000:.1f}mA$',
            xy=(0, IC_eje * 1000), xytext=(0.8, IC_eje * 1000 + 0.3),
            fontsize=9, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue'))

ax.plot(VCE_eje, 0, 'gs', markersize=8, zorder=5)
ax.annotate(f'Corte\n$V_{{CE}} = {VCE_eje}V$',
            xy=(VCE_eje, 0), xytext=(VCE_eje - 1.5, 0.5),
            fontsize=9, color='green',
            arrowprops=dict(arrowstyle='->', color='green'))

ax.set_title(f'Recta de Carga DC ($V_{{CC}}={VCC}V$, $R_C={RC/1000:.1f}kΩ$, $R_E={RE}Ω$)', fontsize=13)
ax.set_xlabel('$V_{CE}$ [V]', fontsize=12)
ax.set_ylabel('$I_C$ [mA]', fontsize=12)
ax.set_xlim(-0.5, 13)
ax.set_ylim(-0.2, IC_eje * 1000 * 1.2)
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend(loc='upper right', fontsize=8)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'bjt_recta_carga_dc.png'), dpi=120)
print("Generada: bjt_recta_carga_dc.png")

# ═══════════════ GRÁFICA 3: REGIONES DE OPERACIÓN ═══════════════
fig, ax = plt.subplots(figsize=(9, 6))

# Dibujar regiones
VCE_full = np.linspace(0, 15, 500)

# Saturación (VCE < VCE_sat)
ax.axvspan(0, VCE_sat, alpha=0.25, color='#ff9999', label='Saturación')

# Corte (IC ≈ 0)
ax.axhspan(0, 0.3, alpha=0.15, color='#99ccff', label='Corte')

# Curvas para contexto
for IB in [20e-6, 40e-6, 60e-6, 80e-6]:
    IC = bjt_ic(VCE_full, IB, beta=beta)
    ax.plot(VCE_full, IC * 1000, color='gray', linewidth=1, alpha=0.6)

# Etiquetas
ax.text(0.08, 8, 'SAT', fontsize=14, color='red', fontweight='bold', rotation=90, va='center')
ax.text(7, 8, 'REGIÓN ACTIVA\n(Amplificación)', fontsize=14, color='darkgreen',
        ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#eeffee', alpha=0.7))
ax.text(7, 0.1, 'CORTE', fontsize=12, color='blue', ha='center', fontweight='bold')

# Línea de ruptura
ax.axvline(14, color='orange', linestyle='--', linewidth=2)
ax.text(14.2, 5, 'Ruptura\n$V_{CEO}$', fontsize=10, color='darkorange', fontweight='bold')

ax.set_title('Regiones de Operación del BJT', fontsize=14)
ax.set_xlabel('$V_{CE}$ [V]', fontsize=12)
ax.set_ylabel('$I_C$ [mA]', fontsize=12)
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'bjt_regiones_operacion.png'), dpi=120)
print("Generada: bjt_regiones_operacion.png")

print("\n✅ Todas las gráficas BJT generadas en:", OUTPUT_DIR)
