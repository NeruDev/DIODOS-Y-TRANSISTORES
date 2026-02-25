"""
DIO-gen-nota5-rectificador-onda-completa-central.py
───────────────────
Genera el esquemático de circuito y las formas de onda del rectificador
monofásico de onda completa con transformador de derivación central.

Salida:
  - 01-Circuitos-Diodos/media/generated/nota5_circuito.png
  - 01-Circuitos-Diodos/media/generated/nota5_formas_onda.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota5-rectificador-onda-completa-central.py

::SCRIPT_METADATA::
script_id: DIO-gen-nota5-rectificador-onda-completa-central
module: DIO
generates:
  - nota5_circuito.png
  - nota5_formas_onda.png
  - nota5_diodos_ac.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota5.md
last_updated: 2026-02-25
"""

import matplotlib
matplotlib.use('Agg')  # Backend sin GUI — obligatorio en entornos sin display
import numpy as np
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
import os

# ── Directorio de salida ────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Parámetros del circuito ─────────────────────────────────────────────────
Vm        = 20.0           # Voltaje pico de cada mitad del secundario [V]
f         = 60.0           # Frecuencia [Hz]
T         = 1.0 / f        # Período [s]
VD        = 0.7            # Caída de voltaje del diodo de silicio [V]

# Valores derivados
Vo_peak_ideal = Vm                          # Diodo ideal
Vo_peak_real  = Vm - VD                     # Diodo real
VDC_ideal     = 2 * Vm / np.pi             # Voltaje promedio ideal
VDC_real      = 2 * (Vm - VD) / np.pi      # Voltaje promedio real
Vrms_ideal    = Vm / np.sqrt(2)             # Vrms ideal
PIV           = 2 * Vm                      # Tensión inversa de pico

# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 1: Esquemático del circuito
# ═══════════════════════════════════════════════════════════════════════════
fname_sch = os.path.join(OUTPUT_DIR, "nota5_circuito.png")

with schemdraw.Drawing(show=False, dpi=160) as d:
    d.config(fontsize=11)

    # ── Fuente AC (primario) ─────────────────────────────────────────────
    d += (src := elm.SourceSin().up()
          .label('$V_p$', loc='left', ofst=0.4))

    d += elm.Line().right(2.0)

    # ── Primario del transformador (4 loops → más altura → espacio para RL)
    d += (prim := elm.Inductor2(loops=4).down()
          .label('$N_1$', loc='left', ofst=0.15))

    d += elm.Line().left().to(src.start)

    # ── Núcleo magnético (dos líneas verticales) ─────────────────────────
    cx1 = prim.start[0] + 1.0
    cx2 = prim.start[0] + 1.25
    d += (elm.Line()
          .at((cx1, prim.start[1] + 0.3))
          .to((cx1, prim.end[1] - 0.3))
          .color('dimgray').linewidth(3))
    d += (elm.Line()
          .at((cx2, prim.start[1] + 0.3))
          .to((cx2, prim.end[1] - 0.3))
          .color('dimgray').linewidth(3))

    # ── Coordenadas del secundario ───────────────────────────────────────
    sec_x     = prim.start[0] + 2.2
    sec_top_y = prim.start[1]
    sec_bot_y = prim.end[1]
    sec_mid_y = (sec_top_y + sec_bot_y) / 2

    # ── Secundario SUPERIOR (3 loops para densidad visual) ───────────────
    d += (sec_top := elm.Inductor2(loops=3).down().flip()
          .at((sec_x, sec_top_y))
          .to((sec_x, sec_mid_y)))

    # ── Secundario INFERIOR ──────────────────────────────────────────────
    d += (sec_bot := elm.Inductor2(loops=3).down().flip()
          .at((sec_x, sec_mid_y))
          .to((sec_x, sec_bot_y)))

    # ── Derivación central (CT) ──────────────────────────────────────────
    d += elm.Dot().at((sec_x, sec_mid_y))
    d += elm.Label().at((sec_x - 0.5, sec_mid_y - 0.35)).label('CT', fontsize=9)

    # ── Etiquetas de voltaje del secundario ──────────────────────────────
    # Los bumps van a la izquierda (flip), así que la derecha está limpia.
    # Posicionar las etiquetas a la derecha del devanado, entre el inductor
    # y los diodos, separadas verticalmente para no solapar con RL.
    mid_top_y = (sec_top_y + sec_mid_y) / 2
    mid_bot_y = (sec_mid_y + sec_bot_y) / 2

    # V_s1 — mitad superior (su centro está arriba de RL → sin conflicto)
    d += elm.Label().at((sec_x + 0.50, mid_top_y)).label(
        '$V_{s1}$', fontsize=11)
    d += elm.Label().at((sec_x + 0.50, sec_top_y - 0.12)).label(
        '$+$', fontsize=10, color='#1565C0')

    # V_s2 — mitad inferior (su centro está abajo de RL → sin conflicto)
    d += elm.Label().at((sec_x + 0.50, mid_bot_y)).label(
        '$V_{s2}$', fontsize=11)
    d += elm.Label().at((sec_x + 0.50, sec_bot_y + 0.12)).label(
        '$-$', fontsize=10, color='#7B1FA2')

    # ── Diodo D1 (desde extremo superior del secundario) ─────────────────
    d += elm.Line().right(1.5).at(sec_top.start)
    d += (D1 := elm.Diode().right()
          .label('$D_1$', loc='top'))

    # ── Diodo D2 (desde extremo inferior del secundario) ─────────────────
    d += elm.Line().right(1.5).at(sec_bot.end)
    d += (D2 := elm.Diode().right()
          .label('$D_2$', loc='bot'))

    # ── Leyendas de voltaje de los diodos ────────────────────────────────
    d += elm.Gap().at(D1.start).to(D1.end).label(
        ['+', '$v_{D_1}$', '−'], loc='bot', ofst=0.45)

    d += elm.Gap().at(D2.start).to(D2.end).label(
        ['+', '$v_{D_2}$', '−'], loc='top', ofst=0.45)

    # ── Unión de cátodos de D1 y D2 (nodo A: terminal (+) de Vo) ────────
    cathode_x = D1.end[0]
    d += elm.Line().down().at(D1.end).to((cathode_x, sec_mid_y))
    d += elm.Line().up().at(D2.end).to((cathode_x, sec_mid_y))
    d += elm.Dot().at((cathode_x, sec_mid_y))

    # ── RL horizontal POR DENTRO del circuito ────────────────────────────
    # RL conecta: cátodos (+) ←──RL──→ CT (−)
    # Trazado horizontal a nivel sec_mid_y, entre D1 y D2 (con espacio)
    d += (RL_elm := elm.Resistor().left()
          .at((cathode_x, sec_mid_y))
          .to((sec_x, sec_mid_y))
          .label('$R_L$', loc='bot', ofst=0.15))

    # ── Indicador de Vo sobre la resistencia ─────────────────────────────
    d += elm.Gap().at((cathode_x, sec_mid_y)).to((sec_x, sec_mid_y)).label(
        ['+', '$V_o$', '−'], loc='top', ofst=0.45)

    d.save(fname_sch)

print(f"Generado: {fname_sch}")

# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 2: Formas de onda
# ═══════════════════════════════════════════════════════════════════════════
fname_waves = os.path.join(OUTPUT_DIR, "nota5_formas_onda.png")

owt = np.linspace(0, 4 * np.pi, 4000)   # 2 ciclos completos

# Señales
vs_top = Vm * np.sin(owt)                        # Mitad superior del secundario
vs_bot = -Vm * np.sin(owt)                       # Mitad inferior (desfasada 180°)
vo_ideal = np.abs(Vm * np.sin(owt))              # Salida ideal (onda completa)
vo_real = np.maximum(np.abs(Vm * np.sin(owt)) - VD, 0)  # Salida con diodo real

# Tensión inversa en cada diodo
vD1 = np.where(vs_top > VD, VD, -vs_top - vo_real)   # Aprox: cuando no conduce, soporta ≈ -2Vm
vD1_inv = np.where(np.sin(owt) >= 0, 0, -2 * Vm * np.abs(np.sin(owt)))

# Para PIV más preciso:
# Cuando D1 conduce (semiciclo +): vD1 ≈ 0 (ideal)
# Cuando D1 no conduce (semiciclo -): vD1 = vs_top - vo = -Vm*sin(ωt) - Vm*|sin(ωt)|
#   en semiciclo negativo sin(ωt) < 0 → |sin(ωt)| = -sin(ωt)
#   vD1 = -Vm*sin(ωt) - Vm*(-sin(ωt)) = 0?  No, eso no es correcto.
# Revisemos: cuando D2 conduce, vo = Vm*|sin(ωt)|. D1 tiene ánodo en +vs_top = Vm*sin(ωt) (negativo)
# y cátodo en vo = Vm*|sin(ωt)|. Entonces vD1 = vs_top - vo = Vm*sin(ωt) - Vm*|sin(ωt)|
# En semiciclo negativo: sin(ωt) < 0, |sin(ωt)| = -sin(ωt)
# vD1 = Vm*sin(ωt) - Vm*(-sin(ωt)) = 2*Vm*sin(ωt) → negativo (ya que sin < 0)
# PIV = max|vD1| = 2*Vm  ✓

vD1_ideal = np.where(np.sin(owt) >= 0, 0, 2 * Vm * np.sin(owt))  # negativo en semiciclo -

pi_ticks = np.arange(0, 4*np.pi + 0.1, np.pi/2)
pi_labels = ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$',
             r'$\frac{5\pi}{2}$', r'$3\pi$', r'$\frac{7\pi}{2}$', r'$4\pi$']

fig, axes = plt.subplots(3, 1, figsize=(12, 11), sharex=True)
fig.suptitle(
    "Rectificador Monofásico de Onda Completa — Derivación Central\n"
    rf"$V_m = {Vm:.0f}\,V$,  $f = {f:.0f}\,Hz$,  Diodo Ideal vs Real ($V_D = {VD}\,V$)",
    fontsize=13, fontweight='bold'
)

# Colores
c_top = '#2196F3'    # azul
c_bot = '#9C27B0'    # púrpura
c_out = '#4CAF50'    # verde
c_vd  = '#F44336'    # rojo
c_dc  = 'darkorange' # naranja

# ── Subplot 1: Voltajes del secundario ──────────────────────────────────────
ax1 = axes[0]
ax1.plot(owt, vs_top, color=c_top, linewidth=2, label=r'$v_{s1}(\omega t)$ — Mitad superior')
ax1.plot(owt, vs_bot, color=c_bot, linewidth=1.8, linestyle='--',
         label=r'$v_{s2}(\omega t)$ — Mitad inferior')
ax1.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax1.axhline(Vm, color=c_top, linewidth=0.7, linestyle='--', alpha=0.4)
ax1.axhline(-Vm, color=c_top, linewidth=0.7, linestyle='--', alpha=0.4)

# Anotaciones de semiciclos
ax1.annotate(f'$+V_m = +{Vm:.0f}\\,V$',
             xy=(np.pi/2, Vm), xytext=(np.pi/2 + 0.5, Vm + 2),
             fontsize=9, color=c_top,
             arrowprops=dict(arrowstyle='->', color=c_top, lw=1.1))
ax1.annotate(f'$-V_m = -{Vm:.0f}\\,V$',
             xy=(3*np.pi/2, -Vm), xytext=(3*np.pi/2 + 0.5, -Vm - 3),
             fontsize=9, color=c_top,
             arrowprops=dict(arrowstyle='->', color=c_top, lw=1.1))

# Sombreado de semiciclos
ax1.fill_between(owt, vs_top, 0, where=(vs_top > 0), alpha=0.08, color=c_top)
ax1.fill_between(owt, vs_top, 0, where=(vs_top < 0), alpha=0.08, color='gray')

# Indicación de qué diodo conduce
for k in range(2):  # 2 ciclos
    base = 2 * np.pi * k
    ax1.text(base + np.pi/2, -Vm * 0.65, '$D_1$ ON',
             ha='center', fontsize=8.5, color='#1B5E20', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#C8E6C9', alpha=0.8))
    ax1.text(base + 3*np.pi/2, -Vm * 0.65, '$D_2$ ON',
             ha='center', fontsize=8.5, color='#4A148C', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#E1BEE7', alpha=0.8))

ax1.set_ylabel('Tensión (V)', fontsize=10)
ax1.set_ylim(-Vm * 1.5, Vm * 1.5)
ax1.set_title('Voltajes del secundario del transformador (respecto a derivación central)',
              fontsize=10)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.5)

# ── Subplot 2: Voltaje de salida vo ─────────────────────────────────────────
ax2 = axes[1]
ax2.plot(owt, vo_ideal, color=c_out, linewidth=2, alpha=0.4,
         label=r'$v_o$ — Diodo ideal')
ax2.plot(owt, vo_real, color=c_out, linewidth=2,
         label=rf'$v_o$ — Diodo real ($V_D = {VD}\,V$)')

# Niveles DC
ax2.axhline(VDC_ideal, color=c_dc, linewidth=1.4, linestyle='--', alpha=0.9,
            label=f'$V_{{DC}}$ ideal $= {VDC_ideal:.2f}\\,V$')
ax2.axhline(VDC_real, color='brown', linewidth=1.2, linestyle=':', alpha=0.9,
            label=f'$V_{{DC}}$ real $= {VDC_real:.2f}\\,V$')
ax2.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax2.axhline(Vm, color=c_out, linewidth=0.7, linestyle='--', alpha=0.4)

ax2.annotate(f'$V_m = {Vm:.0f}\\,V$',
             xy=(np.pi/2, Vm), xytext=(np.pi/2 + 0.5, Vm + 1.5),
             fontsize=9, color='#2E7D32',
             arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.1))

# Sombreado
ax2.fill_between(owt, vo_real, 0, alpha=0.12, color=c_out)

# Texto: frecuencia duplicada
ax2.text(0.02, 0.88, f'$f_{{rizo}} = 2f = {2*f:.0f}\\,Hz$',
         transform=ax2.transAxes, fontsize=9, color='navy',
         bbox=dict(boxstyle='round,pad=0.25', fc='lightyellow', alpha=0.8))

ax2.set_ylabel('Tensión (V)', fontsize=10)
ax2.set_ylim(-2, Vm * 1.35)
ax2.set_title('Voltaje de salida en $R_L$ — Onda completa rectificada', fontsize=10)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.5)

# ── Subplot 3: Tensión inversa en D1 ────────────────────────────────────────
ax3 = axes[2]
ax3.plot(owt, vD1_ideal, color=c_vd, linewidth=2,
         label=r'$v_{D1}(\omega t)$ — Tensión en $D_1$')
ax3.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax3.axhline(-PIV, color=c_vd, linewidth=0.8, linestyle='--', alpha=0.5)
ax3.fill_between(owt, vD1_ideal, 0, where=(vD1_ideal < 0), alpha=0.12, color=c_vd)

# Zona de conducción
for k in range(2):
    base = 2 * np.pi * k
    ax3.text(base + np.pi/2, 2, 'Conducción\n$V_{D1} = 0\\,V$',
             ha='center', va='bottom', fontsize=8, color='#2E7D32',
             bbox=dict(boxstyle='round,pad=0.2', fc='#E8F5E9', alpha=0.85))

# PIV
ax3.annotate(
    f'PIV = $2V_m = {PIV:.0f}\\,V$',
    xy=(3*np.pi/2, -PIV), xytext=(3*np.pi/2 + 0.8, -PIV + 8),
    fontsize=9, color='#B71C1C',
    arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.2))

ax3.text(3*np.pi/2, -PIV * 0.4, 'Bloqueo',
         ha='center', va='center', fontsize=8.5, color='#B71C1C',
         bbox=dict(boxstyle='round,pad=0.2', fc='#FFEBEE', alpha=0.85))

ax3.set_ylabel('Tensión (V)', fontsize=10)
ax3.set_xlabel(r'$\omega t$ (rad)', fontsize=10)
ax3.set_ylim(-PIV * 1.3, PIV * 0.3)
ax3.set_title(r'Tensión inversa en $D_1$ — Voltaje Inverso de Pico (PIV = $2V_m$)', fontsize=10)
ax3.legend(loc='upper right', fontsize=9)
ax3.grid(True, linestyle=':', alpha=0.5)

# Eje x con etiquetas en radianes
for ax in axes:
    ax.axvline(np.pi, color='black', linewidth=0.6, linestyle='--', alpha=0.3)
    ax.axvline(2*np.pi, color='black', linewidth=0.6, linestyle='--', alpha=0.3)
    ax.axvline(3*np.pi, color='black', linewidth=0.6, linestyle='--', alpha=0.3)
    ax.set_xlim(0, 4*np.pi)
    ax.set_xticks(pi_ticks)
    ax.set_xticklabels(pi_labels, fontsize=10)

# ── Tabla resumen ────────────────────────────────────────────────────────────
table_data = [
    ['Voltaje pico de salida (ideal)', '$V_{o,m}$', f'{Vo_peak_ideal:.1f} V'],
    ['Voltaje DC (ideal)',             '$V_{{DC}}$', f'{VDC_ideal:.2f} V'],
    ['Voltaje rms (ideal)',            '$V_{{rms}}$', f'{Vrms_ideal:.2f} V'],
    ['Voltaje pico de salida (real)',  '$V_{o,m}$', f'{Vo_peak_real:.2f} V'],
    ['Voltaje DC (real)',              '$V_{{DC}}$', f'{VDC_real:.2f} V'],
    ['PIV por diodo',                  'PIV',        f'{PIV:.0f} V'],
    ['Frecuencia de rizado',           '$f_r$',      f'{2*f:.0f} Hz'],
]

ax_tbl = fig.add_axes([0.58, 0.01, 0.40, 0.14])
ax_tbl.axis('off')
tbl = ax_tbl.table(
    cellText=[[row[1], row[2]] for row in table_data],
    colLabels=['Símbolo', 'Valor'],
    rowLabels=[row[0] for row in table_data],
    cellLoc='center',
    loc='center'
)
tbl.auto_set_font_size(False)
tbl.set_fontsize(7.5)
tbl.scale(1, 1.25)

plt.tight_layout(rect=[0, 0.16, 1, 1])
plt.savefig(fname_waves, dpi=120, bbox_inches='tight')
plt.close()
print(f"Generado: {fname_waves}")

# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 3: Comportamiento de cada diodo en AC
# ═══════════════════════════════════════════════════════════════════════════
fname_diodos = os.path.join(OUTPUT_DIR, "nota5_diodos_ac.png")

RL_val = 100.0  # Resistencia de carga de referencia [Ω] (para escalar corrientes)

# ── Señales por diodo (diodo ideal) ─────────────────────────────────────────
# D1: ánodo conectado a la mitad superior → conduce cuando sin(ωt) > 0
# D2: ánodo conectado a la mitad inferior → conduce cuando sin(ωt) < 0

# Voltajes en cada diodo (ideal):
#   Conducción: vD = 0 V
#   Bloqueo:    vD = v_ánodo - v_cátodo = v_si - vo
#     D1 bloqueado (semiciclo -): vD1 = Vm·sin(ωt) - Vm·|sin(ωt)| = 2Vm·sin(ωt) < 0
#     D2 bloqueado (semiciclo +): vD2 = -Vm·sin(ωt) - Vm·|sin(ωt)| = -2Vm·sin(ωt) < 0

vD1_ac = np.where(np.sin(owt) >= 0, 0.0, 2 * Vm * np.sin(owt))
vD2_ac = np.where(np.sin(owt) <  0, 0.0, -2 * Vm * np.sin(owt))

# Corrientes por cada diodo (ideal):
#   Conducción: iD = Vm·|sin(ωt)| / RL
#   Bloqueo:    iD = 0
iD1_ac = np.where(np.sin(owt) >= 0, Vm * np.sin(owt) / RL_val, 0.0)
iD2_ac = np.where(np.sin(owt) <  0, Vm * np.abs(np.sin(owt)) / RL_val, 0.0)

# Corriente total en RL = iD1 + iD2
iRL_ac = iD1_ac + iD2_ac

# Corriente pico
Im = Vm / RL_val  # A

fig3, axes3 = plt.subplots(4, 1, figsize=(12, 14), sharex=True)
fig3.suptitle(
    "Comportamiento Individual de los Diodos en AC — Derivación Central\n"
    rf"$V_m = {Vm:.0f}\,V$,  $R_L = {RL_val:.0f}\,\Omega$,  Diodos Ideales",
    fontsize=13, fontweight='bold'
)

# Colores
c_d1v = '#1565C0'    # azul oscuro (voltaje D1)
c_d1i = '#42A5F5'    # azul claro  (corriente D1)
c_d2v = '#7B1FA2'    # púrpura oscuro (voltaje D2)
c_d2i = '#BA68C8'    # púrpura claro  (corriente D2)
c_irl = '#2E7D32'    # verde oscuro   (corriente RL)

pi_ticks_3 = np.arange(0, 2*np.pi + 0.1, np.pi/2)
pi_labels_3 = ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']

# ── Subplot 1: Voltaje en D1 ────────────────────────────────────────────────
ax = axes3[0]
ax.plot(owt, vD1_ac, color=c_d1v, linewidth=2.2, label=r'$v_{D_1}(\omega t)$')
ax.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax.axhline(-PIV, color=c_d1v, linewidth=0.8, linestyle='--', alpha=0.45)
ax.fill_between(owt, vD1_ac, 0, where=(vD1_ac == 0), alpha=0.10, color='#4CAF50')
ax.fill_between(owt, vD1_ac, 0, where=(vD1_ac < 0),  alpha=0.12, color=c_d1v)

# Anotaciones
for k in range(2):
    base = 2 * np.pi * k
    ax.text(base + np.pi/2, 3, r'$D_1$ ON' + '\n' + r'$v_{D_1} = 0$',
            ha='center', va='bottom', fontsize=8.5, color='#1B5E20', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='#E8F5E9', alpha=0.85))
    ax.text(base + 3*np.pi/2, -PIV * 0.35, r'$D_1$ OFF' + '\n' + r'$v_{D_1} = 2V_m \sin(\omega t)$',
            ha='center', va='center', fontsize=8, color='#0D47A1',
            bbox=dict(boxstyle='round,pad=0.2', fc='#E3F2FD', alpha=0.85))

ax.annotate(f'PIV = $-2V_m = -{PIV:.0f}\\,V$',
            xy=(3*np.pi/2, -PIV), xytext=(3*np.pi/2 + 1.2, -PIV + 7),
            fontsize=9, color='#B71C1C',
            arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.2))

ax.set_ylabel('$v_{D_1}$ (V)', fontsize=10)
ax.set_ylim(-PIV * 1.25, PIV * 0.2)
ax.set_title(r'Tensión en el diodo $D_1$', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.5)

# ── Subplot 2: Corriente en D1 ──────────────────────────────────────────────
ax = axes3[1]
ax.plot(owt, iD1_ac * 1000, color=c_d1i, linewidth=2.2, label=r'$i_{D_1}(\omega t)$')
ax.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax.axhline(Im * 1000, color=c_d1i, linewidth=0.8, linestyle='--', alpha=0.45)
ax.fill_between(owt, iD1_ac * 1000, 0, where=(iD1_ac > 0), alpha=0.15, color=c_d1i)

# Anotaciones
ax.annotate(f'$I_m = {Im*1000:.0f}\\,mA$',
            xy=(np.pi/2, Im * 1000), xytext=(np.pi/2 + 0.6, Im * 1000 + 30),
            fontsize=9, color='#0D47A1',
            arrowprops=dict(arrowstyle='->', color='#0D47A1', lw=1.1))

for k in range(2):
    base = 2 * np.pi * k
    ax.text(base + np.pi/2, Im * 1000 * 0.4, r'$D_1$ conduce',
            ha='center', fontsize=8.5, color='#1565C0', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='#BBDEFB', alpha=0.8))
    ax.text(base + 3*np.pi/2, Im * 1000 * 0.25, r'$i_{D_1} = 0$',
            ha='center', fontsize=8.5, color='gray',
            bbox=dict(boxstyle='round,pad=0.2', fc='#F5F5F5', alpha=0.8))

ax.set_ylabel('$i_{D_1}$ (mA)', fontsize=10)
ax.set_ylim(-Im * 1000 * 0.15, Im * 1000 * 1.35)
ax.set_title(r'Corriente por el diodo $D_1$ — Conduce en semiciclo positivo', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.5)

# ── Subplot 3: Voltaje en D2 ────────────────────────────────────────────────
ax = axes3[2]
ax.plot(owt, vD2_ac, color=c_d2v, linewidth=2.2, label=r'$v_{D_2}(\omega t)$')
ax.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax.axhline(-PIV, color=c_d2v, linewidth=0.8, linestyle='--', alpha=0.45)
ax.fill_between(owt, vD2_ac, 0, where=(vD2_ac == 0), alpha=0.10, color='#4CAF50')
ax.fill_between(owt, vD2_ac, 0, where=(vD2_ac < 0),  alpha=0.12, color=c_d2v)

# Anotaciones
for k in range(2):
    base = 2 * np.pi * k
    ax.text(base + np.pi/2, -PIV * 0.35, r'$D_2$ OFF' + '\n' + r'$v_{D_2} = -2V_m \sin(\omega t)$',
            ha='center', va='center', fontsize=8, color='#4A148C',
            bbox=dict(boxstyle='round,pad=0.2', fc='#F3E5F5', alpha=0.85))
    ax.text(base + 3*np.pi/2, 3, r'$D_2$ ON' + '\n' + r'$v_{D_2} = 0$',
            ha='center', va='bottom', fontsize=8.5, color='#1B5E20', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='#E8F5E9', alpha=0.85))

ax.annotate(f'PIV = $-2V_m = -{PIV:.0f}\\,V$',
            xy=(np.pi/2, -PIV), xytext=(np.pi/2 + 1.2, -PIV + 7),
            fontsize=9, color='#B71C1C',
            arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.2))

ax.set_ylabel('$v_{D_2}$ (V)', fontsize=10)
ax.set_ylim(-PIV * 1.25, PIV * 0.2)
ax.set_title(r'Tensión en el diodo $D_2$', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.5)

# ── Subplot 4: Corriente en D2 ──────────────────────────────────────────────
ax = axes3[3]
ax.plot(owt, iD2_ac * 1000, color=c_d2i, linewidth=2.2, label=r'$i_{D_2}(\omega t)$')
ax.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax.axhline(Im * 1000, color=c_d2i, linewidth=0.8, linestyle='--', alpha=0.45)
ax.fill_between(owt, iD2_ac * 1000, 0, where=(iD2_ac > 0), alpha=0.15, color=c_d2i)

# Anotaciones
ax.annotate(f'$I_m = {Im*1000:.0f}\\,mA$',
            xy=(3*np.pi/2, Im * 1000), xytext=(3*np.pi/2 + 0.6, Im * 1000 + 30),
            fontsize=9, color='#4A148C',
            arrowprops=dict(arrowstyle='->', color='#4A148C', lw=1.1))

for k in range(2):
    base = 2 * np.pi * k
    ax.text(base + np.pi/2, Im * 1000 * 0.25, r'$i_{D_2} = 0$',
            ha='center', fontsize=8.5, color='gray',
            bbox=dict(boxstyle='round,pad=0.2', fc='#F5F5F5', alpha=0.8))
    ax.text(base + 3*np.pi/2, Im * 1000 * 0.4, r'$D_2$ conduce',
            ha='center', fontsize=8.5, color='#7B1FA2', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', fc='#E1BEE7', alpha=0.8))

ax.set_ylabel('$i_{D_2}$ (mA)', fontsize=10)
ax.set_xlabel(r'$\omega t$ (rad)', fontsize=10)
ax.set_ylim(-Im * 1000 * 0.15, Im * 1000 * 1.35)
ax.set_title(r'Corriente por el diodo $D_2$ — Conduce en semiciclo negativo', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.5)

# Líneas divisorias y formato de ejes
for ax in axes3:
    ax.axvline(np.pi, color='black', linewidth=0.6, linestyle='--', alpha=0.35)
    ax.set_xlim(0, 2*np.pi)
    ax.set_xticks(pi_ticks_3)
    ax.set_xticklabels(pi_labels_3, fontsize=10)

plt.tight_layout()
plt.savefig(fname_diodos, dpi=120, bbox_inches='tight')
plt.close()
print(f"Generado: {fname_diodos}")
