import numpy as np
import matplotlib.pyplot as plt

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
    
    # 1. Corriente Directa (Shockley)
    # Evitar overflow en exp con clip
    arg_wd = V / (n * Vt)
    arg_wd = np.clip(arg_wd, -100, 100) 
    i_forward = Is * (np.exp(arg_wd) - 1)
    
    # 2. Corriente Ruptura (Modelo simple exponencial)
    # Asumimos pequeño coeficiente positivo de temperatura para Vbr (Avalancha)
    # |Vbr| aumenta ligeramente con la temperatura. 0.1%/C
    alpha_br = 0.001 
    Vbr_T = Vbr_nominal * (1 + alpha_br * (T_celsius - 25))
    
    # La corriente fluye negativa fuerte cuando V < Vbr_T
    # Usamos inversa de exp para modelar la caida
    arg_br = -(V - Vbr_T) / (n * Vt)
    arg_br = np.clip(arg_br, -100, 100)
    
    # Solo "activamos" la corriente de ruptura si V < Vbr_T (aprox) para sumar limpio
    i_breakdown = -Is * np.exp(arg_br)
    
    return i_forward + i_breakdown

# Definir casos con nuevos colores solicitados
temps = [
    {"T": -100, "label": "-100°C (Frío)",     "color": "green", "vth_teorico": 1.01},
    {"T": 25,   "label": "25°C (Ambiente)",   "color": "blue",  "vth_teorico": 0.70},
    {"T": 100,  "label": "100°C (Caliente)",  "color": "red",   "vth_teorico": 0.51}
]

# Rango amplio para ver Inversa (-6V) y Directa (+1.2V)
v = np.linspace(-6.0, 1.2, 5000)

plt.figure(figsize=(12, 7))

for item in temps:
    i = diode_current_viz(v, item["T"])
    # Plot en mA
    plt.plot(v, i * 1000, label=f'T = {item["T"]}°C', color=item["color"], linewidth=2)
    
    # Marcadores de Vth (solo en la parte positiva para no saturar)
    if item["vth_teorico"] < 1.1:
        plt.axvline(item["vth_teorico"], color=item["color"], linestyle=':', alpha=0.5)
        # Etiqueta rotada
        plt.text(item["vth_teorico"], 5, f'$V_{{th}}({item["T"]}°C)$', 
                 rotation=90, verticalalignment='bottom', color=item["color"], fontsize=9)

plt.title('Efecto de la Temperatura: Directa, Inversa y Ruptura', fontsize=14)
plt.xlabel('Voltaje ($V_D$) [V]', fontsize=12)
plt.ylabel('Corriente ($I_D$) [mA]', fontsize=12)

# Ejes centrados (cruz)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# Grid
plt.grid(True, linestyle='--', alpha=0.5)

# Leyenda
plt.legend(loc='lower right')

# Ajuste de límites para ver bien ruptura y codo directo
plt.ylim(-15, 25)  # mA
plt.xlim(-6.2, 1.3) # V

# Anotaciones de regiones
plt.text(-3.0, 2, 'Región de Polarización Inversa ($I \\approx 0$)', 
         ha='center', fontsize=10, style='italic', color='gray')
plt.text(-5.2, -12, 'Región de\nRuptura', 
         ha='right', fontsize=10, fontweight='bold', color='purple')

output_path = 'Tema 1/curva_temperatura_diodo.png'
plt.savefig(output_path, dpi=100)
print(f"Gráfica actualizada guardada en: {output_path}")
