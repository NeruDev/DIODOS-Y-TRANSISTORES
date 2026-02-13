"""
PRO-gen-fuente-alimentacion.py
──────────────────────────────
Genera gráficas del diseño de fuente de alimentación regulada:
  1. Formas de onda de rectificación (media onda, onda completa, puente)
  2. Efecto del filtrado con capacitor
  3. Regulación de voltaje (LM317 y 78xx)
  4. Disipación térmica del regulador

::SCRIPT_METADATA::
script_id: PRO-gen-fuente-alimentacion
module: PRO
generates:
  - pro_formas_onda_rectificacion.png
  - pro_efecto_filtrado_capacitor.png
  - pro_diseno_lm317.png
referenced_by: []
last_updated: 2026-02-13

Dependencias: numpy, matplotlib
Salida: 05-Proyecto-Final/media/generated/

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/PRO-gen-fuente-alimentacion.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join("05-Proyecto-Final", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parámetros de la fuente
Vp = 17.0    # Voltaje pico del secundario (transformador 12V RMS)
VK = 0.7     # Caída del diodo Si
f = 60       # Hz (frecuencia de línea)
T = 1 / f

t = np.linspace(0, 4 * T, 4000)
v_sec = Vp * np.sin(2 * np.pi * f * t)

# ═══════════════ GRÁFICA 1: FORMAS DE ONDA RECTIFICACIÓN ═══════════════
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Media onda
v_half = np.maximum(v_sec - VK, 0)
axes[0].plot(t * 1000, v_sec, 'b-', alpha=0.3, linewidth=1, label='$V_{sec}$')
axes[0].plot(t * 1000, v_half, 'r-', linewidth=2, label='$V_{out}$ (media onda)')
axes[0].axhline(0, color='black', linewidth=0.5)
axes[0].set_ylabel('Voltaje [V]', fontsize=11)
axes[0].set_title('Rectificador de Media Onda', fontsize=12, fontweight='bold')
axes[0].legend(loc='upper right', fontsize=9)
axes[0].set_ylim(-Vp * 1.1, Vp * 1.1)
axes[0].grid(True, linestyle=':', alpha=0.4)
axes[0].text(2, Vp * 0.7, f'$V_{{DC}} \\approx {(Vp-VK)/np.pi:.1f}V$', fontsize=11, color='darkred')

# Onda completa (tap central)
v_full = np.abs(v_sec) - VK
v_full = np.maximum(v_full, 0)
axes[1].plot(t * 1000, v_sec, 'b-', alpha=0.3, linewidth=1, label='$V_{sec}$')
axes[1].plot(t * 1000, v_full, 'g-', linewidth=2, label='$V_{out}$ (onda completa)')
axes[1].axhline(0, color='black', linewidth=0.5)
axes[1].set_ylabel('Voltaje [V]', fontsize=11)
axes[1].set_title('Rectificador de Onda Completa (Tap Central)', fontsize=12, fontweight='bold')
axes[1].legend(loc='upper right', fontsize=9)
axes[1].set_ylim(-2, Vp * 1.1)
axes[1].grid(True, linestyle=':', alpha=0.4)
axes[1].text(2, Vp * 0.7, f'$V_{{DC}} \\approx {2*(Vp-VK)/np.pi:.1f}V$', fontsize=11, color='darkgreen')

# Puente
v_bridge = np.abs(v_sec) - 2 * VK
v_bridge = np.maximum(v_bridge, 0)
axes[2].plot(t * 1000, v_sec, 'b-', alpha=0.3, linewidth=1, label='$V_{sec}$')
axes[2].plot(t * 1000, v_bridge, 'm-', linewidth=2, label='$V_{out}$ (puente)')
axes[2].axhline(0, color='black', linewidth=0.5)
axes[2].set_ylabel('Voltaje [V]', fontsize=11)
axes[2].set_xlabel('Tiempo [ms]', fontsize=11)
axes[2].set_title('Rectificador Puente', fontsize=12, fontweight='bold')
axes[2].legend(loc='upper right', fontsize=9)
axes[2].set_ylim(-2, Vp * 1.1)
axes[2].grid(True, linestyle=':', alpha=0.4)
axes[2].text(2, Vp * 0.7, f'$V_{{DC}} \\approx {2*(Vp-2*VK)/np.pi:.1f}V$', fontsize=11, color='purple')

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'pro_formas_onda_rectificacion.png'), dpi=120)
print("Generada: pro_formas_onda_rectificacion.png")

# ═══════════════ GRÁFICA 2: EFECTO DEL FILTRADO ═══════════════
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Simulación simplificada del filtro con capacitor
# V_filtrado desciende linealmente (descarga RC) y se recarga en cada pico
RL = 1000     # Ω (carga)
IL = 0.015    # A (15 mA promedio)

Vp_rect = Vp - 2 * VK  # Puente
fr = 2 * f  # Frecuencia de rizado (onda completa)

for ax_idx, (C, label) in enumerate([(100e-6, '100 μF'), (1000e-6, '1000 μF')]):
    # Rizado pico a pico
    Vr_pp = IL / (fr * C)
    VDC = Vp_rect - Vr_pp / 2
    
    # Forma de onda aproximada (diente de sierra)
    t_detail = np.linspace(0, 4 * T, 8000)
    v_rect = np.abs(Vp * np.sin(2 * np.pi * f * t_detail)) - 2 * VK
    v_rect = np.maximum(v_rect, 0)
    
    # Simulación simple del filtro (track-hold)
    v_filtered = np.zeros_like(t_detail)
    v_cap = 0
    tau = RL * C
    dt = t_detail[1] - t_detail[0]
    
    for i, t_val in enumerate(t_detail):
        if v_rect[i] > v_cap:
            v_cap = v_rect[i]  # Capacitor se carga al pico
        else:
            v_cap = v_cap * np.exp(-dt / tau)  # Descarga exponencial
        v_filtered[i] = v_cap
    
    axes[ax_idx].plot(t_detail * 1000, v_rect, 'b-', alpha=0.3, linewidth=1, label='Rectificada')
    axes[ax_idx].plot(t_detail * 1000, v_filtered, 'r-', linewidth=2, label=f'Filtrada (C = {label})')
    axes[ax_idx].axhline(VDC, color='green', linestyle='--', alpha=0.7)
    axes[ax_idx].text(t_detail[-1] * 1000 * 0.75, VDC + 0.3, 
                      f'$V_{{DC}} \\approx {VDC:.1f}V$\n$V_{{r(pp)}} \\approx {Vr_pp:.2f}V$',
                      fontsize=10, color='green',
                      bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    axes[ax_idx].set_ylabel('Voltaje [V]', fontsize=11)
    axes[ax_idx].set_title(f'Filtrado con C = {label} (Rectificador Puente)', fontsize=12, fontweight='bold')
    axes[ax_idx].legend(loc='lower right', fontsize=9)
    axes[ax_idx].grid(True, linestyle=':', alpha=0.4)
    axes[ax_idx].set_ylim(0, Vp_rect * 1.1)

axes[1].set_xlabel('Tiempo [ms]', fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'pro_efecto_filtrado_capacitor.png'), dpi=120)
print("Generada: pro_efecto_filtrado_capacitor.png")

# ═══════════════ GRÁFICA 3: REGULACIÓN LM317 ═══════════════
fig, ax = plt.subplots(figsize=(9, 6))

R1 = 240  # Ω (valor estándar recomendado)
Vref = 1.25  # V

R2_values = np.linspace(0, 5000, 500)
Vo_values = Vref * (1 + R2_values / R1)

ax.plot(R2_values, Vo_values, 'b-', linewidth=2.5)

# Puntos de diseño populares
design_points = [
    (0, 1.25, '1.25V'),
    (390, 3.28, '~3.3V'),
    (680, 4.79, '~5V'),
    (1500, 9.06, '~9V'),
    (2000, 11.67, '~12V'),
    (2700, 15.31, '~15V'),
    (4300, 23.60, '~24V'),
]

for R2, Vo_exp, label in design_points:
    Vo_calc = Vref * (1 + R2 / R1)
    ax.plot(R2, Vo_calc, 'ro', markersize=8, zorder=5)
    offset_y = 1.0 if Vo_calc < 20 else -1.5
    ax.annotate(f'{label}\n($R_2={R2}Ω$)', 
                xy=(R2, Vo_calc), xytext=(R2 + 200, Vo_calc + offset_y),
                fontsize=8, color='red',
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.6))

ax.set_title('Diseño del LM317 — $V_o$ vs $R_2$ ($R_1 = 240Ω$)', fontsize=14)
ax.set_xlabel('$R_2$ [Ω]', fontsize=12)
ax.set_ylabel('$V_o$ [V]', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_xlim(-100, 5200)
ax.set_ylim(0, 28)

# Fórmula
ax.text(3000, 5, r'$V_o = 1.25\left(1 + \frac{R_2}{R_1}\right)$',
        fontsize=14, color='darkblue',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'pro_diseno_lm317.png'), dpi=120)
print("Generada: pro_diseno_lm317.png")

print("\n✅ Todas las gráficas del Proyecto Final generadas en:", OUTPUT_DIR)
