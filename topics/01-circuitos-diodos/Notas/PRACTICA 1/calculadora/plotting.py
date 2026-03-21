"""
plotting.py — Visualizaciones para rectificadores monofasicos
==============================================================================
Modulo de graficacion backend-agnostico.
NO configura el backend de matplotlib - el caller debe hacerlo antes de importar.

Funciones de graficacion:
  - plot_waveforms: Formas de onda (vs, rectificada, filtrada, corriente)
  - plot_fourier: Serie de Fourier y espectro
  - plot_filter_design: Curvas de diseno de filtros
  - save_all_figures: Genera y guarda todas las figuras

::SCRIPT_METADATA::
script_id    : practica1-plotting
module       : DIO
generates    : figuras matplotlib (PNG o interactivas)
referenced_by: calculadora/run_headless.py, calculadora/ui_tkinter.py
last_updated : 2026-03-21
"""

import numpy as np
from typing import Optional, Tuple
from matplotlib.figure import Figure
from matplotlib.axes import Axes

# Importar core para usar las funciones de generacion de senales
# Soporta tanto import relativo (como paquete) como absoluto (script directo)
try:
    from . import core
except ImportError:
    import core


# =============================================================================
# PALETA DE COLORES (ESTILO OSCURO)
# =============================================================================

class ColorPalette:
    """Colores consistentes para todas las graficas."""

    BG_MAIN = "#1e1e2e"
    BG_PANEL = "#2a2a3e"
    FG_TITLE = "#cdd6f4"
    FG_LABEL = "#a6adc8"
    FG_VALUE = "#89dceb"
    FG_STEP = "#fab387"
    ACCENT = "#89b4fa"

    # Colores para trazas
    VS = "#89b4fa"       # Azul - secundario
    RECT = "#f38ba8"     # Rosa - rectificada
    FILT = "#a6e3a1"     # Verde - filtrada
    ID = "#fab387"       # Naranja - corriente
    DC = "#6c7086"       # Gris - linea DC
    GRID = "#313244"     # Grid oscuro
    ZERO = "#45475a"     # Linea cero

    # Colores para armonicos
    HARMONICS = ["#89b4fa", "#a6e3a1", "#fab387", "#f38ba8", "#cba6f7"]


COLORS = ColorPalette()


# =============================================================================
# FUNCIONES DE CONFIGURACION DE EJES
# =============================================================================

def setup_dark_axis(ax: Axes, title: str = "", ylabel: str = "V / A") -> None:
    """Configura un eje con estilo oscuro."""
    ax.set_facecolor(COLORS.BG_MAIN)
    ax.tick_params(colors="#6c7086", labelsize=8)
    for sp in ax.spines.values():
        sp.set_color("#45475a")
    if title:
        ax.set_title(title, color=COLORS.FG_STEP, fontsize=9,
                     fontfamily="monospace", pad=3)
    ax.set_ylabel(ylabel, color="#6c7086", fontsize=8)
    ax.grid(True, color=COLORS.GRID, linewidth=0.5, linestyle=":")
    ax.axhline(0, color=COLORS.ZERO, linewidth=0.7)


def add_legend(ax: Axes, loc: str = "upper right") -> None:
    """Agrega leyenda con estilo oscuro."""
    ax.legend(loc=loc, fontsize=7, facecolor="#313244",
              labelcolor=COLORS.FG_LABEL, edgecolor="#45475a")


# =============================================================================
# PLOT DE FORMAS DE ONDA
# =============================================================================

def plot_waveforms(fig: Figure, params: core.InputParams,
                   results: core.CalcResults) -> None:
    """
    Grafica las formas de onda del rectificador.

    4 subplots:
      1. Secundario del transformador
      2. Salida rectificada sin filtro
      3. Salida con filtro capacitivo
      4. Corriente secundario: sin/con inductor

    Parameters
    ----------
    fig : Figure
        Figura de matplotlib (ya creada)
    params : InputParams
        Parametros del circuito
    results : CalcResults
        Resultados de calculo
    """
    fig.set_facecolor(COLORS.BG_MAIN)

    # Generar senales temporales
    t = core.generate_time_array(params.f_red, n_cycles=4, n_points=5000)
    t_ms = t * 1e3

    vs = core.generate_secondary_voltage(t, results.Vm, params.f_red)
    v_rect = core.generate_rectified_voltage(t, results.Vm_red, params.f_red, params.Vd)
    v_fc = core.generate_capacitor_filtered(t, v_rect, params.R_carga, params.C_uF * 1e-6)
    i_carga = v_rect / params.R_carga
    i_RL = core.generate_inductor_filtered_current(t, results, params)

    # Crear subplots
    axs = fig.subplots(4, 1, sharex=True)
    fig.subplots_adjust(hspace=0.45, left=0.07, right=0.97, top=0.95, bottom=0.07)

    lw = 1.8

    # AX0 - Secundario del transformador
    axs[0].plot(t_ms, vs, color=COLORS.VS, lw=lw,
                label=f"vs(t)   Vm = {results.Vm:.2f} V  |  Vs_rms = {params.Vs_rms:.1f} V")
    axs[0].axhline(results.Vo_dc, ls="--", color=COLORS.DC, lw=1.0,
                   label=f"Vo(dc) = {results.Vo_dc:.3f} V")
    setup_dark_axis(axs[0], "vs(t) — Secundario transformador  [inciso c]")
    add_legend(axs[0])

    # AX1 - Salida rectificada sin filtro
    axs[1].plot(t_ms, v_rect, color=COLORS.RECT, lw=lw,
                label=f"v_rect(t)   f_out = {results.f_out:.0f} Hz")
    axs[1].axhline(results.Vo_dc, ls="--", color=COLORS.DC, lw=1.0,
                   label=f"Vo(cd) = {results.Vo_dc:.3f} V")
    setup_dark_axis(axs[1], "v_rect(t) — Salida rectificada sin filtro  [incisos c, f]")
    add_legend(axs[1])

    # AX2 - Salida con filtro capacitivo
    axs[2].plot(t_ms, v_rect, color=COLORS.RECT, lw=0.9, ls="--", alpha=0.4,
                label="v_rect (sin filtro)")
    axs[2].plot(t_ms, v_fc, color=COLORS.FILT, lw=lw,
                label=f"v_filt_C(t)  C={params.C_uF:.0f} uF  FRi={results.FRi:.1f}%")
    axs[2].axhline(results.Vo_dc_C, ls="--", color=COLORS.DC, lw=1.0,
                   label=f"Vo_dc_C = {results.Vo_dc_C:.3f} V")
    setup_dark_axis(axs[2],
                    f"v_filt_C(t) — Con filtro capacitivo  [incisos l, m]  "
                    f"FRi = {results.FRi:.1f} %  (obj <= {params.FR_obj*100:.0f} %)")
    add_legend(axs[2])

    # AX3 - Corriente secundario
    axs[3].plot(t_ms, i_carga, color=COLORS.VS, lw=0.9, ls="--", alpha=0.5,
                label="Is(t) sin inductor")
    axs[3].plot(t_ms, i_RL, color=COLORS.ID, lw=lw,
                label=f"Is(t) con L={params.L_H:.2f}H, RL={params.RL_Ohm:.0f}Ohm")
    axs[3].axhline(results.Io_dc_RL, ls="--", color=COLORS.DC, lw=1.0,
                   label=f"Io(dc)_RL = {results.Io_dc_RL:.3f} A  (vs {results.Io_dc:.3f}A sin L)")
    axs[3].set_xlabel("Tiempo [ms]", color="#6c7086", fontsize=8)
    setup_dark_axis(axs[3], "is(t) — Corriente secundario: sin / con inductor L  [incisos h, i, j]")
    add_legend(axs[3])


# =============================================================================
# PLOT DE SERIE DE FOURIER
# =============================================================================

def plot_fourier(fig: Figure, params: core.InputParams,
                 results: core.CalcResults) -> None:
    """
    Grafica la serie de Fourier del voltaje de salida.

    2 subplots:
      1. Senal real vs reconstruccion por Fourier
      2. Espectro de amplitudes

    Parameters
    ----------
    fig : Figure
        Figura de matplotlib
    params : InputParams
        Parametros del circuito
    results : CalcResults
        Resultados de calculo
    """
    fig.set_facecolor(COLORS.BG_MAIN)

    # Generar senales
    t = core.generate_time_array(params.f_red, n_cycles=4, n_points=5000)
    t_ms = t * 1e3
    w = 2.0 * np.pi * params.f_red

    v_real = np.abs(results.Vm_red * np.sin(w * t))
    v_fourier = core.generate_fourier_reconstruction(t, results.Vm_red, results.Vo_dc,
                                                      params.f_red, n_harmonics=10)

    freqs = results.fourier_freqs
    amps = results.fourier_amps

    # Crear subplots
    ax1, ax2 = fig.subplots(1, 2)
    fig.subplots_adjust(left=0.07, right=0.97, top=0.88, bottom=0.13, wspace=0.32)

    for ax in (ax1, ax2):
        ax.set_facecolor(COLORS.BG_MAIN)
        ax.tick_params(colors="#6c7086", labelsize=8)
        for sp in ax.spines.values():
            sp.set_color("#45475a")
        ax.grid(True, color=COLORS.GRID, linewidth=0.5, linestyle=":")

    # Izquierda - Reconstruccion
    ax1.plot(t_ms, v_real, color=COLORS.RECT, lw=1.2, ls="--", alpha=0.7,
             label="|vs| real")
    ax1.plot(t_ms, v_fourier, color=COLORS.FILT, lw=1.8,
             label="Fourier N=10 arm.")
    ax1.axhline(results.Vo_dc, color=COLORS.DC, lw=1.0, ls=":",
                label=f"Vo(dc) = {results.Vo_dc:.3f} V")
    ax1.set_title("Senal real vs reconstruccion de Fourier",
                  color=COLORS.FG_STEP, fontsize=9, fontfamily="monospace")
    ax1.set_xlabel("Tiempo [ms]", color="#6c7086", fontsize=8)
    ax1.set_ylabel("Voltaje [V]", color="#6c7086", fontsize=8)
    add_legend(ax1)

    # Derecha - Espectro de barras
    ax2.bar([0], [results.Vo_dc], color="#6c7086", width=12, alpha=0.85,
            label=f"DC  {results.Vo_dc:.2f} V")
    for k, (fk, ak) in enumerate(zip(freqs, amps)):
        ax2.bar([fk], [ak], color=COLORS.HARMONICS[k], width=12, alpha=0.85,
                label=f"{fk:.0f} Hz  {ak:.3f} V")
    ax2.set_title("Espectro de amplitudes  [comparar con FFT]",
                  color=COLORS.FG_STEP, fontsize=9, fontfamily="monospace")
    ax2.set_xlabel("Frecuencia [Hz]", color="#6c7086", fontsize=8)
    ax2.set_ylabel("Amplitud [V]", color="#6c7086", fontsize=8)
    add_legend(ax2)
    ax2.set_xlim(-20, max(freqs) * 1.15)
    ax2.set_xticks([0] + list(freqs))
    ax2.set_xticklabels(["0"] + [f"{fk:.0f}" for fk in freqs], rotation=30, fontsize=7)


# =============================================================================
# PLOT DE DISENO DE FILTROS
# =============================================================================

def plot_filter_design(fig: Figure, params: core.InputParams,
                        results: core.CalcResults) -> None:
    """
    Grafica las curvas de diseno de filtros.

    2 subplots:
      1. Factor de rizo vs capacitancia
      2. Atenuacion de armonicos vs inductancia

    Parameters
    ----------
    fig : Figure
        Figura de matplotlib
    params : InputParams
        Parametros del circuito
    results : CalcResults
        Resultados de calculo
    """
    fig.set_facecolor(COLORS.BG_MAIN)

    f_out = results.f_out
    R = params.R_carga
    RL = params.RL_Ohm
    L = params.L_H

    # Generar curvas
    C_arr_uF, FR_arr = core.generate_fr_vs_capacitance(f_out, R)
    L_arr_mH, attenuation = core.generate_attenuation_vs_inductance(f_out, R, RL)

    # Crear subplots
    ax1, ax2 = fig.subplots(1, 2)
    fig.subplots_adjust(left=0.08, right=0.97, top=0.88, bottom=0.13, wspace=0.32)

    for ax in (ax1, ax2):
        ax.set_facecolor(COLORS.BG_MAIN)
        ax.tick_params(colors="#6c7086", labelsize=8)
        for sp in ax.spines.values():
            sp.set_color("#45475a")
        ax.grid(True, color=COLORS.GRID, linewidth=0.5, linestyle=":")

    # Izquierda - FR vs C
    ax1.semilogx(C_arr_uF, FR_arr, color=COLORS.ACCENT, lw=2.0, label="FR(C)")
    ax1.axhline(params.FR_obj * 100, color=COLORS.RECT, lw=1.5, ls="--",
                label=f"Objetivo FR = {params.FR_obj*100:.0f}%")
    ax1.axvline(results.C_min_uF, color="#fab387", lw=1.5, ls=":",
                label=f"C_min = {results.C_min_uF:.0f} uF")
    ax1.axvline(params.C_uF, color=COLORS.FILT, lw=1.5, ls="-.",
                label=f"C_actual = {params.C_uF:.0f} uF -> {results.FR_C*100:.1f}%")
    ax1.set_xlabel("Capacitancia C [uF]", color="#6c7086", fontsize=8)
    ax1.set_ylabel("Factor de rizo FR [%]", color="#6c7086", fontsize=8)
    ax1.set_title(f"FR vs C  (f_out={f_out:.0f} Hz, R={R:.0f} Ohm)",
                  color=COLORS.FG_STEP, fontsize=9, fontfamily="monospace")
    add_legend(ax1)
    y_max = min(80, FR_arr[0] * 1.1) if FR_arr[0] > 0 else 80
    ax1.set_ylim(0, max(1, y_max))

    # Derecha - Atenuacion vs L
    for nk in range(1, 6):
        ax2.semilogx(L_arr_mH, attenuation[nk], color=COLORS.HARMONICS[nk-1], lw=1.8,
                     label=f"arm. {2*nk}  ({2*nk*f_out:.0f} Hz)")
    ax2.axvline(L * 1e3, color="white", lw=1.5, ls="--",
                label=f"L = {L:.2f} H  ({L*1e3:.1f} mH)")
    ax2.set_xlabel("Inductancia L [mH]", color="#6c7086", fontsize=8)
    ax2.set_ylabel("I_arm / I_arm_sin_L [%]", color="#6c7086", fontsize=8)
    ax2.set_title("Atenuacion de corriente armonica\nvs inductancia del filtro",
                  color=COLORS.FG_STEP, fontsize=9, fontfamily="monospace")
    add_legend(ax2)
    ax2.set_ylim(0, 105)


# =============================================================================
# FUNCION DE GUARDADO DE FIGURAS
# =============================================================================

def save_all_figures(params: core.InputParams, results: core.CalcResults,
                      output_dir: str = ".", prefix: str = "practica1",
                      dpi: int = 150) -> list:
    """
    Genera y guarda todas las figuras en archivos PNG.

    Parameters
    ----------
    params : InputParams
        Parametros del circuito
    results : CalcResults
        Resultados de calculo
    output_dir : str
        Directorio de salida
    prefix : str
        Prefijo para los nombres de archivo
    dpi : int
        Resolucion en DPI

    Returns
    -------
    list : Lista de rutas de archivos generados
    """
    import os
    os.makedirs(output_dir, exist_ok=True)

    files = []

    # Figura 1 - Formas de onda
    fig1 = Figure(figsize=(12, 9), facecolor=COLORS.BG_MAIN)
    plot_waveforms(fig1, params, results)
    path1 = os.path.join(output_dir, f"{prefix}_formas_onda.png")
    fig1.savefig(path1, dpi=dpi, facecolor=fig1.get_facecolor(), edgecolor='none')
    files.append(path1)

    # Figura 2 - Fourier
    fig2 = Figure(figsize=(12, 5), facecolor=COLORS.BG_MAIN)
    plot_fourier(fig2, params, results)
    path2 = os.path.join(output_dir, f"{prefix}_fourier.png")
    fig2.savefig(path2, dpi=dpi, facecolor=fig2.get_facecolor(), edgecolor='none')
    files.append(path2)

    # Figura 3 - Diseno de filtros
    fig3 = Figure(figsize=(12, 5), facecolor=COLORS.BG_MAIN)
    plot_filter_design(fig3, params, results)
    path3 = os.path.join(output_dir, f"{prefix}_filtros.png")
    fig3.savefig(path3, dpi=dpi, facecolor=fig3.get_facecolor(), edgecolor='none')
    files.append(path3)

    return files


def create_figure(figsize: Tuple[float, float] = (10, 6)) -> Figure:
    """
    Crea una figura con el fondo oscuro configurado.

    Parameters
    ----------
    figsize : tuple
        Tamano de la figura (ancho, alto)

    Returns
    -------
    Figure : Figura de matplotlib
    """
    fig = Figure(figsize=figsize, facecolor=COLORS.BG_MAIN)
    return fig
