"""
DIO-gen-nota7-filtro-inductivo.py
───────────────────
Genera el esquemático de un rectificador tipo puente con filtro inductivo
(inductor en serie con la carga).

Salida:
  - 01-Circuitos-Diodos/media/generated/nota7_filtro_inductivo.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota7-filtro-inductivo.py

::SCRIPT_METADATA::
script_id: DIO-gen-nota7-filtro-inductivo
module: DIO
generates:
  - nota7_filtro_inductivo.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota7.md
last_updated: 2026-03-04
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
import os

OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# Esquemático: Rectificador puente + Filtro inductivo (L serie)
# ═══════════════════════════════════════════════════════════════
# Topología: Fuente AC → Puente de diodos → L (serie) → R_L
# Usa el elemento integrado Rectifier de schemdraw (anclajes N/S/E/W).

with schemdraw.Drawing(file=os.path.join(OUTPUT_DIR, 'nota7_filtro_inductivo.png'),
                       show=False, dpi=150) as d:
    d.config(fontsize=14, unit=3.5)

    # ── Fuente AC ──
    d += (vs := elm.SourceSin().up().label('$v_s$', loc='left', ofst=0.55))

    # ── Línea al puente (entrada superior) ──
    d += elm.Line().right().length(1.0)
    ac_top = d.here

    # ── Puente rectificador (elemento integrado) ──
    # Anclas: N = DC+, S = DC−, W = AC entrada izq, E = AC entrada der
    # Diodos internos: A(θ=45), B(θ=-45), C(θ=-135 rev), D(θ=135 rev)
    d += (bridge := elm.Rectifier(
        labels=['$D_1$', '$D_2$', '$D_3$', '$D_4$']
    ).at(ac_top).anchor('W').right())

    # ── Conectar entrada inferior de la fuente al puente ──
    d.here = vs.start
    d += elm.Line().right().tox(bridge.E[0])
    d += elm.Line().up().toy(bridge.E[1])

    # ── Salida DC+: inductor en serie ──
    d.here = bridge.N
    d += elm.Dot()
    d += elm.Line().right().length(0.5)
    d += (L := elm.Inductor2(loops=3).right().label('$L$', loc='top'))
    d += elm.Line().right().length(0.5)
    d += elm.Dot()
    load_top = d.here

    # ── Resistencia de carga ──
    d += (rl := elm.Resistor().down().label('$R_L$', loc='right'))
    d += elm.Dot()
    load_bot = d.here

    # ── Extender hacia abajo al nivel de bridge.S y conectar retorno ──
    # (El diamante del puente es más alto que el resistor, hay que bajar)
    d += elm.Line().down().toy(bridge.S[1])
    d += elm.Dot()
    gnd_right = d.here
    d += elm.Line().left().tox(bridge.S[0])

    # ── Tierra en el nodo de retorno (debajo de R_L) ──
    d.here = gnd_right
    d += elm.Ground()

    # ── Indicadores de polaridad ──
    d += elm.Label().at((load_top[0] + 0.5, load_top[1])).label('$+$', fontsize=16)
    d += elm.Label().at((load_top[0] + 0.5, gnd_right[1])).label('$-$', fontsize=16)

    # ── Etiqueta voltaje de salida ──
    mid_y = (load_top[1] + gnd_right[1]) / 2
    d += elm.Label().at((load_top[0] + 1.2, mid_y)).label('$v_o$', fontsize=16)

print("Generada: nota7_filtro_inductivo.png")
