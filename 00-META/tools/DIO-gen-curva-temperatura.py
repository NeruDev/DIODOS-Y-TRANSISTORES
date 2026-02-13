"""
DIO-gen-curva-temperatura.py
─────────────────────────────
Genera gráfica COMBINADA del efecto de la temperatura en el diodo
(regiones directa, inversa y ruptura en una sola figura).

::SCRIPT_METADATA::
script_id: DIO-gen-curva-temperatura
module: DIO
generates:
  - DIO-curva-temp-01-combinada.png
referenced_by:
  - 01-Circuitos-Diodos/media/generated/image-metadata.json
last_updated: 2026-02-13

Nomenclatura de salida (en 01-Circuitos-Diodos/media/generated/):
  DIO-curva-temp-01-combinada.png

  Convención: {PREFIJO}-{tema}-{NN}-{descriptor}.png
    • PREFIJO    = módulo (DIO)
    • tema       = concepto físico (curva-temp)
    • NN         = secuencia global (01 = combinada)
    • descriptor = contenido

Modelo:
  ► Región Directa: Is(T) calibrada al coeficiente empírico del Vth
    (−2.5 mV/°C) para obtener los voltajes de umbral correctos.
  ► Región Inversa/Ruptura: Is empírica ("se duplica cada 10°C").

  Véase DIO-gen-curva-temperatura-split.py para detalles del modelo.

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-curva-temperatura.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ════════════════════════════════════════════════════════════════
#  CONFIGURACIÓN
# ════════════════════════════════════════════════════════════════
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)
DPI = 150

# ════════════════════════════════════════════════════════════════
#  CONSTANTES Y PARÁMETROS
# ════════════════════════════════════════════════════════════════
K_B = 1.380649e-23
Q_E = 1.60217663e-19

VTH_REF  = 0.7
T_REF    = 25
KTC      = -2.5e-3
N        = 1
VBR_NOM  = -5.0
ALPHA_BR = 0.001
IS_REF   = 1e-12
I_CAL    = 1e-3

# ════════════════════════════════════════════════════════════════
#  FUNCIONES
# ════════════════════════════════════════════════════════════════
def Vt(T_c):
    return K_B * (T_c + 273.15) / Q_E

def Vth(T_c):
    return VTH_REF + KTC * (T_c - T_REF)

def Is_calibrada(T_c):
    return I_CAL / (np.exp(Vth(T_c) / (N * Vt(T_c))) - 1)

def Is_empirica(T_c):
    return IS_REF * 2 ** ((T_c - T_REF) / 10)

def diode_current_combined(V, T_c):
    """
    Modelo híbrido para la gráfica combinada:
    • V > 0  → Is calibrada  (Vth correcto)
    • V ≤ 0  → Is empírica   (fuga y ruptura visibles)
    """
    vt_val  = Vt(T_c)
    Vbr_T   = VBR_NOM * (1 + ALPHA_BR * (T_c - T_REF))
    Is_fwd  = Is_calibrada(T_c)
    Is_inv  = Is_empirica(T_c)

    i_total = np.zeros_like(V)
    for idx, v in enumerate(V):
        if v > 0:
            arg = min(v / (N * vt_val), 100)
            i_total[idx] = Is_fwd * (np.exp(arg) - 1)
        else:
            arg_fwd = max(v / (N * vt_val), -100)
            i_fwd = Is_inv * (np.exp(arg_fwd) - 1)
            arg_br = min(-(v - Vbr_T) / (N * vt_val), 100)
            i_br = -Is_inv * np.exp(arg_br)
            i_total[idx] = i_fwd + i_br
    return i_total

# ════════════════════════════════════════════════════════════════
#  DEFINIR CASOS
# ════════════════════════════════════════════════════════════════
temps = [
    {"T": -100, "label": "-100°C (Frío)",    "color": "#2ca02c", "vth": round(Vth(-100), 2)},
    {"T":   25, "label":  "25°C (Ambiente)",  "color": "#1f77b4", "vth": round(Vth(25), 2)},
    {"T":  100, "label": "100°C (Caliente)",  "color": "#d62728", "vth": round(Vth(100), 2)},
]

# ════════════════════════════════════════════════════════════════
#  GRAFICAR
# ════════════════════════════════════════════════════════════════
v = np.linspace(-6.0, 1.3, 5000)
fig, ax = plt.subplots(figsize=(12, 7))

for t in temps:
    i = diode_current_combined(v, t["T"])
    ax.plot(v, i * 1e3, color=t["color"], linewidth=2,
            label=f'T = {t["T"]}°C')

    # Línea punteada y etiqueta en Vth
    if t["vth"] < 1.2:
        ax.axvline(t["vth"], color=t["color"], linestyle=":", alpha=0.5)
        ax.text(t["vth"], 6,
                f'$V_{{th}}({t["T"]}°C)$ ≈ {t["vth"]}V',
                rotation=90, va="bottom", color=t["color"], fontsize=9)

ax.set_title("Efecto de la Temperatura: Directa, Inversa y Ruptura", fontsize=14)
ax.set_xlabel("Voltaje ($V_D$) [V]", fontsize=12)
ax.set_ylabel("Corriente ($I_D$) [mA]", fontsize=12)

ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend(loc="lower right")

ax.set_ylim(-15, 25)
ax.set_xlim(-6.2, 1.4)

ax.text(-3.0, 2, "Región de Polarización Inversa ($I \\approx 0$)",
        ha="center", fontsize=10, style="italic", color="gray")
ax.text(-5.2, -12, "Región de\nRuptura",
        ha="right", fontsize=10, fontweight="bold", color="purple")

fig.tight_layout()
fname = "DIO-curva-temp-01-combinada.png"
fig.savefig(os.path.join(OUTPUT_DIR, fname), dpi=DPI)
plt.close(fig)
print(f"  ✓ {fname}")
