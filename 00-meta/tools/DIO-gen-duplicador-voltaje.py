"""
DIO-gen-duplicador-voltaje.py
───────────────────────────────
Genera el diagrama esquemático de un circuito duplicador de voltaje.

::SCRIPT_METADATA::
script_id: DIO-gen-duplicador-voltaje
module: DIO
generates:
  - duplicador-voltaje.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota9.md
last_updated: 2026-03-18

Salida:
  - 01-Circuitos-Diodos/media/generated/duplicador-voltaje.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-duplicador-voltaje.py

Directivas aplicadas:
  - Tamaño ampliado (unit=3.0) para circuitos complejos
  - Colores diferenciados para dispositivos (fines didácticos):
    * Azul: fuente AC y transformador
    * Rojo: diodos
    * Verde: capacitores
    * Naranja: resistencia de carga
    * Gris oscuro: conexiones y tierra
  - DPI alto (300) para mejor legibilidad
  - Espaciado cuidadoso entre componentes
  - Transformador compacto (separación 1.0 unidades)
"""

import matplotlib
matplotlib.use('Agg')  # backend sin GUI — evita TclError de tkinter

import schemdraw
import schemdraw.elements as elm
import os

# Directorio de salida (relativo a la raíz del repo)
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === PALETA DE COLORES DIDÁCTICOS ===
COLOR_FUENTE = '#2563EB'       # Azul - fuente AC y transformador
COLOR_DIODO = '#DC2626'        # Rojo - diodos
COLOR_CAPACITOR = '#16A34A'    # Verde - capacitores
COLOR_RESISTOR = '#EA580C'     # Naranja - resistencia
COLOR_CONEXION = '#374151'     # Gris oscuro - líneas y nodos
COLOR_VOLTAJE = '#7C3AED'      # Violeta - indicadores de voltaje
COLOR_NODO = '#111827'         # Negro - puntos de nodo

# Crear el esquemático del duplicador de voltaje con transformador
with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'duplicador-voltaje.png'),
                       show=False, dpi=300, unit=3.0) as d:
    d.config(fontsize=12, font='sans-serif')

    # ===============================
    # TRANSFORMADOR (lado izquierdo)
    # ===============================

    # Fuente de AC
    d += (vin := elm.SourceSin().up().length(4.0)
          .label('$V_p$', loc='left', ofst=0.4)
          .color(COLOR_FUENTE))

    # Línea superior hacia primario
    d += elm.Line().right().length(0.6).color(COLOR_CONEXION)

    # Primario del transformador
    d += (prim := elm.Inductor2(loops=4).down().length(4.0).color(COLOR_FUENTE))

    # Línea inferior de retorno
    d += elm.Line().left().tox(vin.start).color(COLOR_CONEXION)

    # Secundario del transformador (separación compacta de 1.0)
    sec_x = prim.start[0] + 1.0
    d += (sec := elm.Inductor2(loops=4).down().length(4.0).flip()
          .at((sec_x, prim.start[1])).color(COLOR_FUENTE))

    # Etiqueta de relación de vueltas
    cx = (prim.start[0] + sec_x) / 2
    d += elm.Label().at((cx, prim.start[1] + 0.6)).label('$N_1$:$N_2$', fontsize=10)

    # Etiqueta Vs del secundario
    d += elm.Label().at((sec_x + 0.8, (sec.start[1] + sec.end[1])/2)).label(
        '$V_s$', fontsize=11, color=COLOR_VOLTAJE)

    # ===============================
    # CIRCUITO DUPLICADOR
    # Topología: Sec_sup -> C1 -> nodo_A -> D1 -> nodo_B -> Sec_inf
    #                              |-> D2 -> nodo_C -> C2 -> nodo_B
    #                              |-> R_L -> nodo_B
    # ===============================

    # Coordenadas base
    y_top = sec.start[1]      # Nivel superior (secundario superior)
    y_mid = y_top - 2.0       # Nivel medio (nodo A)
    y_bot = sec.end[1]        # Nivel inferior (nodo B, tierra)

    x_sec = sec.start[0]      # X del secundario
    x_c1 = x_sec + 2.5        # X de C1 y nodo A
    x_d2_top = x_c1 + 2.5     # X del nodo C (arriba de D2)
    x_c2 = x_d2_top + 2.0     # X de C2
    x_rl = x_c1 + 4.5         # X de R_L

    # --- Conexión superior: Sec_sup -> C1 ---
    d += elm.Line().at(sec.start).right().length(2.5).color(COLOR_CONEXION)
    nodo_sec_sup = (x_c1, y_top)
    d += elm.Dot().at(nodo_sec_sup).color(COLOR_NODO)

    # C1: vertical desde nivel superior hasta nodo A
    d += (c1 := elm.Capacitor().at(nodo_sec_sup).down().length(2.0)
          .label('$C_1$', loc='left', ofst=0.3)
          .color(COLOR_CAPACITOR))

    # Nodo A (central): C1, D1(+), D2(-), R_L
    nodo_A = (x_c1, y_mid)
    d += elm.Dot().at(nodo_A).color(COLOR_NODO)
    d += elm.Label().at((nodo_A[0] - 0.4, nodo_A[1])).label('A', fontsize=10, color=COLOR_CONEXION)

    # D1: desde nodo A hacia abajo (ánodo arriba, cátodo abajo)
    d += (d1 := elm.Diode().at(nodo_A).down().length(2.0)
          .label('$D_1$', loc='left', ofst=0.3)
          .color(COLOR_DIODO))

    # Nodo B (inferior): D1(-), C2, R_L, Sec_inf, GND
    nodo_B = (x_c1, y_bot)
    d += elm.Dot().at(nodo_B).color(COLOR_NODO)
    d += elm.Label().at((nodo_B[0] - 0.4, nodo_B[1])).label('B', fontsize=10, color=COLOR_CONEXION)

    # --- Rama D2 -> C2 ---
    # D2: desde nodo A hacia la derecha-arriba (cátodo en A, ánodo hacia arriba-derecha)
    # Primero línea horizontal desde A hacia la derecha
    d += elm.Line().at(nodo_A).right().length(2.5).color(COLOR_CONEXION)
    nodo_pre_d2 = (x_d2_top, y_mid)
    d += elm.Dot().at(nodo_pre_d2).color(COLOR_NODO)

    # D2: vertical hacia arriba (cátodo abajo en nodo_pre_d2, ánodo arriba)
    d += (d2 := elm.Diode().at(nodo_pre_d2).up().length(2.0)
          .label('$D_2$', loc='left', ofst=0.3)
          .color(COLOR_DIODO))

    # Nodo C (arriba de D2)
    nodo_C = (x_d2_top, y_top)
    d += elm.Dot().at(nodo_C).color(COLOR_NODO)
    d += elm.Label().at((nodo_C[0] + 0.4, nodo_C[1] + 0.3)).label('C', fontsize=10, color=COLOR_CONEXION)

    # Línea horizontal desde nodo C hacia C2
    d += elm.Line().at(nodo_C).right().length(2.0).color(COLOR_CONEXION)
    nodo_pre_c2 = (x_c2, y_top)
    d += elm.Dot().at(nodo_pre_c2).color(COLOR_NODO)

    # C2: vertical hacia abajo
    d += (c2 := elm.Capacitor().at(nodo_pre_c2).down().toy(y_bot)
          .label('$C_2$', loc='right', ofst=0.3)
          .color(COLOR_CAPACITOR))

    # Nodo D (debajo de C2)
    nodo_D = (x_c2, y_bot)
    d += elm.Dot().at(nodo_D).color(COLOR_NODO)
    d += elm.Label().at((nodo_D[0] + 0.4, nodo_D[1] - 0.3)).label('D', fontsize=10, color=COLOR_CONEXION)

    # --- Resistencia de carga R_L ---
    # Línea desde nodo A hacia la derecha para R_L
    d += elm.Line().at(nodo_A).right().length(4.5).color(COLOR_CONEXION)
    nodo_pre_rl = (x_rl, y_mid)
    d += elm.Dot().at(nodo_pre_rl).color(COLOR_NODO)

    # R_L: vertical hacia abajo
    d += (rl := elm.Resistor().at(nodo_pre_rl).down().toy(y_bot)
          .label('$R_L$', loc='right', ofst=0.3)
          .color(COLOR_RESISTOR))

    # Nodo E (debajo de R_L)
    nodo_E = (x_rl, y_bot)
    d += elm.Dot().at(nodo_E).color(COLOR_NODO)

    # --- Conexiones inferiores ---
    # Línea horizontal inferior: nodo B -> nodo D -> nodo E
    d += elm.Line().at(nodo_B).right().tox(nodo_D[0]).color(COLOR_CONEXION)
    d += elm.Line().at(nodo_D).right().tox(nodo_E[0]).color(COLOR_CONEXION)

    # Conexión desde nodo B hacia el secundario inferior
    d += elm.Line().at(nodo_B).left().tox(sec.end[0]).color(COLOR_CONEXION)
    d += elm.Dot().at(sec.end).color(COLOR_NODO)

    # Tierra en nodo B
    d += elm.Ground().at(nodo_B).color(COLOR_CONEXION)

    # ===============================
    # INDICADORES DE VOLTAJE
    # ===============================

    # Voltaje de salida Vo (a la derecha de C2)
    gap_x = x_c2 + 1.2
    d += elm.Gap().at((gap_x, y_top)).down().toy(y_bot).label(
        ['+', '$V_o = 2V_m$', '−'], fontsize=11, color=COLOR_VOLTAJE)

    # Etiqueta de voltaje en C1
    d += elm.Label().at((x_c1 + 1.0, (y_top + y_mid)/2)).label(
        '$V_{C1} = V_m$', fontsize=10, color=COLOR_VOLTAJE)

    # Etiqueta de voltaje en C2
    d += elm.Label().at((x_c2 + 1.8, (y_top + y_bot)/2)).label(
        '$V_{C2} = V_m$', fontsize=10, color=COLOR_VOLTAJE)

print(f"✓ Generada: {os.path.join(OUTPUT_DIR, 'duplicador-voltaje.png')}")
