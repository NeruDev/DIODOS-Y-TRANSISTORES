"""
DIO-gen-pequena-senal.py
───────────────────
Gráfica de linealización del punto Q y modelo de pequeña señal del diodo.

::SCRIPT_METADATA::
script_id: DIO-gen-pequena-senal
module: DIO
generates:
  - diodo_pequena_senal.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota1.md
last_updated: 2026-02-13

Salida:
  - 01-Circuitos-Diodos/media/generated/diodo_pequena_senal.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-pequena-senal.py
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del diodo
n = 1  # Factor de idealidad
Vt = 0.025  # Tensión térmica a temperatura ambiente (aprox. 25mV)
Is = 1e-12  # Corriente de saturación inversa

# Curva característica del diodo
Vd = np.linspace(0.6, 0.8, 400)
Id = Is * (np.exp(Vd / (n * Vt)) - 1)

# Punto de operación (Q-point)
Vdq = 0.7
Idq = Is * (np.exp(Vdq / (n * Vt)) - 1)

# Resistencia dinámica (de pequeña señal)
rd = (n * Vt) / Idq

# Recta tangente (modelo de pequeña señal)
V_tangente = np.linspace(Vdq - 0.05, Vdq + 0.05, 100)
I_tangente = Idq + (1/rd) * (V_tangente - Vdq)

# Creación de la gráfica
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(10, 7))

# Graficar la curva del diodo
ax.plot(Vd, Id, label='Curva Característica del Diodo')

# Graficar la recta tangente
ax.plot(V_tangente, I_tangente, '--', color='red', label=f'Modelo de Pequeña Señal (Recta Tangente)')

# Marcar el punto Q
ax.plot(Vdq, Idq, 'o', color='black', markersize=8, label=f'Punto de Operación Q\n(Vdq={Vdq}V, Idq={Idq*1000:.2f}mA)')

# Anotar la resistencia dinámica
ax.text(Vdq + 0.005, Idq - Id.max()*0.1, rf'$r_d = \frac{{dV_D}}{{dI_D}} \approx {rd*1000:.2f} \, m\Omega$', fontsize=12)

# Configuración de la gráfica
ax.set_title('Análisis de Pequeña Señal del Diodo', fontsize=16)
ax.set_xlabel('Tensión del Diodo, $V_D$ (V)', fontsize=12)
ax.set_ylabel('Corriente del Diodo, $I_D$ (A)', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True)

# Ajustar límites para visualizar mejor la zona de operación
ax.set_xlim(Vdq - 0.08, Vdq + 0.08)
ax.set_ylim(Idq - Id.max()*0.4, Idq + Id.max()*0.4)

# Guardar la figura
output_path = '01-Circuitos-Diodos/media/generated/diodo_pequena_senal.png'
plt.savefig(output_path)

print(f"Gráfica guardada en: {output_path}")
