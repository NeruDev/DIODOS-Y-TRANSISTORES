"""
practica1_calculadora.py
──────────────────────────────────────────────────────────────────────────────
Calculadora interactiva para la Práctica 1:
  "Análisis e implementación de rectificadores monofásicos"
  INSTITUTO TECNOLÓGICO DE TOLUCA — Diodos y Transistores

Orden de cálculo (incisos de la práctica):
  PASO 1 │ Parámetros del transformador (Vs_rms → Vm)
  PASO 2 │ Voltaje y corriente DC promedio (Vo_cd, Io_cd)
  PASO 3 │ Voltaje y corriente RMS sin filtro (Vo_rms, Io_rms)
  PASO 4 │ Factor de forma y rizo sin filtro (FF, Vr_rms, FR)
  PASO 5 │ Parámetros de los diodos (ID_prom, ID_rms, VPR, P_diodo)
  PASO 6 │ Potencias y rendimiento (Po_cd, Po_CA, η)
  PASO 7 │ Serie de Fourier del voltaje de salida (5 armónicos)
  PASO 8 │ Filtro inductivo R-L (atenuación de armónicos de corriente)
  PASO 9 │ Diseño del filtro capacitivo (FR_i ≤ 5%)

Interfaz gráfica (tkinter + matplotlib):
  ┌─ Panel izquierdo ── datos de entrada por sección ───────────────────────┐
  │  Tab "Cálculos por Pasos"  → tabla: param | fórmula | teórico | medido  │
  │  Tab "Formas de Onda"      → vs, v_rect, v_filt_C, iD (matplotlib)      │
  │  Tab "Serie de Fourier"    → reconstrucción + espectro de barras         │
  │  Tab "Diseño de Filtros"   → FR vs C, atenuación vs L                   │
  └──────────────────────────────────────────────────────────────────────────┘

::SCRIPT_METADATA::
script_id    : practica1-calculadora
module       : DIO
generates    : interfaz gráfica interactiva (sin PNG — script standalone)
referenced_by: 01-Circuitos-Diodos/Notas/PRACTICA 1/PRACTICA_1.md
last_updated : 2026-03-14

Dependencias: numpy, matplotlib  (incluidas en .venv del repositorio)
Ejecutar desde la raíz del repositorio:
  python "01-Circuitos-Diodos/Notas/PRACTICA 1/practica1_calculadora.py"
O directamente desde la carpeta de la práctica:
  python practica1_calculadora.py
"""

# ─── IMPORTACIONES ─────────────────────────────────────────────────────────────
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")                           # backend embebible en tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

# ─── PARÁMETROS DEFAULT (NOMINALES / TEÓRICOS) ────────────────────────────────
# Estos son los valores de diseño de la práctica.
# ► Cuando obtenga las mediciones reales en el laboratorio, ACTUALICE cada campo
#   en el panel "Datos de Entrada" de la interfaz.  Los resultados se recalculan
#   al presionar "⟳ CALCULAR TODO".
DEFAULTS = {
    # ── Transformador ──────────────────────────────────────────────────────────
    # Vs_rms  Voltaje RMS en el secundario del transformador.
    #   CÓMO MEDIR : Multímetro en modo CA sobre las terminales del secundario.
    #   ESPERADO   : ~12 V (puede variar ±5 % según carga y regulación de red).
    "Vs_rms": 12.0,           # V RMS   ← DATO EXPERIMENTAL  (multímetro AC)

    # f_red   Frecuencia de la red eléctrica.
    #   CÓMO MEDIR : Osciloscopio sobre vs(t) → medir período T → f = 1/T.
    #   ESPERADO   : 60 Hz (México).
    "f_red": 60.0,            # Hz      ← confirmar con osciloscopio

    # ── Diodos 1N4005 ─────────────────────────────────────────────────────────
    # Vd      Caída de voltaje directa por diodo en conducción.
    #   CÓMO MEDIR : Multímetro en modo "diodo" sobre D1 mientras conduce;
    #                o medir la diferencia Vm − Vo_pico con el osciloscopio.
    #   ESPERADO   : 0.60 – 0.75 V para silicio; 1N4005 típico ≈ 0.7 V a 1 A.
    #   NOTA       : En el puente Graetz hay 2 diodos en serie → caída total = 2·Vd.
    "Vd": 0.7,                # V       ← DATO EXPERIMENTAL  (multímetro / osci.)

    # ── Carga ─────────────────────────────────────────────────────────────────
    # R_carga  Resistencia de la carga.
    #   CÓMO MEDIR : Multímetro en Ω con la resistencia DESCONECTADA del circuito.
    #   ESPERADO   : ~10 Ω (resistor 10 Ω / 25 W); tolerancia ±5 % usual.
    "R_carga": 10.0,          # Ω       ← DATO EXPERIMENTAL  (multímetro Ω)

    # ── Filtro inductivo (inciso i) ────────────────────────────────────────────
    # L_H     Inductancia del primario del transformador auxiliar (usado como L).
    #   CÓMO MEDIR : Puente LCR a f_prueba = 100 Hz (según indica el inciso i).
    #   ESPERADO   : ~1.5 H para primario 120V/12V@2A (valor típico propuesto).
    #                Puede variar ampliamente — siempre medir en el lab.
    "L_H": 1.5,               # H       ← DATO EXPERIMENTAL  (puente LCR a 100 Hz)

    # RL_Ohm  Resistencia del devanado del inductor (alambre del primario).
    #   CÓMO MEDIR : Puente LCR a 100 Hz (mide L y R simultáneamente), o
    #                multímetro en modo Ω directamente sobre las terminales.
    #   ESPERADO   : ~40 Ω para primario 120V/12V@2A (impedancia del alambre).
    #   EFECTO     : R_L crea una caída de voltaje DC que REDUCE el voltaje en R.
    #                Voltaje en carga = Io_dc × R  (no Vo(cd) completo).
    "RL_Ohm": 40.0,           # Ω       ← DATO EXPERIMENTAL  (puente LCR / multímetro)

    # ── Filtro capacitivo (inciso l) ───────────────────────────────────────────
    # C_uF    Capacitor electrolítico instalado en paralelo con la carga.
    #   CALCULAR   : El script determina C_min; sustituir aquí el valor estándar
    #                comercial más próximo que se haya utilizado en el laboratorio.
    #   ESPERADO   : 2200 – 4700 µF para R = 10 Ω, f_out = 120 Hz y FR ≤ 5 %.
    "C_uF": 2200.0,           # µF      ← DATO EXPERIMENTAL  (valor real usado)

    # FR_obj  Factor de rizo máximo permitido (objetivo del inciso l).
    #   VALOR FIJO : 5 % (según enunciado de la práctica).
    "FR_obj": 0.05,           # ≤ 5 %   (no modificar sin nueva especificación)
}

# ─── FUNCIONES DE CÁLCULO: PASO A PASO ────────────────────────────────────────

def calcular_todo(p: dict) -> dict:
    """
    Ejecuta los 9 pasos de cálculo de la práctica en orden.

    Parámetros
    ----------
    p : dict  — valores de entrada (claves coinciden con DEFAULTS)

    Retorna
    -------
    r : dict  — todos los resultados intermedios y finales
    """
    r = {}

    Vs    = p["Vs_rms"]
    f     = p["f_red"]
    Vd    = p["Vd"]
    R     = p["R_carga"]
    L     = p["L_H"]
    RL    = p["RL_Ohm"]               # Ω  resistencia del devanado del inductor
    RT    = R + RL                    # Ω  resistencia total con filtro inductivo
    C     = p["C_uF"] * 1e-6          # µF → F
    FR_o  = p["FR_obj"]
    w_red = 2.0 * np.pi * f           # rad/s (frecuencia angular de la red)

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 1 — PARÁMETROS DEL TRANSFORMADOR
    # ──────────────────────────────────────
    # La relación fundamental entre el valor RMS y el pico de una sinusoide:
    #   Vm = Vs_rms × √2
    # El rectificador puente tiene DOS diodos en serie durante cada semiciclo,
    # por lo que el voltaje pico disponible en la carga se reduce en 2·Vd.
    # La frecuencia de salida se DUPLICA respecto a la red (onda completa).
    # ══════════════════════════════════════════════════════════════════════════
    r["Vm"]      = Vs * np.sqrt(2)             # V pico del secundario
    r["Vm_red"]  = r["Vm"] - 2.0 * Vd         # V pico disponible (con 2 diodos)
    r["f_out"]   = 2.0 * f                     # Hz (onda completa ↔ 2×f_red)
    r["T_out"]   = 1.0 / r["f_out"]           # s período de la señal de salida

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 2 — VOLTAJE Y CORRIENTE DC (PROMEDIO)
    # ───────────────────────────────────────────
    # Para el rectificador de onda completa tipo puente (Graetz):
    #   Vo(cd) = (2/π) × Vm_red
    # Valor ideal sin pérdidas: Vo(cd) = (2/π) × Vm ≈ 0.6366 × Vm
    # ESPERADO (Vs = 12 V RMS, Vd = 0.7 V): Vo(cd) ≈ 10.8 V
    # ══════════════════════════════════════════════════════════════════════════
    r["Vo_dc"]   = (2.0 / np.pi) * r["Vm_red"]
    r["Io_dc"]   = r["Vo_dc"] / R

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 3 — VOLTAJE Y CORRIENTE RMS (SIN FILTRO)
    # ──────────────────────────────────────────────
    # La señal rectificada de onda completa v(t) = |Vm·sin(ωt)| tiene el mismo
    # valor eficaz (RMS) que la sinusoide original:
    #   Vo(rms) = Vm_red / √2
    # ESPERADO: Vo(rms) ≈ 11.0 V  (mayor que Vo(cd) ≈ 10.8 V)
    # ══════════════════════════════════════════════════════════════════════════
    r["Vo_rms"]  = r["Vm_red"] / np.sqrt(2.0)
    r["Io_rms"]  = r["Vo_rms"] / R

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 4 — FACTOR DE FORMA Y RIZO (SIN FILTRO)
    # ─────────────────────────────────────────────
    # Factor de forma FF = Vo(rms) / Vo(cd)
    #   Teórico ideal: FF = π / (2√2) ≈ 1.11
    #
    # Componente de rizo RMS:
    #   Vr(rms) = √[ Vo(rms)² − Vo(cd)² ]   (por definición de RMS)
    #
    # Factor de rizo FR = Vr(rms) / Vo(cd) = √(FF² − 1) ≈ 0.483 (48.3%)
    # ESPERADO SIN FILTRO: FR ≈ 48 %  → justifica la necesidad de filtros.
    # ══════════════════════════════════════════════════════════════════════════
    r["FF"]      = r["Vo_rms"] / r["Vo_dc"]
    r["Vr_rms"]  = np.sqrt(max(r["Vo_rms"]**2 - r["Vo_dc"]**2, 0.0))
    r["FR"]      = r["Vr_rms"] / r["Vo_dc"]   # adimensional

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 5 — PARÁMETROS DE LOS DIODOS
    # ───────────────────────────────────
    # En el puente Graetz, por cada semiciclo conducen DOS diodos, pero CADA
    # diodo individual conduce sólo durante su propio semiciclo (50% del ciclo).
    #
    # ID(prom) = Io(cd) / 2   (cada diodo "ve" la mitad del promedio)
    # ID(rms)  = Io(rms) / √2 (misma distribución 50/50)
    #
    # Tensión de pico inversa (VPR):
    #   Puente Graetz → VPR = Vm   (la más favorable: solo el pico del secundario)
    #   Tap central   → VPR = 2·Vm (el doble; favorece al puente)
    #
    # ESPERADO: VPR ≈ 17 V — el 1N4005 soporta 600 V (factor de seguridad ×35).
    # ══════════════════════════════════════════════════════════════════════════
    r["ID_prom"] = r["Io_dc"] / 2.0
    r["ID_rms"]  = r["Io_rms"] / np.sqrt(2.0)
    r["VPR"]     = r["Vm"]
    r["P_diodo"] = Vd * r["ID_prom"]         # W disipados por cada diodo

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 6 — POTENCIAS Y RENDIMIENTO
    # ──────────────────────────────────
    # Po(cd) = Vo(cd)² / R        potencia DC útil en la carga
    # Po(CA) = Vo(rms)² / R       potencia AC total entregada al circuito
    # η      = Po(cd)/Po(CA)×100  rendimiento (efficiency)
    #   Teórico onda completa ideal: η = 8/π² × 100 ≈ 81.1 %
    # ══════════════════════════════════════════════════════════════════════════
    r["Po_dc"]   = r["Vo_dc"]**2  / R
    r["Po_ca"]   = r["Vo_rms"]**2 / R
    r["eta"]     = (r["Po_dc"] / r["Po_ca"]) * 100.0   # %

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 7 — SERIE DE FOURIER DEL VOLTAJE DE SALIDA
    # ────────────────────────────────────────────────
    # La señal v_o(t) = |Vm·sin(ω₀t)| se representa como:
    #
    #   v_o(t) = Vo(dc) + Σ [−4·Vm/(π·(4n²−1))] · cos(2n·ω₀·t)   n = 1,2,3,…
    #
    # donde ω₀ = 2π·f_out y los armónicos ocurren a FRECUENCIAS PARES:
    #   n=1 → 2·f_out = 120 Hz   (armónico dominante)
    #   n=2 → 4·f_out = 240 Hz
    #   n=3 → 6·f_out = 360 Hz   … etc.
    #
    # El osciloscopio con FFT debe mostrar picos en 120, 240, 360, 480, 600 Hz.
    # ══════════════════════════════════════════════════════════════════════════
    N_HARM = 5
    r["fourier_freqs"] = [2.0 * (k + 1) * f  for k in range(N_HARM)]   # Hz
    r["fourier_amps"]  = [
        abs(4.0 * r["Vm_red"] / (np.pi * (4.0 * (k + 1)**2 - 1.0)))
        for k in range(N_HARM)
    ]                                                                     # V

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 8 — FILTRO INDUCTIVO R-L (atenuación de armónicos de corriente)
    # ──────────────────────────────────────────────────────────────────────
    # El inductor se conecta en SERIE con la carga. Su devanado tiene una
    # resistencia parásita RL, por lo que la resistencia total es RT = R + RL.
    #
    # Efecto en la componente DC:
    #   El inductor ideal no cae DC, pero RL sí lo hace:
    #   Io_dc_RL = Vo(cd) / RT
    #   V_carga  = Io_dc_RL × R   (solo la fracción sobre R llega a la carga)
    #   ESPERADO (L=1.5H, RL=40Ω, RT=50Ω): Io_dc_RL ≈ 0.198 A,  V_carga ≈ 1.98V
    #
    # Impedancia para el k-ésimo armónico de Fourier (a frecuencia n_k × f_out):
    #   ω_k  = n_k × ω_out = n_k × 2π × f_out   [rad/s]
    #   Zk   = √[ RT² + (n_k · ω_out · L)² ]
    #
    #   NOTA: el índice n_k corre 1, 2, 3,… mapeando las frecuencias 120, 240, 360 Hz.
    #   ω_out = 2π×120 rad/s → para n_k=1 (120 Hz): XL = 2π×120×1.5 = 1131 Ω
    #   Z1 = √(50² + 1131²) ≈ 1132 Ω   (coincide con el documento)
    #
    # Atenuación del armónico de corriente respecto al caso sin filtro (sólo R):
    #   aten_k = (In_con_L / In_sin_L) × 100 = (R / Zk) × 100 %
    #   Donde In_sin_L = Vn/R y In_con_L = Vn/Zk
    # ══════════════════════════════════════════════════════════════════════════
    w_out = 2.0 * np.pi * r["f_out"]
    r["RT"]        = RT
    r["Io_dc_RL"]  = r["Vo_dc"] / RT             # A  corriente DC con filtro RL
    r["V_carga_RL"]= r["Io_dc_RL"] * R            # V  voltaje solo sobre R (carga)
    r["Z_RL_arms"] = []
    r["IL_arms"]   = []
    r["aten_RL"]   = []
    for k in range(N_HARM):
        n_k  = k + 1
        Vn   = r["fourier_amps"][k]
        # Reactancia inductiva del armónico n_k·f_out:  XL = n_k·ω_out·L
        Zn   = np.sqrt(RT**2 + (n_k * w_out * L)**2)
        r["Z_RL_arms"].append(Zn)
        r["IL_arms"].append(Vn / Zn)
        r["aten_RL"].append(R / Zn * 100.0)   # % respecto a sin filtro (base=R)

    # Factor de rizo con filtro inductivo (inciso k, usando armónico n_k=1)
    # Ir(rms) ≈ I1/√2  (el armónico dominante es cuasisinusoidal)
    r["Ir_rms_RL"] = r["IL_arms"][0] / np.sqrt(2.0)
    r["FRi_RL"]    = (r["Ir_rms_RL"] / r["Io_dc_RL"]) * 100.0   # %

    # ══════════════════════════════════════════════════════════════════════════
    # PASO 9 — DISEÑO DEL FILTRO CAPACITIVO (FR_i ≤ 5 %)
    # ─────────────────────────────────────────────────────
    # Se retira el inductor y se coloca C en paralelo con R.
    #
    # Rizo pico a pico (modelado como descarga RC hasta el siguiente pico):
    #   Vr(pp) ≈ Vm_red / (f_out · C · R)
    #   (usa el voltaje de PICO disponible, no el promedio)
    #
    # Voltaje DC de salida real con filtro (desplazado medio rizo hacia abajo):
    #   Vo(dc)_C = Vm_red − Vr(pp)/2
    #   ESPERADO con C=2200µF: Vr(pp)≈5.89V, Vo(dc)_C≈12.63V
    #
    # Rizo RMS (onda triangular):
    #   Vr(rms)_C = Vr(pp) / (2√3)
    #
    # Factor de rizo con filtro:
    #   FRi = Vr(rms)_C / Vo(dc)_C × 100 %
    #   ESPERADO con C=2200µF: FRi ≈ 13.4 %  (≠ 5 %, no es suficiente)
    #
    # Capacitor mínimo para FRi ≤ 5 %:
    #   Planteando FR = Vr(pp)/(2√3) / [Vm_red − Vr(pp)/2] = FR_obj
    #   Sea x = 1/(f_out·R·C):  x / [2√3·(1−x/2)] = FR_obj
    #   Solución exacta:  x = 2√3·FR_obj / (1 + √3·FR_obj)
    #   C_min = 1 / (x · f_out · R)
    #   ESPERADO con FR_obj=5%: C_min ≈ 5229 µF → usar 5600 µF o 6800 µF comercial
    # ══════════════════════════════════════════════════════════════════════════
    r["Vr_pp"]    = r["Vm_red"] / (r["f_out"] * C * R)
    r["Vo_dc_C"]  = r["Vm_red"] - r["Vr_pp"] / 2.0
    r["Vr_rms_C"] = r["Vr_pp"] / (2.0 * np.sqrt(3.0))
    r["Ir_rms_C"] = r["Vr_rms_C"] / R
    r["FR_C"]     = r["Vr_rms_C"] / r["Vo_dc_C"]          # adimensional
    r["FRi"]      = r["FR_C"] * 100.0                      # %

    # C_min — solución exacta (no aproximación 1/(4√3·f·C·R))
    x_min         = 2.0 * np.sqrt(3.0) * FR_o / (1.0 + np.sqrt(3.0) * FR_o)
    r["C_min_uF"] = 1.0 / (x_min * r["f_out"] * R) * 1e6

    return r


# ─── CLASE PRINCIPAL: INTERFAZ GRÁFICA ────────────────────────────────────────

class App(tk.Tk):
    """Ventana principal de la calculadora de Práctica 1."""

    # Paleta oscura (estilo editor de código)
    BG_MAIN  = "#1e1e2e"
    BG_PANEL = "#2a2a3e"
    BG_TAB   = "#24243a"
    BG_ENTRY = "#313244"
    FG_TITLE = "#cdd6f4"
    FG_LABEL = "#a6adc8"
    FG_VALUE = "#89dceb"   # valor teórico calculado
    FG_EXP   = "#a6e3a1"   # pistas de dato experimental
    FG_WARN  = "#f38ba8"   # advertencia
    FG_STEP  = "#fab387"   # encabezado de paso
    ACCENT   = "#89b4fa"   # azul acento
    CLR      = {           # colores de gráficas
        "vs":   "#89b4fa",
        "rect": "#f38ba8",
        "filt": "#a6e3a1",
        "id":   "#fab387",
        "dc":   "#6c7086",
        "grid": "#313244",
        "zero": "#45475a",
    }

    def __init__(self):
        super().__init__()
        self.title(
            "Práctica 1 — Rectificadores Monofásicos | ITT · Diodos y Transistores"
        )
        self.configure(bg=self.BG_MAIN)
        self.geometry("1300x840")
        self.minsize(1050, 700)

        # Variables tkinter para cada parámetro de entrada
        self._params = {k: tk.DoubleVar(value=v) for k, v in DEFAULTS.items()}
        self._resultados: dict = {}

        self._build_styles()
        self._build_gui()
        self._calcular()

    # ── ESTILOS ttk ───────────────────────────────────────────────────────────
    def _build_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        s.configure("TNotebook",
                    background=self.BG_MAIN, borderwidth=0)
        s.configure("TNotebook.Tab",
                    background=self.BG_PANEL, foreground=self.FG_LABEL,
                    padding=[14, 6], font=("Consolas", 10, "bold"))
        s.map("TNotebook.Tab",
              background=[("selected", self.ACCENT)],
              foreground=[("selected", self.BG_MAIN)])
        s.configure("TFrame",     background=self.BG_PANEL)
        s.configure("TLabel",     background=self.BG_PANEL, foreground=self.FG_LABEL,
                    font=("Consolas", 9))
        s.configure("TEntry",     fieldbackground=self.BG_ENTRY,
                    foreground=self.FG_TITLE, insertcolor=self.FG_TITLE)
        s.configure("Treeview",   background=self.BG_MAIN, foreground=self.FG_LABEL,
                    rowheight=21, fieldbackground=self.BG_MAIN,
                    font=("Consolas", 9))
        s.configure("Treeview.Heading",
                    background=self.BG_PANEL, foreground=self.ACCENT,
                    font=("Consolas", 9, "bold"))
        s.configure("Calc.TButton",
                    background=self.ACCENT, foreground=self.BG_MAIN,
                    font=("Consolas", 10, "bold"), padding=8)
        s.map("Calc.TButton",
              background=[("active", "#7aa2f7")])
        s.configure("TScrollbar",
                    background=self.BG_PANEL, troughcolor=self.BG_MAIN,
                    arrowcolor=self.FG_LABEL)

    # ── CONSTRUCCIÓN PRINCIPAL ─────────────────────────────────────────────────
    def _build_gui(self):
        main = tk.Frame(self, bg=self.BG_MAIN)
        main.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        # Barra de título
        hdr = tk.Frame(main, bg=self.BG_MAIN)
        hdr.pack(fill=tk.X, pady=(0, 5))
        tk.Label(hdr,
                 text="PRÁCTICA 1  —  ANÁLISIS E IMPLEMENTACIÓN DE RECTIFICADORES MONOFÁSICOS",
                 bg=self.BG_MAIN, fg=self.FG_TITLE,
                 font=("Consolas", 12, "bold")).pack(side=tk.LEFT, padx=4)
        tk.Label(hdr, text="ITT · Electrónica · Diodos y Transistores",
                 bg=self.BG_MAIN, fg=self.FG_LABEL,
                 font=("Consolas", 9)).pack(side=tk.RIGHT, padx=6)

        # PanedWindow: panel izquierdo (entrada) | notebook derecho (resultados)
        paned = tk.PanedWindow(main, orient=tk.HORIZONTAL,
                               bg=self.BG_MAIN, sashwidth=5, sashrelief=tk.FLAT)
        paned.pack(fill=tk.BOTH, expand=True)

        # Panel izquierdo
        left = tk.Frame(paned, bg=self.BG_PANEL, width=270)
        left.pack_propagate(False)
        paned.add(left, minsize=240)
        self._build_input_panel(left)

        # Notebook derecho
        nb = ttk.Notebook(paned)
        paned.add(nb, minsize=720)
        self.nb = nb

        self._tab_calcs   = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_ondas   = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_fourier = tk.Frame(nb, bg=self.BG_TAB)
        self._tab_filtros = tk.Frame(nb, bg=self.BG_TAB)

        nb.add(self._tab_calcs,   text="  Cálculos por Pasos  ")
        nb.add(self._tab_ondas,   text="  Formas de Onda  ")
        nb.add(self._tab_fourier, text="  Serie de Fourier  ")
        nb.add(self._tab_filtros, text="  Diseño de Filtros  ")

        self._build_tab_calcs(self._tab_calcs)
        self._build_tab_ondas(self._tab_ondas)
        self._build_tab_fourier(self._tab_fourier)
        self._build_tab_filtros(self._tab_filtros)

    # ── PANEL DE ENTRADA ───────────────────────────────────────────────────────
    def _build_input_panel(self, parent):
        """Panel izquierdo con campos de entrada organizados por sección."""

        # Canvas con scroll para el panel largo
        canvas = tk.Canvas(parent, bg=self.BG_PANEL, highlightthickness=0)
        vsb    = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        inner = tk.Frame(canvas, bg=self.BG_PANEL)
        win_id = canvas.create_window((0, 0), window=inner, anchor=tk.NW)

        def _resize(e=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(win_id, width=canvas.winfo_width())

        inner.bind("<Configure>", _resize)
        canvas.bind("<Configure>", _resize)

        # Scroll con rueda del ratón
        def _scroll(e):
            canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        canvas.bind_all("<MouseWheel>", _scroll)

        # ── Título ─────────────────────────────────────────────────────────────
        tk.Label(inner, text="DATOS DE ENTRADA",
                 bg=self.BG_PANEL, fg=self.ACCENT,
                 font=("Consolas", 11, "bold")).pack(pady=(10, 0))
        tk.Label(inner, text="Sustituir con valores medidos\nen laboratorio y recalcular",
                 bg=self.BG_PANEL, fg="#585b70",
                 font=("Consolas", 7), justify=tk.CENTER).pack(pady=(0, 6))

        # ── Helper: sección con borde ──────────────────────────────────────────
        def seccion(titulo):
            frm = tk.LabelFrame(inner, text=f"  {titulo}  ",
                                bg=self.BG_PANEL, fg=self.ACCENT,
                                font=("Consolas", 9, "bold"),
                                bd=1, relief=tk.GROOVE)
            frm.pack(fill=tk.X, padx=8, pady=4)
            return frm

        # ── Helper: fila de entrada (label + Entry + unidad) ───────────────────
        def entry_row(frm, label, var, unit="", hint=""):
            row = tk.Frame(frm, bg=self.BG_PANEL)
            row.pack(fill=tk.X, padx=6, pady=2)
            tk.Label(row, text=label, bg=self.BG_PANEL, fg=self.FG_LABEL,
                     font=("Consolas", 9), width=9, anchor=tk.W).pack(side=tk.LEFT)
            ent = tk.Entry(row, textvariable=var,
                           bg=self.BG_ENTRY, fg=self.FG_TITLE,
                           insertbackground=self.FG_TITLE,
                           font=("Consolas", 9), width=9, relief=tk.FLAT)
            ent.pack(side=tk.LEFT, padx=4)
            tk.Label(row, text=unit, bg=self.BG_PANEL, fg=self.FG_STEP,
                     font=("Consolas", 9)).pack(side=tk.LEFT)
            if hint:
                tk.Label(frm, text=f"   ↑ {hint}",
                         bg=self.BG_PANEL, fg="#585b70",
                         font=("Consolas", 7)).pack(anchor=tk.W, padx=6)

        # ── Secciones de entrada ───────────────────────────────────────────────
        s1 = seccion("TRANSFORMADOR")
        entry_row(s1, "Vs_rms",  self._params["Vs_rms"],  "V",
                  "multímetro AC (secundario)")
        entry_row(s1, "f_red",   self._params["f_red"],   "Hz",
                  "osciloscopio → 1/T")

        s2 = seccion("DIODOS 1N4005")
        entry_row(s2, "Vd (c/u)", self._params["Vd"],     "V",
                  "multímetro modo diodo")
        tk.Label(s2, text="   (2 en serie por semiciclo → 2·Vd total)",
                 bg=self.BG_PANEL, fg="#585b70",
                 font=("Consolas", 7)).pack(anchor=tk.W, padx=6, pady=(0, 4))

        s3 = seccion("CARGA")
        entry_row(s3, "R_carga", self._params["R_carga"], "Ω",
                  "multímetro Ω (desconectado)")

        s4 = seccion("FILTRO INDUCTIVO")
        entry_row(s4, "L",       self._params["L_H"],     "H",
                  "puente LCR a 100 Hz")
        entry_row(s4, "RL",      self._params["RL_Ohm"],  "Ω",
                  "R devanado (LCR / multímetro)")

        s5 = seccion("FILTRO CAPACITIVO")
        entry_row(s5, "C",       self._params["C_uF"],    "µF",
                  "valor estándar instalado")
        entry_row(s5, "FR_obj",  self._params["FR_obj"],  "",
                  "objetivo (0.05 = 5 %)")

        # ── Botón calcular ─────────────────────────────────────────────────────
        tk.Frame(inner, height=8, bg=self.BG_PANEL).pack()
        ttk.Button(inner, text="⟳  CALCULAR TODO",
                   style="Calc.TButton",
                   command=self._calcular).pack(fill=tk.X, padx=12, pady=4)
        tk.Label(inner,
                 text="Cada vez que ingrese datos reales\npresione este botón para actualizar\ntodos los resultados y gráficas.",
                 bg=self.BG_PANEL, fg="#585b70",
                 font=("Consolas", 7), justify=tk.CENTER).pack(pady=(2, 12))

    # ── TAB 1: CÁLCULOS POR PASOS ─────────────────────────────────────────────
    def _build_tab_calcs(self, parent):
        """Tabla paso a paso: parámetro | fórmula | valor teórico | dónde medir."""
        tk.Label(parent,
                 text="ORDEN DE CÁLCULO — Puente Graetz / Rectificador de Onda Completa",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))
        tk.Label(parent,
                 text="Columna 'Teórico': valor calculado con los parámetros actuales. "
                      " Columna 'Experimental': anote el valor medido en laboratorio.",
                 bg=self.BG_TAB, fg=self.FG_LABEL,
                 font=("Consolas", 8)).pack(pady=(0, 4))

        cols = ("paso", "param", "formula", "teorico", "unidad", "donde_medir")
        frm  = tk.Frame(parent, bg=self.BG_TAB)
        frm.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

        vsb = ttk.Scrollbar(frm, orient=tk.VERTICAL)
        hsb = ttk.Scrollbar(frm, orient=tk.HORIZONTAL)
        tree = ttk.Treeview(frm, columns=cols, show="headings",
                            yscrollcommand=vsb.set, xscrollcommand=hsb.set,
                            height=30)
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        vsb.pack(side=tk.RIGHT,  fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        hdrs = [("paso",      "Paso",                   55,  tk.W),
                ("param",     "Parámetro",              115,  tk.W),
                ("formula",   "Fórmula",                305,  tk.W),
                ("teorico",   "Teórico",                 90,  tk.E),
                ("unidad",    "Unidad",                  55,  tk.W),
                ("donde_medir", "Dónde / cómo medir experimentalmente", 280, tk.W)]
        for col, text, w, anchor in hdrs:
            tree.heading(col, text=text, anchor=anchor)
            tree.column(col,  width=w, minwidth=40, anchor=anchor)

        tree.tag_configure("header",
                           background="#313244", foreground=self.FG_STEP,
                           font=("Consolas", 9, "bold"))
        tree.tag_configure("value",
                           background=self.BG_MAIN, foreground=self.FG_VALUE)
        tree.tag_configure("warn",
                           background=self.BG_MAIN, foreground=self.FG_WARN)

        self._tree_calcs = tree

    def _poblar_tabla_calcs(self):
        """Llena (o refresca) la tabla de cálculos con los resultados actuales."""
        r    = self._resultados
        tree = self._tree_calcs
        p    = {k: v.get() for k, v in self._params.items()}

        for item in tree.get_children():
            tree.delete(item)

        def h(paso, texto):
            tree.insert("", tk.END,
                        values=(paso, texto, "", "", "", ""),
                        tags=("header",))

        def v(paso, param, formula, val, unit, hint=""):
            s = f"{val:.5g}" if isinstance(val, float) else str(val)
            tree.insert("", tk.END,
                        values=(paso, param, formula, s, unit, hint),
                        tags=("value",))

        # ── PASO 1 ──────────────────────────────────────────────────────────────
        h("PASO 1", "▸ TRANSFORMADOR — Voltaje de pico del secundario")
        v("1.1", "Vm",
          "Vs_rms × √2",
          r["Vm"], "V",
          "← osciloscopio: medir Vpico en el secundario (canal CH1)")
        v("1.2", "Vm_red",
          "Vm − 2·Vd",
          r["Vm_red"], "V",
          "← Vm medido − 2 × Vd medido con multímetro")
        v("1.3", "f_out",
          "2 × f_red  (onda completa duplica la frecuencia)",
          r["f_out"], "Hz",
          "← osciloscopio: medir frecuencia de Vout (esperar ~120 Hz)")
        v("1.4", "T_out",
          "1 / f_out",
          r["T_out"] * 1e3, "ms",
          "← período de la señal rectificada")

        # ── PASO 2 ──────────────────────────────────────────────────────────────
        h("PASO 2", "▸ VOLTAJE Y CORRIENTE DC PROMEDIO — inciso a)")
        v("2.1", "Vo(cd)",
          "(2/π) × Vm_red",
          r["Vo_dc"], "V",
          "← osciloscopio: modo MEAN sobre Vout (o multímetro DC)")
        v("2.2", "Io(cd)",
          "Vo(cd) / R",
          r["Io_dc"], "A",
          "← sonda de efecto Hall: corriente promedio en la carga (inciso e)")

        # ── PASO 3 ──────────────────────────────────────────────────────────────
        h("PASO 3", "▸ VOLTAJE Y CORRIENTE RMS — sin filtro — inciso a)")
        v("3.1", "Vo(rms)",
          "Vm_red / √2",
          r["Vo_rms"], "V",
          "← osciloscopio: función RMS sobre Vout (modo AC)")
        v("3.2", "Io(rms)",
          "Vo(rms) / R",
          r["Io_rms"], "A",
          "← sonda de efecto Hall: corriente RMS en la carga (inciso e)")

        # ── PASO 4 ──────────────────────────────────────────────────────────────
        h("PASO 4", "▸ FACTOR DE FORMA Y RIZO — sin filtro — inciso a) y k)")
        v("4.1", "FF",
          "Vo(rms) / Vo(cd)   [ideal: π/(2√2) ≈ 1.11]",
          r["FF"], "—",
          "← calcular a partir de Vo(rms) y Vo(cd) medidos")
        v("4.2", "Vr(rms)",
          "√[ Vo(rms)² − Vo(cd)² ]",
          r["Vr_rms"], "V",
          "← osciloscopio: modo AC + RMS sobre Vout (rizo)")
        v("4.3", "FR",
          "√(FF²−1)  =  Vr(rms)/Vo(cd)",
          r["FR"], "—",
          f"← ~0.483 sin filtro (48.3 %) — muy alto, justifica filtros")
        v("4.4", "FR [%]",
          "FR × 100",
          r["FR"] * 100, "%",
          "← medir Ir(rms) y calcular Ir(rms)/Vo(cd) × 100 (inciso k)")

        # ── PASO 5 ──────────────────────────────────────────────────────────────
        h("PASO 5", "▸ PARÁMETROS DE LOS DIODOS — inciso a)")
        v("5.1", "ID(prom)",
          "Io(cd) / 2   [cada diodo conduce 50% del ciclo]",
          r["ID_prom"], "A",
          "← medir con sonda Hall en serie con D1 (semiciclo positivo)")
        v("5.2", "ID(rms)",
          "Io(rms) / √2",
          r["ID_rms"], "A",
          "← función RMS de la corriente de D1 en el osciloscopio")
        v("5.3", "VPR",
          "Vm   [puente Graetz: VPR = Vm, no 2Vm como en tap central]",
          r["VPR"], "V",
          "← osciloscopio: tensión inversa sobre D2 durante semiciclo +")
        v("5.4", "P_diodo",
          "Vd × ID(prom)   [por cada diodo]",
          r["P_diodo"], "W",
          "← potencia disipada por diodo (para verificar disipador)")

        # ── PASO 6 ──────────────────────────────────────────────────────────────
        h("PASO 6", "▸ POTENCIAS Y RENDIMIENTO — inciso a)")
        v("6.1", "Po(cd)",
          "Vo(cd)² / R   =   Vo(cd)·Io(cd)",
          r["Po_dc"], "W",
          "← potencia DC útil entregada a la carga")
        v("6.2", "Po(CA)",
          "Vo(rms)² / R   =   Vo(rms)·Io(rms)",
          r["Po_ca"], "W",
          "← potencia AC total entregada por el rectificador")
        v("6.3", "η",
          "Po(cd)/Po(CA)×100   [ideal onda completa: 81.1 %]",
          r["eta"], "%",
          "← calcular con valores medidos de voltaje y corriente")

        # ── PASO 7 ──────────────────────────────────────────────────────────────
        h("PASO 7", "▸ SERIE DE FOURIER de vo(t) — incisos f) y g)")
        lbl_n = ["2f₀", "4f₀", "6f₀", "8f₀", "10f₀"]
        for k in range(5):
            nk  = k + 1
            fq  = r["fourier_freqs"][k]
            amp = r["fourier_amps"][k]
            tree.insert("", tk.END, values=(
                f"7.{k+1}",
                f"a_{2*nk}  ({lbl_n[k]})",
                f"4·Vm_red / [π·(4n²−1)],  n={nk}",
                f"{amp:.5g}",
                "V",
                f"← FFT osciloscopio: pico a {fq:.0f} Hz (inciso f)"
            ), tags=("value",))

        # ── PASO 8 ──────────────────────────────────────────────────────────────
        h("PASO 8", "▸ FILTRO INDUCTIVO R-L — atenuación de armónicos de corriente — incisos i) j) k)")
        v("8.0", "RT",
          "R + R_L   (resistencia total con inductor)",
          r["RT"], "Ω",
          f"← R={p['R_carga']:.1f}Ω + R_L={p['RL_Ohm']:.1f}Ω  (medir R_L con LCR/multímetro)")
        v("8.1", "Io(dc)_RL",
          "Vo(cd) / RT   [DC se distribuye en todo RT]",
          r["Io_dc_RL"], "A",
          "← corriente DC reducida por RL del devanado (sonda Hall, modo DC)")
        v("8.2", "V_carga_RL",
          "Io(dc)_RL × R   [voltaje efectivo sobre la carga]",
          r["V_carga_RL"], "V",
          "← medir con multímetro DC o osciloscopio en modo DC sobre R")
        for k in range(5):
            nk   = k + 1
            fq   = r["fourier_freqs"][k]
            zn   = r["Z_RL_arms"][k]
            il   = r["IL_arms"][k]
            atn  = r["aten_RL"][k]
            tree.insert("", tk.END, values=(
                f"8.{k+3}",
                f"|Z_{2*nk}|  ({lbl_n[k]})",
                f"sqrt(RT^2+(n*w_out*L)^2), n={nk}",
                f"{zn:.4g}",
                "Ω",
                f"arm. {2*nk} → I={il*1e3:.2f}mA  ({atn:.1f}% del caso sin filtro)"
            ), tags=("value",))
        v("8.8", "Ir(rms)_RL",
          "I_arm1 / √2   (arm. dominante 120 Hz)",
          r["Ir_rms_RL"] * 1e3, "mA",
          "← osciloscopio modo AC: corriente de rizo (inciso k)")
        v("8.9", "FRi_RL",
          "Ir(rms)_RL / Io(dc)_RL × 100",
          r["FRi_RL"], "%",
          "← factor de rizo con filtro inductivo (comparar con FR sin filtro ≈48%)")

        # ── PASO 9 ──────────────────────────────────────────────────────────────
        h("PASO 9", "▸ FILTRO CAPACITIVO — diseño FR_i ≤ 5 % — incisos k) y l)")
        v("9.1", "C_min",
          "sol. exacta: x=2√3·FR_obj/(1+√3·FR_obj), C=1/(x·f_out·R)",
          r["C_min_uF"], "µF",
          "← usar valor estándar ≥ C_min (ej. 5600/6800 µF o 3×2200 µF en paralelo)")
        v("9.2", "Vr(pp)",
          "Vm_red / (f_out·C·R)",
          r["Vr_pp"], "V",
          "← osciloscopio modo AC: medir pico a pico del rizo (inciso k)")
        v("9.3", "Vo(dc)_C",
          "Vm_red − Vr(pp)/2",
          r["Vo_dc_C"], "V",
          "← multímetro DC o osciloscopio modo DC sobre Vout con C instalado")
        v("9.4", "Vr(rms)_C",
          "Vr(pp) / (2√3)",
          r["Vr_rms_C"], "V",
          "← osciloscopio modo AC+RMS: rizo sobre la carga")
        v("9.5", "Ir(rms)_C",
          "Vr(rms)_C / R",
          r["Ir_rms_C"], "A",
          "← sonda Hall modo AC: corriente RMS de rizo")
        v("9.6", "FRi",
          "Vr(rms)_C / Vo(dc)_C × 100  [objetivo ≤ 5 %]",
          r["FRi"], "%",
          "← calcular con valores medidos; debe ser ≤ 5 % con C_min")

        # Advertencia si FRi > 5 %
        if r["FRi"] > 5.5:
            tree.insert("", tk.END, values=(
                "!!", "ADVERTENCIA",
                f"FRi = {r['FRi']:.2f}% > 5% — capacitor insuficiente",
                f"{r['FRi']:.2f}", "%",
                f"← aumentar C a ≥ {r['C_min_uF']:.0f} µF para cumplir objetivo"
            ), tags=("warn",))

    # ── TAB 2: FORMAS DE ONDA ─────────────────────────────────────────────────
    def _build_tab_ondas(self, parent):
        tk.Label(parent,
                 text="FORMAS DE ONDA — Puente Graetz (señales teóricas con parámetros actuales)",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))
        tk.Label(parent,
                 text="Compararlas con las obtenidas en el osciloscopio (incisos c, d, e, g, h).",
                 bg=self.BG_TAB, fg=self.FG_LABEL,
                 font=("Consolas", 8)).pack(pady=(0, 4))

        self._fig_ondas = Figure(figsize=(10, 7.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_ondas, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_ondas = c

    def _actualizar_ondas(self):
        r   = self._resultados
        p   = {k: v.get() for k, v in self._params.items()}
        fig = self._fig_ondas
        fig.clear()

        f   = p["f_red"]
        R   = p["R_carga"]
        C   = p["C_uF"] * 1e-6
        Vm  = r["Vm"]
        Vmr = r["Vm_red"]
        Vd  = p["Vd"]

        # Señales temporales (4 ciclos completos de la red)
        t      = np.linspace(0, 4.0 / f, 5000)
        t_ms   = t * 1e3
        omega  = 2.0 * np.pi * f
        vs     = Vm  * np.sin(omega * t)                        # secundario
        v_rect = np.maximum(np.abs(vs) - 2.0 * Vd, 0.0)        # puente Graetz

        # Filtrado capacitivo (simulación muestra a muestra)
        v_fc  = np.zeros_like(t)
        v_cap = v_rect[0]
        dt    = t[1] - t[0]
        tau   = R * C
        for i in range(len(t)):
            if v_rect[i] >= v_cap:
                v_cap = v_rect[i]
            else:
                v_cap *= np.exp(-dt / tau)
            v_fc[i] = v_cap

        # Corriente en la carga (sin filtro)
        i_carga = v_rect / R

        # Corriente diodo D1 (conduce en semiciclo positivo de vs)
        i_D1 = np.where(vs >= 0, i_carga, 0.0)

        # Corriente en la carga con filtro inductivo
        # Reconstrucción armónica: Io_dc_RL + Σ In_RL·cos(n_k·w_out·t + φn)
        # Donde Zn = √(RT²+(n_k·w_out·L)²) y φn = −atan(n_k·w_out·L / RT)
        RT    = p["R_carga"] + p["RL_Ohm"]
        w_out = 2.0 * np.pi * r["f_out"]
        i_RL  = np.full_like(t, r["Io_dc_RL"])   # DC reducido por RL del devanado
        for k in range(5):
            nk   = k + 1
            Vn   = r["fourier_amps"][k]
            XL   = nk * w_out * p["L_H"]         # reactancia: n·ω_out·L  (NO 2·n·ω)
            Zn   = np.sqrt(RT**2 + XL**2)
            phi  = -np.arctan2(XL, RT)
            coef = -4.0 * Vmr / (np.pi * (4.0 * nk**2 - 1.0))
            In   = (coef / Zn if Zn > 0 else 0.0)
            i_RL += In * np.cos(nk * w_out * t + phi)

        # ── Subplots ─────────────────────────────────────────────────────────
        axs = fig.subplots(4, 1, sharex=True)
        fig.subplots_adjust(hspace=0.45, left=0.07, right=0.97,
                            top=0.95, bottom=0.07)

        lw   = 1.8
        clr  = self.CLR

        def _ax_fmt(ax, title):
            ax.set_facecolor(self.BG_MAIN)
            ax.tick_params(colors="#6c7086", labelsize=8)
            for sp in ax.spines.values():
                sp.set_color("#45475a")
            ax.set_title(title, color=self.FG_STEP, fontsize=9,
                         fontfamily="Consolas", pad=3)
            ax.set_ylabel("V / A", color="#6c7086", fontsize=8)
            ax.grid(True, color=clr["grid"], linewidth=0.5, linestyle=":")
            ax.axhline(0, color=clr["zero"], linewidth=0.7)

        def _leg(ax):
            ax.legend(loc="upper right", fontsize=7,
                      facecolor="#313244", labelcolor=self.FG_LABEL,
                      edgecolor="#45475a")

        # AX0 — Secundario del transformador
        axs[0].plot(t_ms, vs, color=clr["vs"], lw=lw,
                    label=f"vs(t)   Vm = {Vm:.2f} V  |  Vs_rms = {p['Vs_rms']:.1f} V")
        axs[0].axhline(r["Vo_dc"], ls="--", color=clr["dc"], lw=1.0,
                       label=f"Vo(dc) = {r['Vo_dc']:.3f} V")
        _ax_fmt(axs[0], "vs(t) — Secundario transformador  [inciso c]")
        _leg(axs[0])

        # AX1 — Salida rectificada sin filtro
        axs[1].plot(t_ms, v_rect, color=clr["rect"], lw=lw,
                    label=f"v_rect(t)   f_out = {r['f_out']:.0f} Hz")
        axs[1].axhline(r["Vo_dc"], ls="--", color=clr["dc"], lw=1.0,
                       label=f"Vo(cd) = {r['Vo_dc']:.3f} V")
        _ax_fmt(axs[1], "v_rect(t) — Salida rectificada sin filtro  [incisos c, f]")
        _leg(axs[1])

        # AX2 — Salida con filtro capacitivo
        axs[2].plot(t_ms, v_rect, color=clr["rect"],  lw=0.9,
                    ls="--", alpha=0.4, label="v_rect (sin filtro)")
        axs[2].plot(t_ms, v_fc,   color=clr["filt"],  lw=lw,
                    label=f"v_filt_C(t)  C={p['C_uF']:.0f} µF  "
                          f"FRi={r['FRi']:.1f}%")
        axs[2].axhline(r["Vo_dc_C"], ls="--", color=clr["dc"], lw=1.0,
                       label=f"Vo_dc_C = {r['Vo_dc_C']:.3f} V")
        _ax_fmt(axs[2],
                f"v_filt_C(t) — Con filtro capacitivo  [incisos l, m]  "
                f"FRi = {r['FRi']:.1f} %  (obj ≤ {p['FR_obj']*100:.0f} %)")
        _leg(axs[2])

        # AX3 — Is secundario: sin y con inductor
        axs[3].plot(t_ms, i_carga, color=clr["vs"],  lw=0.9,
                    ls="--", alpha=0.5, label="Is(t) sin inductor")
        axs[3].plot(t_ms, i_RL,    color=clr["id"],  lw=lw,
                    label=f"Is(t) con L={p['L_H']:.2f}H, RL={p['RL_Ohm']:.0f}Ω")
        axs[3].axhline(r["Io_dc_RL"], ls="--", color=clr["dc"], lw=1.0,
                       label=f"Io(dc)_RL = {r['Io_dc_RL']:.3f} A  (vs {r['Io_dc']:.3f}A sin L)")
        axs[3].set_xlabel("Tiempo [ms]", color="#6c7086", fontsize=8)
        _ax_fmt(axs[3],
                "is(t) — Corriente secundario: sin / con inductor L  [incisos h, i, j]")
        _leg(axs[3])

        self._canvas_ondas.draw()

    # ── TAB 3: SERIE DE FOURIER ───────────────────────────────────────────────
    def _build_tab_fourier(self, parent):
        tk.Label(parent,
                 text="SERIE DE FOURIER — Espectro del voltaje de salida vo(t)",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))
        tk.Label(parent,
                 text="Izq: señal real vs reconstrucción armónica  |  "
                      "Der: espectro de amplitudes (comparar con FFT del osciloscopio, inciso f)",
                 bg=self.BG_TAB, fg=self.FG_LABEL,
                 font=("Consolas", 8)).pack(pady=(0, 4))

        self._fig_fourier = Figure(figsize=(10, 4.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_fourier, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_fourier = c

        # Tabla de armónicos
        tk.Label(parent,
                 text="Primeros 5 armónicos del voltaje de salida (verificar con FFT del osciloscopio, inciso f):",
                 bg=self.BG_TAB, fg=self.ACCENT,
                 font=("Consolas", 9, "bold")).pack(anchor=tk.W, padx=10, pady=(6, 0))

        cols = ("n", "freq", "amp_V", "pct_dc", "hint")
        tree = ttk.Treeview(parent, columns=cols, show="headings", height=5)
        for col, heading, w, anc in [
            ("n",      "Armónico",             110, tk.W),
            ("freq",   "Frecuencia",            110, tk.E),
            ("amp_V",  "Amplitud [V]",          110, tk.E),
            ("pct_dc", "% de Vo(dc)",           100, tk.E),
            ("hint",   "Verificar con FFT del osciloscopio", 380, tk.W),
        ]:
            tree.heading(col, text=heading, anchor=anc)
            tree.column(col, width=w, minwidth=40, anchor=anc)
        tree.tag_configure("arm",
                           background=self.BG_MAIN, foreground=self.FG_VALUE)
        tree.pack(fill=tk.X, padx=8, pady=(2, 6))
        self._tree_fourier = tree

    def _actualizar_fourier(self):
        r   = self._resultados
        p   = {k: v.get() for k, v in self._params.items()}
        fig = self._fig_fourier
        fig.clear()

        f    = p["f_red"]
        Vmr  = r["Vm_red"]
        t    = np.linspace(0, 4.0 / f, 5000)
        t_ms = t * 1e3
        w    = 2.0 * np.pi * f

        # Señal real y reconstrucción por Fourier (N=10 armónicos)
        v_real    = np.abs(Vmr * np.sin(w * t))
        v_fourier = np.full_like(t, r["Vo_dc"])
        for n in range(1, 11):
            coef = -4.0 * Vmr / (np.pi * (4.0 * n**2 - 1.0))
            v_fourier += coef * np.cos(2.0 * n * w * t)

        freqs = r["fourier_freqs"]
        amps  = r["fourier_amps"]

        ax1, ax2 = fig.subplots(1, 2)
        fig.subplots_adjust(left=0.07, right=0.97, top=0.88,
                            bottom=0.13, wspace=0.32)

        BG = self.BG_MAIN
        for ax in (ax1, ax2):
            ax.set_facecolor(BG)
            ax.tick_params(colors="#6c7086", labelsize=8)
            for sp in ax.spines.values():
                sp.set_color("#45475a")
            ax.grid(True, color=self.CLR["grid"], linewidth=0.5, linestyle=":")

        # Izquierda: reconstrucción
        ax1.plot(t_ms, v_real,    color=self.CLR["rect"], lw=1.2,
                 ls="--", alpha=0.7, label="|vs| real")
        ax1.plot(t_ms, v_fourier, color=self.CLR["filt"], lw=1.8,
                 label="Fourier N=10 arm.")
        ax1.axhline(r["Vo_dc"], color=self.CLR["dc"], lw=1.0, ls=":",
                    label=f"Vo(dc) = {r['Vo_dc']:.3f} V")
        ax1.set_title("Señal real vs reconstrucción de Fourier",
                      color=self.FG_STEP, fontsize=9, fontfamily="Consolas")
        ax1.set_xlabel("Tiempo [ms]", color="#6c7086", fontsize=8)
        ax1.set_ylabel("Voltaje [V]", color="#6c7086", fontsize=8)
        ax1.legend(loc="upper right", fontsize=7, facecolor="#313244",
                   labelcolor=self.FG_LABEL, edgecolor="#45475a")

        # Derecha: espectro de barras
        colores = ["#89b4fa", "#a6e3a1", "#fab387", "#f38ba8", "#cba6f7"]
        ax2.bar([0], [r["Vo_dc"]], color="#6c7086", width=12,
                alpha=0.85, label=f"DC  {r['Vo_dc']:.2f} V")
        for k, (fk, ak) in enumerate(zip(freqs, amps)):
            ax2.bar([fk], [ak], color=colores[k], width=12, alpha=0.85,
                    label=f"{fk:.0f} Hz  {ak:.3f} V")
        ax2.set_title("Espectro de amplitudes  [comparar con FFT]",
                      color=self.FG_STEP, fontsize=9, fontfamily="Consolas")
        ax2.set_xlabel("Frecuencia [Hz]", color="#6c7086", fontsize=8)
        ax2.set_ylabel("Amplitud [V]",    color="#6c7086", fontsize=8)
        ax2.legend(loc="upper right", fontsize=7, facecolor="#313244",
                   labelcolor=self.FG_LABEL, edgecolor="#45475a")
        ax2.set_xlim(-20, max(freqs) * 1.15)
        ax2.set_xticks([0] + list(freqs))
        ax2.set_xticklabels(["0"] + [f"{fk:.0f}" for fk in freqs],
                             rotation=30, fontsize=7)

        self._canvas_fourier.draw()

        # Tabla de armónicos
        tree = self._tree_fourier
        for item in tree.get_children():
            tree.delete(item)
        lbl5 = ["2f₀ (fund. salida)", "4f₀", "6f₀", "8f₀", "10f₀"]
        for k, (fk, ak) in enumerate(zip(freqs, amps)):
            pct = ak / r["Vo_dc"] * 100.0
            tree.insert("", tk.END, values=(
                lbl5[k],
                f"{fk:.0f} Hz",
                f"{ak:.5g} V",
                f"{pct:.2f} %",
                f"← buscar pico FFT en osciloscopio a {fk:.0f} Hz (inciso f)"
            ), tags=("arm",))

    # ── TAB 4: DISEÑO DE FILTROS ──────────────────────────────────────────────
    def _build_tab_filtros(self, parent):
        tk.Label(parent,
                 text="DISEÑO DE FILTROS PASIVOS — Reducción del factor de rizo",
                 bg=self.BG_TAB, fg=self.FG_TITLE,
                 font=("Consolas", 10, "bold")).pack(pady=(8, 2))
        tk.Label(parent,
                 text="Izq: factor de rizo FR vs capacitancia C  |  "
                      "Der: atenuación de armónicos de corriente vs inductancia L",
                 bg=self.BG_TAB, fg=self.FG_LABEL,
                 font=("Consolas", 8)).pack(pady=(0, 4))

        self._fig_filtros = Figure(figsize=(10, 4.5), facecolor=self.BG_MAIN)
        c = FigureCanvasTkAgg(self._fig_filtros, master=parent)
        c.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=6, pady=2)
        tf = tk.Frame(parent, bg=self.BG_TAB)
        tf.pack(fill=tk.X, padx=6)
        NavigationToolbar2Tk(c, tf)
        self._canvas_filtros = c

        self._lbl_filtros_res = tk.Label(
            parent, text="", bg=self.BG_TAB, fg=self.FG_VALUE,
            font=("Consolas", 9), justify=tk.LEFT)
        self._lbl_filtros_res.pack(anchor=tk.W, padx=12, pady=(4, 6))

    def _actualizar_filtros(self):
        r   = self._resultados
        p   = {k: v.get() for k, v in self._params.items()}
        fig = self._fig_filtros
        fig.clear()

        f_out = r["f_out"]
        R     = p["R_carga"]
        RL    = p["RL_Ohm"]
        RT    = R + RL
        L     = p["L_H"]
        C_act = p["C_uF"] * 1e-6
        FR_o  = p["FR_obj"]
        w_out = 2.0 * np.pi * f_out

        # Curva FR(C): usando la fórmula correcta Vm_red/(f_out·R·C) (no 1/(4√3·f·C·R))
        # FR = [Vm_red/(f_out·R·C)/(2√3)] / [Vm_red − Vm_red/(2·f_out·R·C)]
        # Sea x = 1/(f_out·R·C): FR(x) = x / (2√3·(1−x/2))
        C_arr = np.logspace(2, 5, 600) * 1e-6     # 100 µF … 100 000 µF
        x_arr = 1.0 / (f_out * R * C_arr)
        FR_arr = (x_arr / (2.0 * np.sqrt(3.0) * (1.0 - x_arr / 2.0))) * 100.0  # %
        FR_arr = np.clip(FR_arr, 0, 200)

        # Curva atenuación [%] vs L para cada armónico: usando RT y Zn=√(RT²+(n·w_out·L)²)
        # Referencia sin filtro: In_0 = Vn/R;  Con filtro: In = Vn/Zn;  aten = R/Zn × 100%
        L_arr   = np.logspace(-3, 0, 500)   # 1 mH … 1 H
        n_arms  = [1, 2, 3, 4, 5]
        colores = ["#89b4fa", "#a6e3a1", "#fab387", "#f38ba8", "#cba6f7"]

        ax1, ax2 = fig.subplots(1, 2)
        fig.subplots_adjust(left=0.08, right=0.97, top=0.88,
                            bottom=0.13, wspace=0.32)

        for ax in (ax1, ax2):
            ax.set_facecolor(self.BG_MAIN)
            ax.tick_params(colors="#6c7086", labelsize=8)
            for sp in ax.spines.values():
                sp.set_color("#45475a")
            ax.grid(True, color=self.CLR["grid"], linewidth=0.5, linestyle=":")

        # ── Izquierda: FR vs C ────────────────────────────────────────────────
        ax1.semilogx(C_arr * 1e6, FR_arr, color="#89b4fa", lw=2.0,
                     label="FR(C)")
        ax1.axhline(FR_o * 100, color=self.CLR["rect"], lw=1.5, ls="--",
                    label=f"Objetivo FR = {FR_o*100:.0f}%")
        ax1.axvline(r["C_min_uF"], color="#fab387", lw=1.5, ls=":",
                    label=f"C_min = {r['C_min_uF']:.0f} µF")
        ax1.axvline(p["C_uF"], color=self.CLR["filt"], lw=1.5, ls="-.",
                    label=f"C_actual = {p['C_uF']:.0f} µF → {r['FR_C']*100:.1f}%")
        ax1.set_xlabel("Capacitancia C [µF]", color="#6c7086", fontsize=8)
        ax1.set_ylabel("Factor de rizo FR [%]", color="#6c7086", fontsize=8)
        ax1.set_title(
            f"FR vs C  (f_out={f_out:.0f} Hz, R={R:.0f} Ω)",
            color=self.FG_STEP, fontsize=9, fontfamily="Consolas")
        ax1.legend(fontsize=7, facecolor="#313244",
                   labelcolor=self.FG_LABEL, edgecolor="#45475a")
        ax1.set_ylim(0, min(80, FR_arr[0] * 1.1))

        # ── Derecha: atenuación corriente por armónico vs L ───────────────────
        for k, nk in enumerate(n_arms):
            # Zn = √(RT² + (n_k·ω_out·L)²)  donde n_k mapea arm. 2,4,6,8,10
            Zn_arr   = np.sqrt(RT**2 + (nk * w_out * L_arr)**2)
            aten_arr = R / Zn_arr * 100.0   # % vs sin inductor (base = solo R)
            ax2.semilogx(L_arr * 1e3, aten_arr, color=colores[k], lw=1.8,
                         label=f"arm. {2*nk}  ({2*nk*f_out:.0f} Hz)")
        ax2.axvline(L * 1e3, color="white", lw=1.5, ls="--",
                    label=f"L = {L:.2f} H  ({L*1e3:.1f} mH)")
        ax2.set_xlabel("Inductancia L [mH]", color="#6c7086", fontsize=8)
        ax2.set_ylabel("I_arm / I_arm_sin_L [%]", color="#6c7086", fontsize=8)
        ax2.set_title(
            "Atenuación de corriente armónica\nvs inductancia del filtro",
            color=self.FG_STEP, fontsize=9, fontfamily="Consolas")
        ax2.legend(fontsize=7, facecolor="#313244",
                   labelcolor=self.FG_LABEL, edgecolor="#45475a")
        ax2.set_ylim(0, 105)

        self._canvas_filtros.draw()

        # Resumen textual
        Z1   = np.sqrt(RT**2 + (1.0 * w_out * L)**2)   # armónico fund. 120Hz con RT
        at1  = R / Z1 * 100.0
        self._lbl_filtros_res.config(text=(
            f"  Resumen:  "
            f"C_min = {r['C_min_uF']:.0f} µF  |  "
            f"Con C = {p['C_uF']:.0f} µF → FRi = {r['FRi']:.1f} %  |  "
            f"L = {L:.2f} H, RL = {RL:.0f} Ω, RT = {RT:.0f} Ω  |  "
            f"arm. fund. (120Hz) llega al {at1:.2f} % (Io_dc_RL = {r['Io_dc_RL']:.3f} A)"
        ))

    # ── ACCIÓN: CALCULAR TODO ─────────────────────────────────────────────────
    def _calcular(self):
        """Lee parámetros de los campos, ejecuta los 9 pasos y actualiza todos los tabs."""
        try:
            p = {k: v.get() for k, v in self._params.items()}
            # Validaciones básicas
            if p["Vs_rms"] <= 0 or p["R_carga"] <= 0 or p["C_uF"] <= 0:
                messagebox.showerror("Parámetro inválido",
                                     "Vs_rms, R_carga y C_uF deben ser > 0.")
                return
            if p["Vd"] < 0 or p["Vd"] >= p["Vs_rms"]:
                messagebox.showerror("Parámetro inválido",
                                     "Vd debe ser ≥ 0 y menor que Vs_rms.")
                return

            self._resultados = calcular_todo(p)
            self._poblar_tabla_calcs()
            self._actualizar_ondas()
            self._actualizar_fourier()
            self._actualizar_filtros()

        except Exception as exc:
            import traceback
            messagebox.showerror(
                "Error de cálculo",
                f"Revise los parámetros de entrada:\n\n{exc}\n\n"
                + traceback.format_exc()
            )


# ─── PUNTO DE ENTRADA ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()
