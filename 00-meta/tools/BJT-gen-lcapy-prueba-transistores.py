"""
::SCRIPT_METADATA::
script_id: BJT-gen-lcapy-prueba-transistores
module: BJT
generates:
  - bjt-lcapy-prueba-npn.png
  - bjt-lcapy-prueba-pnp.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota2.md
last_updated: 2026-04-15
"""

from pathlib import Path

from lcapy import Circuit


OUTPUT_DIR = Path("topics/02-transistor-bjt/assets")


def build_npn() -> Circuit:
    netlist = """
Q1 c b e npn; right
V1 c 0 V; down, l=$V_C$
V2 b 0_1 V; down, l=$V_B$
V3 e 0_2 V; down, l=$V_E$
"""
    return Circuit(netlist)


def build_pnp() -> Circuit:
    netlist = """
Q1 c b e pnp; right
V1 c 0 V; down, l=$V_C$
V2 b 0_1 V; down, l=$V_B$
V3 e 0_2 V; down, l=$V_E$
"""
    return Circuit(netlist)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    build_npn().draw(str(OUTPUT_DIR / "bjt-lcapy-prueba-npn.png"), dpi=600)
    build_pnp().draw(str(OUTPUT_DIR / "bjt-lcapy-prueba-pnp.png"), dpi=600)


if __name__ == "__main__":
    main()
