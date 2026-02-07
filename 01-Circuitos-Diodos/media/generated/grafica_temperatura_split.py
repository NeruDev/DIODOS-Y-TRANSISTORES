import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ----------------- FUNCIONES FÍSICAS -----------------
def get_vt(T_celsius):
    """Calcula voltaje térmico Vt = kT/q"""
    k = 1.380649e-23
    q = 1.60217663e-19
    T_kelvin = T_celsius + 273.15
    return (k * T_kelvin) / q

def get_is_approx(T_celsius, Is_ref=1e-12, T_ref=25):
    """
    Calcula Is usando la regla empírica: se duplica cada 10°C.
    Is_ref: Corriente a T_ref (default 1pA a 25°C)
    """
    delta_T = T_celsius - T_ref
    factor = 2 ** (delta_T / 10)
    return Is_ref * factor

def diode_current_viz(V, T_celsius, Is_ref=1e-12, n=1, Vbr_nominal=-5.0):
    Vt = get_vt(T_celsius)
    Is = get_is_approx(T_celsius, Is_ref)
    
    # Parámetros Ruptura
    alpha_br = 0.001 
    Vbr_T = Vbr_nominal * (1 + alpha_br * (T_celsius - 25))
    
    # Cálculo vectorial seguro
    i_total = np.zeros_like(V)
    
    for idx, v_val in enumerate(V):
        # 1. Directa
        arg_wd = v_val / (n * Vt)
        if arg_wd > 100: arg_wd = 100
        elif arg_wd < -100: arg_wd = -100
        i_fwd = Is * (np.exp(arg_wd) - 1)
        
        # 2. Ruptura
        # Solo calculamos si estamos cerca de Vbr o por debajo
        # Para suavizar, calculamos siempre y sumamos, pero con cuidado
        arg_br = -(v_val - Vbr_T) / (n * Vt)
        if arg_br > 100: arg_br = 100
        elif arg_br < -100: arg_br = -100
        i_br = -Is * np.exp(arg_br)
        
        i_total[idx] = i_fwd + i_br
        
    return i_total

# Definición de casos (Colores actualizados)
temps = [
    {"T": -100, "label": "-100°C (Frío)",      "color": "green", "vth_teorico": 1.01},
    {"T": 25,   "label": "25°C (Ambiente)",    "color": "blue",  "vth_teorico": 0.70},
    {"T": 100,  "label": "100°C (Caliente)",   "color": "red",   "vth_teorico": 0.51}
]

# ----------------- GRÁFICA 1: POLARIZACIÓN DIRECTA -----------------
v_fwd = np.linspace(0, 1.3, 1000)
plt.figure(figsize=(8, 6))

for item in temps:
    i = diode_current_viz(v_fwd, item["T"])
    plt.plot(v_fwd, i * 1000, label=f'T = {item["T"]}°C', color=item["color"], linewidth=2)
    # Marcador Vth
    if item["T"] == 25:
         plt.text(item["vth_teorico"], 2, f'$V_{{th}} \\approx {item["vth_teorico"]}V$', 
                 rotation=90, verticalalignment='bottom', color=item["color"], fontsize=10)

plt.title('Región de Polarización Directa (Encendido)')
plt.xlabel('Voltaje ($V_D$) [V]')
plt.ylabel('Corriente ($I_D$) [mA]')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.ylim(0, 20)
plt.xlim(0, 1.3)
plt.savefig('01-Circuitos-Diodos/01-Polarizacion-Recta-Carga/media/generated/curva_temp_directa.png', dpi=100)
print("Generada: curva_temp_directa.png")

# ----------------- GRÁFICA 2: POLARIZACIÓN INVERSA (ZOOM) -----------------
# Aquí la corriente es Is ~ pA. Es MUY pequeña.
# Usaremos escala pA (Pico Amperios) para visualizar algo.
v_rev = np.linspace(-4.0, 0, 1000) # Lejos de ruptura (-5V)

plt.figure(figsize=(8, 6))

for item in temps:
    i = diode_current_viz(v_rev, item["T"])
    # Convertir a pA (1e12)
    plt.plot(v_rev, i * 1e12, label=f'T = {item["T"]}°C', color=item["color"], linewidth=2)

plt.title('Región de Polarización Inversa (Corriente de Fuga)')
plt.xlabel('Voltaje ($V_D$) [V]')
plt.ylabel('Corriente de Fuga ($I_S$) [pA]')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
# Ajuste manual para ver diferencias
# A 100°C, Is crece mucho -> ~180pA
# A 25°C -> 1pA
# A -100°C -> ~0pA
plt.yscale('symlog', linthresh=1) # Log scale para ver diferencias grandes
plt.ylim(-200, 10) # Hasta un poco por encima de 0
plt.savefig('01-Circuitos-Diodos/01-Polarizacion-Recta-Carga/media/generated/curva_temp_inversa.png', dpi=100)
print("Generada: curva_temp_inversa.png")

# ----------------- GRÁFICA 3: REGIÓN DE RUPTURA -----------------
v_br = np.linspace(-6.0, -4.5, 1000)

plt.figure(figsize=(8, 6))

for item in temps:
    i = diode_current_viz(v_br, item["T"])
    plt.plot(v_br, i * 1000, label=f'T = {item["T"]}°C', color=item["color"], linewidth=2)

plt.title('Región de Ruptura (Avalancha)')
plt.xlabel('Voltaje ($V_D$) [V]')
plt.ylabel('Corriente ($I_D$) [mA]')
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower left')
plt.ylim(-20, 0)
plt.xlim(-6.0, -4.5)
plt.savefig('01-Circuitos-Diodos/01-Polarizacion-Recta-Carga/media/generated/curva_temp_ruptura.png', dpi=100)
print("Generada: curva_temp_ruptura.png")
