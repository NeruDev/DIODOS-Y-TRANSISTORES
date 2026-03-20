"""
DIO-gen-duplicador-voltaje-horizontal.py
─────────────────────────────────────────
Genera 3 versiones del duplicador de voltaje con layout horizontal (flujo L→R).

::SCRIPT_METADATA::
script_id: DIO-gen-duplicador-voltaje-horizontal
module: DIO
generates:
  - duplicador-voltaje-h1.png
  - duplicador-voltaje-h2.png
  - duplicador-voltaje-h3.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota9.md
last_updated: 2026-03-18

Estándar de diseño horizontal (Layout L→R):
  - Una línea superior para conexiones de nodos (positivos)
  - Una línea inferior para referencia a tierra (negativos)
  - Fuente AC separada del transformador
  - D2 con ánodo en nodo A, cátodo hacia C2
  - Alta resolución (300 DPI) y espacio amplio

Versiones:
  - H1: Compacta (unit=2.5, comp_length=2.5, separation=1.0, fontsize=11)
  - H2: Expandida (unit=3.0, comp_length=3.0, separation=1.5, fontsize=12)
  - H3: Grande - ESTÁNDAR RECOMENDADO (unit=3.5, comp_length=3.5, separation=2.0, fontsize=13)

Especificaciones técnicas H3 (estándar recomendado para circuitos complejos):
  - unit_size: 3.5    → Espaciado amplio entre componentes
  - comp_length: 3.5  → Longitud de componentes para buena proporción
  - separation: 2.0   → Separación generosa entre secciones
  - fontsize: 13      → Etiquetas legibles a cualquier tamaño
  - dpi: 300          → Alta resolución para impresión y pantalla

Reglas de posicionamiento de etiquetas:
  - Las etiquetas de nodo NUNCA deben solaparse con líneas de conexión ni componentes
  - Usar offsets negativos o posiciones absolutas para alejar etiquetas de elementos
  - Etiquetas en línea superior: loc='top' con ofst=0.3
  - Etiquetas en línea inferior: usar coordenadas absolutas desplazadas a la izquierda
  - Etiquetas de voltaje: ubicar en espacio libre, nunca sobre componentes

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-duplicador-voltaje-horizontal.py
"""

import matplotlib
matplotlib.use('Agg')

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


def generar_version(version_num, unit_size, comp_length, separation, fontsize):
    """
    Genera una versión del diagrama con parámetros configurables.

    Topología (flujo L→R):

    Vs ─── [Trafo] ─── C1 ─── A ─── D2(invertido) ─── C ─── C2 ─── D
                              │                                    │
                              D1                                   │
                              │                                    │
    GND ──────────────────── B ─────────────────────────── R_L ───┘

    D2: ánodo en A, cátodo en C (invertido respecto a V1 original)
    """

    filename = f'duplicador-voltaje-h{version_num}.png'

    with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, filename),
                           show=False, dpi=300, unit=unit_size) as d:
        d.config(fontsize=fontsize, font='sans-serif')

        # === FUENTE AC (separada del transformador) ===
        d += (vs := elm.SourceSin().up().length(comp_length)
              .label('$V_s$', loc='left', ofst=0.4)
              .color(COLOR_FUENTE))

        # Línea de separación hacia el transformador
        d += elm.Line().right().length(separation).color(COLOR_CONEXION)

        # === TRANSFORMADOR ===
        # Primario
        d += (L1 := elm.Inductor2(loops=4).down().length(comp_length)
              .label('$N_1$', loc='left', ofst=0.3)
              .color(COLOR_FUENTE))

        # Línea inferior de retorno a la fuente
        d += elm.Line().left().tox(vs.start).color(COLOR_CONEXION)

        # Secundario (separado del primario)
        sec_x = L1.start[0] + 0.8
        d += (L2 := elm.Inductor2(loops=4).at((sec_x, L1.start[1]))
              .down().length(comp_length).flip()
              .label('$N_2$', loc='right', ofst=0.3)
              .color(COLOR_FUENTE))

        # Coordenadas de referencia
        y_top = L2.start[1]
        y_bot = L2.end[1]

        # === LÍNEA SUPERIOR (conexiones positivas) ===
        # Desde secundario superior hacia la derecha
        d += elm.Line().at(L2.start).right().length(separation).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)
        x_after_trafo = d.here[0]

        # C1 hacia la derecha (horizontal)
        d += (c1 := elm.Capacitor().right().length(comp_length * 0.8)
              .label('$C_1$', loc='top', ofst=0.2)
              .color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_A = d.here
        d += elm.Label().at(nodo_A).label('A', loc='top', ofst=0.3, fontsize=fontsize-1, color=COLOR_CONEXION)

        # D2 hacia la derecha (ánodo en A, cátodo a la derecha) - INVERTIDO
        # Usamos .reverse() o dibujamos en dirección contraria
        d += (d2 := elm.Diode().right().length(comp_length * 0.8).reverse()
              .label('$D_2$', loc='top', ofst=0.2)
              .color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_C = d.here
        d += elm.Label().at(nodo_C).label('C', loc='top', ofst=0.3, fontsize=fontsize-1, color=COLOR_CONEXION)

        # C2 hacia la derecha (horizontal)
        d += (c2 := elm.Capacitor().right().length(comp_length * 0.8)
              .label('$C_2$', loc='top', ofst=0.2)
              .color(COLOR_CAPACITOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_D = d.here
        d += elm.Label().at(nodo_D).label('D', loc='top', ofst=0.3, fontsize=fontsize-1, color=COLOR_CONEXION)

        # Continuar línea superior hasta R_L
        d += elm.Line().right().length(separation).color(COLOR_CONEXION)
        d += elm.Dot().color(COLOR_NODO)
        nodo_RL_top = d.here

        # === COMPONENTES VERTICALES ===

        # D1 desde nodo A hacia abajo (ánodo arriba, cátodo abajo)
        d += (d1 := elm.Diode().at(nodo_A).down().toy(y_bot)
              .label('$D_1$', loc='left', ofst=0.3)
              .color(COLOR_DIODO))
        d += elm.Dot().color(COLOR_NODO)
        nodo_B = d.here
        # Etiqueta B a la izquierda del nodo para evitar solapamiento con línea de tierra
        d += elm.Label().at((nodo_B[0] - 0.5, nodo_B[1])).label('B', fontsize=fontsize-1, color=COLOR_CONEXION)

        # R_L desde nodo superior hacia abajo
        d += (rl := elm.Resistor().at(nodo_RL_top).down().toy(y_bot)
              .label('$R_L$', loc='right', ofst=0.3)
              .color(COLOR_RESISTOR))
        d += elm.Dot().color(COLOR_NODO)
        nodo_RL_bot = d.here

        # === LÍNEA INFERIOR (referencia a tierra) ===

        # Conexión desde secundario inferior
        d += elm.Line().at(L2.end).right().tox(nodo_B[0]).color(COLOR_CONEXION)
        d += elm.Dot().at(L2.end).color(COLOR_NODO)

        # Línea inferior continua: B -> RL_bot
        d += elm.Line().at(nodo_B).right().tox(nodo_RL_bot[0]).color(COLOR_CONEXION)

        # Tierra en el centro de la línea inferior
        tierra_x = (nodo_B[0] + nodo_RL_bot[0]) / 2
        d += elm.Ground().at((tierra_x, y_bot)).color(COLOR_CONEXION)

        # === INDICADORES DE VOLTAJE ===

        # Vo a la derecha de R_L
        gap_x = nodo_RL_top[0] + separation * 0.5
        d += elm.Gap().at((gap_x, y_top)).down().toy(y_bot).label(
            ['+', '$V_o = 2V_m$', '−'], fontsize=fontsize, color=COLOR_VOLTAJE)

        # Etiquetas de voltaje en capacitores
        d += elm.Label().at((c1.center[0], c1.center[1] - comp_length * 0.4)).label(
            '$V_{C1}=V_m$', fontsize=fontsize-2, color=COLOR_VOLTAJE)
        d += elm.Label().at((c2.center[0], c2.center[1] - comp_length * 0.4)).label(
            '$V_{C2}=V_m$', fontsize=fontsize-2, color=COLOR_VOLTAJE)

        # Etiqueta de versión (pequeña, en esquina)
        d += elm.Label().at((vs.start[0], y_bot - 0.5)).label(
            f'Versión H{version_num}', fontsize=fontsize-3, color='#9CA3AF')

    print(f"✓ Generada: {filename}")
    return filename


# ============================================================
# GENERAR LAS 3 VERSIONES
# ============================================================
if __name__ == "__main__":
    print("\n=== Generando 3 versiones horizontales del duplicador de voltaje ===\n")

    # Versión H1: Compacta
    generar_version(
        version_num=1,
        unit_size=2.5,
        comp_length=2.5,
        separation=1.0,
        fontsize=11
    )

    # Versión H2: Expandida (más separación)
    generar_version(
        version_num=2,
        unit_size=3.0,
        comp_length=3.0,
        separation=1.5,
        fontsize=12
    )

    # Versión H3: Grande (componentes más grandes)
    generar_version(
        version_num=3,
        unit_size=3.5,
        comp_length=3.5,
        separation=2.0,
        fontsize=13
    )

    print(f"\n✓ Las 3 versiones horizontales se encuentran en: {OUTPUT_DIR}/")
    print("  - duplicador-voltaje-h1.png (compacta)")
    print("  - duplicador-voltaje-h2.png (expandida)")
    print("  - duplicador-voltaje-h3.png (grande)")
