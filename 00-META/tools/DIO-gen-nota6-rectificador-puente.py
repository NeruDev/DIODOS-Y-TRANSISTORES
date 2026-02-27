"""
DIO-gen-nota6-rectificador-puente.py
───────────────────
Genera los esquemáticos del rectificador monolítico tipo H (puente de Graetz)
con transformador de devanado simple, cuatro diodos y carga R_L.

Incluye:
  - Esquemático del circuito completo con schemdraw
  - Anotaciones de pares de conducción (D1+D2, D3+D4)
  - Indicadores de polaridad y voltaje de salida
  - Dos diagramas de flujo de corriente (semiciclo + en azul, semiciclo − en rojo)
  - Formas de onda: v_s, v_o (ideal y real), tensión inversa en D3 (PIV)

Salida:
  - 01-Circuitos-Diodos/media/generated/nota6_circuito.png
  - 01-Circuitos-Diodos/media/generated/nota6_flujo_corriente.png
  - 01-Circuitos-Diodos/media/generated/nota6_formas_onda.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota6-rectificador-puente.py

::SCRIPT_METADATA::
script_id: DIO-gen-nota6-rectificador-puente
module: DIO
generates:
  - nota6_circuito.png
  - nota6_flujo_corriente.png
  - nota6_formas_onda.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota6.md
last_updated: 2026-02-27
"""

import matplotlib
matplotlib.use('Agg')  # Backend sin GUI — evita TclError de tkinter
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
import os

# ── Directorio de salida ────────────────────────────────────────────────────
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 1: Esquemático del rectificador puente tipo H
# ═══════════════════════════════════════════════════════════════════════════
fname_sch = os.path.join(OUTPUT_DIR, "nota6_circuito.png")

with schemdraw.Drawing(show=False, dpi=160) as d:
    d.config(fontsize=11)

    # ── Fuente AC (primario del transformador) ───────────────────────────
    d += (src := elm.SourceSin().up()
          .label('$V_p$', loc='left', ofst=0.55))

    d += elm.Line().right(2.0)

    # ── Primario del transformador (4 loops para altura adecuada) ────────
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

    # ── Relación de vueltas sobre el núcleo ──────────────────────────────
    cx_nucleo = (cx1 + cx2) / 2
    d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label(
        '$n:1$', fontsize=10)

    # ── Coordenadas del secundario ───────────────────────────────────────
    sec_x     = prim.start[0] + 2.2
    sec_top_y = prim.start[1]
    sec_bot_y = prim.end[1]

    # ── Secundario (devanado simple — sin derivación central) ────────────
    d += (sec := elm.Inductor2(loops=4).down().flip()
          .at((sec_x, sec_top_y))
          .to((sec_x, sec_bot_y)))

    # ── N_2: a la derecha del secundario, misma altura que N_1 ────────
    sec_mid_y = (sec_top_y + sec_bot_y) / 2
    d += elm.Label().at((sec_x + 0.65, sec_mid_y)).label(
        '$N_2$', fontsize=10)

    # ── Voltaje V_s con polaridad: sobre las líneas sec→puente ───────
    #    + cerca del terminal superior, − cerca del inferior,
    #    V_s centrado entre ambos
    vs_label_x = (sec_x + sec_x + 2.0) / 2   # mitad del tramo sec→bridge
    d += elm.Label().at((vs_label_x, sec_top_y + 0.30)).label(
        '$+$', fontsize=11, color='#1565C0')
    d += elm.Label().at((vs_label_x, sec_mid_y)).label(
        '$V_s$', fontsize=11)
    d += elm.Label().at((vs_label_x, sec_bot_y - 0.30)).label(
        '$-$', fontsize=11, color='#7B1FA2')

    # ══════════════════════════════════════════════════════════════════════
    # PUENTE DE DIODOS  (configuración tipo H / rombo)
    #
    #   Disposición:
    #                      D1
    #          sec_top ─────►──── nodo_pos (+Vo)
    #                            │
    #              D4 ▲          │           ▲ D2
    #                 │          RL          │
    #              D4 │          │           │ D2
    #                            │
    #          sec_bot ─────►──── nodo_neg (−Vo / GND)
    #                      D3
    #
    #   Semiciclo +: D1 + D2 conducen
    #   Semiciclo −: D3 + D4 conducen
    # ══════════════════════════════════════════════════════════════════════

    # Dimensiones del puente
    bridge_left_x  = sec_x + 2.0     # Nodos izquierdos (desde secundario)
    bridge_right_x = bridge_left_x + 3.0   # Nodos derechos (hacia RL)
    bridge_top_y   = sec_top_y        # Nodo superior
    bridge_bot_y   = sec_bot_y        # Nodo inferior
    bridge_mid_y   = (bridge_top_y + bridge_bot_y) / 2  # Altura central

    # ── Conexiones desde el secundario hasta los nodos del puente ────────
    # Línea horizontal desde extremo superior del secundario al nodo izq-superior
    d += elm.Line().right().at(sec.start).to((bridge_left_x, sec_top_y))
    d += elm.Dot().at((bridge_left_x, sec_top_y))

    # ── Flecha de sentido de corriente (semiciclo +) en línea superior ──
    arrow_x = (sec_x + bridge_left_x) / 2 + 0.3
    d += elm.Label().at((arrow_x, sec_top_y + 0.35)).label(
        '$\\longrightarrow\\; i$', fontsize=9, color='#1565C0')

    # Línea horizontal desde extremo inferior del secundario al nodo izq-inferior
    d += elm.Line().right().at(sec.end).to((bridge_left_x, sec_bot_y))
    d += elm.Dot().at((bridge_left_x, sec_bot_y))

    # ── D1: nodo izq-superior → nodo der-superior (hacia la derecha) ────
    # Primero, línea diagonal/vertical desde (bridge_left_x, top) al punto medio arriba
    # Diseño: nodo_izq_top → diodo → nodo_der (positivo de Vo)
    d += elm.Line().at((bridge_left_x, bridge_top_y)).to(
        ((bridge_left_x + bridge_right_x) / 2, bridge_top_y))
    d += (D1 := elm.Diode().right()
          .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_top_y))
          .to((bridge_right_x, bridge_top_y))
          .label('$D_1$', loc='top'))

    # ── D3: nodo izq-inferior → nodo der-inferior ───────────────────────
    d += elm.Line().at((bridge_left_x, bridge_bot_y)).to(
        ((bridge_left_x + bridge_right_x) / 2, bridge_bot_y))
    d += (D3 := elm.Diode().right()
          .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_bot_y))
          .to((bridge_right_x, bridge_bot_y))
          .label('$D_3$', loc='bot'))

    # ── Nodos derechos (salidas del puente) ──────────────────────────────
    d += elm.Dot().at((bridge_right_x, bridge_top_y))
    d += elm.Dot().at((bridge_right_x, bridge_bot_y))

    # ── D4: nodo izq-superior → nodo izq-inferior (lado izquierdo, vertical)
    # D4 conduce de abajo hacia arriba (semiciclo negativo)
    # Ánodo abajo, cátodo arriba
    d += (D4 := elm.Diode().up()
          .at((bridge_left_x, bridge_bot_y))
          .to((bridge_left_x, bridge_top_y))
          .label('$D_4$', loc='left'))

    # ── D2: nodo der-inferior → nodo der-superior (lado derecho, vertical)
    # D2 conduce de abajo hacia arriba (semiciclo positivo)
    d += (D2 := elm.Diode().up()
          .at((bridge_right_x, bridge_bot_y))
          .to((bridge_right_x, bridge_top_y))
          .label('$D_2$', loc='right'))

    # ── RL: entre nodo der-superior y nodo der-inferior ──────────────────
    # Posicionar RL a la derecha del puente
    rl_x = bridge_right_x + 2.5
    d += elm.Line().right().at((bridge_right_x, bridge_top_y)).to(
        (rl_x, bridge_top_y))
    d += (RL := elm.Resistor().down()
          .at((rl_x, bridge_top_y))
          .to((rl_x, bridge_bot_y))
          .label('$R_L$', loc='left', ofst=0.15))
    d += elm.Line().left().at((rl_x, bridge_bot_y)).to(
        (bridge_right_x, bridge_bot_y))

    # ── Indicadores de polaridad de Vo (a la derecha de RL, sin solape) ─
    d += elm.Label().at((rl_x + 0.55, bridge_top_y - 0.10)).label(
        '$+$', fontsize=11)
    d += elm.Label().at((rl_x + 0.55, (bridge_top_y + bridge_bot_y) / 2)).label(
        '$V_o$', fontsize=11)
    d += elm.Label().at((rl_x + 0.55, bridge_bot_y + 0.10)).label(
        '$-$', fontsize=11)

    # ── Anotaciones de pares de conducción ───────────────────────────────
    annotation_y_top = bridge_top_y + 0.85
    annotation_y_bot = bridge_bot_y - 0.85

    d += elm.Label().at(((bridge_left_x + bridge_right_x) / 2, annotation_y_top)).label(
        'Semiciclo +: $D_1$, $D_2$', fontsize=9, color='#2E7D32')
    d += elm.Label().at(((bridge_left_x + bridge_right_x) / 2, annotation_y_bot)).label(
        'Semiciclo −: $D_3$, $D_4$', fontsize=9, color='#C62828')

    # ── Ground en la línea inferior de retorno (separado de RL) ──────────
    gnd_x = (rl_x + bridge_right_x) / 2
    d += elm.Ground().at((gnd_x, bridge_bot_y))

    d.save(fname_sch)

print(f"Generado: {fname_sch}")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 2: Flujo de corriente por semiciclo (azul = +, rojo = −)
#            Puente en forma de DIAMANTE (rombo) — disposición canónica
#            para visualizar los caminos de corriente.
#
#  Topología del diamante:
#
#              TOP (+Vo)
#             / \
#           D1↑   D2↑         ← cátodos de D1 y D2 se unen en TOP
#           /       \
#       LEFT         RIGHT    ← AC source entre LEFT y RIGHT
#           \       /
#           D4↑   D3↑         ← ánodos de D3 y D4 se unen en BOTTOM
#             \ /
#            BOTTOM (−Vo)
#
#   D1: LEFT → TOP      D2: RIGHT → TOP
#   D3: BOTTOM → RIGHT  D4: BOTTOM → LEFT
#
#   Sem+: LEFT(+), RIGHT(−) → D1 + D3 conducen
#   Sem−: RIGHT(+), LEFT(−) → D2 + D4 conducen
# ═══════════════════════════════════════════════════════════════════════════
fname_flow = os.path.join(OUTPUT_DIR, "nota6_flujo_corriente.png")

import numpy as np

# ── Colores ──────────────────────────────────────────────────────────────
BLUE    = '#1565C0'
RED     = '#C62828'
GRAY    = '#BDBDBD'
DGRAY   = '#757575'
BLACK   = '#212121'


def draw_diode_triangle(ax, start, end, color, lw=2.0, alpha=1.0):
    """Dibuja un símbolo de diodo (triángulo + barra) entre start y end.
       El triángulo apunta de start (ánodo) hacia end (cátodo)."""
    sx, sy = start
    ex, ey = end
    dx, dy = ex - sx, ey - sy
    L = np.hypot(dx, dy)
    ux, uy = dx / L, dy / L       # unitario paralelo
    nx, ny = -uy, ux               # normal perpendicular

    # Posición del triángulo (centrado en el segmento)
    mx, my = (sx + ex) / 2, (sy + ey) / 2
    s = 0.28  # semi-tamaño del triángulo

    # Vértices del triángulo
    base1 = (mx - s * ux + s * nx, my - s * uy + s * ny)
    base2 = (mx - s * ux - s * nx, my - s * uy - s * ny)
    tip   = (mx + s * ux,          my + s * uy)

    tri = plt.Polygon([base1, base2, tip], closed=True,
                       fc=color, ec=color, alpha=alpha, zorder=4)
    ax.add_patch(tri)

    # Barra en el cátodo (perpendicular al eje)
    bar_x = mx + s * ux
    bar_y = my + s * uy
    bw = s * 0.75
    ax.plot([bar_x + bw * nx, bar_x - bw * nx],
            [bar_y + bw * ny, bar_y - bw * ny],
            color=color, lw=lw + 1.5, alpha=alpha, solid_capstyle='round',
            zorder=4)

    # Líneas de conexión (ánodo → triángulo, barra → cátodo)
    ax.plot([sx, mx - s * ux], [sy, my - s * uy],
            color=color, lw=lw, alpha=alpha, zorder=3)
    ax.plot([mx + s * ux, ex], [my + s * uy, ey],
            color=color, lw=lw, alpha=alpha, zorder=3)


def draw_resistor(ax, start, end, color='black', lw=2.0, n=5):
    """Dibuja una resistencia en zigzag entre start y end."""
    sx, sy = start
    ex, ey = end
    dx, dy = ex - sx, ey - sy
    L = np.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux

    lead = 0.22 * L
    ax.plot([sx, sx + lead * ux], [sy, sy + lead * uy],
            color=color, lw=lw, zorder=3)
    ax.plot([ex - lead * ux, ex], [ey - lead * uy, ey],
            color=color, lw=lw, zorder=3)

    # Zigzag
    zx_s, zy_s = sx + lead * ux, sy + lead * uy
    zx_e, zy_e = ex - lead * ux, ey - lead * uy
    amp = 0.18
    pts = [(zx_s, zy_s)]
    for i in range(1, 2 * n + 1):
        t = i / (2 * n)
        px = zx_s + t * (zx_e - zx_s)
        py = zy_s + t * (zy_e - zy_s)
        sign = 1 if (i % 2 == 1) else -1
        px += sign * amp * nx
        py += sign * amp * ny
        pts.append((px, py))
    pts.append((zx_e, zy_e))
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=color, lw=lw, zorder=3)


def draw_source_sin(ax, center, radius=0.4, color='black'):
    """Dibuja un símbolo de fuente senoidal (círculo + onda)."""
    cx, cy = center
    circle = plt.Circle((cx, cy), radius, fc='white', ec=color, lw=2, zorder=5)
    ax.add_patch(circle)
    t = np.linspace(-0.7, 0.7, 50)
    sx = cx + t * radius * 0.85
    sy = cy + np.sin(t * np.pi / 0.7) * radius * 0.3
    ax.plot(sx, sy, color=color, lw=1.5, zorder=6)


def draw_flow_diagram(ax, half_cycle):
    """
    Dibuja el puente rectificador en forma de diamante con la ruta
    de corriente resaltada para el semiciclo indicado.

    half_cycle: 'positive' → azul (D1 + D3)
                'negative' → rojo (D2 + D4)
    """
    active_color = BLUE if half_cycle == 'positive' else RED

    # ── Coordenadas de los 4 nodos del diamante ─────────────────────────
    LEFT   = np.array([1.0, 3.0])
    TOP    = np.array([4.0, 5.8])
    RIGHT  = np.array([7.0, 3.0])
    BOTTOM = np.array([4.0, 0.2])

    mid_y  = 3.0

    # ── Diodos ───────────────────────────────────────────────────────────
    #   D1: LEFT → TOP   (sem+)     D2: RIGHT → TOP   (sem−)
    #   D3: BOTTOM→RIGHT (sem+)     D4: BOTTOM→LEFT    (sem−)
    if half_cycle == 'positive':
        active_set  = {'D1', 'D3'}
    else:
        active_set  = {'D2', 'D4'}

    diodes = {
        'D1': (LEFT,   TOP,    'left'),
        'D2': (RIGHT,  TOP,    'right'),
        'D3': (BOTTOM, RIGHT,  'right'),
        'D4': (BOTTOM, LEFT,   'left'),
    }

    for name, (start, end, label_side) in diodes.items():
        is_on = name in active_set
        col   = active_color if is_on else DGRAY
        lw    = 3.0 if is_on else 1.2
        alpha = 1.0 if is_on else 0.35

        draw_diode_triangle(ax, start, end, col, lw=lw, alpha=alpha)

        # Etiqueta del diodo
        mx = (start[0] + end[0]) / 2
        my = (start[1] + end[1]) / 2
        dx, dy = end[0] - start[0], end[1] - start[1]
        L = np.hypot(dx, dy)
        nx, ny = -dy / L, dx / L  # normal
        ofst = 0.45 if label_side == 'left' else -0.45
        ax.text(mx + ofst * nx, my + ofst * ny,
                f'$D_{name[1]}$', fontsize=13, ha='center', va='center',
                color=col, fontweight='bold', alpha=max(alpha, 0.5))

    # ── RL vertical (TOP → BOTTOM) ──────────────────────────────────────
    draw_resistor(ax, TOP, BOTTOM, color=active_color, lw=2.5)
    rl_mid = (TOP + BOTTOM) / 2
    ax.text(rl_mid[0] + 0.55, rl_mid[1], '$R_L$', fontsize=13,
            ha='left', va='center', color=BLACK)

    # Indicadores +Vo / −Vo
    ax.text(TOP[0] + 0.45, TOP[1] - 0.15, '$+$', fontsize=12,
            ha='left', va='center', color=active_color, fontweight='bold')
    ax.text(TOP[0], TOP[1] + 0.35, '$V_o$', fontsize=12,
            ha='center', va='bottom', color=active_color, fontweight='bold')
    ax.text(BOTTOM[0] + 0.45, BOTTOM[1] + 0.15, '$-$', fontsize=12,
            ha='left', va='center', color=active_color, fontweight='bold')

    # ── Fuente Vi (entre LEFT y RIGHT, por debajo del diamante) ─────────
    src_center = np.array([4.0, mid_y])
    draw_source_sin(ax, src_center, radius=0.42, color=BLACK)
    ax.text(src_center[0], src_center[1] - 0.65, '$V_s$', fontsize=12,
            ha='center', va='top', color=BLACK)

    # Líneas de conexión fuente → nodos laterales
    ax.plot([LEFT[0], src_center[0] - 0.42], [LEFT[1], mid_y],
            color=BLACK, lw=1.8, zorder=2)
    ax.plot([src_center[0] + 0.42, RIGHT[0]], [mid_y, RIGHT[1]],
            color=BLACK, lw=1.8, zorder=2)

    # ── Polaridad de la fuente ───────────────────────────────────────────
    if half_cycle == 'positive':
        ax.text(LEFT[0] - 0.35, LEFT[1] + 0.05, '$(+)$', fontsize=12,
                ha='right', va='center', color=BLUE, fontweight='bold')
        ax.text(RIGHT[0] + 0.35, RIGHT[1] + 0.05, '$(-)$', fontsize=12,
                ha='left', va='center', color=BLUE, fontweight='bold')
    else:
        ax.text(LEFT[0] - 0.35, LEFT[1] + 0.05, '$(-)$', fontsize=12,
                ha='right', va='center', color=RED, fontweight='bold')
        ax.text(RIGHT[0] + 0.35, RIGHT[1] + 0.05, '$(+)$', fontsize=12,
                ha='left', va='center', color=RED, fontweight='bold')

    # ── Nodos (puntos) ───────────────────────────────────────────────────
    for node in [LEFT, TOP, RIGHT, BOTTOM]:
        ax.plot(node[0], node[1], 'o', color=BLACK, markersize=7, zorder=6)

    # ── GND ──────────────────────────────────────────────────────────────
    gnd_y = BOTTOM[1] - 0.25
    ax.plot([BOTTOM[0]], [gnd_y], 'v', color=BLACK, markersize=10, zorder=5)
    ax.plot([BOTTOM[0] - 0.2, BOTTOM[0] + 0.2], [gnd_y - 0.12] * 2,
            color=BLACK, lw=2, zorder=5)
    ax.plot([BOTTOM[0] - 0.12, BOTTOM[0] + 0.12], [gnd_y - 0.22] * 2,
            color=BLACK, lw=1.5, zorder=5)

    # ═════════════════════════════════════════════════════════════════════
    # FLECHAS DE FLUJO DE CORRIENTE (convencional)
    # ═════════════════════════════════════════════════════════════════════
    arrow_kw = dict(
        arrowstyle='->,head_width=0.35,head_length=0.25',
        color=active_color, lw=2.8, zorder=10,
        connectionstyle='arc3,rad=0',
    )
    # Posiciones intermedias para las flechas (sobre las ramas activas)
    if half_cycle == 'positive':
        # Ruta: LEFT(+) → D1 → TOP → RL ↓ → BOTTOM → D3 → RIGHT(−)
        # Flecha 1: sobre D1 (LEFT → TOP)
        f1s = LEFT * 0.65 + TOP * 0.35
        f1e = LEFT * 0.35 + TOP * 0.65
        ax.annotate('', xy=f1e, xytext=f1s, arrowprops=arrow_kw)
        # Flecha "i" label
        f1m = (f1s + f1e) / 2
        ax.text(f1m[0] - 0.6, f1m[1] + 0.1, '$i$', fontsize=13,
                color=active_color, fontstyle='italic', fontweight='bold')

        # Flecha 2: sobre RL (TOP → BOTTOM)
        f2s = TOP * 0.70 + BOTTOM * 0.30
        f2e = TOP * 0.30 + BOTTOM * 0.70
        ax.annotate('', xy=f2e, xytext=f2s, arrowprops=arrow_kw)

        # Flecha 3: sobre D3 (BOTTOM → RIGHT)
        f3s = BOTTOM * 0.65 + RIGHT * 0.35
        f3e = BOTTOM * 0.35 + RIGHT * 0.65
        ax.annotate('', xy=f3e, xytext=f3s, arrowprops=arrow_kw)

        # Flecha 4: retorno por fuente (RIGHT → LEFT, curva por debajo)
        ax.annotate('', xy=(LEFT[0] + 0.4, mid_y - 0.6),
                    xytext=(RIGHT[0] - 0.4, mid_y - 0.6),
                    arrowprops=dict(
                        arrowstyle='->,head_width=0.3,head_length=0.2',
                        color=active_color, lw=2.0, zorder=8,
                        connectionstyle='arc3,rad=-0.25',
                        linestyle='dashed'))
        ax.text(4.0, mid_y - 1.25, 'retorno interno $V_s$',
                fontsize=9, ha='center', va='top', color=active_color,
                fontstyle='italic')

    else:
        # Ruta: RIGHT(+) → D2 → TOP → RL ↓ → BOTTOM → D4 → LEFT(−)
        # Flecha 1: sobre D2 (RIGHT → TOP)
        f1s = RIGHT * 0.65 + TOP * 0.35
        f1e = RIGHT * 0.35 + TOP * 0.65
        ax.annotate('', xy=f1e, xytext=f1s, arrowprops=arrow_kw)
        f1m = (f1s + f1e) / 2
        ax.text(f1m[0] + 0.6, f1m[1] + 0.1, '$i$', fontsize=13,
                color=active_color, fontstyle='italic', fontweight='bold')

        # Flecha 2: sobre RL (TOP → BOTTOM)
        f2s = TOP * 0.70 + BOTTOM * 0.30
        f2e = TOP * 0.30 + BOTTOM * 0.70
        ax.annotate('', xy=f2e, xytext=f2s, arrowprops=arrow_kw)

        # Flecha 3: sobre D4 (BOTTOM → LEFT)
        f3s = BOTTOM * 0.65 + LEFT * 0.35
        f3e = BOTTOM * 0.35 + LEFT * 0.65
        ax.annotate('', xy=f3e, xytext=f3s, arrowprops=arrow_kw)

        # Flecha 4: retorno por fuente (LEFT → RIGHT, curva por debajo)
        ax.annotate('', xy=(RIGHT[0] - 0.4, mid_y - 0.6),
                    xytext=(LEFT[0] + 0.4, mid_y - 0.6),
                    arrowprops=dict(
                        arrowstyle='->,head_width=0.3,head_length=0.2',
                        color=active_color, lw=2.0, zorder=8,
                        connectionstyle='arc3,rad=-0.25',
                        linestyle='dashed'))
        ax.text(4.0, mid_y - 1.25, 'retorno interno $V_s$',
                fontsize=9, ha='center', va='top', color=active_color,
                fontstyle='italic')

    ax.set_xlim(-0.8, 8.8)
    ax.set_ylim(-1.0, 6.8)
    ax.set_aspect('equal')
    ax.axis('off')


# ── Generar la figura combinada ──────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(18, 8))
fig.suptitle("Flujo de corriente en el rectificador tipo puente (Graetz)",
             fontsize=16, fontweight='bold', y=1.02)

# (a) Semiciclo positivo — azul
draw_flow_diagram(axes[0], 'positive')
axes[0].set_title(
    "(a) Semiciclo positivo ($0 < \\omega t < \\pi$)\n"
    "$D_1$ y $D_3$ conducen — $D_2$ y $D_4$ en corte",
    fontsize=12, color=BLUE, pad=12)

# (b) Semiciclo negativo — rojo
draw_flow_diagram(axes[1], 'negative')
axes[1].set_title(
    "(b) Semiciclo negativo ($\\pi < \\omega t < 2\\pi$)\n"
    "$D_2$ y $D_4$ conducen — $D_1$ y $D_3$ en corte",
    fontsize=12, color=RED, pad=12)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(fname_flow, dpi=160, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print(f"Generado: {fname_flow}")


# ═══════════════════════════════════════════════════════════════════════════
# FIGURA 3: Formas de onda del rectificador puente
#   (a) Voltaje de entrada v_s(ωt) = Vm sin(ωt)
#   (b) Voltaje de salida v_o(ωt) = |Vm sin(ωt)| − 2V_D  (diodo real)
#       con indicación de qué par de diodos conduce en cada semiciclo
#   (c) Voltaje en un diodo representativo (D3 o D4) — PIV
# ═══════════════════════════════════════════════════════════════════════════
fname_waves = os.path.join(OUTPUT_DIR, "nota6_formas_onda.png")

# ── Parámetros del circuito ──────────────────────────────────────────────
Vm   = 20.0        # Voltaje pico del secundario [V]
VD   = 0.7         # Caída del diodo de silicio [V]
f    = 60.0        # Frecuencia [Hz]
RL   = 100.0       # Resistencia de carga [Ω]

# Valores derivados
Vo_peak_ideal = Vm
Vo_peak_real  = Vm - 2 * VD
VDC_ideal     = 2 * Vm / np.pi
VDC_real      = 2 * (Vm - 2 * VD) / np.pi
PIV_bridge    = Vm - VD             # PIV en el puente = Vm - VD (aprox Vm)
Im            = Vo_peak_real / RL   # Corriente pico [A]

# Eje temporal: 2 ciclos completos
owt = np.linspace(0, 4 * np.pi, 2000)
sin_wt = np.sin(owt)

# Señales
v_s  = Vm * sin_wt                                       # Entrada
v_o_ideal = Vm * np.abs(sin_wt)                           # Salida ideal
v_o_real  = np.maximum(Vm * np.abs(sin_wt) - 2 * VD, 0)  # Salida real

# Voltaje inverso en D3 (bloqueado en semiciclo +):
# D3 conduce en el semiciclo negativo (mask_neg).
# En semiciclo positivo (mask_pos), D3 está bloqueado.
# KVL en red externa para D3: Vs + vD3 - v_load - vD2 = 0 ? No.
# La tensión inversa pico es aprox Vm.
vD3 = np.where(sin_wt >= 0,
               -(Vm * sin_wt - VD),   # bloqueado: PIV negativo (Vm - VD)
               -VD)                   # conduciendo: caída directa

# Voltaje inverso en D1 (bloqueado en semiciclo -):
# D1 conduce en el semiciclo positivo (mask_pos).
# En semiciclo negativo (mask_neg), D1 está bloqueado.
# La tensión inversa es similar pero en el otro semiciclo.
vD1 = np.where(sin_wt < 0,
               -(Vm * np.abs(sin_wt) - VD), # bloqueado
               -VD)                         # conduciendo

# Marcadores de semiciclo para sombreado
mask_pos = sin_wt >= 0   # D1 y D2 conducen
mask_neg = sin_wt <  0   # D3 y D4 conducen

# ── Etiquetas del eje x ─────────────────────────────────────────────────
pi_ticks  = np.arange(0, 4 * np.pi + 0.1, np.pi / 2)
pi_labels = ['$0$', r'$\frac{\pi}{2}$', r'$\pi$',
             r'$\frac{3\pi}{2}$', r'$2\pi$',
             r'$\frac{5\pi}{2}$', r'$3\pi$',
             r'$\frac{7\pi}{2}$', r'$4\pi$']

# ── Colores ──────────────────────────────────────────────────────────────
C_VS   = '#388E3C'     # verde — entrada
C_D12  = '#1565C0'     # azul  — D1+D2 (sem+)
C_D34  = '#C62828'     # rojo  — D3+D4 (sem−)
C_REAL = '#E65100'     # naranja — diodo real
C_VDC  = '#6A1B9A'     # púrpura — valor DC

# ═════════════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(4, 1, figsize=(14, 16), sharex=True)
fig.suptitle(
    "Formas de Onda — Rectificador Puente (Full-Bridge)\n"
    rf"$V_m = {Vm:.0f}\,V$,  $V_D = {VD}\,V$,  $R_L = {RL:.0f}\,\Omega$,  $f = {f:.0f}\,Hz$",
    fontsize=14, fontweight='bold', y=0.98
)

# ─────────────────────────────────────────────────────────────────────────
# (a) Voltaje de entrada v_s
# ─────────────────────────────────────────────────────────────────────────
ax1 = axes[0]
ax1.plot(owt, v_s, color=C_VS, linewidth=2.2, label=r'$v_s = V_m \sin(\omega t)$')
ax1.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax1.axhline(Vm, color=C_VS, linewidth=0.7, linestyle='--', alpha=0.5)
ax1.axhline(-Vm, color=C_VS, linewidth=0.7, linestyle='--', alpha=0.5)

# Sombreado por semiciclos
ax1.fill_between(owt, v_s, 0, where=mask_pos, alpha=0.10, color=C_D12)
ax1.fill_between(owt, v_s, 0, where=mask_neg, alpha=0.10, color=C_D34)

# Anotaciones de semiciclos
for k in range(2):
    base = 2 * np.pi * k
    ax1.text(base + np.pi / 2, Vm * 0.55, '$D_1, D_2$ ON',
             ha='center', fontsize=9, color=C_D12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#E3F2FD', alpha=0.85))
    ax1.text(base + 3 * np.pi / 2, -Vm * 0.55, '$D_3, D_4$ ON',
             ha='center', fontsize=9, color=C_D34, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.2', fc='#FFEBEE', alpha=0.85))

ax1.set_ylabel(r'$v_s(\omega t)$ [V]', fontsize=11)
ax1.set_title(r'(a) Voltaje de entrada — $v_s = V_m \sin(\omega t)$', fontsize=11)
ax1.set_yticks([-Vm, 0, Vm])
ax1.set_yticklabels([r'$-V_m$', '0', r'$V_m$'])
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle=':', alpha=0.5)

# ─────────────────────────────────────────────────────────────────────────
# (b) Voltaje de salida v_o
# ─────────────────────────────────────────────────────────────────────────
ax2 = axes[1]

# Ideal (semitransparente) + Real (sólida)
ax2.plot(owt, v_o_ideal, color=C_D12, linewidth=1.2, linestyle='--',
         alpha=0.45, label=r'$v_o$ ideal $= V_m |\sin(\omega t)|$')
ax2.plot(owt, v_o_real, color=C_REAL, linewidth=2.2,
         label=r'$v_o$ real $= V_m |\sin(\omega t)| - 2V_D$')

# Sombreado por pares de diodos
ax2.fill_between(owt, v_o_real, 0, where=mask_pos, alpha=0.12, color=C_D12,
                 label=r'$D_1 + D_2$ conducen')
ax2.fill_between(owt, v_o_real, 0, where=mask_neg, alpha=0.12, color=C_D34,
                 label=r'$D_3 + D_4$ conducen')

# Nivel DC
ax2.axhline(VDC_real, color=C_VDC, linewidth=1.5, linestyle='-.',
            label=rf'$V_{{DC}} = {VDC_real:.2f}\,V$')
ax2.axhline(0, color='black', linewidth=0.6, linestyle=':')

# Anotación de pico real
ax2.annotate(
    rf'$V_{{o,m}} = V_m - 2V_D = {Vo_peak_real:.1f}\,V$',
    xy=(np.pi / 2, Vo_peak_real),
    xytext=(np.pi / 2 + 1.5, Vo_peak_real + 3),
    fontsize=9, color=C_REAL, fontweight='bold',
    arrowprops=dict(arrowstyle='->', color=C_REAL, lw=1.2)
)

# Anotación 2VD
ax2.annotate(
    rf'$2V_D = {2*VD:.1f}\,V$',
    xy=(np.pi / 2, Vo_peak_ideal[0] if hasattr(Vo_peak_ideal, '__len__') else Vm),
    xytext=(np.pi / 2 + 2.5, Vm + 2),
    fontsize=9, color='gray',
    arrowprops=dict(arrowstyle='->', color='gray', lw=1.0)
)

ax2.set_ylabel(r'$v_o(\omega t)$ [V]', fontsize=11)
ax2.set_title(r'(b) Voltaje de salida en $R_L$ — Onda completa rectificada', fontsize=11)
ax2.set_yticks([0, VDC_real, Vo_peak_real, Vm])
ax2.set_yticklabels(['0', rf'$V_{{DC}}$', rf'$V_m - 2V_D$', rf'$V_m$'])
ax2.set_ylim(-Vm * 0.1, Vm * 1.25)
ax2.legend(loc='upper right', fontsize=8.5, ncols=2)
ax2.grid(True, linestyle=':', alpha=0.5)

# ─────────────────────────────────────────────────────────────────────────
# (c) Voltaje en diodo D3 (Bloqueado en ciclo positivo) - PIV
# ─────────────────────────────────────────────────────────────────────────
ax3 = axes[2]
ax3.plot(owt, vD3, color='#7B1FA2', linewidth=2.2,
         label=r'$v_{D_3}(\omega t)$')
ax3.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax3.axhline(-(Vm - VD), color='#B71C1C', linewidth=0.8, linestyle='--', alpha=0.5)

ax3.fill_between(owt, vD3, 0, where=(vD3 >= -VD - 0.1), alpha=0.12, color='#4CAF50')
ax3.fill_between(owt, vD3, 0, where=(vD3 < -VD - 0.1), alpha=0.12, color='#7B1FA2')

# Anotaciones
for k in range(2):
    base = 2 * np.pi * k
    ax3.text(base + np.pi / 2, -(Vm - VD) * 0.35,
             r'$D_3$ OFF (Cycle +)',
             ha='center', fontsize=8.5, color='#4A148C',
             bbox=dict(boxstyle='round,pad=0.2', fc='#F3E5F5', alpha=0.85))

ax3.annotate(
    rf'PIV $= V_m - V_D = {Vm - VD:.1f}\,V$',
    xy=(np.pi / 2, -(Vm - VD)),
    xytext=(np.pi / 2 + 1.8, -(Vm - VD) + 6),
    fontsize=9.5, color='#B71C1C', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.3)
)

ax3.set_ylabel(r'$v_{D_3}$ [V]', fontsize=11)
ax3.set_title(r'(c) Tensión inversa en $D_3$ (Bloqueado en ciclo positivo)', fontsize=11)
ax3.set_ylim(-(Vm - VD) * 1.35, (Vm - VD) * 0.25)
ax3.legend(loc='upper right', fontsize=10)
ax3.grid(True, linestyle=':', alpha=0.5)

# ─────────────────────────────────────────────────────────────────────────
# (d) Voltaje en diodo D1 (Bloqueado en ciclo negativo) - PIV
# ─────────────────────────────────────────────────────────────────────────
ax4 = axes[3]
ax4.plot(owt, vD1, color='#0D47A1', linewidth=2.2,
         label=r'$v_{D_1}(\omega t)$')
ax4.axhline(0, color='black', linewidth=0.6, linestyle=':')
ax4.axhline(-(Vm - VD), color='#B71C1C', linewidth=0.8, linestyle='--', alpha=0.5)

ax4.fill_between(owt, vD1, 0, where=(vD1 >= -VD - 0.1), alpha=0.12, color='#4CAF50')
ax4.fill_between(owt, vD1, 0, where=(vD1 < -VD - 0.1), alpha=0.12, color='#0D47A1')

# Anotaciones
for k in range(2):
    base = 2 * np.pi * k
    ax4.text(base + 3*np.pi / 2, -(Vm - VD) * 0.35,
             r'$D_1$ OFF (Cycle -)',
             ha='center', fontsize=8.5, color='#0D47A1',
             bbox=dict(boxstyle='round,pad=0.2', fc='#E3F2FD', alpha=0.85))

ax4.annotate(
    rf'PIV $= V_m - V_D$',
    xy=(3*np.pi / 2, -(Vm - VD)),
    xytext=(3*np.pi / 2 + 1.8, -(Vm - VD) + 6),
    fontsize=9.5, color='#B71C1C', fontweight='bold',
    arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=1.3)
)

ax4.set_ylabel(r'$v_{D_1}$ [V]', fontsize=11)
ax4.set_xlabel(r'$\omega t$ (rad)', fontsize=11)
ax4.set_title(r'(d) Tensión inversa en $D_1$ (Bloqueado en ciclo negativo)', fontsize=11)
ax4.set_ylim(-(Vm - VD) * 1.35, (Vm - VD) * 0.25)
ax4.legend(loc='upper right', fontsize=10)
ax4.grid(True, linestyle=':', alpha=0.5)


# ── Formato de ejes x ───────────────────────────────────────────────────
for ax in axes:
    for xv in np.arange(np.pi, 4 * np.pi + 0.1, np.pi):
        ax.axvline(xv, color='black', linewidth=0.5, linestyle='--', alpha=0.25)
    ax.set_xlim(0, 4 * np.pi)
    ax.set_xticks(pi_ticks)
    ax.set_xticklabels(pi_labels, fontsize=10)

# ── Tabla resumen ────────────────────────────────────────────────────────
table_data = [
    ['Voltaje pico (ideal)',   r'$V_{o,m}$',   f'{Vo_peak_ideal:.1f} V'],
    ['Voltaje pico (real)',    r'$V_{o,m}$',   f'{Vo_peak_real:.1f} V'],
    ['Voltaje DC (ideal)',     r'$V_{DC}$',    f'{VDC_ideal:.2f} V'],
    ['Voltaje DC (real)',      r'$V_{DC}$',    f'{VDC_real:.2f} V'],
    ['PIV por diodo',          'PIV',          f'{PIV_bridge:.1f} V'],
    ['Frecuencia de rizado',   r'$f_r$',       f'{2*f:.0f} Hz'],
    ['Corriente pico',         r'$I_m$',       f'{Im*1000:.1f} mA'],
]

ax_tbl = fig.add_axes([0.58, 0.005, 0.40, 0.08])
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
tbl.scale(1, 1.2)

plt.tight_layout(rect=[0, 0.10, 1, 0.96])
plt.savefig(fname_waves, dpi=140, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print(f"Generado: {fname_waves}")
print("¡Script completado exitosamente!")
