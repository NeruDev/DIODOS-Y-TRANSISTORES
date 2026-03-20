"""
DIO-gen-practica1-rectificadores.py
───────────────────
Genera los esquemáticos de los tres circuitos rectificadores de la Práctica 1:
  - Figura 1: Rectificador puente monofásico de onda completa
  - Figura 2: Rectificador tipo-H con filtro inductivo
  - Figura 3: Rectificador tipo-H con filtro capacitivo

Parámetros del circuito (según la práctica):
  - Transformador: 120V primario / 12V secundario (10:1)
  - Diodos: 1N4005 (VD ≈ 0.7V)
  - Carga: R_L = 10Ω / 25W

Salida:
  - 01-Circuitos-Diodos/Notas/PRACTICA 1/media/practica1_figura1_puente.png
  - 01-Circuitos-Diodos/Notas/PRACTICA 1/media/practica1_figura2_filtro_L.png
  - 01-Circuitos-Diodos/Notas/PRACTICA 1/media/practica1_figura3_filtro_C.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-practica1-rectificadores.py

::SCRIPT_METADATA::
script_id: DIO-gen-practica1-rectificadores
module: DIO
generates:
  - practica1_figura1_puente.png
  - practica1_figura2_filtro_L.png
  - practica1_figura3_filtro_C.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/PRACTICA 1/PRACTICA_1.md
last_updated: 2026-03-17
"""

import matplotlib
matplotlib.use('Agg')  # Backend sin GUI
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
import os

# ══════════════════════════════════════════════════════════════════════════════
# Directorio de salida (en la carpeta de la práctica)
# ══════════════════════════════════════════════════════════════════════════════
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "Notas", "PRACTICA 1", "media")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Parámetros del circuito
VP = 120       # Voltaje primario RMS [V]
VS = 12        # Voltaje secundario RMS [V]
RATIO = "10:1" # Relación de transformación
RL = 10        # Resistencia de carga [Ω]
FREQ = 60      # Frecuencia [Hz]


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 1: Rectificador puente monofásico de onda completa
# ══════════════════════════════════════════════════════════════════════════════
def generar_figura1():
    """Genera el esquemático del rectificador puente básico."""
    fname = os.path.join(OUTPUT_DIR, "practica1_figura1_puente.png")

    with schemdraw.Drawing(show=False, dpi=160) as d:
        d.config(fontsize=11, unit=3.0)

        # ── Fuente AC (primario del transformador) ─────────────────────────
        d += (src := elm.SourceSin().up()
              .label(f'$V_p = {VP}\\,V_{{rms}}$\n$f = {FREQ}\\,Hz$',
                     loc='left', ofst=0.6))

        d += elm.Line().right(2.0)

        # ── Primario del transformador ─────────────────────────────────────
        d += (prim := elm.Inductor2(loops=4).down()
              .label('$N_1$', loc='left', ofst=0.15))

        d += elm.Line().left().to(src.start)

        # ── Núcleo magnético ───────────────────────────────────────────────
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

        # ── Relación de vueltas ────────────────────────────────────────────
        cx_nucleo = (cx1 + cx2) / 2
        d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label(
            f'${RATIO}$', fontsize=10)

        # ── Secundario ─────────────────────────────────────────────────────
        sec_x = prim.start[0] + 2.2
        sec_top_y = prim.start[1]
        sec_bot_y = prim.end[1]

        d += (sec := elm.Inductor2(loops=4).down().flip()
              .at((sec_x, sec_top_y))
              .to((sec_x, sec_bot_y)))

        sec_mid_y = (sec_top_y + sec_bot_y) / 2
        # N2 a la derecha del extremo inferior del secundario
        d += elm.Label().at((sec_x + 0.65, sec_bot_y)).label('$N_2$', fontsize=10)
        # Etiqueta de voltaje secundario debajo del secundario
        d += elm.Label().at((sec_x, sec_bot_y - 0.5)).label(
            f'$V_s = {VS}\\,V_{{rms}}$', fontsize=10)

        # ══════════════════════════════════════════════════════════════════
        # PUENTE DE DIODOS (D1, D2, D3, D4)
        # ══════════════════════════════════════════════════════════════════
        bridge_left_x = sec_x + 2.0
        bridge_right_x = bridge_left_x + 3.0
        bridge_top_y = sec_top_y
        bridge_bot_y = sec_bot_y

        # Conexiones desde secundario al puente
        d += elm.Line().right().at(sec.start).to((bridge_left_x, sec_top_y))
        d += elm.Dot().at((bridge_left_x, sec_top_y))

        d += elm.Line().right().at(sec.end).to((bridge_left_x, sec_bot_y))
        d += elm.Dot().at((bridge_left_x, sec_bot_y))

        # ── D1: superior horizontal ────────────────────────────────────────
        d += elm.Line().at((bridge_left_x, bridge_top_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_top_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_top_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_1$', loc='top'))

        # ── D3: inferior horizontal ────────────────────────────────────────
        d += elm.Line().at((bridge_left_x, bridge_bot_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_bot_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_bot_y))
              .to((bridge_right_x, bridge_bot_y))
              .label('$D_3$', loc='bot'))

        # Nodos derechos
        d += elm.Dot().at((bridge_right_x, bridge_top_y))
        d += elm.Dot().at((bridge_right_x, bridge_bot_y))

        # ── D4: vertical izquierdo ─────────────────────────────────────────
        d += (elm.Diode().up()
              .at((bridge_left_x, bridge_bot_y))
              .to((bridge_left_x, bridge_top_y))
              .label('$D_4$', loc='left'))

        # ── D2: vertical derecho ───────────────────────────────────────────
        d += (elm.Diode().up()
              .at((bridge_right_x, bridge_bot_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_2$', loc='right'))

        # ══════════════════════════════════════════════════════════════════
        # CARGA R_L
        # ══════════════════════════════════════════════════════════════════
        rl_x = bridge_right_x + 2.5
        d += elm.Line().right().at((bridge_right_x, bridge_top_y)).to(
            (rl_x, bridge_top_y))
        d += (elm.Resistor().down()
              .at((rl_x, bridge_top_y))
              .to((rl_x, bridge_bot_y))
              .label(f'$R_L = {RL}\\,\\Omega$', loc='right', ofst=0.2))
        d += elm.Line().left().at((rl_x, bridge_bot_y)).to(
            (bridge_right_x, bridge_bot_y))

        # ── Indicadores de voltaje de salida ───────────────────────────────
        d += elm.Label().at((rl_x + 0.8, bridge_top_y - 0.1)).label('$+$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, (bridge_top_y + bridge_bot_y) / 2)).label(
            '$V_o$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, bridge_bot_y + 0.1)).label('$-$', fontsize=12)

        # ── Ground ─────────────────────────────────────────────────────────
        gnd_x = (rl_x + bridge_right_x) / 2
        d += elm.Ground().at((gnd_x, bridge_bot_y))

        # ── Título ─────────────────────────────────────────────────────────
        d += elm.Label().at(((bridge_left_x + rl_x) / 2, bridge_top_y + 1.2)).label(
            'Figura 1: Rectificador puente de onda completa', fontsize=12)

        d.save(fname)

    print(f"Generada: {fname}")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 2: Rectificador con filtro inductivo (L en serie)
# ══════════════════════════════════════════════════════════════════════════════
def generar_figura2():
    """Genera el esquemático del rectificador con filtro inductivo."""
    fname = os.path.join(OUTPUT_DIR, "practica1_figura2_filtro_L.png")

    with schemdraw.Drawing(show=False, dpi=160) as d:
        d.config(fontsize=11, unit=3.0)

        # ── Fuente AC ──────────────────────────────────────────────────────
        d += (src := elm.SourceSin().up()
              .label(f'$V_p = {VP}\\,V_{{rms}}$\n$f = {FREQ}\\,Hz$',
                     loc='left', ofst=0.6))

        d += elm.Line().right(2.0)

        # ── Primario ───────────────────────────────────────────────────────
        d += (prim := elm.Inductor2(loops=4).down()
              .label('$N_1$', loc='left', ofst=0.15))

        d += elm.Line().left().to(src.start)

        # ── Núcleo ─────────────────────────────────────────────────────────
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

        cx_nucleo = (cx1 + cx2) / 2
        d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label(
            f'${RATIO}$', fontsize=10)

        # ── Secundario ─────────────────────────────────────────────────────
        sec_x = prim.start[0] + 2.2
        sec_top_y = prim.start[1]
        sec_bot_y = prim.end[1]

        d += (sec := elm.Inductor2(loops=4).down().flip()
              .at((sec_x, sec_top_y))
              .to((sec_x, sec_bot_y)))

        sec_mid_y = (sec_top_y + sec_bot_y) / 2
        d += elm.Label().at((sec_x + 0.65, sec_mid_y)).label('$N_2$', fontsize=10)

        # ══════════════════════════════════════════════════════════════════
        # PUENTE DE DIODOS
        # ══════════════════════════════════════════════════════════════════
        bridge_left_x = sec_x + 2.0
        bridge_right_x = bridge_left_x + 3.0
        bridge_top_y = sec_top_y
        bridge_bot_y = sec_bot_y

        d += elm.Line().right().at(sec.start).to((bridge_left_x, sec_top_y))
        d += elm.Dot().at((bridge_left_x, sec_top_y))
        d += elm.Line().right().at(sec.end).to((bridge_left_x, sec_bot_y))
        d += elm.Dot().at((bridge_left_x, sec_bot_y))

        # D1 superior
        d += elm.Line().at((bridge_left_x, bridge_top_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_top_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_top_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_1$', loc='top'))

        # D3 inferior
        d += elm.Line().at((bridge_left_x, bridge_bot_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_bot_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_bot_y))
              .to((bridge_right_x, bridge_bot_y))
              .label('$D_3$', loc='bot'))

        d += elm.Dot().at((bridge_right_x, bridge_top_y))
        d += elm.Dot().at((bridge_right_x, bridge_bot_y))

        # D4 izquierdo
        d += (elm.Diode().up()
              .at((bridge_left_x, bridge_bot_y))
              .to((bridge_left_x, bridge_top_y))
              .label('$D_4$', loc='left'))

        # D2 derecho
        d += (elm.Diode().up()
              .at((bridge_right_x, bridge_bot_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_2$', loc='right'))

        # ══════════════════════════════════════════════════════════════════
        # FILTRO INDUCTIVO (L en serie con R_L)
        # ══════════════════════════════════════════════════════════════════
        ind_x = bridge_right_x + 1.0
        d += elm.Line().right().at((bridge_right_x, bridge_top_y)).to((ind_x, bridge_top_y))
        d += elm.Dot().at((ind_x, bridge_top_y))

        # Inductor
        d += (elm.Inductor2(loops=3).right()
              .at((ind_x, bridge_top_y))
              .label('$L$', loc='top'))

        ind_end_x = d.here[0]
        d += elm.Line().right().length(0.5)
        rl_x = d.here[0]
        d += elm.Dot()

        # Resistencia de carga
        d += (elm.Resistor().down()
              .to((rl_x, bridge_bot_y))
              .label(f'$R_L = {RL}\\,\\Omega$', loc='right', ofst=0.2))
        d += elm.Line().left().to((bridge_right_x, bridge_bot_y))

        # ── Indicadores de voltaje de salida ───────────────────────────────
        d += elm.Label().at((rl_x + 0.8, bridge_top_y - 0.1)).label('$+$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, (bridge_top_y + bridge_bot_y) / 2)).label(
            '$V_o$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, bridge_bot_y + 0.1)).label('$-$', fontsize=12)

        # ── Ground ─────────────────────────────────────────────────────────
        gnd_x = (rl_x + bridge_right_x) / 2
        d += elm.Ground().at((gnd_x, bridge_bot_y))

        # ── Título ─────────────────────────────────────────────────────────
        d += elm.Label().at(((bridge_left_x + rl_x) / 2, bridge_top_y + 1.2)).label(
            'Figura 2: Rectificador con filtro inductivo', fontsize=12)

        d.save(fname)

    print(f"Generada: {fname}")


# ══════════════════════════════════════════════════════════════════════════════
# FIGURA 3: Rectificador con filtro capacitivo (C en paralelo)
# ══════════════════════════════════════════════════════════════════════════════
def generar_figura3():
    """Genera el esquemático del rectificador con filtro capacitivo."""
    fname = os.path.join(OUTPUT_DIR, "practica1_figura3_filtro_C.png")

    with schemdraw.Drawing(show=False, dpi=160) as d:
        d.config(fontsize=11, unit=3.0)

        # ── Fuente AC ──────────────────────────────────────────────────────
        d += (src := elm.SourceSin().up()
              .label(f'$V_p = {VP}\\,V_{{rms}}$\n$f = {FREQ}\\,Hz$',
                     loc='left', ofst=0.6))

        d += elm.Line().right(2.0)

        # ── Primario ───────────────────────────────────────────────────────
        d += (prim := elm.Inductor2(loops=4).down()
              .label('$N_1$', loc='left', ofst=0.15))

        d += elm.Line().left().to(src.start)

        # ── Núcleo ─────────────────────────────────────────────────────────
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

        cx_nucleo = (cx1 + cx2) / 2
        d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label(
            f'${RATIO}$', fontsize=10)

        # ── Secundario ─────────────────────────────────────────────────────
        sec_x = prim.start[0] + 2.2
        sec_top_y = prim.start[1]
        sec_bot_y = prim.end[1]

        d += (sec := elm.Inductor2(loops=4).down().flip()
              .at((sec_x, sec_top_y))
              .to((sec_x, sec_bot_y)))

        sec_mid_y = (sec_top_y + sec_bot_y) / 2
        d += elm.Label().at((sec_x + 0.65, sec_mid_y)).label('$N_2$', fontsize=10)

        # ══════════════════════════════════════════════════════════════════
        # PUENTE DE DIODOS
        # ══════════════════════════════════════════════════════════════════
        bridge_left_x = sec_x + 2.0
        bridge_right_x = bridge_left_x + 3.0
        bridge_top_y = sec_top_y
        bridge_bot_y = sec_bot_y

        d += elm.Line().right().at(sec.start).to((bridge_left_x, sec_top_y))
        d += elm.Dot().at((bridge_left_x, sec_top_y))
        d += elm.Line().right().at(sec.end).to((bridge_left_x, sec_bot_y))
        d += elm.Dot().at((bridge_left_x, sec_bot_y))

        # D1 superior
        d += elm.Line().at((bridge_left_x, bridge_top_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_top_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_top_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_1$', loc='top'))

        # D3 inferior
        d += elm.Line().at((bridge_left_x, bridge_bot_y)).to(
            ((bridge_left_x + bridge_right_x) / 2, bridge_bot_y))
        d += (elm.Diode().right()
              .at(((bridge_left_x + bridge_right_x) / 2 - 0.5, bridge_bot_y))
              .to((bridge_right_x, bridge_bot_y))
              .label('$D_3$', loc='bot'))

        d += elm.Dot().at((bridge_right_x, bridge_top_y))
        d += elm.Dot().at((bridge_right_x, bridge_bot_y))

        # D4 izquierdo
        d += (elm.Diode().up()
              .at((bridge_left_x, bridge_bot_y))
              .to((bridge_left_x, bridge_top_y))
              .label('$D_4$', loc='left'))

        # D2 derecho
        d += (elm.Diode().up()
              .at((bridge_right_x, bridge_bot_y))
              .to((bridge_right_x, bridge_top_y))
              .label('$D_2$', loc='right'))

        # ══════════════════════════════════════════════════════════════════
        # FILTRO CAPACITIVO (C en paralelo con R_L)
        # ══════════════════════════════════════════════════════════════════
        cap_x = bridge_right_x + 1.5
        rl_x = cap_x + 2.0

        # Línea superior
        d += elm.Line().right().at((bridge_right_x, bridge_top_y)).to((rl_x, bridge_top_y))
        d += elm.Dot().at((cap_x, bridge_top_y))
        d += elm.Dot().at((rl_x, bridge_top_y))

        # Capacitor
        d += (elm.Capacitor().down()
              .at((cap_x, bridge_top_y))
              .to((cap_x, bridge_bot_y))
              .label('$C$', loc='left', ofst=0.2))

        # Resistencia de carga
        d += (elm.Resistor().down()
              .at((rl_x, bridge_top_y))
              .to((rl_x, bridge_bot_y))
              .label(f'$R_L = {RL}\\,\\Omega$', loc='right', ofst=0.2))

        # Línea inferior (retorno)
        d += elm.Line().left().at((rl_x, bridge_bot_y)).to((bridge_right_x, bridge_bot_y))
        d += elm.Dot().at((cap_x, bridge_bot_y))

        # ── Indicadores de voltaje de salida ───────────────────────────────
        d += elm.Label().at((rl_x + 0.8, bridge_top_y - 0.1)).label('$+$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, (bridge_top_y + bridge_bot_y) / 2)).label(
            '$V_o$', fontsize=12)
        d += elm.Label().at((rl_x + 0.8, bridge_bot_y + 0.1)).label('$-$', fontsize=12)

        # ── Ground ─────────────────────────────────────────────────────────
        gnd_x = (cap_x + bridge_right_x) / 2
        d += elm.Ground().at((gnd_x, bridge_bot_y))

        # ── Título ─────────────────────────────────────────────────────────
        d += elm.Label().at(((bridge_left_x + rl_x) / 2, bridge_top_y + 1.2)).label(
            'Figura 3: Rectificador con filtro capacitivo', fontsize=12)

        d.save(fname)

    print(f"Generada: {fname}")


# ══════════════════════════════════════════════════════════════════════════════
# EJECUCIÓN PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generando esquemáticos de la Práctica 1...")
    print(f"Directorio de salida: {OUTPUT_DIR}")
    print("-" * 50)

    generar_figura1()
    generar_figura2()
    generar_figura3()

    print("-" * 50)
    print("¡Script completado exitosamente!")
