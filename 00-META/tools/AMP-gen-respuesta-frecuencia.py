"""
AMP-gen-respuesta-frecuencia.py
───────────────────────────────
Genera gráficas de amplificadores en pequeña señal:
  1. Diagrama de Bode — respuesta en frecuencia de un amplificador EC
  2. Comparativa de ganancia EC / BC / CC
  3. Efecto de la carga RL en la ganancia

Dependencias: numpy, matplotlib, scipy (opcional para Bode preciso)
Salida: 04-Amplificadores/media/generated/

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/AMP-gen-respuesta-frecuencia.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = os.path.join("04-Amplificadores", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ═══════════════ GRÁFICA 1: RESPUESTA EN FRECUENCIA (BODE) ═══════════════
# Modelo simplificado de amplificador EC con acoplamiento
# Av_mid = -150 (ganancia en banda media)
# fL = 100 Hz (frecuencia de corte inferior — capacitores de acoplamiento)
# fH = 500 kHz (frecuencia de corte superior — capacitancias parásitas)

Av_mid = 150
fL = 100         # Hz
fH = 500e3       # Hz

f = np.logspace(0, 8, 2000)  # 1 Hz a 100 MHz
omega = 2 * np.pi * f
omega_L = 2 * np.pi * fL
omega_H = 2 * np.pi * fH

# Función de transferencia: Av(f) = Av_mid * (jf/fL)/(1+jf/fL) * 1/(1+jf/fH)
# Magnitud:
Av_mag = Av_mid * (f / fL) / np.sqrt(1 + (f / fL)**2) * 1 / np.sqrt(1 + (f / fH)**2)
Av_dB = 20 * np.log10(Av_mag + 1e-20)

# Fase
phase = np.degrees(np.arctan(fL / f) - np.arctan(f / fH))

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Magnitud
ax1.semilogx(f, Av_dB, 'b-', linewidth=2)
ax1.axhline(20 * np.log10(Av_mid), color='gray', linestyle=':', alpha=0.5)
ax1.axhline(20 * np.log10(Av_mid) - 3, color='red', linestyle='--', alpha=0.7, label='−3 dB')
ax1.axvline(fL, color='green', linestyle=':', alpha=0.6)
ax1.axvline(fH, color='green', linestyle=':', alpha=0.6)
ax1.text(fL, Av_dB.max() + 2, f'$f_L = {fL}$ Hz', fontsize=9, color='green', ha='center')
ax1.text(fH, Av_dB.max() + 2, f'$f_H = {fH/1000:.0f}$ kHz', fontsize=9, color='green', ha='center')

# Ancho de banda
ax1.annotate('', xy=(fL, 20*np.log10(Av_mid)-3), xytext=(fH, 20*np.log10(Av_mid)-3),
            arrowprops=dict(arrowstyle='<->', color='purple', linewidth=1.5))
ax1.text(np.sqrt(fL * fH), 20*np.log10(Av_mid) - 5, 'BW (Ancho de Banda)',
         fontsize=10, color='purple', ha='center')

ax1.set_ylabel('$|A_v|$ [dB]', fontsize=12)
ax1.set_title('Diagrama de Bode — Amplificador Emisor Común', fontsize=14)
ax1.grid(True, which='both', linestyle='--', alpha=0.3)
ax1.legend(fontsize=10)
ax1.set_ylim(0, Av_dB.max() + 8)

# Fase
ax2.semilogx(f, phase, 'r-', linewidth=2)
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(fL, color='green', linestyle=':', alpha=0.6)
ax2.axvline(fH, color='green', linestyle=':', alpha=0.6)
ax2.set_ylabel('Fase [°]', fontsize=12)
ax2.set_xlabel('Frecuencia [Hz]', fontsize=12)
ax2.grid(True, which='both', linestyle='--', alpha=0.3)
ax2.set_ylim(-100, 100)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'amp_bode_emisor_comun.png'), dpi=120)
print("Generada: amp_bode_emisor_comun.png")

# ═══════════════ GRÁFICA 2: COMPARATIVA EC / BC / CC ═══════════════
configs = {
    'Emisor Común (EC)': {'Av': 150, 'Zi_kOhm': 2.5, 'Zo_kOhm': 4.0, 'Ai': 120, 'Fase': '180°'},
    'Base Común (BC)':   {'Av': 150, 'Zi_kOhm': 0.025, 'Zo_kOhm': 4.0, 'Ai': 0.99, 'Fase': '0°'},
    'Colector Común (CC)': {'Av': 0.98, 'Zi_kOhm': 250, 'Zo_kOhm': 0.025, 'Ai': 151, 'Fase': '0°'},
}

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

params = ['Av', 'Zi_kOhm', 'Zo_kOhm']
titles = ['Ganancia de Voltaje $|A_v|$', 'Impedancia de Entrada $Z_i$ [kΩ]', 'Impedancia de Salida $Z_o$ [kΩ]']
colors_bar = ['#2196F3', '#4CAF50', '#FF9800']

for ax, param, title, color in zip(axes, params, titles, colors_bar):
    names = list(configs.keys())
    values = [configs[n][param] for n in names]
    
    bars = ax.barh(names, values, color=color, alpha=0.8, edgecolor='black', linewidth=0.5)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xscale('log')
    ax.grid(True, axis='x', linestyle=':', alpha=0.4)
    
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() * 1.1, bar.get_y() + bar.get_height()/2,
                f'{val:.2f}' if val < 10 else f'{val:.0f}',
                va='center', fontsize=9, fontweight='bold')

plt.suptitle('Comparativa — Configuraciones BJT en Pequeña Señal', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'amp_comparativa_ec_bc_cc.png'), dpi=120, bbox_inches='tight')
print("Generada: amp_comparativa_ec_bc_cc.png")

# ═══════════════ GRÁFICA 3: EFECTO DE RL EN GANANCIA ═══════════════
re = 17.3e-3  # re = 26mV / 1.5mA = 17.3 Ω
RC = 4000     # 4 kΩ
Zi_base = 150 * re  # β*re

RL_values = np.logspace(1, 6, 200)  # 10 Ω a 1 MΩ

Av_RL = (RC * RL_values / (RC + RL_values)) / re  # |Av| = (RC||RL)/re

fig, ax = plt.subplots(figsize=(9, 6))
ax.semilogx(RL_values, Av_RL, 'b-', linewidth=2.5)

# Caso sin carga
Av_no_load = RC / re
ax.axhline(Av_no_load, color='gray', linestyle=':', alpha=0.6)
ax.text(20, Av_no_load + 3, f'Sin carga: $|A_v| = R_C/r_e = {Av_no_load:.0f}$',
        fontsize=10, color='gray')

# Puntos notables
for RL_mark in [100, 1000, 10000]:
    Av_mark = (RC * RL_mark / (RC + RL_mark)) / re
    ax.plot(RL_mark, Av_mark, 'ro', markersize=6)
    ax.annotate(f'$R_L={RL_mark/1000:.0f}kΩ$\n$|A_v|={Av_mark:.0f}$' if RL_mark >= 1000 
                else f'$R_L={RL_mark}Ω$\n$|A_v|={Av_mark:.0f}$',
                xy=(RL_mark, Av_mark), xytext=(RL_mark * 2.5, Av_mark - 15),
                fontsize=9, arrowprops=dict(arrowstyle='->', color='red'))

ax.set_title('Efecto de $R_L$ en la Ganancia — Emisor Común', fontsize=14)
ax.set_xlabel('$R_L$ [Ω]', fontsize=12)
ax.set_ylabel('$|A_v|$', fontsize=12)
ax.grid(True, which='both', linestyle='--', alpha=0.3)
ax.set_ylim(0, Av_no_load * 1.15)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'amp_efecto_rl_ganancia.png'), dpi=120)
print("Generada: amp_efecto_rl_ganancia.png")

print("\n✅ Todas las gráficas de amplificadores generadas en:", OUTPUT_DIR)
