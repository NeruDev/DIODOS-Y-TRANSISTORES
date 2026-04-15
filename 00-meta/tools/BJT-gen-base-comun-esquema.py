"""
::SCRIPT_METADATA::
script_id: BJT-gen-base-comun-esquema
module: BJT
generates:
  - bjt-base-comun-esquema.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota1.md
last_updated: 2026-04-15
"""

import matplotlib
matplotlib.use('Agg')

from pathlib import Path

import schemdraw
import schemdraw.elements as elm


OUTPUT_PATH = Path("topics/02-transistor-bjt/assets/bjt-base-comun-esquema.png")


def build_diagram() -> schemdraw.Drawing:
    d = schemdraw.Drawing(unit=4.0, fontsize=14)

    q1 = d.add(elm.BjtNpn().at((0, 0)))

    base_left = (q1.base[0] - 3.2, q1.base[1])
    d.add(elm.Line().at(q1.base).to(base_left))
    d.add(elm.Ground().at(base_left))
    d.add(elm.Label().at((base_left[0] - 0.1, base_left[1] + 0.35)).label("Base (B)"))

    emitter_left = (q1.emitter[0] - 3.4, q1.emitter[1])
    d.add(elm.Line().at(q1.emitter).to(emitter_left))
    d.add(elm.Dot().at(q1.emitter))
    d.add(elm.Label().at((emitter_left[0] - 0.2, emitter_left[1] + 0.35)).label("Entrada"))

    emitter_bottom = (q1.emitter[0], q1.emitter[1] - 3.4)
    d.add(elm.Resistor().at(q1.emitter).down().to(emitter_bottom).label("$R_E$", loc="right", ofst=0.2))

    supply_x_pos = q1.collector[0] + 4.6
    supply_x_neg = q1.emitter[0] - 4.6
    ground_y = q1.emitter[1] - 6.4

    emitter_bus = (supply_x_neg, emitter_bottom[1])
    d.add(elm.Line().at(emitter_bottom).to(emitter_bus))

    d.add(
        elm.SourceV()
        .at(emitter_bus)
        .down()
        .to((supply_x_neg, ground_y))
        .reverse()
        .label("$V_{EE}$", loc="right", ofst=0.2)
    )
    d.add(elm.Ground().at((supply_x_neg, ground_y)))

    collector_top = (q1.collector[0], q1.collector[1] + 3.4)
    d.add(elm.Resistor().at(q1.collector).up().to(collector_top).label("$R_C$", loc="right", ofst=0.2))

    vcc_top_y = q1.collector[1] + 6.2
    collector_bus = (supply_x_pos, collector_top[1])
    d.add(elm.Line().at(collector_top).to(collector_bus))
    d.add(elm.Line().at(collector_bus).to((supply_x_pos, vcc_top_y)))

    d.add(
        elm.SourceV()
        .at((supply_x_pos, ground_y))
        .up()
        .to((supply_x_pos, vcc_top_y))
        .label("$V_{CC}$", loc="right", ofst=0.2)
    )
    d.add(elm.Ground().at((supply_x_pos, ground_y)))

    collector_right = (q1.collector[0] + 3.4, q1.collector[1])
    d.add(elm.Line().at(q1.collector).to(collector_right))
    d.add(elm.Dot().at(q1.collector))
    d.add(elm.Label().at((collector_right[0] + 0.2, collector_right[1] + 0.35)).label("Salida"))

    d.add(elm.Label().at((q1.emitter[0] + 0.65, q1.emitter[1] - 0.7)).label("Emisor (E)"))
    d.add(elm.Label().at((q1.collector[0] + 0.65, q1.collector[1] + 0.7)).label("Colector (C)"))

    vbe_x = q1.base[0] + 0.8
    d.add(elm.Arrow().at((vbe_x, q1.base[1])).to((vbe_x, q1.emitter[1])).label("$V_{BE}$", loc="right", ofst=0.2))

    vcb_x = q1.base[0] + 1.6
    d.add(elm.Arrow().at((vcb_x, q1.collector[1])).to((vcb_x, q1.base[1])).label("$V_{CB}$", loc="right", ofst=0.2))

    return d


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    diagram = build_diagram()
    diagram.save(str(OUTPUT_PATH), dpi=600)


if __name__ == "__main__":
    main()
