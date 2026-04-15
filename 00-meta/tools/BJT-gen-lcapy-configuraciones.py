"""
::SCRIPT_METADATA::
script_id: BJT-gen-lcapy-configuraciones
module: BJT
generates:
  - bjt-lcapy-npn-espaciado.png
  - bjt-lcapy-pnp-espaciado.png
  - bjt-lcapy-emisor-comun.png
  - bjt-lcapy-colector-comun.png
  - bjt-lcapy-base-comun.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota2.md
last_updated: 2026-04-15
"""

from pathlib import Path

from lcapy import Circuit


OUTPUT_DIR = Path("topics/02-transistor-bjt/assets")


def build_npn_spaced() -> Circuit:
    netlist = """
Q1 c b e npn; right
W c c1; right, l=$C$
V1 c1 0_1 V; down, l=$V_C$
W b b1; right, l=$B$
V2 b1 0_2 V; down, l=$V_B$
W e e1; right, l=$E$
V3 e1 0_3 V; down, l=$V_E$
"""
    return Circuit(netlist)


def build_pnp_spaced() -> Circuit:
    netlist = """
Q1 c b e pnp; right
W c c1; right, l=$C$
V1 c1 0_1 V; down, l=$V_C$
W b b1; right, l=$B$
V2 b1 0_2 V; down, l=$V_B$
W e e1; right, l=$E$
V3 e1 0_3 V; down, l=$V_E$
"""
    return Circuit(netlist)


def build_emisor_comun() -> Circuit:
    netlist = """
VCC vcc 0_1 V; up, l=$V_{CC}$
RC vcc c R; down, l=$R_C$
Q1 c b e npn; right
RE e 0_2 R; down, l=$R_E$
Vin b 0_3 V; down, l=$v_{in}$
W c out; right, l=$v_{out}$
"""
    return Circuit(netlist)


def build_colector_comun() -> Circuit:
    netlist = """
VCC vcc 0_1 V; up, l=$V_{CC}$
Q1 vcc b e npn; right
RE e 0_2 R; down, l=$R_E$
Vin b 0_3 V; down, l=$v_{in}$
W e out; right, l=$v_{out}$
"""
    return Circuit(netlist)


def build_base_comun() -> Circuit:
    netlist = """
VCC vcc 0_1 V; up, l=$V_{CC}$
RC vcc c R; down, l=$R_C$
Q1 c b e npn; right
RE e 0_2 R; down, l=$R_E$
W b b1; right, l=$B$
W b1 0_3; down
W e e1; right, l=$E$
Vin e1 0_4 V; down, l=$v_{in}$
W c out; right, l=$v_{out}$
"""
    return Circuit(netlist)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_npn_spaced().draw(str(OUTPUT_DIR / "bjt-lcapy-npn-espaciado.png"), dpi=600)
    build_pnp_spaced().draw(str(OUTPUT_DIR / "bjt-lcapy-pnp-espaciado.png"), dpi=600)
    build_emisor_comun().draw(str(OUTPUT_DIR / "bjt-lcapy-emisor-comun.png"), dpi=600)
    build_colector_comun().draw(str(OUTPUT_DIR / "bjt-lcapy-colector-comun.png"), dpi=600)
    build_base_comun().draw(str(OUTPUT_DIR / "bjt-lcapy-base-comun.png"), dpi=600)


if __name__ == "__main__":
    main()
