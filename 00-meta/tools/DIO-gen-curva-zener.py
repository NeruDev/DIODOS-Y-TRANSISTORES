"""
::SCRIPT_METADATA::
Prefix: DIO
Description: Genera la curva característica I-V de un diodo Zener.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

# Configurar backend no interactivo
matplotlib.use('Agg')

# Parámetros del Diodo Zener
V_z = -5.1      # Voltaje Zener
V_k = 0.7       # Voltaje de umbral en directa
I_s = 1e-9      # Corriente de saturación (fuga)
R_z = 10.0      # Resistencia dinámica en la región Zener
V_t = 0.026     # Voltaje térmico
n = 1.0         # Factor de idealidad

# Rangos de voltaje
V_fwd = np.linspace(0, 1.2, 500)
V_rev = np.linspace(-8.0, 0, 500)

# Ecuaciones de corriente
# 1. Región directa (Shockley)
I_fwd = I_s * (np.exp(V_fwd / (n * V_t)) - 1)

# 2. Región inversa y ruptura
I_rev = np.zeros_like(V_rev)
for i, v in enumerate(V_rev):
    if v > V_z:
        I_rev[i] = -I_s # Corriente de fuga
    else:
        # Modelo lineal simple para avalancha/zener
        I_rev[i] = -I_s + (v - V_z) / R_z

# Concatenar
V_total = np.concatenate((V_rev, V_fwd))
I_total = np.concatenate((I_rev, I_fwd))

# Convertir a mA para la gráfica
I_mA = I_total * 1000

# Crear la figura
plt.figure(figsize=(10, 6))

# Trazar la curva
plt.plot(V_total, I_mA, color='#DC2626', linewidth=2.5, label='Curva I-V Zener')

# Ejes
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# Anotaciones Región Zener
plt.axvline(V_z, color='#7C3AED', linestyle='--', alpha=0.7)
plt.text(V_z - 0.2, -40, f'$V_Z = {abs(V_z)}$ V\nRegión Zener', 
         color='#7C3AED', horizontalalignment='right', fontsize=11)

# Anotaciones Región Directa
plt.axvline(V_k, color='#16A34A', linestyle='--', alpha=0.7)
plt.text(V_k + 0.1, 40, f'$V_K \\approx {V_k}$ V\nPolarización\nDirecta', 
         color='#16A34A', horizontalalignment='left', fontsize=11)

# Zonas sombreadas
plt.axvspan(-8, V_z, color='#7C3AED', alpha=0.1)
plt.text(-6.5, 20, "Región de\nRuptura", ha='center', color='#7C3AED', fontsize=12, fontweight='bold')

plt.axvspan(V_z, 0, color='#374151', alpha=0.1)
plt.text(-2.5, 20, "Región Inversa\n(Bloqueo)", ha='center', color='#374151', fontsize=12, fontweight='bold')

plt.axvspan(0, 2, color='#16A34A', alpha=0.1)
plt.text(1.2, -20, "Región\nDirecta", ha='center', color='#16A34A', fontsize=12, fontweight='bold')

# Configuración del gráfico
plt.title('Curva Característica I-V del Diodo Zener', fontsize=16, fontweight='bold', pad=15)
plt.xlabel('Voltaje $V_D$ (V)', fontsize=13)
plt.ylabel('Corriente $I_D$ (mA)', fontsize=13)
plt.xlim(-8, 2)
plt.ylim(-60, 60)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='lower right')

# Guardar
output_dir = '01-Circuitos-Diodos/media/generated'
os.makedirs(output_dir, exist_ok=True)
plt.tight_layout()
plt.savefig(f'{output_dir}/DIO-curva-zener-01-iv.png', dpi=300)
plt.close()

# ---------------------------------------------------------
# Gráfica 2: Zoom a la región de bloqueo (Cercana a cero)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))

# Rangos para el zoom: Vz no incluido, cerca a cero y un poco de directa
V_zoom_rev = np.linspace(-4.5, 0, 300)
V_zoom_fwd = np.linspace(0, 0.15, 300)

I_zoom_rev = -I_s * np.ones_like(V_zoom_rev)
I_zoom_fwd = I_s * (np.exp(V_zoom_fwd / (n * V_t)) - 1)

V_zoom = np.concatenate((V_zoom_rev, V_zoom_fwd))
I_zoom = np.concatenate((I_zoom_rev, I_zoom_fwd))

# Convertir a nanoamperios para esta gráfica
I_nA = I_zoom * 1e9

plt.plot(V_zoom, I_nA, color='#374151', linewidth=2.5, label='Corriente de fuga ($I_S$)')

# Ejes
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# Anotaciones
plt.axvspan(-4.5, 0, color='#374151', alpha=0.1)
plt.text(-2.25, -1.5, "Región Inversa de Bloqueo\n$I_D \\approx -I_S$", ha='center', color='#374151', fontsize=11)

plt.title('Zoom: Región de Bloqueo del Diodo Zener', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Voltaje $V_D$ (V)', fontsize=12)
plt.ylabel('Corriente $I_D$ (nA)', fontsize=12)
plt.xlim(-4.5, 0.15)
plt.ylim(-3, 3)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig(f'{output_dir}/DIO-curva-zener-02-zoom.png', dpi=300)
plt.close()