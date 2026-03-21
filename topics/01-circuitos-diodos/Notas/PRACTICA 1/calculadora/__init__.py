"""
calculadora — Paquete modular para calculos de rectificadores
==============================================================================

Estructura del paquete:
  core.py        - Calculos matematicos puros (sin GUI)
  plotting.py    - Generacion de graficas (backend-agnostico)
  run_headless.py - Ejecucion sin GUI (Codespaces/CI)
  ui_tkinter.py  - Interfaz grafica Tkinter
  main.py        - Punto de entrada con auto-deteccion

Uso rapido:
    # Modo automatico (detecta display)
    python -m calculadora

    # Modo headless explicito
    python -m calculadora --headless

    # Modo GUI explicito
    python -m calculadora --gui

    # Ejecutar directamente headless
    python calculadora/run_headless.py --json

::SCRIPT_METADATA::
script_id    : practica1-pkg
module       : DIO
generates    : paquete Python
referenced_by: PRACTICA_1.md
last_updated : 2026-03-21
"""

from .core import (
    InputParams,
    CalcResults,
    calcular_todo,
    validate_params,
    params_from_dict,
    results_to_dict,
    DEFAULT_PARAMS,
    # Funciones de generacion de senales
    generate_time_array,
    generate_secondary_voltage,
    generate_rectified_voltage,
    generate_capacitor_filtered,
    generate_inductor_filtered_current,
    generate_fourier_reconstruction,
    generate_fr_vs_capacitance,
    generate_attenuation_vs_inductance,
)

__all__ = [
    # Clases
    "InputParams",
    "CalcResults",
    # Funciones principales
    "calcular_todo",
    "validate_params",
    "params_from_dict",
    "results_to_dict",
    # Constantes
    "DEFAULT_PARAMS",
    # Funciones de senales
    "generate_time_array",
    "generate_secondary_voltage",
    "generate_rectified_voltage",
    "generate_capacitor_filtered",
    "generate_inductor_filtered_current",
    "generate_fourier_reconstruction",
    "generate_fr_vs_capacitance",
    "generate_attenuation_vs_inductance",
]

__version__ = "2.0.0"
