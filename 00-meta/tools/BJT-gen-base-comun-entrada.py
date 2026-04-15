"""
::SCRIPT_METADATA::
script_id: BJT-gen-base-comun-entrada
module: BJT
generates:
  - bjt-base-comun-entrada.png
referenced_by:
  - topics/02-transistor-bjt/Notas/Nota1.md
last_updated: 2026-04-15
"""

import matplotlib
matplotlib.use('Agg')

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


OUTPUT_PATH = Path("topics/02-transistor-bjt/assets/bjt-base-comun-entrada.png")


def build_data():
    vbe = np.linspace(0.55, 0.82, 240)
    is_current = 1.0e-9
    nvt = 0.044
    vcb_values = [0, 2, 4, 6]
    curves = []
    for vcb in vcb_values:
        shift = 0.005 * vcb
        vbe_eff = vbe - shift
        ie = is_current * (np.exp(vbe_eff / nvt) - 1.0)
        curves.append((vcb, ie * 1e3))
    return vbe, curves


def main() -> None:
    vbe, curves = build_data()

    plt.figure(figsize=(7.8, 5.2))
    for vcb, ie_ma in curves:
        plt.plot(vbe, ie_ma, linewidth=2.2, label=f"$V_{{CB}} = {vcb}\\,V$")

    plt.title("Caracteristicas de entrada (Base Comun)")
    plt.xlabel("$V_{BE}$ (V)")
    plt.ylabel("$I_E$ (mA)")
    plt.grid(True, which="both", linestyle="--", alpha=0.6)
    plt.legend(title="Parametros", loc="upper left")

    plt.annotate(
        "$V_{CB}$ mayor -> curva a la izquierda",
        xy=(0.66, 2.0),
        xytext=(0.70, 6.5),
        arrowprops=dict(arrowstyle="->", lw=1.4),
        fontsize=10,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=600)
    plt.close()


if __name__ == "__main__":
    main()
