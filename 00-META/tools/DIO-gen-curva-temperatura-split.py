"""
DIO-gen-curva-temperatura-split.py
──────────────────────────────────
Genera 3 gráficas separadas del efecto de temperatura en el diodo de silicio.

Nomenclatura de salida (en 01-Circuitos-Diodos/media/generated/):
  DIO-curva-temp-02-directa.png   ← Polarización directa (encendido)
  DIO-curva-temp-03-inversa.png   ← Polarización inversa (corriente de fuga)
  DIO-curva-temp-04-ruptura.png   ← Región de ruptura (avalancha)

  Convención: {PREFIJO}-{tema}-{NN}-{descriptor}.png
    • PREFIJO = módulo (DIO)
    • tema    = concepto físico (curva-temp)
    • NN      = secuencia global dentro del tema (01 = combinada, 02-04 = splits)
    • descriptor = región o contenido

Modelo Físico:
  ► Región Directa: Ecuación de Shockley con Is(T) CALIBRADA al coeficiente
    de temperatura empírico del voltaje de umbral:
        Vth(T) = Vth(Tref) + Ktc · (T − Tref),  Ktc ≈ −2.5 mV/°C
    Se resuelve Is de: I_cal = Is · (exp(Vth/(n·Vt)) − 1)  →  Is = I_cal / (...)
    Esto garantiza que cada curva cruce la corriente de referencia (1 mA) en el
    Vth teórico: {100°C → 0.51V, 25°C → 0.70V, −100°C → 1.01V}.

    NOTA: el modelo anterior usaba la regla empírica "Is se duplica cada 10°C",
    que es válida para rangos pequeños (±30°C) pero FALLA a temperaturas extremas
    porque ignora la dependencia del bandgap. Eso producía curvas con ordenamiento
    incorrecto (−100°C conducía antes que 25°C).

  ► Región Inversa y Ruptura: regla empírica "Is se duplica cada 10°C"
    (Is_ref = 1 pA a 25°C), consistente con la explicación teórica DIO-01
    y adecuada para visualizar la magnitud relativa de la corriente de fuga.

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-curva-temperatura-split.py
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

# ════════════════════════════════════════════════════════════════
#  CONFIGURACIÓN
# ════════════════════════════════════════════════════════════════
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FILE_PREFIX = "DIO-curva-temp"
DPI = 150

# ════════════════════════════════════════════════════════════════
#  CONSTANTES FÍSICAS
# ════════════════════════════════════════════════════════════════
K_B = 1.380649e-23      # Constante de Boltzmann  [J/K]
Q_E = 1.60217663e-19    # Carga del electrón      [C]

# ════════════════════════════════════════════════════════════════
#  PARÁMETROS DEL DIODO (Silicio)
# ════════════════════════════════════════════════════════════════
VTH_REF     = 0.7        # Voltaje de umbral a T_REF         [V]
T_REF       = 25         # Temperatura de referencia          [°C]
KTC         = -2.5e-3    # Coef. de temperatura del Vth       [V/°C]
N           = 1          # Factor de idealidad
VBR_NOM     = -5.0       # Voltaje de ruptura nominal         [V]
ALPHA_BR    = 0.001      # Coef. de temperatura de Vbr        [1/°C]
IS_REF_EMP  = 1e-12      # Is empírica a 25°C (1 pA)         [A]
I_CAL       = 1e-3       # Corriente de calibración para Vth  [A]

# ════════════════════════════════════════════════════════════════
#  FUNCIONES DEL MODELO
# ════════════════════════════════════════════════════════════════
def Vt(T_c):
    """Voltaje térmico: Vt = kT/q  [V]"""
    return K_B * (T_c + 273.15) / Q_E

def Vth(T_c):
    """Voltaje de umbral empírico: Vth(T) = Vth(Tref) + Ktc·(T−Tref) [V]"""
    return VTH_REF + KTC * (T_c - T_REF)

def Is_calibrada(T_c):
    """
    Is calibrada para la región directa.
    Se obtiene de: I_CAL = Is · (exp(Vth/(n·Vt)) − 1)
    Garantiza que la curva de Shockley cruce I_CAL en V = Vth(T).
    """
    return I_CAL / (np.exp(Vth(T_c) / (N * Vt(T_c))) - 1)

def Is_empirica(T_c):
    """Is con regla empírica: se duplica cada 10°C (para inv/ruptura)."""
    return IS_REF_EMP * 2 ** ((T_c - T_REF) / 10)

def shockley(V, T_c, Is):
    """Corriente directa de Shockley (vectorizada)."""
    arg = np.clip(V / (N * Vt(T_c)), -100, 100)
    return Is * (np.exp(arg) - 1)

def i_breakdown(V, T_c, Is):
    """Corriente de ruptura (modelo exponencial simple)."""
    Vbr_T = VBR_NOM * (1 + ALPHA_BR * (T_c - T_REF))
    arg = np.clip(-(V - Vbr_T) / (N * Vt(T_c)), -100, 100)
    return -Is * np.exp(arg)

# ════════════════════════════════════════════════════════════════
#  CASOS DE TEMPERATURA
# ════════════════════════════════════════════════════════════════
temps = [
    {"T": -100, "label": "-100°C (Frío)",     "color": "#2ca02c"},
    {"T":   25, "label":  "25°C (Ambiente)",   "color": "#1f77b4"},
    {"T":  100, "label": "100°C (Caliente)",   "color": "#d62728"},
]
for t in temps:
    t["vth"] = round(Vth(t["T"]), 2)

# ════════════════════════════════════════════════════════════════
#  GRÁFICA 1 — POLARIZACIÓN DIRECTA  (Is calibrada → Vth exactos)
# ════════════════════════════════════════════════════════════════
v_fwd = np.linspace(0, 1.3, 2000)
fig, ax = plt.subplots(figsize=(9, 6))

for t in temps:
    Is = Is_calibrada(t["T"])
    I  = shockley(v_fwd, t["T"], Is)
    ax.plot(v_fwd, I * 1e3, color=t["color"], linewidth=2,
            label=f'T = {t["T"]}°C  ($V_{{th}}$ ≈ {t["vth"]}V)')
    ax.axvline(t["vth"], color=t["color"], linestyle=":", alpha=0.55, linewidth=1.2)

ax.set_title("Efecto de Temperatura — Polarización Directa (Encendido)", fontsize=13)
ax.set_xlabel("Voltaje ($V_D$) [V]")
ax.set_ylabel("Corriente ($I_D$) [mA]")
ax.set_xlim(0, 1.3)
ax.set_ylim(0, 20)
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left", fontsize=10)
fig.tight_layout()

fname1 = f"{FILE_PREFIX}-02-directa.png"
fig.savefig(os.path.join(OUTPUT_DIR, fname1), dpi=DPI)
plt.close(fig)
print(f"  ✓ {fname1}")

# ════════════════════════════════════════════════════════════════
#  GRÁFICA 2 — POLARIZACIÓN INVERSA  (Is empírica → fuga realista)
# ════════════════════════════════════════════════════════════════
v_inv = np.linspace(-4.0, 0, 1200)
fig, ax = plt.subplots(figsize=(9, 6))

for t in temps:
    Is = Is_empirica(t["T"])
    I  = shockley(v_inv, t["T"], Is) + i_breakdown(v_inv, t["T"], Is)
    Is_pA = Is * 1e12
    lbl = f'T = {t["T"]}°C  ($I_S$ ≈ {Is_pA:.1f} pA)' if Is_pA >= 0.1 \
        else f'T = {t["T"]}°C  ($I_S$ ≈ {Is*1e15:.2f} fA)'
    ax.plot(v_inv, I * 1e12, color=t["color"], linewidth=2, label=lbl)

ax.set_title("Efecto de Temperatura — Polarización Inversa (Corriente de Fuga)", fontsize=13)
ax.set_xlabel("Voltaje ($V_D$) [V]")
ax.set_ylabel("Corriente de Fuga ($I_S$) [pA]")
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(fontsize=10)
ax.set_yscale("symlog", linthresh=1)
ax.set_ylim(-300, 10)
fig.tight_layout()

fname2 = f"{FILE_PREFIX}-03-inversa.png"
fig.savefig(os.path.join(OUTPUT_DIR, fname2), dpi=DPI)
plt.close(fig)
print(f"  ✓ {fname2}")

# ════════════════════════════════════════════════════════════════
#  GRÁFICA 3 — REGIÓN DE RUPTURA  (Is empírica → avalancha visible)
# ════════════════════════════════════════════════════════════════
v_br = np.linspace(-6.5, -4.0, 1500)
fig, ax = plt.subplots(figsize=(9, 6))

for t in temps:
    Is = Is_empirica(t["T"])
    I  = shockley(v_br, t["T"], Is) + i_breakdown(v_br, t["T"], Is)
    Vbr_T = VBR_NOM * (1 + ALPHA_BR * (t["T"] - T_REF))
    ax.plot(v_br, I * 1e3, color=t["color"], linewidth=2,
            label=f'T = {t["T"]}°C  ($V_{{BR}}$ ≈ {Vbr_T:.2f}V)')

ax.set_title("Efecto de Temperatura — Región de Ruptura (Avalancha)", fontsize=13)
ax.set_xlabel("Voltaje ($V_D$) [V]")
ax.set_ylabel("Corriente ($I_D$) [mA]")
ax.axhline(0, color="black", linewidth=0.8)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="lower left", fontsize=10)
ax.set_ylim(-25, 1)
ax.set_xlim(-6.5, -4.0)
fig.tight_layout()

fname3 = f"{FILE_PREFIX}-04-ruptura.png"
fig.savefig(os.path.join(OUTPUT_DIR, fname3), dpi=DPI)
plt.close(fig)
print(f"  ✓ {fname3}")

# ════════════════════════════════════════════════════════════════
#  RESUMEN
# ════════════════════════════════════════════════════════════════
print("\n── Parámetros utilizados ──")
for t in temps:
    Is_cal = Is_calibrada(t["T"])
    Is_emp = Is_empirica(t["T"])
    print(f"  T = {t['T']:>5}°C  │  Vth = {t['vth']:.2f}V"
          f"  │  Is(cal) = {Is_cal:.3e}A"
          f"  │  Is(emp) = {Is_emp:.3e}A"
          f"  │  Vt = {Vt(t['T'])*1e3:.2f}mV")
print("\nListo — 3 imágenes generadas.")
