#!/usr/bin/env python3
"""
run_headless.py — Ejecutor sin GUI para Codespaces/CI
==============================================================================
Script de ejecucion headless para ambientes sin display (Linux CI, Codespaces).

Uso:
    python run_headless.py                     # Valores por defecto
    python run_headless.py --Vs_rms 15 --R_carga 12
    python run_headless.py --output-dir ./resultados
    python run_headless.py --json              # Salida JSON
    python run_headless.py --help

::SCRIPT_METADATA::
script_id    : practica1-headless
module       : DIO
generates    : PNG y/o JSON con resultados
referenced_by: CI/CD, Codespaces
last_updated : 2026-03-21
"""

# ============================================================================
# CONFIGURACION DE BACKEND ANTES DE CUALQUIER IMPORT DE MATPLOTLIB
# ============================================================================
import matplotlib
matplotlib.use("Agg")  # Backend sin GUI - DEBE ir antes de importar pyplot

import argparse
import json
import os
import sys
from pathlib import Path

# Agregar el directorio padre al path para imports relativos
sys.path.insert(0, str(Path(__file__).parent))

# Imports con soporte para paquete y script directo
try:
    from .core import (
        InputParams,
        CalcResults,
        calcular_todo,
        validate_params,
        results_to_dict,
        DEFAULT_PARAMS,
    )
    from .plotting import save_all_figures
except ImportError:
    from core import (
        InputParams,
        CalcResults,
        calcular_todo,
        validate_params,
        results_to_dict,
        DEFAULT_PARAMS,
    )
    from plotting import save_all_figures


# ============================================================================
# FUNCION PRINCIPAL
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de rectificadores monofasicos (modo headless)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python run_headless.py
  python run_headless.py --Vs_rms 15 --C_uF 4700
  python run_headless.py --output-dir ./outputs --prefix test
  python run_headless.py --json --no-plots
        """
    )

    # Parametros del circuito
    parser.add_argument("--Vs_rms", type=float, default=DEFAULT_PARAMS.Vs_rms,
                        help=f"Voltaje RMS secundario [V] (default: {DEFAULT_PARAMS.Vs_rms})")
    parser.add_argument("--f_red", type=float, default=DEFAULT_PARAMS.f_red,
                        help=f"Frecuencia de red [Hz] (default: {DEFAULT_PARAMS.f_red})")
    parser.add_argument("--Vd", type=float, default=DEFAULT_PARAMS.Vd,
                        help=f"Caida de voltaje por diodo [V] (default: {DEFAULT_PARAMS.Vd})")
    parser.add_argument("--R_carga", type=float, default=DEFAULT_PARAMS.R_carga,
                        help=f"Resistencia de carga [Ohm] (default: {DEFAULT_PARAMS.R_carga})")
    parser.add_argument("--L_H", type=float, default=DEFAULT_PARAMS.L_H,
                        help=f"Inductancia del filtro [H] (default: {DEFAULT_PARAMS.L_H})")
    parser.add_argument("--RL_Ohm", type=float, default=DEFAULT_PARAMS.RL_Ohm,
                        help=f"Resistencia del devanado [Ohm] (default: {DEFAULT_PARAMS.RL_Ohm})")
    parser.add_argument("--C_uF", type=float, default=DEFAULT_PARAMS.C_uF,
                        help=f"Capacitancia del filtro [uF] (default: {DEFAULT_PARAMS.C_uF})")
    parser.add_argument("--FR_obj", type=float, default=DEFAULT_PARAMS.FR_obj,
                        help=f"Factor de rizo objetivo (default: {DEFAULT_PARAMS.FR_obj})")

    # Opciones de salida
    parser.add_argument("--output-dir", "-o", type=str, default="./outputs",
                        help="Directorio de salida (default: ./outputs)")
    parser.add_argument("--prefix", type=str, default="practica1",
                        help="Prefijo para archivos de salida (default: practica1)")
    parser.add_argument("--dpi", type=int, default=150,
                        help="Resolucion de imagenes [DPI] (default: 150)")
    parser.add_argument("--json", action="store_true",
                        help="Exportar resultados a JSON")
    parser.add_argument("--no-plots", action="store_true",
                        help="No generar graficas (solo calculos)")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Modo silencioso (sin salida a consola)")

    args = parser.parse_args()

    # Crear parametros de entrada
    params = InputParams(
        Vs_rms=args.Vs_rms,
        f_red=args.f_red,
        Vd=args.Vd,
        R_carga=args.R_carga,
        L_H=args.L_H,
        RL_Ohm=args.RL_Ohm,
        C_uF=args.C_uF,
        FR_obj=args.FR_obj,
    )

    # Validar parametros
    is_valid, error = validate_params(params)
    if not is_valid:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)

    # Ejecutar calculos
    if not args.quiet:
        print("=" * 60)
        print("CALCULADORA DE RECTIFICADORES - Modo Headless")
        print("=" * 60)
        print(f"\nParametros de entrada:")
        print(f"  Vs_rms = {params.Vs_rms} V")
        print(f"  f_red  = {params.f_red} Hz")
        print(f"  Vd     = {params.Vd} V")
        print(f"  R      = {params.R_carga} Ohm")
        print(f"  L      = {params.L_H} H")
        print(f"  RL     = {params.RL_Ohm} Ohm")
        print(f"  C      = {params.C_uF} uF")
        print(f"  FR_obj = {params.FR_obj * 100}%")
        print()

    results = calcular_todo(params)

    # Mostrar resultados principales
    if not args.quiet:
        print("Resultados principales:")
        print("-" * 40)
        print(f"  Vm     = {results.Vm:.3f} V")
        print(f"  Vm_red = {results.Vm_red:.3f} V")
        print(f"  f_out  = {results.f_out:.0f} Hz")
        print()
        print(f"  Vo_dc  = {results.Vo_dc:.3f} V")
        print(f"  Io_dc  = {results.Io_dc:.3f} A")
        print()
        print(f"  FF     = {results.FF:.4f}")
        print(f"  FR     = {results.FR * 100:.2f}%")
        print()
        print(f"  eta    = {results.eta:.2f}%")
        print()
        print(f"  FRi (con C={params.C_uF:.0f}uF) = {results.FRi:.2f}%")
        print(f"  C_min  = {results.C_min_uF:.0f} uF")
        print()

    # Crear directorio de salida
    os.makedirs(args.output_dir, exist_ok=True)

    # Guardar JSON si se solicita
    if args.json:
        json_path = os.path.join(args.output_dir, f"{args.prefix}_results.json")
        output_data = {
            "params": {
                "Vs_rms": params.Vs_rms,
                "f_red": params.f_red,
                "Vd": params.Vd,
                "R_carga": params.R_carga,
                "L_H": params.L_H,
                "RL_Ohm": params.RL_Ohm,
                "C_uF": params.C_uF,
                "FR_obj": params.FR_obj,
            },
            "results": results_to_dict(results),
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        if not args.quiet:
            print(f"JSON guardado: {json_path}")

    # Generar graficas
    if not args.no_plots:
        if not args.quiet:
            print("\nGenerando graficas...")
        files = save_all_figures(params, results, args.output_dir, args.prefix, args.dpi)
        if not args.quiet:
            for f in files:
                print(f"  -> {f}")
            print(f"\nTotal: {len(files)} archivos generados")

    if not args.quiet:
        print("\nCompletado.")


if __name__ == "__main__":
    main()
