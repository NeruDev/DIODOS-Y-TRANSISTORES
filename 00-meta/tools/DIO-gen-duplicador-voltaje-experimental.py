"""
DIO-gen-duplicador-voltaje-experimental.py
───────────────────────────────────────────
Genera 3 versiones experimentales del circuito duplicador de voltaje
usando diferentes enfoques de diseño.

Versiones:
  - V1: schemdraw con layout horizontal (flujo izquierda-derecha)
  - V2: matplotlib puro con formas geométricas
  - V3: schemdraw con elemento Transformer y estructura en escalera

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-duplicador-voltaje-experimental.py
"""

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc
import numpy as np
import schemdraw
import schemdraw.elements as elm
import os

# Directorio de salida
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === PALETA DE COLORES DIDÁCTICOS ===
COLOR_FUENTE = '#2563EB'       # Azul
COLOR_DIODO = '#DC2626'        # Rojo
COLOR_CAPACITOR = '#16A34A'    # Verde
COLOR_RESISTOR = '#EA580C'     # Naranja
COLOR_CONEXION = '#374151'     # Gris oscuro
COLOR_VOLTAJE = '#7C3AED'      # Violeta
COLOR_NODO = '#111827'         # Negro
COLOR_FONDO = '#FFFFFF'        # Blanco

# ============================================================
# VERSIÓN 1: schemdraw con layout HORIZONTAL (flujo L-R)
# ============================================================
def generar_v1():
    """Layout horizontal: transformador a la izquierda, circuito fluye hacia la derecha"""
    with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'duplicador-voltaje-v1.png'),
                           show=False, dpi=300) as d:
        d.config(fontsize=11, font='sans-serif', unit=2.5)

        # Inicio en origen
        # Fuente AC
        d += (vs := elm.SourceSin().up().label('$V_s$', loc='left').color(COLOR_FUENTE))

        # Primario del transformador
        d += elm.Line().right().length(0.5).color(COLOR_CONEXION)
        d += (L1 := elm.Inductor2(loops=3).down().label('$N_1$', loc='left').color(COLOR_FUENTE))
        d += elm.Line().left().tox(vs.start).color(COLOR_CONEXION)

        # Secundario (usando Transformer element si disponible, sino manual)
        # Posicionar secundario a la derecha del primario
        d += elm.Line().at(L1.start).right().length(0.8).color(COLOR_CONEXION)
        sec_start = d.here
        d += (L2 := elm.Inductor2(loops=3).down().color(COLOR_FUENTE))
        d += elm.Line().at(L2.start).right().length(0.3).color(COLOR_CONEXION)

        # Etiqueta N2
        d += elm.Label().at(L2.center).label('$N_2$', loc='right', ofst=0.3)

        # C1 horizontal desde secundario superior
        d += elm.Line().at(L2.start).right().length(1.5).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)
        d += (c1 := elm.Capacitor().right().label('$C_1$', loc='top').color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_A = d.here
        d += elm.Label().at(nodo_A).label('A', loc='top', ofst=0.2, fontsize=9)

        # D1 hacia abajo desde nodo A
        d += (d1 := elm.Diode().down().label('$D_1$', loc='right').color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_B = d.here
        d += elm.Label().at(nodo_B).label('B', loc='bot', ofst=0.2, fontsize=9)

        # D2 hacia arriba desde nodo A (en realidad hacia la derecha y arriba)
        d += elm.Line().at(nodo_A).right().length(1.0).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)
        d += (d2 := elm.Diode().up().label('$D_2$', loc='right').color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_C = d.here
        d += elm.Label().at(nodo_C).label('C', loc='top', ofst=0.2, fontsize=9)

        # C2 horizontal desde nodo C
        d += elm.Line().right().length(0.5).color(COLOR_CONEXION)
        d += (c2 := elm.Capacitor().down().toy(nodo_B).label('$C_2$', loc='right').color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_D = d.here

        # R_L en paralelo con C2
        d += elm.Line().at(nodo_C).right().length(1.5).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)
        d += (rl := elm.Resistor().down().toy(nodo_B).label('$R_L$', loc='right').color(COLOR_RESISTOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_E = d.here

        # Conexiones inferiores
        d += elm.Line().at(nodo_B).right().tox(nodo_D).color(COLOR_CONEXION)
        d += elm.Line().at(nodo_D).right().tox(nodo_E).color(COLOR_CONEXION)

        # Conexión inferior al secundario
        d += elm.Line().at(nodo_B).left().tox(L2.end).color(COLOR_CONEXION)
        d += elm.Dot().at(L2.end).color(COLOR_NODO)

        # Tierra
        d += elm.Ground().at(nodo_B).color(COLOR_CONEXION)

        # Indicador Vo
        d += elm.Gap().at(nodo_E).up().toy(nodo_C).label(['+', '$V_o=2V_m$', '−'],
                                                          fontsize=10, color=COLOR_VOLTAJE)

    print("✓ V1 generada: duplicador-voltaje-v1.png")


# ============================================================
# VERSIÓN 2: matplotlib PURO con formas geométricas
# ============================================================
def generar_v2():
    """Dibujo manual con matplotlib - máximo control sobre posicionamiento"""

    fig, ax = plt.subplots(1, 1, figsize=(14, 8), dpi=300)
    ax.set_xlim(-1, 15)
    ax.set_ylim(-1, 9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor(COLOR_FONDO)
    fig.patch.set_facecolor(COLOR_FONDO)

    lw = 2.0  # line width

    # Función helper para dibujar línea
    def linea(x1, y1, x2, y2, color=COLOR_CONEXION):
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, solid_capstyle='round')

    # Función helper para dibujar nodo
    def nodo(x, y, label=None, label_pos='top'):
        ax.plot(x, y, 'o', color=COLOR_NODO, markersize=6, zorder=10)
        if label:
            offset = {'top': (0, 0.3), 'bot': (0, -0.4), 'left': (-0.3, 0), 'right': (0.3, 0)}
            ox, oy = offset.get(label_pos, (0, 0.3))
            ax.text(x + ox, y + oy, label, fontsize=10, ha='center', va='center', color=COLOR_CONEXION)

    # Función para dibujar fuente AC (círculo con onda)
    def fuente_ac(x, y, size=0.6):
        circle = Circle((x, y), size, fill=False, color=COLOR_FUENTE, linewidth=lw)
        ax.add_patch(circle)
        # Onda senoidal dentro
        t = np.linspace(0, 2*np.pi, 30)
        wave_x = x + 0.35 * np.sin(t) * 0.8
        wave_y = y + t/(2*np.pi) * size * 1.2 - size * 0.6
        ax.plot(wave_x, wave_y, color=COLOR_FUENTE, linewidth=1.5)
        ax.text(x - size - 0.4, y, '$V_s$', fontsize=11, color=COLOR_FUENTE, ha='right', va='center')

    # Función para dibujar bobina (inductor)
    def bobina(x1, y1, x2, y2, loops=4, label=None):
        # Dibujar arcos para simular bobina
        length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        angle = np.arctan2(y2-y1, x2-x1)

        for i in range(loops):
            t = i / loops
            cx = x1 + (x2-x1) * (t + 0.5/loops)
            cy = y1 + (y2-y1) * (t + 0.5/loops)
            # Semicírculo
            arc = Arc((cx, cy), 0.4, 0.25, angle=90, theta1=0, theta2=180,
                      color=COLOR_FUENTE, linewidth=lw)
            ax.add_patch(arc)

        if label:
            mx, my = (x1+x2)/2, (y1+y2)/2
            ax.text(mx - 0.5, my, label, fontsize=10, color=COLOR_FUENTE, ha='right', va='center')

    # Función para dibujar capacitor
    def capacitor(x1, y1, x2, y2, label=None, label_side='right'):
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = x2-x1, y2-y1
        length = np.sqrt(dx**2 + dy**2)
        ux, uy = dx/length, dy/length  # vector unitario
        px, py = -uy, ux  # perpendicular

        # Líneas hacia el capacitor
        gap = 0.15
        linea(x1, y1, mx - ux*gap, my - uy*gap, COLOR_CAPACITOR)
        linea(mx + ux*gap, my + uy*gap, x2, y2, COLOR_CAPACITOR)

        # Placas del capacitor
        plate_len = 0.4
        ax.plot([mx - ux*gap - py*plate_len, mx - ux*gap + py*plate_len],
                [my - uy*gap - px*plate_len, my - uy*gap + px*plate_len],
                color=COLOR_CAPACITOR, linewidth=lw+1)
        ax.plot([mx + ux*gap - py*plate_len, mx + ux*gap + py*plate_len],
                [my + uy*gap - px*plate_len, my + uy*gap + px*plate_len],
                color=COLOR_CAPACITOR, linewidth=lw+1)

        if label:
            offset = 0.5 if label_side == 'right' else -0.5
            ax.text(mx + py*offset, my + px*offset, label, fontsize=11,
                   color=COLOR_CAPACITOR, ha='center', va='center')

    # Función para dibujar diodo
    def diodo(x1, y1, x2, y2, label=None, label_side='right'):
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = x2-x1, y2-y1
        length = np.sqrt(dx**2 + dy**2)
        ux, uy = dx/length, dy/length
        px, py = -uy, ux

        # Líneas
        linea(x1, y1, mx - ux*0.2, my - uy*0.2, COLOR_DIODO)
        linea(mx + ux*0.2, my + uy*0.2, x2, y2, COLOR_DIODO)

        # Triángulo (ánodo)
        tri_size = 0.25
        tri = plt.Polygon([
            [mx - ux*0.2, my - uy*0.2],
            [mx + ux*0.1 + py*tri_size, my + uy*0.1 + px*tri_size],
            [mx + ux*0.1 - py*tri_size, my + uy*0.1 - px*tri_size]
        ], closed=True, fill=True, facecolor=COLOR_DIODO, edgecolor=COLOR_DIODO)
        ax.add_patch(tri)

        # Barra (cátodo)
        ax.plot([mx + ux*0.15 - py*tri_size, mx + ux*0.15 + py*tri_size],
                [my + uy*0.15 - px*tri_size, my + uy*0.15 + px*tri_size],
                color=COLOR_DIODO, linewidth=lw+1)

        if label:
            offset = 0.5 if label_side == 'right' else -0.5
            ax.text(mx + py*offset, my + px*offset, label, fontsize=11,
                   color=COLOR_DIODO, ha='center', va='center')

    # Función para dibujar resistor
    def resistor(x1, y1, x2, y2, label=None, label_side='right'):
        mx, my = (x1+x2)/2, (y1+y2)/2
        dx, dy = x2-x1, y2-y1
        length = np.sqrt(dx**2 + dy**2)
        ux, uy = dx/length, dy/length
        px, py = -uy, ux

        # Líneas de entrada/salida
        linea(x1, y1, mx - ux*0.4, my - uy*0.4, COLOR_RESISTOR)
        linea(mx + ux*0.4, my + uy*0.4, x2, y2, COLOR_RESISTOR)

        # Zigzag
        n_zigs = 5
        zig_amp = 0.15
        points_x = []
        points_y = []
        for i in range(n_zigs * 2 + 1):
            t = (i / (n_zigs * 2)) - 0.5
            zx = mx + ux * t * 0.8
            zy = my + uy * t * 0.8
            if i % 2 == 1:
                zx += py * zig_amp * (1 if (i//2) % 2 == 0 else -1)
                zy += px * zig_amp * (1 if (i//2) % 2 == 0 else -1)
            points_x.append(zx)
            points_y.append(zy)
        ax.plot(points_x, points_y, color=COLOR_RESISTOR, linewidth=lw)

        if label:
            offset = 0.5 if label_side == 'right' else -0.5
            ax.text(mx + py*offset, my + px*offset, label, fontsize=11,
                   color=COLOR_RESISTOR, ha='center', va='center')

    # Función para tierra
    def tierra(x, y):
        linea(x, y, x, y-0.3, COLOR_CONEXION)
        for i, w in enumerate([0.4, 0.25, 0.1]):
            ax.plot([x-w, x+w], [y-0.3-i*0.1, y-0.3-i*0.1], color=COLOR_CONEXION, linewidth=lw)

    # === DIBUJAR CIRCUITO ===

    # Coordenadas principales
    y_top, y_mid, y_bot = 7, 4.5, 2
    x_vs = 1
    x_trafo = 3
    x_c1 = 5.5
    x_nodoA = 7.5
    x_d2 = 9
    x_c2 = 11
    x_rl = 13

    # Fuente AC
    fuente_ac(x_vs, (y_top + y_bot)/2)

    # Conexiones fuente -> transformador
    linea(x_vs, y_top - 0.5, x_vs, y_top)
    linea(x_vs, y_top, x_trafo - 0.5, y_top)
    linea(x_vs, y_bot + 0.5, x_vs, y_bot)
    linea(x_vs, y_bot, x_trafo - 0.5, y_bot)

    # Transformador (dos bobinas verticales)
    # Primario
    ax.text(x_trafo - 0.3, (y_top + y_bot)/2, '$N_1$', fontsize=10, color=COLOR_FUENTE, ha='right')
    for i in range(4):
        y_arc = y_bot + 0.5 + i * 1.0
        arc = Arc((x_trafo - 0.3, y_arc), 0.5, 0.8, angle=0, theta1=-90, theta2=90,
                  color=COLOR_FUENTE, linewidth=lw)
        ax.add_patch(arc)

    # Secundario
    ax.text(x_trafo + 0.8, (y_top + y_bot)/2, '$N_2$', fontsize=10, color=COLOR_FUENTE, ha='left')
    for i in range(4):
        y_arc = y_bot + 0.5 + i * 1.0
        arc = Arc((x_trafo + 0.3, y_arc), 0.5, 0.8, angle=0, theta1=90, theta2=270,
                  color=COLOR_FUENTE, linewidth=lw)
        ax.add_patch(arc)

    # Línea núcleo
    linea(x_trafo, y_bot + 0.2, x_trafo, y_top - 0.2, '#94A3B8')

    # Conexiones secundario -> circuito
    linea(x_trafo + 0.5, y_top, x_c1, y_top)
    nodo(x_c1, y_top)

    # C1 (vertical)
    capacitor(x_c1, y_top, x_c1, y_mid, '$C_1$', 'left')
    nodo(x_c1, y_mid, 'A', 'left')

    # Línea nodo A hacia D1 y hacia derecha
    linea(x_c1, y_mid, x_nodoA, y_mid)
    nodo(x_nodoA, y_mid)

    # D1 (vertical hacia abajo)
    diodo(x_nodoA, y_mid, x_nodoA, y_bot, '$D_1$', 'left')
    nodo(x_nodoA, y_bot, 'B', 'left')

    # Línea hacia D2
    linea(x_nodoA, y_mid, x_d2, y_mid)
    nodo(x_d2, y_mid)

    # D2 (vertical hacia arriba)
    diodo(x_d2, y_mid, x_d2, y_top, '$D_2$', 'right')
    nodo(x_d2, y_top, 'C', 'top')

    # Línea C -> C2
    linea(x_d2, y_top, x_c2, y_top)
    nodo(x_c2, y_top)

    # C2 (vertical)
    capacitor(x_c2, y_top, x_c2, y_bot, '$C_2$', 'right')
    nodo(x_c2, y_bot, 'D', 'bot')

    # Línea hacia RL
    linea(x_d2, y_top, x_rl, y_top)
    nodo(x_rl, y_top)

    # RL (vertical)
    resistor(x_rl, y_top, x_rl, y_bot, '$R_L$', 'right')
    nodo(x_rl, y_bot)

    # Conexiones inferiores
    linea(x_nodoA, y_bot, x_c2, y_bot)
    linea(x_c2, y_bot, x_rl, y_bot)

    # Conexión inferior al secundario
    linea(x_trafo + 0.5, y_bot, x_nodoA, y_bot)
    nodo(x_trafo + 0.5, y_bot)

    # Tierra
    tierra(x_nodoA, y_bot)

    # Indicador Vo
    ax.annotate('', xy=(x_rl + 0.8, y_top), xytext=(x_rl + 0.8, y_bot),
                arrowprops=dict(arrowstyle='<->', color=COLOR_VOLTAJE, lw=2))
    ax.text(x_rl + 1.3, (y_top + y_bot)/2, '$V_o = 2V_m$', fontsize=12,
            color=COLOR_VOLTAJE, ha='left', va='center', fontweight='bold')
    ax.text(x_rl + 0.8, y_top + 0.2, '+', fontsize=12, color=COLOR_VOLTAJE, ha='center')
    ax.text(x_rl + 0.8, y_bot - 0.2, '−', fontsize=14, color=COLOR_VOLTAJE, ha='center')

    # Etiquetas de voltaje en capacitores
    ax.text(x_c1 - 0.8, (y_top + y_mid)/2, '$V_{C1}=V_m$', fontsize=9,
            color=COLOR_VOLTAJE, ha='right', va='center')
    ax.text(x_c2 + 0.8, (y_top + y_bot)/2, '$V_{C2}=V_m$', fontsize=9,
            color=COLOR_VOLTAJE, ha='left', va='center')

    # Título
    ax.text(7, 8.3, 'Duplicador de Voltaje (V2 - matplotlib)', fontsize=14,
            ha='center', fontweight='bold', color='#1F2937')

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'duplicador-voltaje-v2.png'),
                dpi=300, bbox_inches='tight', facecolor=COLOR_FONDO)
    plt.close()

    print("✓ V2 generada: duplicador-voltaje-v2.png")


# ============================================================
# VERSIÓN 3: schemdraw con estructura en ESCALERA (ladder)
# ============================================================
def generar_v3():
    """Estructura tipo escalera con ramificaciones claras"""
    with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'duplicador-voltaje-v3.png'),
                           show=False, dpi=300) as d:
        d.config(fontsize=12, font='sans-serif', unit=3.5)

        # Usar el elemento Transformer si está disponible
        try:
            # Transformador completo
            d += (xf := elm.Transformer(t1=4, t2=4).color(COLOR_FUENTE))
            d += elm.Label().at(xf.p1).label('$V_p$', loc='left', ofst=0.5, color=COLOR_FUENTE)
            d += elm.Label().at(xf.s1).label('$V_s$', loc='right', ofst=0.5, color=COLOR_VOLTAJE)

            # Desde secundario superior
            d += elm.Line().at(xf.s1).right().length(2).color(COLOR_CONEXION)
            d += elm.Dot().color(COLOR_NODO)
            pos_top_right = d.here

        except:
            # Fallback: dibujamos manual
            d += (vs := elm.SourceSin().up().length(4).label('$V_p$', loc='left').color(COLOR_FUENTE))
            d += elm.Line().right().length(0.5).color(COLOR_CONEXION)
            d += (L1 := elm.Inductor2(loops=4).down().length(4).color(COLOR_FUENTE))
            d += elm.Line().left().tox(vs.start).color(COLOR_CONEXION)

            sec_x = L1.start[0] + 1.2
            d += (L2 := elm.Inductor2(loops=4).at((sec_x, L1.start[1])).down().length(4).flip().color(COLOR_FUENTE))

            d += elm.Label().at(((L1.start[0] + sec_x)/2, L1.start[1] + 0.5)).label('$N_1$:$N_2$', fontsize=10)

            d += elm.Line().at(L2.start).right().length(2).color(COLOR_CONEXION)
            d += elm.Dot().color(COLOR_NODO)
            pos_top_right = d.here
            xf = type('obj', (object,), {'s2': L2.end})()  # mock object

        # === RAMA PRINCIPAL: C1 -> nodo A -> D1 -> nodo B ===

        # C1 hacia abajo
        d += (c1 := elm.Capacitor().down().length(2)
              .label('$C_1$', loc='left', ofst=0.3)
              .color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_A = d.here
        d += elm.Label().at(nodo_A).label('A', loc='left', ofst=0.3, fontsize=10, color=COLOR_CONEXION)

        # D1 hacia abajo
        d += (d1 := elm.Diode().down().length(2)
              .label('$D_1$', loc='left', ofst=0.3)
              .color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_B = d.here
        d += elm.Label().at(nodo_B).label('B', loc='left', ofst=0.3, fontsize=10, color=COLOR_CONEXION)

        # === RAMA D2 -> C2 (desde nodo A hacia arriba-derecha) ===

        # D2: cátodo en nodo A, ánodo hacia la derecha-arriba
        d.push()  # guardar posición
        d += elm.Line().at(nodo_A).right().length(2.5).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)

        d += (d2 := elm.Diode().up().length(2)
              .label('$D_2$', loc='right', ofst=0.3)
              .color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_C = d.here
        d += elm.Label().at(nodo_C).label('C', loc='top', ofst=0.2, fontsize=10, color=COLOR_CONEXION)

        # C2 horizontal hacia la derecha y luego hacia abajo
        d += elm.Line().right().length(1.5).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)

        d += (c2 := elm.Capacitor().down().toy(nodo_B)
              .label('$C_2$', loc='right', ofst=0.3)
              .color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_D = d.here
        d += elm.Label().at(nodo_D).label('D', loc='bot', ofst=0.2, fontsize=10, color=COLOR_CONEXION)

        # === R_L desde nodo C hacia abajo ===

        d += elm.Line().at(nodo_C).right().length(2.5).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)

        d += (rl := elm.Resistor().down().toy(nodo_B)
              .label('$R_L$', loc='right', ofst=0.3)
              .color(COLOR_RESISTOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_E = d.here

        # === CONEXIONES INFERIORES ===

        # Línea inferior conectando todos los nodos
        d += elm.Line().at(nodo_B).right().tox(nodo_D).color(COLOR_CONEXION)
        d += elm.Line().at(nodo_D).right().tox(nodo_E).color(COLOR_CONEXION)

        # Conexión al secundario inferior
        d += elm.Line().at(nodo_B).left().tox(xf.s2).color(COLOR_CONEXION)
        d += elm.Dot().at(xf.s2).color(COLOR_NODO)

        # Tierra
        d += elm.Ground().at(nodo_B).color(COLOR_CONEXION)

        # === INDICADORES DE VOLTAJE ===

        # Vo a la derecha de RL
        gap_x = nodo_E[0] + 0.8
        d += elm.Gap().at((gap_x, nodo_C[1])).down().toy(nodo_B).label(
            ['+', '$V_o = 2V_m$', '−'], fontsize=11, color=COLOR_VOLTAJE)

        # Etiquetas adicionales
        d += elm.Label().at((c1.center[0] + 1.0, c1.center[1])).label(
            '$V_{C1}=V_m$', fontsize=9, color=COLOR_VOLTAJE)
        d += elm.Label().at((c2.center[0] + 1.0, c2.center[1])).label(
            '$V_{C2}=V_m$', fontsize=9, color=COLOR_VOLTAJE)

    print("✓ V3 generada: duplicador-voltaje-v3.png")


# ============================================================
# EJECUTAR LAS 3 VERSIONES
# ============================================================
if __name__ == "__main__":
    print("\n=== Generando 3 versiones experimentales del duplicador de voltaje ===\n")

    generar_v1()
    generar_v2()
    generar_v3()

    print(f"\n✓ Las 3 versiones se encuentran en: {OUTPUT_DIR}/")
    print("  - duplicador-voltaje-v1.png (schemdraw horizontal)")
    print("  - duplicador-voltaje-v2.png (matplotlib puro)")
    print("  - duplicador-voltaje-v3.png (schemdraw escalera)")
