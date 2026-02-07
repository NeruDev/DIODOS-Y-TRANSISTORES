"""
DIO-gen-curva-iv.py
───────────────────
Genera la curva característica I-V completa del diodo (directa, inversa, ruptura)
y un zoom de la región inversa mostrando la corriente de fuga Is.

Salida:
  - 01-Circuitos-Diodos/media/generated/curva_diodo_general.png
  - 01-Circuitos-Diodos/media/generated/curva_diodo_zoom_inversa.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-curva-iv.py
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Directorio de salida (relativo a la raíz del repo)
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def diode_current_complete(V, Is=1e-12, n=1, Vt=0.026, Vbr=-5.0):
    i_shockley = Is * (np.exp(V / (n * Vt)) - 1)
    i_breakdown = -Is * np.exp(-(V - Vbr) / (n * Vt))
    return i_shockley + i_breakdown

# Parámetros visuales
Is_viz = 1e-4
Vbr_val = -5.0

# ---------------- GRAFICA 1: GENERAL ----------------
v = np.linspace(-6.0, 1.0, 1000)
i = diode_current_complete(v, Is=Is_viz, Vbr=Vbr_val)

plt.figure(figsize=(10, 6))
plt.plot(v, i, color='purple', linewidth=2, label='Curva I-V Diodo')
plt.title('Curva Característica del Diodo (Completa)')
plt.xlabel('Voltaje (V)')
plt.ylabel('Corriente (A)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)

# Anotaciones Generales
# Región Directa
plt.text(0.8, 1.0, 'Región Directa', color='red', fontsize=10, ha='center')
plt.plot([0.7], [0], 'rx', markersize=8)
plt.text(0.7, -0.4, '$V_K \\approx 0.7V$', color='red', fontsize=9)

# Región Ruptura
plt.text(-5.5, -1.0, 'Región de\nRuptura', color='darkorange', fontsize=10, ha='center')
plt.plot([Vbr_val], [0], 'x', color='darkorange', markersize=8)
plt.text(Vbr_val, 0.2, '$V_{BR}$', color='darkorange', fontsize=9, ha='center')

# Región Inversa (Texto)
plt.text(-2.5, 0.5, 'Región Inversa\n(Ver zoom para detalle)', color='blue', ha='center', fontsize=9)
plt.annotate('', xy=(-4.5, 0.1), xytext=(-0.5, 0.1), arrowprops=dict(arrowstyle='<->', color='blue'))

plt.ylim(-3, 3) 
plt.xlim(-6.5, 1.5)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'curva_diodo_general.png'), dpi=100)
print("Generada: curva_diodo_general.png")

# ---------------- GRAFICA 2: ZOOM INVERSA ----------------
plt.clf()
v_zoom = np.linspace(-4.5, 0.1, 500)
i_zoom = diode_current_complete(v_zoom, Is=Is_viz, Vbr=Vbr_val)

plt.figure(figsize=(8, 5))
plt.plot(v_zoom, i_zoom, color='blue', linewidth=2)
plt.title('Zoom: Región Inversa y Corriente de Fuga')
plt.xlabel('Voltaje Inverso ($V_R$)')
plt.ylabel('Corriente muy pequeña ($I$)')

plt.axhline(0, color='black', linewidth=1.5, alpha=0.8)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)

plt.ylim(-2.5e-4, 1.0e-4)
plt.xlim(-4.5, 0.2)

# Línea de referencia Is
plt.axhline(-Is_viz, color='green', linestyle='--', linewidth=1, label='Nivel $I_S$')

# Anotaciones
plt.annotate('Magnitud de Corriente de Fuga ($I_S$)\n(Desfase respecto a cero)', 
             xy=(-2.0, -Is_viz), xytext=(-2.0, -0.00005),
             arrowprops=dict(arrowstyle='->', color='red', linewidth=2),
             color='red', fontsize=10, ha='center')

plt.text(-3.0, 0.00002, 'Eje Cero ($I=0$)', color='black', fontsize=9)
plt.text(-4.0, 0.00005, 'Voltaje Inverso Aplicado', color='purple', fontsize=9)

plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'curva_diodo_zoom_inversa.png'), dpi=100)
print("Generada: curva_diodo_zoom_inversa.png")
