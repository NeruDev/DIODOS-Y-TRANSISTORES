"""
DIO-gen-nota8-recortadores.py
───────────────────
Genera esquemáticos y formas de onda de circuitos recortadores (clippers)
básicos con diodo.

::SCRIPT_METADATA::
script_id: DIO-gen-nota8-recortadores
module: DIO
generates:
  - nota8_recortador_paralelo_pos.png
  - nota8_recortador_formas_onda.png
  - nota8_recortador_polarizado.png
  - nota8_recortador_polarizado_formas_onda.png
  - nota8_recortador_serie.png
  - nota8_recortador_serie_formas_onda.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota8.md
last_updated: 2026-03-11

Salida:
  - topics/01-circuitos-diodos/assets/nota8_recortador_paralelo_pos.png
  - topics/01-circuitos-diodos/assets/nota8_recortador_formas_onda.png
  - topics/01-circuitos-diodos/assets/nota8_recortador_polarizado.png
  - topics/01-circuitos-diodos/assets/nota8_recortador_polarizado_formas_onda.png
  - topics/01-circuitos-diodos/assets/nota8_recortador_serie.png
  - topics/01-circuitos-diodos/assets/nota8_recortador_serie_formas_onda.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota8-recortadores.py
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import schemdraw
import schemdraw.elements as elm
import os

# ── Directorio de salida ──
OUTPUT_DIR = os.path.join("topics", "01-circuitos-diodos", "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# FIGURA 1: Esquemático — Recortador paralelo positivo
# ═══════════════════════════════════════════════════════════════

with schemdraw.Drawing(
    file=os.path.join(OUTPUT_DIR, 'nota8_recortador_paralelo_pos.png'),
    show=False, dpi=150
) as d:
    d.config(fontsize=14)

    # Fuente senoidal a la izquierda
    d += (src := elm.SourceSin().up().label(
        '$v_s = V_m \\sin(\\omega t)$', loc='left', ofst=0.6
    ))
    # Nodo superior
    d += elm.Dot()
    # Resistencia en serie
    d += (R := elm.Resistor().right().label('$R$', loc='top'))
    # Nodo de salida superior
    d += elm.Dot()

    # Diodo hacia GND (paralelo, ánodo arriba → recorta positivo)
    d += (D := elm.Diode().down().label('$D$', loc='right'))
    # Nodo inferior
    d += elm.Dot()
    d += elm.Ground()

    # Línea inferior de retorno
    d += elm.Line().left().to(src.start)
    d += elm.Dot()

    # Etiquetas de entrada/salida
    # v_i entre los terminales de la fuente
    d += elm.Label().at(src.start).label('$-$', loc='left', ofst=0.15)
    d += elm.Label().at(src.end).label('$+$', loc='left', ofst=0.15)

    # v_o entre los terminales del diodo
    x_out = R.end[0] + 0.8
    d += elm.Line().at(R.end).right(0.8)
    d += elm.Dot(open=True).label('$v_o$', loc='right')
    d += elm.Line().at(D.end).right(0.8)
    d += elm.Dot(open=True)

print("Generada: nota8_recortador_paralelo_pos.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 2: Formas de onda — Recortador paralelo positivo
# ═══════════════════════════════════════════════════════════════

Vm = 10.0       # Amplitud de la señal de entrada (V)
Vk = 0.7        # Voltaje de umbral del diodo (V)

wt = np.linspace(0, 4 * np.pi, 2000)
vs = Vm * np.sin(wt)

# Para el recortador paralelo positivo (diodo al derecho):
#   - Cuando vs > Vk: el diodo conduce → vo ≈ Vk
#   - Cuando vs ≤ Vk: el diodo NO conduce → vo ≈ vs
vo = np.where(vs > Vk, Vk, vs)

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle('Recortador Paralelo Positivo — Formas de Onda',
             fontsize=14, fontweight='bold')

# Señal de entrada
ax1 = axes[0]
ax1.plot(wt / np.pi, vs, 'b-', linewidth=1.5, label='$v_s$')
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axhline(y=Vk, color='r', linewidth=0.8, linestyle='--',
            label=f'$V_K = {Vk}\\,V$')
ax1.set_ylabel('$v_s$ (V)', fontsize=12)
ax1.set_ylim(-Vm * 1.2, Vm * 1.2)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_title('Señal de entrada', fontsize=11)

# Señal de salida
ax2 = axes[1]
ax2.plot(wt / np.pi, vo, 'r-', linewidth=1.5, label='$v_o$')
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axhline(y=Vk, color='r', linewidth=0.8, linestyle='--', alpha=0.5)
ax2.fill_between(wt / np.pi, vs, vo, where=(vs > Vk),
                 alpha=0.15, color='red', label='Zona recortada')
ax2.set_ylabel('$v_o$ (V)', fontsize=12)
ax2.set_xlabel('$\\omega t \\;/\\; \\pi$', fontsize=12)
ax2.set_ylim(-Vm * 1.2, Vm * 1.2)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_title('Señal de salida (recortada)', fontsize=11)

# Anotaciones
ax2.annotate(f'Recorte en $V_K = {Vk}\\,V$',
             xy=(0.5, Vk), xytext=(1.0, Vk + 3),
             fontsize=10, color='red',
             arrowprops=dict(arrowstyle='->', color='red', lw=1.2))
ax2.annotate(f'$-V_m = -{Vm}\\,V$',
             xy=(1.5, -Vm), xytext=(2.0, -Vm + 2),
             fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', color='blue', lw=1.2))

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'nota8_recortador_formas_onda.png'),
            dpi=150, bbox_inches='tight')
plt.close()

print("Generada: nota8_recortador_formas_onda.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 3: Esquemático — Recortador paralelo positivo CON POLARIZACIÓN
#
#   Nota sobre SourceV en schemdraw:
#     SourceV(): start = (−), end = (+)
#     SourceV().down(): start(top)=(−), end(bottom)=(+)
#     SourceV().down().reverse(): start(top)=(+), end(bottom)=(−)  ← CORRECTO
#
#   Topología:
#     (+)vs ──R──┬── vo(+)
#                │
#                D (ánodo arriba, cátodo abajo)
#                │
#               (+) V_DC (-)
#                │         │
#       GND ─── (-)vs     GND  ── vo(-)
# ═══════════════════════════════════════════════════════════════

Vdc = 5.0  # Voltaje de polarización DC (V)

with schemdraw.Drawing(
    file=os.path.join(OUTPUT_DIR, 'nota8_recortador_polarizado.png'),
    show=False, dpi=150
) as d:
    d.config(fontsize=14)

    # 1. Fuente AC (start=abajo=(-), end=arriba=(+))
    d += (src := elm.SourceSin().up())
    d += elm.Dot()

    # 2. Resistencia en serie
    d += (R := elm.Resistor().right().label('$R$', loc='top'))
    d += elm.Dot()  # Nodo A

    # 3. Diodo hacia abajo (ánodo=arriba, cátodo=abajo)
    d += (D := elm.Diode().down().label('$D$', loc='right'))

    # 4. Fuente DC: .reverse() → (+) arriba (cátodo), (−) abajo (GND)
    d += (Vbat := elm.SourceV().down().reverse())

    # 5. Tierra en terminal (−) de V_DC
    d += elm.Ground()

    # 6. Tierra en terminal (−) de fuente AC
    d += elm.Ground().at(src.start)

    # 7. Etiqueta vs a la izquierda, lejos de líneas
    d += elm.Label().at((src.center[0] - 2.0, src.center[1])).label(
        '$v_s = V_m \\sin(\\omega t)$'
    )

    # 8. Etiqueta V_DC a la derecha, alejada del símbolo
    d += elm.Label().at((Vbat.center[0] + 1.2, Vbat.center[1])).label(
        '$V_{DC}$'
    )

    # 9. Terminales de salida vo
    d += elm.Line().at(R.end).right(0.8)
    d += elm.Dot(open=True).label('$v_o$', loc='right')
    d += elm.Line().at(Vbat.end).right(0.8)
    d += elm.Dot(open=True)

print("Generada: nota8_recortador_polarizado.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 4: Formas de onda — Recortador polarizado positivo
# ═══════════════════════════════════════════════════════════════

V_clip = Vdc + Vk  # Nivel de recorte = V_DC + V_K

vs_b = Vm * np.sin(wt)
vo_b = np.where(vs_b > V_clip, V_clip, vs_b)

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    f'Recortador Paralelo Positivo con Polarización ($V_{{DC}} = {Vdc}\\,V$) — Formas de Onda',
    fontsize=13, fontweight='bold'
)

# Señal de entrada
ax1 = axes[0]
ax1.plot(wt / np.pi, vs_b, 'b-', linewidth=1.5, label='$v_s$')
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axhline(y=V_clip, color='darkorange', linewidth=0.8, linestyle='--',
            label=f'$V_{{DC}} + V_K = {V_clip}\\,V$')
ax1.set_ylabel('$v_s$ (V)', fontsize=12)
ax1.set_ylim(-Vm * 1.2, Vm * 1.2)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_title('Señal de entrada', fontsize=11)

# Señal de salida
ax2 = axes[1]
ax2.plot(wt / np.pi, vo_b, 'r-', linewidth=1.5, label='$v_o$')
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.axhline(y=V_clip, color='darkorange', linewidth=0.8, linestyle='--',
            alpha=0.6)
ax2.axhline(y=Vdc, color='green', linewidth=0.7, linestyle=':',
            label=f'$V_{{DC}} = {Vdc}\\,V$')
ax2.fill_between(wt / np.pi, vs_b, vo_b, where=(vs_b > V_clip),
                 alpha=0.15, color='darkorange', label='Zona recortada')
ax2.set_ylabel('$v_o$ (V)', fontsize=12)
ax2.set_xlabel('$\\omega t \\;/\\; \\pi$', fontsize=12)
ax2.set_ylim(-Vm * 1.2, Vm * 1.2)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_title('Señal de salida (recortada)', fontsize=11)

# Anotaciones
ax2.annotate(
    f'Recorte en $V_{{DC}} + V_K = {V_clip}\\,V$',
    xy=(0.5, V_clip), xytext=(1.0, V_clip + 2.5),
    fontsize=10, color='darkorange',
    arrowprops=dict(arrowstyle='->', color='darkorange', lw=1.2)
)
ax2.annotate(
    f'$-V_m = -{Vm}\\,V$',
    xy=(1.5, -Vm), xytext=(2.0, -Vm + 2),
    fontsize=10, color='blue',
    arrowprops=dict(arrowstyle='->', color='blue', lw=1.2)
)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'nota8_recortador_polarizado_formas_onda.png'),
            dpi=150, bbox_inches='tight')
plt.close()

print("Generada: nota8_recortador_polarizado_formas_onda.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 5: Esquemático — Recortador serie con polarización
#
#   Topología (lazo):
#     vs(+) ── D(ánodo→cátodo) ── R ── V_DC(+)
#      │                                  │
#     vs(-)  ────────────────────── V_DC(-)
#                    GND
#
#   vo se mide a través de R.
# ═══════════════════════════════════════════════════════════════

with schemdraw.Drawing(
    file=os.path.join(OUTPUT_DIR, 'nota8_recortador_serie.png'),
    show=False, dpi=150
) as d:
    d.config(fontsize=14)

    # 1. Fuente AC a la izquierda (start=abajo=(-), end=arriba=(+))
    d += (src := elm.SourceSin().up())
    d += elm.Dot()

    # 2. Diodo en serie hacia la derecha, invertido:
    #    cátodo=izq (hacia vs), ánodo=der (hacia R)
    d += (D := elm.Diode().right().flip().label('$D$', loc='top'))

    # 3. Nodo superior derecho — aquí se mide vo(+)
    d += elm.Dot()
    vo_top = D.end

    # 4. Resistencia hacia abajo
    d += (R := elm.Resistor().down().label('$R$', loc='right'))

    # 5. Nodo inferior derecho — aquí se mide vo(-)
    d += elm.Dot()
    vo_bot = R.end

    # 6. Fuente DC hacia la izquierda: (+) a la derecha (donde R termina),
    #    (-) a la izquierda (donde src empieza)
    #    SourceV().left(): start(derecha)=(−), end(izquierda)=(+)
    #    Con .reverse(): start(derecha)=(+), end(izquierda)=(−) ← CORRECTO
    d += (Vbat := elm.SourceV().left().reverse().tox(src.start))

    # 7. Línea de cierre hasta terminal (-) de vs
    d += elm.Line().left().to(src.start)
    d += elm.Dot()

    # 8. Tierra en nodo inferior izquierdo
    d += elm.Ground().at(src.start)

    # 9. Etiqueta vs
    d += elm.Label().at((src.center[0] - 2.0, src.center[1])).label(
        '$v_s = V_m \\sin(\\omega t)$'
    )

    # 10. Etiqueta V_DC debajo de la fuente DC
    d += elm.Label().at((Vbat.center[0], Vbat.center[1] - 0.6)).label(
        '$V_{DC}$'
    )

    # 11. Terminales de salida vo (a la derecha de R)
    d += elm.Line().at(vo_top).right(0.8)
    d += elm.Dot(open=True).label('$v_o$', loc='right')
    d += elm.Label().at(vo_top).label('$+$', loc='right', ofst=0.15)

    d += elm.Line().at(vo_bot).right(0.8)
    d += elm.Dot(open=True)
    d += elm.Label().at(vo_bot).label('$-$', loc='right', ofst=0.15)

print("Generada: nota8_recortador_serie.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 6: Formas de onda — Recortador serie con polarización
#
#   D conduce cuando vs > V_DC + V_K
#   vo = vs - V_DC - V_K  (cuando conduce)
#   vo = 0                 (cuando no conduce)
# ═══════════════════════════════════════════════════════════════

V_clip_s = Vdc + Vk  # Umbral de conducción

vs_s = Vm * np.sin(wt)
# Cuando vs > V_DC + V_K: el diodo conduce, vo = vs - V_DC - V_K
# Cuando vs ≤ V_DC + V_K: no conduce, vo = 0
vo_s = np.where(vs_s > V_clip_s, vs_s - V_clip_s, 0)

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
fig.suptitle(
    f'Recortador Serie con Polarización ($V_{{DC}} = {Vdc}\\,V$) — Formas de Onda',
    fontsize=13, fontweight='bold'
)

# Señal de entrada
ax1 = axes[0]
ax1.plot(wt / np.pi, vs_s, 'b-', linewidth=1.5, label='$v_s$')
ax1.axhline(y=0, color='k', linewidth=0.5)
ax1.axhline(y=V_clip_s, color='green', linewidth=0.8, linestyle='--',
            label=f'$V_{{DC}} + V_K = {V_clip_s}\\,V$')
ax1.set_ylabel('$v_s$ (V)', fontsize=12)
ax1.set_ylim(-Vm * 1.2, Vm * 1.2)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_title('Señal de entrada', fontsize=11)

# Señal de salida
ax2 = axes[1]
ax2.plot(wt / np.pi, vo_s, 'r-', linewidth=1.5, label='$v_o$')
ax2.axhline(y=0, color='k', linewidth=0.5)
ax2.fill_between(wt / np.pi, 0, vo_s, where=(vo_s > 0),
                 alpha=0.15, color='green', label='D conduce')
ax2.set_ylabel('$v_o$ (V)', fontsize=12)
ax2.set_xlabel('$\\omega t \\;/\\; \\pi$', fontsize=12)
ax2.set_ylim(-1, (Vm - V_clip_s) * 1.3)
ax2.legend(loc='upper right', fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_title('Señal de salida (a través de $R$)', fontsize=11)

# Anotaciones
vo_max = Vm - V_clip_s
ax2.annotate(
    f'$v_{{o,max}} = V_m - V_{{DC}} - V_K = {vo_max:.1f}\\,V$',
    xy=(0.5, vo_max), xytext=(1.2, vo_max - 0.5),
    fontsize=10, color='red',
    arrowprops=dict(arrowstyle='->', color='red', lw=1.2)
)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'nota8_recortador_serie_formas_onda.png'),
            dpi=150, bbox_inches='tight')
plt.close()

print("Generada: nota8_recortador_serie_formas_onda.png")
print("¡Todas las imágenes de Nota8 generadas exitosamente!")
