"""
DIO-gen-rectificador-media-onda-formas-onda.py
───────────────────
Genera las formas de onda de voltaje para el análisis del rectificador de media onda.
1. Voltaje de entrada v_s(t)
2. Voltaje de salida v_o(t)
3. Voltaje en el diodo v_D(t)

Ejes estandarizados en función de omega*t.

Salida:
  - 01-Circuitos-Diodos/media/generated/rectificador_media_onda_ondas.png

::SCRIPT_METADATA::
script_id: DIO-gen-rectificador-media-onda-formas-onda
module: DIO
generates:
  - rectificador_media_onda_ondas.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota3.md
last_updated: 2026-02-18
"""

import numpy as np
import matplotlib.pyplot as plt
import os
# import scienceplots # Optional, commented out to avoid dependency issues if not installed

# Configuración de estilo
try:
    plt.style.use(['science', 'no-latex'])
except:
    plt.style.use('default')

# Directorio de salida
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)
filename = os.path.join(OUTPUT_DIR, 'rectificador_media_onda_ondas.png')

# Parámetros
Vm = 10 # Voltaje pico arbitrario para la gráfica
omega_t = np.linspace(0, 4*np.pi, 1000) # 2 ciclos completos

# Funciones
v_s = Vm * np.sin(omega_t)
v_o = np.where(v_s > 0, v_s, 0) # Diodo ideal: pasa semiciclo positivo
v_d = np.where(v_s > 0, 0, v_s) # Diodo ideal: Vd = 0 en directa, Vd = Vs en inversa

# Gráfica
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# 1. Voltaje de entrada v_s
axs[0].plot(omega_t, v_s, 'g-', label='$v_s$')
axs[0].set_ylabel(r'$v_s(\omega t)$ [V]', color='green')
axs[0].set_title(r'Voltaje de Entrada $v_s = V_m \sin(\omega t)$')
axs[0].grid(True, linestyle=':', alpha=0.6)
axs[0].set_yticks([-Vm, 0, Vm])
axs[0].set_yticklabels([r'$-V_m$', '0', r'$V_m$'])
axs[0].axhline(0, color='black', linewidth=0.8)

# 2. Voltaje de salida v_o
axs[1].plot(omega_t, v_o, 'r-', label='$v_o$')
axs[1].set_ylabel(r'$v_o(\omega t)$ [V]', color='red')
axs[1].set_title(r'Voltaje de Salida $v_o$ (Resistencia $R_L$)')
axs[1].grid(True, linestyle=':', alpha=0.6)
axs[1].set_yticks([-Vm, 0, Vm])
axs[1].set_yticklabels([r'$-V_m$', '0', r'$V_m$'])
axs[1].axhline(0, color='black', linewidth=0.8)

# 3. Voltaje en el diodo v_D
axs[2].plot(omega_t, v_d, 'b-', label='$v_D$')
axs[2].set_xlabel(r'$\omega t$ [rad]')
axs[2].set_ylabel(r'$v_D(\omega t)$ [V]', color='blue')
axs[2].set_title(r'Voltaje en el Diodo $v_D$')
axs[2].grid(True, linestyle=':', alpha=0.6)
axs[2].set_yticks([-Vm, 0, Vm])
axs[2].set_yticklabels([r'$-V_m$', '0', r'$V_m$'])
axs[2].axhline(0, color='black', linewidth=0.8)

# Configuración eje X común
xticks = [0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi]
xticklabels = ['0', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$']
axs[2].set_xticks(xticks)
axs[2].set_xticklabels(xticklabels)

for ax in axs:
    ax.tick_params(axis='both', which='major', labelsize=10)

plt.tight_layout()
plt.savefig(filename, dpi=150)
print(f"Generado: {filename}")
