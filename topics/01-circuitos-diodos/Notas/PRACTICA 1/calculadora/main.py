#!/usr/bin/env python3
"""
main.py — Punto de entrada con auto-deteccion de entorno
==============================================================================
Detecta automaticamente si hay display disponible y elige el modo apropiado:
  - Con DISPLAY: Lanza interfaz grafica (TkAgg)
  - Sin DISPLAY: Ejecuta en modo headless (Agg)

Uso:
    python main.py                  # Auto-detecta
    python main.py --gui            # Forzar GUI
    python main.py --headless       # Forzar headless
    python main.py --help           # Ayuda

::SCRIPT_METADATA::
script_id    : practica1-main
module       : DIO
generates    : depende del modo
referenced_by: PRACTICA_1.md
last_updated : 2026-03-21
"""

import os
import sys
import argparse
from pathlib import Path

# Agregar directorio actual al path
sys.path.insert(0, str(Path(__file__).parent))


def detect_display() -> bool:
    """
    Detecta si hay un display disponible.

    Returns
    -------
    bool : True si hay display disponible
    """
    # En Windows siempre hay display
    if sys.platform == "win32":
        return True

    # En macOS verificar DISPLAY o que no sea SSH sin X11 forwarding
    if sys.platform == "darwin":
        # macOS generalmente tiene display si esta corriendo localmente
        # Verificar si es una sesion SSH sin X11
        if os.environ.get("SSH_CONNECTION") and not os.environ.get("DISPLAY"):
            return False
        return True

    # En Linux verificar DISPLAY
    display = os.environ.get("DISPLAY", "")
    if display:
        # Verificar que X11 este realmente disponible
        try:
            import subprocess
            result = subprocess.run(
                ["xdpyinfo"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=2
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # xdpyinfo no disponible, intentar con DISPLAY
            return bool(display)

    return False


def run_gui():
    """Ejecuta la interfaz grafica."""
    print("Iniciando modo GUI...")
    from ui_tkinter import main
    main()


def run_headless(args=None):
    """Ejecuta en modo headless."""
    print("Iniciando modo headless...")

    # Si hay argumentos adicionales, pasarlos al script headless
    if args:
        sys.argv = ["run_headless.py"] + args
    else:
        # Usar valores por defecto
        sys.argv = ["run_headless.py"]

    from run_headless import main
    main()


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de rectificadores monofasicos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modos de ejecucion:
  Auto-detectar:   python main.py
  Forzar GUI:      python main.py --gui
  Forzar headless: python main.py --headless [opciones]

Opciones para modo headless:
  --Vs_rms, --f_red, --Vd, --R_carga, --L_H, --RL_Ohm, --C_uF, --FR_obj
  --output-dir, --prefix, --dpi, --json, --no-plots, --quiet

Ejemplos:
  python main.py --gui
  python main.py --headless --Vs_rms 15 --C_uF 4700
  python main.py --headless --json --output-dir ./results
        """
    )

    parser.add_argument("--gui", action="store_true",
                        help="Forzar modo GUI (requiere display)")
    parser.add_argument("--headless", action="store_true",
                        help="Forzar modo headless (sin GUI)")
    parser.add_argument("--detect", action="store_true",
                        help="Solo detectar entorno y mostrar info")

    # Capturar argumentos conocidos, pasar el resto a headless
    args, remaining = parser.parse_known_args()

    # Solo detectar
    if args.detect:
        has_display = detect_display()
        print(f"Plataforma: {sys.platform}")
        print(f"DISPLAY: {os.environ.get('DISPLAY', '(no definido)')}")
        print(f"Display disponible: {'Si' if has_display else 'No'}")
        print(f"Modo recomendado: {'GUI' if has_display else 'Headless'}")
        return

    # Determinar modo
    if args.gui and args.headless:
        print("ERROR: No se puede usar --gui y --headless al mismo tiempo",
              file=sys.stderr)
        sys.exit(1)

    if args.gui:
        # Forzar GUI
        has_display = detect_display()
        if not has_display:
            print("ADVERTENCIA: --gui solicitado pero no hay display disponible",
                  file=sys.stderr)
            print("Intentando de todas formas...", file=sys.stderr)
        run_gui()

    elif args.headless:
        # Forzar headless
        run_headless(remaining)

    else:
        # Auto-detectar
        has_display = detect_display()
        if has_display:
            print("Display detectado, iniciando GUI...")
            run_gui()
        else:
            print("No se detecto display, iniciando modo headless...")
            run_headless(remaining)


if __name__ == "__main__":
    main()
