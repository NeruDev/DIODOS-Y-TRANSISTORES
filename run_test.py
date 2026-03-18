import tkinter as tk
import sys
sys.path.append("/workspaces/DIODOS-Y-TRANSISTORES/01-Circuitos-Diodos/Notas/PRACTICA 1")
from practica1_calculadora import App
app = App()
app._params["Vs_rms"].set(20.0)
try:
    app._calcular()
    print("Calcular done")
except Exception as e:
    import traceback
    traceback.print_exc()
app.destroy()
