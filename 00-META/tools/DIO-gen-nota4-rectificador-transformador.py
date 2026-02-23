"""
DIO-gen-nota4-rectificador-transformador.py
───────────────────
Genera el esquemático de circuito y las formas de onda del rectificador
de media onda con transformador reductor 10:1.

Parámetros del ejercicio:
  - Fuente primaria: 120 V rms, 60 Hz
  - Relación de vueltas: Np/Ns = 10:1
  - Resistencia de carga: RL = 5 Ω

Salida:
  - 01-Circuitos-Diodos/media/generated/nota4_circuito.png
  - 01-Circuitos-Diodos/media/generated/nota4_formas_onda.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota4-rectificador-transformador.py

::SCRIPT_METADATA::
script_id: DIO-gen-nota4-rectificador-transformador
module: DIO
generates:
  - nota4_circuito.png
  - nota4_formas_onda.png
  - nota4_voltajes_ideales.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota4.md
last_updated: 2026-02-23
"""

import matplotlib
matplotlib.use('Agg')  # Backend sin GUI — obligatorio en entornos sin display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import schemdraw
import schemdraw.elements as elm
import os

# ── Directorio de salida ────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Parámetros del circuito ─────────────────────────────────────────────────
Vp_rms    = 120.0          # Voltaje rms en el primario [V]
n         = 10.0           # Relación de vueltas Np/Ns
Vs_rms    = Vp_rms / n     # Voltaje rms en el secundario [V]  → 12 V
Vs_peak   = Vs_rms * np.sqrt(2)   # Voltaje pico secundario [V]  → ~16.97 V
f         = 60.0           # Frecuencia [Hz]
T         = 1.0 / f        # Período [s]
RL        = 5.0            # Resistencia de carga [Ω]
VD        = 0.7            # Caída de voltaje del diodo de silicio [V]

# Valores con diodo real
Vo_peak   = Vs_peak - VD               # Voltaje pico de salida [V]
Vo_avg    = Vo_peak / np.pi            # Voltaje promedio de salida [V]  (rectificador media onda)
Io_avg    = Vo_avg / RL                # Corriente promedio de salida [A]
Io_peak   = Vo_peak / RL              # Corriente pico de salida [A]

# ── FIGURA 1: Esquemático del circuito ──────────────────────────────────────
fname_sch = os.path.join(OUTPUT_DIR, "nota4_circuito.png")

with schemdraw.Drawing(show=False, dpi=160) as d:
    d.config(fontsize=11)

    # ── Malla primaria ────────────────────────────────────────────────────
    # Fuente sinusoidal: etiqueta a la izquierda con offset suficiente
    # para que no se superponga con el conductor superior
    d += (src := elm.SourceSin().up()
          .label('$V_p = 120\\ V_{rms}$\n$f = 60\\ Hz$', loc='left', ofst=0.55))

    d += elm.Line().right(2.5)   # conductor superior malla primaria

    # Primario del transformador (bobina hacia abajo, bumps a la derecha → hacia el núcleo)
    d += (prim := elm.Inductor2(loops=3).down()
          .label('$N_1$', loc='left', ofst=0.15))

    d += elm.Line().left().to(src.start)   # conductor inferior cierra malla primaria

    # ── Núcleo magnético ─────────────────────────────────────────────────
    # Separación entre primario y secundario: 2.5 unidades
    # → núcleo centrado en prim.start[0] + 1.25
    # Dos líneas sólidas (núcleo de hierro), separadas 0.25 u, centradas en 1.25
    cx1 = prim.start[0] + 1.125
    cx2 = prim.start[0] + 1.375
    d += (elm.Line()
          .at((cx1, prim.start[1]))
          .to((cx1, prim.end[1]))
          .color('dimgray').linewidth(3))
    d += (elm.Line()
          .at((cx2, prim.start[1]))
          .to((cx2, prim.end[1]))
          .color('dimgray').linewidth(3))

    # Etiqueta de relación de vueltas — elevada para no solaparse con bobinas
    d += elm.Label().at(((cx1 + cx2) / 2, prim.start[1] + 0.70)).label('$10:1$')

    # ── Secundario (simétrico al primario) ───────────────────────────────
    # Colocado 2.5 u a la derecha del primario; .flip() invierte los bumps
    # para que apunten a la IZQUIERDA → hacia el núcleo (requisito del transformador)
    # Etiquetas separadas: N2 en el centro-derecha, Vs en la terminal inferior
    d += (sec := elm.Inductor2(loops=3).down().flip()
          .at((prim.start[0] + 2.5, prim.start[1]))
          .label('$N_2$', loc='right', ofst=0.15)
          .label('$V_s = 12\\ V_{rms}$', loc='bot', ofst=0.15))

    # ── Malla secundaria ─────────────────────────────────────────────────
    # Conductor superior: sale del nodo alto del secundario → diodo → RL
    d += elm.Line().right(1.5).at(sec.start)
    d += (D := elm.Diode().right().label('$D$', loc='top'))
    d += elm.Line().right(0.8)

    # Resistencia de carga (rama vertical)
    d += (RL_elm := elm.Resistor().down()
          .label('$R_L = 5\\ \\Omega$', loc='right'))

    # Indicación de voltaje de salida (+ / Vo / −)
    d += elm.Gap().at(RL_elm.start).to(RL_elm.end).label(
        ['+', '$V_o$', '−'], loc='left', ofst=0.5)

    # Flecha de corriente Io
    d += elm.CurrentLabel(top=True, ofst=0.35, length=1.0).at(RL_elm).label('$I_o$')

    # Conductor inferior: cierra la malla secundaria
    d += elm.Line().left().to(sec.end)

    d.save(fname_sch)

print(f"Generado: {fname_sch}")

# ── FIGURA 2: Formas de onda ─────────────────────────────────────────────────
fname_waves = os.path.join(OUTPUT_DIR, "nota4_formas_onda.png")

omega_t = np.linspace(0, 4 * np.pi, 2000)   # 2 ciclos completos
t_ms    = omega_t / (2 * np.pi * f) * 1000   # tiempo en ms (para el eje)

vs = Vs_peak * np.sin(omega_t)
vo = np.where(vs > VD, vs - VD, 0.0)         # diodo real: conduce cuando vs > Vd
vD = vs - vo                                   # caída en el diodo

fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
fig.suptitle(
    "Rectificador de Media Onda con Transformador Reductor (10:1)\n"
    r"$V_{p} = 120\,V_{rms}$,  $f = 60\,Hz$,  $R_L = 5\,\Omega$",
    fontsize=13, fontweight='bold'
)

# Colores
c_in  = '#2196F3'   # azul
c_out = '#4CAF50'   # verde
c_vd  = '#F44336'   # rojo

# ── Subplot 1: Voltaje de entrada vs ────────────────────────────────────────
ax1 = axes[0]
ax1.plot(t_ms, vs, color=c_in, linewidth=2, label='$v_s(t)$ — Voltaje secundario')
ax1.axhline(0, color='black', linewidth=0.7, linestyle=':')
ax1.axhline(Vs_peak,  color=c_in, linewidth=0.8, linestyle='--', alpha=0.6)
ax1.axhline(-Vs_peak, color=c_in, linewidth=0.8, linestyle='--', alpha=0.6)
ax1.annotate(f'$V_{{s,pico}}$ = {Vs_peak:.2f} V',
             xy=(t_ms[np.argmax(vs)], Vs_peak), xytext=(2, Vs_peak - 3),
             fontsize=9, color=c_in,
             arrowprops=dict(arrowstyle='->', color=c_in, lw=1.2))
ax1.set_ylabel('Tensión (V)', fontsize=10)
ax1.set_ylim(-Vs_peak * 1.3, Vs_peak * 1.3)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.set_title('Voltaje de entrada al rectificador', fontsize=10)
ax1.fill_between(t_ms, vs, 0, where=(vs > 0), alpha=0.12, color=c_in, label='semiciclo+')
ax1.fill_between(t_ms, vs, 0, where=(vs < 0), alpha=0.12, color='gray', label='semiciclo−')

# ── Subplot 2: Voltaje de salida vo ─────────────────────────────────────────
ax2 = axes[1]
ax2.plot(t_ms, vo, color=c_out, linewidth=2, label='$v_o(t)$ — Voltaje en $R_L$')
ax2.axhline(0,       color='black', linewidth=0.7, linestyle=':')
ax2.axhline(Vo_peak, color=c_out, linewidth=0.8, linestyle='--', alpha=0.6)
ax2.axhline(Vo_avg,  color='darkorange', linewidth=1.2, linestyle='--', alpha=0.9,
            label=f'$V_{{o,avg}}$ = {Vo_avg:.2f} V')
ax2.annotate(f'$V_{{o,pico}}$ = {Vo_peak:.2f} V',
             xy=(t_ms[np.argmax(vo)], Vo_peak), xytext=(2, Vo_peak - 3),
             fontsize=9, color=c_out,
             arrowprops=dict(arrowstyle='->', color=c_out, lw=1.2))
ax2.set_ylabel('Tensión (V)', fontsize=10)
ax2.set_ylim(-2, Vo_peak * 1.35)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.set_title('Voltaje de salida (post-diodo, diodo real $V_D = 0.7\\ V$)', fontsize=10)
ax2.fill_between(t_ms, vo, 0, where=(vo > 0), alpha=0.15, color=c_out)

# ── Subplot 3: Caída en el diodo vD ─────────────────────────────────────────
ax3 = axes[2]
ax3.plot(t_ms, vD, color=c_vd, linewidth=2, label='$v_D(t)$ — Tensión en el diodo')
ax3.axhline(0,         color='black',  linewidth=0.7, linestyle=':')
ax3.axhline(-Vs_peak,  color=c_vd, linewidth=0.8, linestyle='--', alpha=0.6)
ax3.annotate(f'PIV = {Vs_peak:.2f} V',
             xy=(t_ms[np.argmin(vD)], -Vs_peak), xytext=(20, -Vs_peak + 3),
             fontsize=9, color=c_vd,
             arrowprops=dict(arrowstyle='->', color=c_vd, lw=1.2))
ax3.set_ylabel('Tensión (V)', fontsize=10)
ax3.set_xlabel('Tiempo (ms)', fontsize=10)
ax3.set_ylim(-Vs_peak * 1.3, Vs_peak * 0.5)
ax3.legend(loc='upper right', fontsize=9)
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.set_title('Tensión inversa en el diodo (PIV)', fontsize=10)
ax3.fill_between(t_ms, vD, 0, where=(vD < 0), alpha=0.12, color=c_vd)

# ── Tabla resumen ────────────────────────────────────────────────────────────
table_data = [
    ['Parámetro', 'Símbolo', 'Valor'],
    ['Voltaje primario (rms)',       '$V_p$',          f'{Vp_rms:.0f} V'],
    ['Relación de vueltas',          '$N_p/N_s$',      f'{int(n)}:1'],
    ['Voltaje secundario (rms)',     '$V_s$',          f'{Vs_rms:.0f} V'],
    ['Voltaje secundario (pico)',    '$V_{{s,m}}$',    f'{Vs_peak:.2f} V'],
    ['Caída de voltaje diodo',       '$V_D$',          f'{VD} V'],
    ['Voltaje de salida (pico)',     '$V_{{o,m}}$',    f'{Vo_peak:.2f} V'],
    ['Voltaje de salida (promedio)', '$V_{{o,avg}}$',  f'{Vo_avg:.2f} V'],
    ['Corriente de carga (pico)',    '$I_{{o,m}}$',    f'{Io_peak:.2f} A'],
    ['Corriente de carga (prom.)',   '$I_{{o,avg}}$',  f'{Io_avg:.2f} A'],
    ['PIV del diodo',                'PIV',            f'{Vs_peak:.2f} V'],
]

ax_tbl = fig.add_axes([0.60, 0.02, 0.38, 0.22])
ax_tbl.axis('off')
tbl = ax_tbl.table(
    cellText=[row[1:] for row in table_data[1:]],
    colLabels=['Símbolo', 'Valor'],
    rowLabels=[row[0] for row in table_data[1:]],
    cellLoc='center',
    loc='center'
)
tbl.auto_set_font_size(False)
tbl.set_fontsize(7.5)
tbl.scale(1, 1.3)

plt.tight_layout(rect=[0, 0.24, 1, 1])
plt.savefig(fname_waves, dpi=120, bbox_inches='tight')
plt.close()
print(f"Generado: {fname_waves}")

# ── FIGURA 3: Voltajes principales — diodo ideal, eje ωt ────────────────────
fname_ideal = os.path.join(OUTPUT_DIR, "nota4_voltajes_ideales.png")

Vm = Vs_peak                             # 16.97 V (diodo ideal: sin caída)
VDC_ideal  = Vm / np.pi                  # 5.40 V
Vrms_ideal = Vm / 2                      # 8.485 V
Vr_ideal   = np.sqrt(Vrms_ideal**2 - VDC_ideal**2)  # ≈ 6.53 V

owt = np.linspace(0, 2 * np.pi, 2000)   # un ciclo completo
vs_i  = Vm * np.sin(owt)
vo_i  = np.where(vs_i >= 0, vs_i, 0.0)  # diodo ideal: conduce cuando vs ≥ 0
vd_i  = vs_i - vo_i                       # 0 en directa; −vs en inversa

pi_ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
pi_labels = ['$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']

fig3, axes3 = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
fig3.suptitle(
    "Rectificador de Media Onda — Diodo Ideal\n"
    r"$V_s = 12\,V_{rms}$,  $V_m = 16.97\,V$,  $R_L = 5\,\Omega$",
    fontsize=13, fontweight='bold'
)

# ── Subplot 1: Vs — senoide completa ────────────────────────────────────────
ax = axes3[0]
ax.plot(owt, vs_i, color='#2196F3', linewidth=2, label=r'$v_s(\omega t)$')
ax.axhline(0,   color='black', linewidth=0.6, linestyle=':')
ax.axhline( Vm, color='#2196F3', linewidth=0.8, linestyle='--', alpha=0.55)
ax.axhline(-Vm, color='#2196F3', linewidth=0.8, linestyle='--', alpha=0.55)
ax.fill_between(owt, vs_i, 0, where=(vs_i > 0), alpha=0.12, color='#2196F3')
ax.fill_between(owt, vs_i, 0, where=(vs_i < 0), alpha=0.10, color='gray')
# Anotaciones +Vm y −Vm
ax.annotate(f'$+V_m = +{Vm:.2f}\\,V$',
            xy=(np.pi/2, Vm), xytext=(np.pi/2 + 0.3, Vm - 2.5),
            fontsize=9, color='#1565C0',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.1))
ax.annotate(f'$-V_m = -{Vm:.2f}\\,V$',
            xy=(3*np.pi/2, -Vm), xytext=(3*np.pi/2 - 1.0, -Vm + 2.5),
            fontsize=9, color='#1565C0',
            arrowprops=dict(arrowstyle='->', color='#1565C0', lw=1.1))
ax.text(0.55, 0.91, f'$V_{{rms}} = {Vs_rms:.0f}\\,V$', transform=ax.transAxes,
        fontsize=9, color='navy',
        bbox=dict(boxstyle='round,pad=0.25', fc='lightyellow', alpha=0.75))
ax.set_ylabel('Tensión (V)', fontsize=10)
ax.set_ylim(-Vm * 1.35, Vm * 1.35)
ax.set_title(r'Señal de entrada $v_s(\omega t)$ — Secundario del transformador', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.55)
ax.tick_params(labelbottom=False)

# ── Subplot 2: Vo — media onda ideal ────────────────────────────────────────
ax = axes3[1]
ax.plot(owt, vo_i, color='#4CAF50', linewidth=2, label=r'$v_o(\omega t)$')
ax.axhline(0,          color='black',      linewidth=0.6, linestyle=':')
ax.axhline(Vm,         color='#4CAF50',    linewidth=0.8, linestyle='--', alpha=0.55)
ax.axhline(VDC_ideal,  color='darkorange', linewidth=1.4, linestyle='--', alpha=0.9,
           label=f'$V_{{DC}} = {VDC_ideal:.2f}\\,V$')
ax.axhline(Vrms_ideal, color='purple',     linewidth=1.0, linestyle=':', alpha=0.8,
           label=f'$V_{{rms}} = {Vrms_ideal:.2f}\\,V$')
ax.fill_between(owt, vo_i, 0, where=(vo_i > 0), alpha=0.15, color='#4CAF50')
# Anotaciones
ax.annotate(f'$V_m = {Vm:.2f}\\,V$',
            xy=(np.pi/2, Vm), xytext=(np.pi/2 + 0.3, Vm - 2.0),
            fontsize=9, color='#2E7D32',
            arrowprops=dict(arrowstyle='->', color='#2E7D32', lw=1.1))
# Flecha y texto del rizo Vr
ax.annotate(
    f'$V_r = {Vr_ideal:.2f}\\,V$',
    xy=(5*np.pi/4, Vrms_ideal), xytext=(5*np.pi/4 + 0.55, Vrms_ideal + 2.2),
    fontsize=9, color='sienna',
    arrowprops=dict(arrowstyle='->', color='sienna', lw=1.1)
)
ax.set_ylabel('Tensión (V)', fontsize=10)
ax.set_ylim(-1.5, Vm * 1.35)
ax.set_title(r'Señal de salida $v_o(\omega t)$ — Voltaje en $R_L$ (diodo ideal)', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.55)
ax.tick_params(labelbottom=False)

# ── Subplot 3: VD — tensión en el diodo ─────────────────────────────────────
ax = axes3[2]
ax.plot(owt, vd_i, color='#F44336', linewidth=2, label=r'$v_D(\omega t)$')
ax.axhline(0,   color='black',   linewidth=0.6, linestyle=':')
ax.axhline(-Vm, color='#F44336', linewidth=0.8, linestyle='--', alpha=0.55)
ax.fill_between(owt, vd_i, 0, where=(vd_i < 0), alpha=0.12, color='#F44336')
ax.fill_between(owt, vd_i, 0, where=(vd_i == 0), alpha=0.08, color='#4CAF50')
# Zona de conducción — cero
ax.text(np.pi/2, 0.6, 'Conducción\n$V_D = 0\\,V$',
        ha='center', va='bottom', fontsize=8.5, color='#2E7D32',
        bbox=dict(boxstyle='round,pad=0.2', fc='#E8F5E9', alpha=0.85))
# Zona de bloqueo — PRV
ax.annotate(
    f'$V_{{PRV}} = -{Vm:.2f}\\,V$',
    xy=(3*np.pi/2, -Vm), xytext=(3*np.pi/2 - 1.1, -Vm + 3.5),
    fontsize=9, color='#B71C1C',
    arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.2)
)
ax.text(3*np.pi/2, -Vm*0.45, 'Bloqueo\n$V_D = -V_s$',
        ha='center', va='center', fontsize=8.5, color='#B71C1C',
        bbox=dict(boxstyle='round,pad=0.2', fc='#FFEBEE', alpha=0.85))
ax.set_ylabel('Tensión (V)', fontsize=10)
ax.set_xlabel(r'$\omega t$ (rad)', fontsize=10)
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-Vm * 1.35, Vm * 0.55)
ax.set_xticks(pi_ticks)
ax.set_xticklabels(pi_labels, fontsize=10)
ax.set_title(r'Tensión en el diodo $v_D(\omega t)$ — Voltaje inverso de pico (PRV)', fontsize=10)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.55)

# Línea divisoria entre semiciclos (referencia visual)
for a in axes3:
    a.axvline(np.pi, color='black', linewidth=0.7, linestyle='--', alpha=0.4)
    a.set_xlim(0, 2*np.pi)
    a.set_xticks(pi_ticks)
    a.set_xticklabels(pi_labels, fontsize=10)

plt.tight_layout()
plt.savefig(fname_ideal, dpi=120, bbox_inches='tight')
plt.close()
print(f"Generado: {fname_ideal}")
