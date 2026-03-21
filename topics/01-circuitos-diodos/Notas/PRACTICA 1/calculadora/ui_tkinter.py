#!/usr/bin/env python3
"""
ui_tkinter.py — Interfaz grafica Tkinter para la calculadora
==============================================================================
Interfaz grafica interactiva usando Tkinter y matplotlib con backend TkAgg.

Requiere: Display disponible (X11, Windows, macOS)
Para uso local, no para Codespaces sin VNC.

::SCRIPT_METADATA::
script_id    : practica1-ui-tkinter
module       : DIO
generates    : interfaz grafica interactiva
referenced_by: main.py
last_updated : 2026-03-21
"""

# ============================================================================
# CONFIGURACION DE BACKEND - DEBE IR ANTES DE OTROS IMPORTS DE MATPLOTLIB
# ============================================================================
import matplotlib
matplotlib.use("TkAgg")

import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import sys
from pathlib import Path

# Agregar directorio padre al path
sys.path.insert(0, str(Path(__file__).parent))

# Imports con soporte para paquete y script directo
try:
    from .core import InputParams, CalcResults, calcular_todo, validate_params, DEFAULT_PARAMS
    from . import plotting
except ImportError:
    from core import InputParams, CalcResults, calcular_todo, validate_params, DEFAULT_PARAMS
    import plotting


# ============================================================================
# CLASE PRINCIPAL DE LA APLICACION
# ============================================================================

class App(tk.Tk):
    """Ventana principal de la calculadora de Practica 1."""

    # Paleta oscura
    BG_MAIN = "#1e1e2e"
    BG_PANEL = "#2a2a3e"
    BG_TAB = "#24243a"
    BG_ENTRY = "#313244"
    FG_TITLE = "#cdd6f4"
    FG_LABEL = "#a6adc8"
    FG_VALUE = "#89dceb"
    FG_EXP = "#a6e3a1"
    FG_WARN = "#f38ba8"
    FG_STEP = "#fab387"
    ACCENT = "#89b4fa"

    def __init__(self):
        super().__init__()
        self.title("Practica 1 — Rectificadores Monofasicos | ITT")
        self.configure(bg=self.BG_MAIN)
        self.geometry("1300x840")
        self.minsize(1050, 700)

        # Variables para parametros de entrada
        self._params = {
            "Vs_rms": tk.StringVar(value=str(DEFAULT_PARAMS.Vs_rms)),
            "f_red": tk.StringVar(value=str(DEFAULT_PARAMS.f_red)),
            "Vd": tk.StringVar(value=str(DEFAULT_PARAMS.Vd)),
            "R_carga": tk.StringVar(value=str(DEFAULT_PARAMS.R_carga)),
            "L_H": tk.StringVar(value=str(DEFAULT_PARAMS.L_H)),
            "RL_Ohm": tk.StringVar(value=str(DEFAULT_PARAMS.RL_Ohm)),
            "C_uF": tk.StringVar(value=str(DEFAULT_PARAMS.C_uF)),
            "FR_obj": tk.StringVar(value=str(DEFAULT_PARAMS.FR_obj)),
        }

        self._results: CalcResults = None
        self._input_params: InputParams = None

        self._build_styles()
        self._build_gui()
        self._calcular()

    def _build_styles(self):
        """Configura estilos ttk."""
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TNotebook", background=self.BG_MAIN, borderwidth=0)
        s.configure("TNotebook.Tab",
                    background=self.BG_PANEL, foreground=self.FG_LABEL,
                    padding=[14, 6], font=("Consolas", 10, "bold"))
        s.map("TNotebook.Tab",
              background=[("selected", self.ACCENT)],
              foreground=[("selected", self.BG_MAIN)])
        s.configure("TFrame", background=self.BG_PANEL)
        s.configure("TLabel", background=self.BG_PANEL, foreground=self.FG_LABEL,
                    font=("Consolas", 9))
        s.configure("TEntry", fieldbackground=self.BG_ENTRY,
                    foreground=self.FG_TITLE, insertcolor=self.FG_TITLE)
        s.configure("Calc.TButton",
                    background=self.ACCENT, foreground=self.BG_MAIN,
                    font=("Consolas", 10, "bold"), padding=8)
        s.map("Calc.TButton", background=[("active", "#7aa2f7")])
        s.configure("TScrollbar",
                    background=self.BG_PANEL, troughcolor=self.BG_MAIN,
                    arrowcolor=self.FG_LABEL)

    def _build_gui(self):
        """Construye la interfaz principal."""
        main = tk.Frame(self, bg=self.BG_MAIN)
        main.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Barra de titulo
        hdr = tk.Frame(main, bg=self.BG_MAIN)
        hdr.pack(fill=tk.X, pady=(0, 5))
        tk.Label(hdr,
                 text="PRACTICA 1 — ANALISIS DE RECTIFICADORES MONOFASICOS",
                 bg=self.BG_MAIN, fg=self.FG_TITLE,
                 font=("Consolas", 12, "bold")).pack(side=tk.LEFT, padx=4)
        tk.Label(hdr, text="ITT - Electronica",
                 bg=self.BG_MAIN, fg=self.FG_LABEL,
                 font=("Consolas", 9)).pack(side=tk.RIGHT, padx=6)

        # PanedWindow
        paned = tk.PanedWindow(main, orient=tk.HORIZONTAL,
                               bg=self.BG_MAIN, sashwidth=5, sashrelief=tk.FLAT)
        paned.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo
        left = tk.Frame(paned, bg=self.BG_PANEL, width=280)
        left.pack_propagate(False)
        paned.add(left, minsize=240)
        self._build_input_panel(left)

        # Notebook derecho
        nb = ttk.Notebook(paned)
        paned.add(nb, minsize=720)
        self.nb = nb

        self._tab_ondas = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_fourier = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_filtros = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_resumen = tk.Frame(nb, bg=self.BG_TAB)

        nb.add(self._tab_ondas, text="  Formas de Onda  ")
        nb.add(self._tab_fourier, text="  Serie de Fourier  ")
        nb.add(self._tab_filtros, text="  Diseno de Filtros  ")
        nb.add(self._tab_resumen, text="  Resumen  ")

        self._build_tab_ondas(self._tab_ondas)
        self._build_tab_fourier(self._tab_fourier)
        self._build_tab_filtros(self._tab_filtros)
        self._build_tab_resumen(self._tab_resumen)

    def _build_input_panel(self, parent):
        """Construye el panel de entrada de parametros."""
        # Canvas con scroll
        canvas = tk.Canvas(parent, bg=self.BG_PANEL, highlightthickness=0)
        vsb = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        inner = tk.Frame(canvas, bg=self.BG_PANEL)
        win_id = canvas.create_window((0, 0), window=inner, anchor=tk.NW)

        def _resize(e=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            if e.widget == canvas:
                canvas.itemconfig(win_id, width=e.width)

        inner.bind("<Configure>", _resize)
        canvas.bind("<Configure>", _resize)

        # Scroll con rueda
        def _on_mousewheel(e):
            if e.num == 4:
                canvas.yview_scroll(-1, "units")
            elif e.num == 5:
                canvas.yview_scroll(1, "units")
            else:
                canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")

        canvas.bind("<Enter>", lambda _: (canvas.bind_all("<MouseWheel>", _on_mousewheel),
                                          canvas.bind_all("<Button-4>", _on_mousewheel),
                                          canvas.bind_all("<Button-5>", _on_mousewheel)))
        canvas.bind("<Leave>", lambda _: (canvas.unbind_all("<MouseWheel>"),
                                          canvas.unbind_all("<Button-4>"),
                                          canvas.unbind_all("<Button-5>")))

        # Titulo
        tk.Label(inner, text="DATOS DE ENTRADA",
                 bg=self.BG_PANEL, fg=self.ACCENT,
                 font=("Consolas", 11, "bold")).pack(pady=(10, 0))
        tk.Label(inner, text="Sustituir con valores medidos\nen laboratorio y recalcular",
                 bg=self.BG_PANEL, fg="#585b70",
                 font=("Consolas", 7), justify=tk.CENTER).pack(pady=(0, 6))

        # Helper: seccion
        def seccion(titulo):
            frm = tk.LabelFrame(inner, text=f"  {titulo}  ",
                                bg=self.BG_PANEL, fg=self.ACCENT,
                                font=("Consolas", 9, "bold"),
                                bd=1, relief=tk.GROOVE)
            frm.pack(fill=tk.X, padx=8, pady=4)
            return frm

        # Helper: fila de entrada
        def entry_row(frm, label, var, unit="", hint=""):
            row = tk.Frame(frm, bg=self.BG_PANEL)
            row.pack(fill=tk.X, padx=6, pady=2)

            tk.Label(row, text=label, bg=self.BG_PANEL, fg=self.FG_LABEL,
                     font=("Consolas", 9), width=10, anchor=tk.W).pack(side=tk.LEFT)
            ent = tk.Entry(row, textvariable=var,
                           bg=self.BG_ENTRY, fg=self.FG_TITLE,
                           insertbackground=self.FG_TITLE,
                           font=("Consolas", 9), width=9, relief=tk.FLAT)
            ent.pack(side=tk.LEFT, padx=4)
            tk.Label(row, text=unit, bg=self.BG_PANEL, fg=self.FG_STEP,
                     font=("Consolas", 9)).pack(side=tk.LEFT)
            if hint:
                tk.Label(frm, text=f"   {hint}",
                         bg=self.BG_PANEL, fg="#585b70",
                         font=("Consolas", 7)).pack(anchor=tk.W, padx=6)

        # Secciones
        s1 = seccion("TRANSFORMADOR")
        entry_row(s1, "Vs_rms", self._params["Vs_rms"], "V", "multimetro AC")
        entry_row(s1, "f_red", self._params["f_red"], "Hz", "frecuencia de red")

        s2 = seccion("DIODOS 1N4005")
        entry_row(s2, "Vd", self._params["Vd"], "V", "caida por diodo")

        s3 = seccion("CARGA")
        entry_row(s3, "R_carga", self._params["R_carga"], "Ohm", "resistencia de carga")

        s4 = seccion("FILTRO INDUCTIVO")
        entry_row(s4, "L", self._params["L_H"], "H", "inductancia")
        entry_row(s4, "RL", self._params["RL_Ohm"], "Ohm", "R devanado")

        s5 = seccion("FILTRO CAPACITIVO")
        entry_row(s5, "C", self._params["C_uF"], "uF", "capacitancia")
        entry_row(s5, "FR_obj", self._params["FR_obj"], "", "objetivo (0.05=5%)")

        # Boton calcular
        tk.Frame(inner, height=8, bg=self.BG_PANEL).pack()
        ttk.Button(inner, text="CALCULAR",
                   style="Calc.TButton",
                   command=self._calcular).pack(fill=tk.X, padx=12, pady=4)
        tk.Label(inner,
                 text="Presione para actualizar\ntodos los resultados y graficas.",
                 bg=self.BG_PANEL, fg="#585b70",
                 font=("Consolas", 7), justify=tk.CENTER).pack(pady=(2, 12))

    def _build_tab_ondas(self, parent):
        """Tab de formas de onda."""
        tk.Label(parent,
                 text="FORMAS DE ONDA — Puente Graetz",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))

        self._fig_ondas = Figure(figsize=(10, 7.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_ondas, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_ondas = c

    def _build_tab_fourier(self, parent):
        """Tab de serie de Fourier."""
        tk.Label(parent,
                 text="SERIE DE FOURIER — Espectro del voltaje",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))

        self._fig_fourier = Figure(figsize=(10, 4.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_fourier, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_fourier = c

    def _build_tab_filtros(self, parent):
        """Tab de diseno de filtros."""
        tk.Label(parent,
                 text="DISENO DE FILTROS — Reduccion del rizo",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))

        self._fig_filtros = Figure(figsize=(10, 4.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_filtros, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_filtros = c

    def _build_tab_resumen(self, parent):
        """Tab de resumen de resultados."""
        tk.Label(parent,
                 text="RESUMEN DE RESULTADOS",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))

        # Text widget para mostrar resultados
        self._text_resumen = tk.Text(parent, bg=self.BG_MAIN, fg=self.FG_VALUE,
                                      font=("Consolas", 10), wrap=tk.WORD,
                                      padx=10, pady=10)
        self._text_resumen.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

    def _get_params(self) -> InputParams:
        """Lee y convierte parametros de entrada."""
        def safe_float(key, default):
            val_str = self._params[key].get().strip().replace(',', '.')
            try:
                return float(val_str) if val_str else default
            except ValueError:
                return default

        return InputParams(
            Vs_rms=safe_float("Vs_rms", DEFAULT_PARAMS.Vs_rms),
            f_red=safe_float("f_red", DEFAULT_PARAMS.f_red),
            Vd=safe_float("Vd", DEFAULT_PARAMS.Vd),
            R_carga=safe_float("R_carga", DEFAULT_PARAMS.R_carga),
            L_H=safe_float("L_H", DEFAULT_PARAMS.L_H),
            RL_Ohm=safe_float("RL_Ohm", DEFAULT_PARAMS.RL_Ohm),
            C_uF=safe_float("C_uF", DEFAULT_PARAMS.C_uF),
            FR_obj=safe_float("FR_obj", DEFAULT_PARAMS.FR_obj),
        )

    def _calcular(self):
        """Ejecuta calculos y actualiza todas las graficas."""
        try:
            self._input_params = self._get_params()

            # Validar
            is_valid, error = validate_params(self._input_params)
            if not is_valid:
                messagebox.showerror("Parametro invalido", error)
                return

            # Calcular
            self._results = calcular_todo(self._input_params)

            # Actualizar graficas
            self._actualizar_ondas()
            self._actualizar_fourier()
            self._actualizar_filtros()
            self._actualizar_resumen()

        except Exception as exc:
            import traceback
            messagebox.showerror(
                "Error de calculo",
                f"Revise los parametros:\n\n{exc}\n\n{traceback.format_exc()}"
            )

    def _actualizar_ondas(self):
        """Actualiza grafica de formas de onda."""
        self._fig_ondas.clear()
        plotting.plot_waveforms(self._fig_ondas, self._input_params, self._results)
        self._canvas_ondas.draw()

    def _actualizar_fourier(self):
        """Actualiza grafica de Fourier."""
        self._fig_fourier.clear()
        plotting.plot_fourier(self._fig_fourier, self._input_params, self._results)
        self._canvas_fourier.draw()

    def _actualizar_filtros(self):
        """Actualiza grafica de filtros."""
        self._fig_filtros.clear()
        plotting.plot_filter_design(self._fig_filtros, self._input_params, self._results)
        self._canvas_filtros.draw()

    def _actualizar_resumen(self):
        """Actualiza resumen de texto."""
        r = self._results
        p = self._input_params

        text = f"""
PARAMETROS DE ENTRADA
{'='*50}
  Vs_rms  = {p.Vs_rms:.2f} V
  f_red   = {p.f_red:.0f} Hz
  Vd      = {p.Vd:.2f} V
  R_carga = {p.R_carga:.1f} Ohm
  L       = {p.L_H:.2f} H
  RL      = {p.RL_Ohm:.1f} Ohm
  C       = {p.C_uF:.0f} uF
  FR_obj  = {p.FR_obj*100:.1f}%

PASO 1 — TRANSFORMADOR
{'='*50}
  Vm      = {r.Vm:.3f} V
  Vm_red  = {r.Vm_red:.3f} V
  f_out   = {r.f_out:.0f} Hz
  T_out   = {r.T_out*1e3:.3f} ms

PASO 2 — DC PROMEDIO
{'='*50}
  Vo_dc   = {r.Vo_dc:.3f} V
  Io_dc   = {r.Io_dc:.3f} A

PASO 3 — RMS SIN FILTRO
{'='*50}
  Vo_rms  = {r.Vo_rms:.3f} V
  Io_rms  = {r.Io_rms:.3f} A

PASO 4 — FACTOR DE FORMA Y RIZO
{'='*50}
  FF      = {r.FF:.4f}
  Vr_rms  = {r.Vr_rms:.3f} V
  FR      = {r.FR*100:.2f}%

PASO 5 — DIODOS
{'='*50}
  ID_prom = {r.ID_prom:.3f} A
  ID_rms  = {r.ID_rms:.3f} A
  VPR     = {r.VPR:.3f} V
  P_diodo = {r.P_diodo:.3f} W

PASO 6 — POTENCIAS
{'='*50}
  Po_dc   = {r.Po_dc:.3f} W
  Po_ca   = {r.Po_ca:.3f} W
  eta     = {r.eta:.2f}%

PASO 9 — FILTRO CAPACITIVO
{'='*50}
  Vr_pp     = {r.Vr_pp:.3f} V
  Vo_dc_C   = {r.Vo_dc_C:.3f} V
  FRi       = {r.FRi:.2f}%
  C_min     = {r.C_min_uF:.0f} uF
"""
        if r.FRi > p.FR_obj * 100:
            text += f"""
!! ADVERTENCIA: FRi ({r.FRi:.1f}%) > objetivo ({p.FR_obj*100:.0f}%)
   Aumentar C a >= {r.C_min_uF:.0f} uF
"""

        self._text_resumen.delete("1.0", tk.END)
        self._text_resumen.insert("1.0", text)


def main():
    """Punto de entrada para GUI."""
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
