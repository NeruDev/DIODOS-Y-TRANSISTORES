"""
core.py — Calculaciones puras para rectificadores monofasicos
==============================================================================
Modulo de logica de negocio SIN dependencias de GUI ni matplotlib.
Todas las funciones son puras: reciben datos, retornan resultados.

Orden de calculo (incisos de la practica):
  PASO 1 | Parametros del transformador (Vs_rms -> Vm)
  PASO 2 | Voltaje y corriente DC promedio (Vo_cd, Io_cd)
  PASO 3 | Voltaje y corriente RMS sin filtro (Vo_rms, Io_rms)
  PASO 4 | Factor de forma y rizo sin filtro (FF, Vr_rms, FR)
  PASO 5 | Parametros de los diodos (ID_prom, ID_rms, VPR, P_diodo)
  PASO 6 | Potencias y rendimiento (Po_cd, Po_CA, eta)
  PASO 7 | Serie de Fourier del voltaje de salida (5 armonicos)
  PASO 8 | Filtro inductivo R-L (atenuacion de armonicos de corriente)
  PASO 9 | Diseno del filtro capacitivo (FR_i <= 5%)

::SCRIPT_METADATA::
script_id    : practica1-core
module       : DIO
generates    : calculos numericos (sin graficos)
referenced_by: calculadora/plotting.py, calculadora/ui_tkinter.py
last_updated : 2026-03-21
"""

from dataclasses import dataclass, field
from typing import List
import numpy as np


# =============================================================================
# PARAMETROS DE ENTRADA (DATACLASS PARA TIPADO SEGURO)
# =============================================================================

@dataclass
class InputParams:
    """Parametros de entrada para los calculos del rectificador."""

    # Transformador
    Vs_rms: float = 12.0      # V RMS secundario
    f_red: float = 60.0       # Hz frecuencia de red

    # Diodos 1N4005
    Vd: float = 0.7           # V caida directa por diodo

    # Carga
    R_carga: float = 10.0     # Ohms resistencia de carga

    # Filtro inductivo
    L_H: float = 1.5          # H inductancia
    RL_Ohm: float = 40.0      # Ohms resistencia del devanado

    # Filtro capacitivo
    C_uF: float = 2200.0      # uF capacitancia
    FR_obj: float = 0.05      # Factor de rizo objetivo (5%)


# =============================================================================
# RESULTADOS (DATACLASS PARA ORGANIZACION)
# =============================================================================

@dataclass
class CalcResults:
    """Resultados de todos los pasos de calculo."""

    # PASO 1 - Transformador
    Vm: float = 0.0           # V pico del secundario
    Vm_red: float = 0.0       # V pico disponible (con 2 diodos)
    f_out: float = 0.0        # Hz frecuencia de salida
    T_out: float = 0.0        # s periodo de salida

    # PASO 2 - DC promedio
    Vo_dc: float = 0.0        # V voltaje DC
    Io_dc: float = 0.0        # A corriente DC

    # PASO 3 - RMS sin filtro
    Vo_rms: float = 0.0       # V voltaje RMS
    Io_rms: float = 0.0       # A corriente RMS

    # PASO 4 - Factor de forma y rizo
    FF: float = 0.0           # Factor de forma
    Vr_rms: float = 0.0       # V rizo RMS
    FR: float = 0.0           # Factor de rizo

    # PASO 5 - Diodos
    ID_prom: float = 0.0      # A corriente promedio diodo
    ID_rms: float = 0.0       # A corriente RMS diodo
    VPR: float = 0.0          # V tension inversa pico
    P_diodo: float = 0.0      # W potencia disipada

    # PASO 6 - Potencias
    Po_dc: float = 0.0        # W potencia DC
    Po_ca: float = 0.0        # W potencia AC
    eta: float = 0.0          # % rendimiento

    # PASO 7 - Fourier
    fourier_freqs: List[float] = field(default_factory=list)
    fourier_amps: List[float] = field(default_factory=list)

    # PASO 8 - Filtro inductivo
    RT: float = 0.0           # Ohms resistencia total
    Io_dc_RL: float = 0.0     # A corriente DC con filtro
    V_carga_RL: float = 0.0   # V voltaje en carga
    Z_RL_arms: List[float] = field(default_factory=list)
    IL_arms: List[float] = field(default_factory=list)
    aten_RL: List[float] = field(default_factory=list)
    Ir_rms_RL: float = 0.0    # A rizo RMS
    FRi_RL: float = 0.0       # % factor de rizo con L

    # PASO 9 - Filtro capacitivo
    Vr_pp: float = 0.0        # V rizo pico a pico
    Vo_dc_C: float = 0.0      # V voltaje DC con filtro C
    Vr_rms_C: float = 0.0     # V rizo RMS con C
    Ir_rms_C: float = 0.0     # A rizo RMS en corriente
    FR_C: float = 0.0         # Factor de rizo con C
    FRi: float = 0.0          # % factor de rizo con C
    C_min_uF: float = 0.0     # uF capacitor minimo


# =============================================================================
# VALORES POR DEFECTO
# =============================================================================

DEFAULT_PARAMS = InputParams()


# =============================================================================
# FUNCION PRINCIPAL DE CALCULO
# =============================================================================

def calcular_todo(params: InputParams) -> CalcResults:
    """
    Ejecuta los 9 pasos de calculo de la practica en orden.

    Parameters
    ----------
    params : InputParams
        Valores de entrada del circuito

    Returns
    -------
    CalcResults
        Todos los resultados intermedios y finales
    """
    r = CalcResults()

    # Extraer parametros
    Vs = params.Vs_rms
    f = params.f_red
    Vd = params.Vd
    R = params.R_carga
    L = params.L_H
    RL = params.RL_Ohm
    RT = R + RL
    C = params.C_uF * 1e-6
    FR_o = params.FR_obj

    N_HARM = 5

    # =========================================================================
    # PASO 1 - PARAMETROS DEL TRANSFORMADOR
    # =========================================================================
    r.Vm = Vs * np.sqrt(2)
    r.Vm_red = r.Vm - 2.0 * Vd
    r.f_out = 2.0 * f
    r.T_out = 1.0 / r.f_out

    # =========================================================================
    # PASO 2 - VOLTAJE Y CORRIENTE DC (PROMEDIO)
    # =========================================================================
    r.Vo_dc = (2.0 / np.pi) * r.Vm_red
    r.Io_dc = r.Vo_dc / R

    # =========================================================================
    # PASO 3 - VOLTAJE Y CORRIENTE RMS (SIN FILTRO)
    # =========================================================================
    r.Vo_rms = r.Vm_red / np.sqrt(2.0)
    r.Io_rms = r.Vo_rms / R

    # =========================================================================
    # PASO 4 - FACTOR DE FORMA Y RIZO (SIN FILTRO)
    # =========================================================================
    r.FF = r.Vo_rms / r.Vo_dc
    r.Vr_rms = np.sqrt(max(r.Vo_rms**2 - r.Vo_dc**2, 0.0))
    r.FR = r.Vr_rms / r.Vo_dc

    # =========================================================================
    # PASO 5 - PARAMETROS DE LOS DIODOS
    # =========================================================================
    r.ID_prom = r.Io_dc / 2.0
    r.ID_rms = r.Io_rms / np.sqrt(2.0)
    r.VPR = r.Vm
    r.P_diodo = Vd * r.ID_prom

    # =========================================================================
    # PASO 6 - POTENCIAS Y RENDIMIENTO
    # =========================================================================
    r.Po_dc = r.Vo_dc**2 / R
    r.Po_ca = r.Vo_rms**2 / R
    r.eta = (r.Po_dc / r.Po_ca) * 100.0

    # =========================================================================
    # PASO 7 - SERIE DE FOURIER DEL VOLTAJE DE SALIDA
    # =========================================================================
    r.fourier_freqs = [2.0 * (k + 1) * f for k in range(N_HARM)]
    r.fourier_amps = [
        abs(4.0 * r.Vm_red / (np.pi * (4.0 * (k + 1)**2 - 1.0)))
        for k in range(N_HARM)
    ]

    # =========================================================================
    # PASO 8 - FILTRO INDUCTIVO R-L
    # =========================================================================
    w_out = 2.0 * np.pi * r.f_out
    r.RT = RT
    r.Io_dc_RL = r.Vo_dc / RT
    r.V_carga_RL = r.Io_dc_RL * R
    r.Z_RL_arms = []
    r.IL_arms = []
    r.aten_RL = []

    for k in range(N_HARM):
        n_k = k + 1
        Vn = r.fourier_amps[k]
        Zn = np.sqrt(RT**2 + (n_k * w_out * L)**2)
        r.Z_RL_arms.append(Zn)
        r.IL_arms.append(Vn / Zn)
        r.aten_RL.append(R / Zn * 100.0)

    r.Ir_rms_RL = r.IL_arms[0] / np.sqrt(2.0)
    r.FRi_RL = (r.Ir_rms_RL / r.Io_dc_RL) * 100.0

    # =========================================================================
    # PASO 9 - DISENO DEL FILTRO CAPACITIVO (FR_i <= 5%)
    # =========================================================================
    r.Vr_pp = r.Vm_red / (r.f_out * C * R)
    r.Vo_dc_C = r.Vm_red - r.Vr_pp / 2.0
    r.Vr_rms_C = r.Vr_pp / (2.0 * np.sqrt(3.0))
    r.Ir_rms_C = r.Vr_rms_C / R
    r.FR_C = r.Vr_rms_C / r.Vo_dc_C
    r.FRi = r.FR_C * 100.0

    x_min = 2.0 * np.sqrt(3.0) * FR_o / (1.0 + np.sqrt(3.0) * FR_o)
    r.C_min_uF = 1.0 / (x_min * r.f_out * R) * 1e6

    return r


# =============================================================================
# FUNCIONES AUXILIARES PARA GENERACION DE SENALES
# =============================================================================

def generate_time_array(f_red: float, n_cycles: int = 4, n_points: int = 5000) -> np.ndarray:
    """Genera array de tiempo para n ciclos de la red."""
    return np.linspace(0, n_cycles / f_red, n_points)


def generate_secondary_voltage(t: np.ndarray, Vm: float, f_red: float) -> np.ndarray:
    """Genera senal del secundario del transformador."""
    omega = 2.0 * np.pi * f_red
    return Vm * np.sin(omega * t)


def generate_rectified_voltage(t: np.ndarray, Vm_red: float, f_red: float, Vd: float = 0.0) -> np.ndarray:
    """Genera senal rectificada de onda completa (puente Graetz)."""
    omega = 2.0 * np.pi * f_red
    Vm_total = Vm_red + 2.0 * Vd
    vs = Vm_total * np.sin(omega * t)
    return np.maximum(np.abs(vs) - 2.0 * Vd, 0.0)


def generate_capacitor_filtered(t: np.ndarray, v_rect: np.ndarray,
                                 R: float, C: float) -> np.ndarray:
    """Simula el filtrado capacitivo muestra a muestra."""
    v_fc = np.zeros_like(t)
    v_cap = v_rect[0]
    dt = t[1] - t[0]
    tau = R * C

    for i in range(len(t)):
        if v_rect[i] >= v_cap:
            v_cap = v_rect[i]
        else:
            v_cap *= np.exp(-dt / tau)
        v_fc[i] = v_cap

    return v_fc


def generate_inductor_filtered_current(t: np.ndarray, results: CalcResults,
                                        params: InputParams) -> np.ndarray:
    """
    Reconstruccion armonica de corriente con filtro inductivo.
    Io_dc_RL + Sum(In_RL * cos(n_k * w_out * t + phi_n))
    """
    w_out = 2.0 * np.pi * results.f_out
    RT = params.R_carga + params.RL_Ohm
    L = params.L_H

    i_RL = np.full_like(t, results.Io_dc_RL)

    for k in range(5):
        nk = k + 1
        XL = nk * w_out * L
        Zn = np.sqrt(RT**2 + XL**2)
        phi = -np.arctan2(XL, RT)
        coef = -4.0 * results.Vm_red / (np.pi * (4.0 * nk**2 - 1.0))
        In = coef / Zn if Zn > 0 else 0.0
        i_RL += In * np.cos(nk * w_out * t + phi)

    return i_RL


def generate_fourier_reconstruction(t: np.ndarray, Vm_red: float,
                                     Vo_dc: float, f_red: float,
                                     n_harmonics: int = 10) -> np.ndarray:
    """Reconstruccion de la senal por serie de Fourier."""
    w = 2.0 * np.pi * f_red
    v_fourier = np.full_like(t, Vo_dc)

    for n in range(1, n_harmonics + 1):
        coef = -4.0 * Vm_red / (np.pi * (4.0 * n**2 - 1.0))
        v_fourier += coef * np.cos(2.0 * n * w * t)

    return v_fourier


def generate_fr_vs_capacitance(f_out: float, R: float,
                                C_range_uF: tuple = (100, 100000),
                                n_points: int = 600) -> tuple:
    """
    Genera curva de factor de rizo vs capacitancia.

    Returns
    -------
    tuple : (C_array_uF, FR_array_percent)
    """
    C_arr = np.logspace(np.log10(C_range_uF[0]), np.log10(C_range_uF[1]), n_points) * 1e-6
    x_arr = 1.0 / (f_out * R * C_arr)
    FR_arr = (x_arr / (2.0 * np.sqrt(3.0) * (1.0 - x_arr / 2.0))) * 100.0
    FR_arr = np.clip(FR_arr, 0, 200)

    return C_arr * 1e6, FR_arr


def generate_attenuation_vs_inductance(f_out: float, R: float, RL: float,
                                        L_range_H: tuple = (0.001, 1.0),
                                        n_points: int = 500) -> tuple:
    """
    Genera curvas de atenuacion de armonicos vs inductancia.

    Returns
    -------
    tuple : (L_array_mH, dict[harmonic_index -> attenuation_percent_array])
    """
    L_arr = np.logspace(np.log10(L_range_H[0]), np.log10(L_range_H[1]), n_points)
    RT = R + RL
    w_out = 2.0 * np.pi * f_out

    attenuation = {}
    for nk in range(1, 6):
        Zn_arr = np.sqrt(RT**2 + (nk * w_out * L_arr)**2)
        attenuation[nk] = R / Zn_arr * 100.0

    return L_arr * 1e3, attenuation


# =============================================================================
# VALIDACION DE PARAMETROS
# =============================================================================

def validate_params(params: InputParams) -> tuple:
    """
    Valida los parametros de entrada.

    Returns
    -------
    tuple : (is_valid: bool, error_message: str)
    """
    if params.Vs_rms <= 0:
        return False, "Vs_rms debe ser > 0"
    if params.R_carga <= 0:
        return False, "R_carga debe ser > 0"
    if params.C_uF <= 0:
        return False, "C_uF debe ser > 0"
    if params.Vd < 0:
        return False, "Vd debe ser >= 0"
    if params.Vd >= params.Vs_rms:
        return False, "Vd debe ser menor que Vs_rms"
    if params.f_red <= 0:
        return False, "f_red debe ser > 0"
    if params.L_H < 0:
        return False, "L_H debe ser >= 0"
    if params.RL_Ohm < 0:
        return False, "RL_Ohm debe ser >= 0"
    if params.FR_obj <= 0 or params.FR_obj >= 1:
        return False, "FR_obj debe estar entre 0 y 1"

    return True, ""


def params_from_dict(d: dict) -> InputParams:
    """Crea InputParams desde un diccionario."""
    return InputParams(
        Vs_rms=float(d.get("Vs_rms", 12.0)),
        f_red=float(d.get("f_red", 60.0)),
        Vd=float(d.get("Vd", 0.7)),
        R_carga=float(d.get("R_carga", 10.0)),
        L_H=float(d.get("L_H", 1.5)),
        RL_Ohm=float(d.get("RL_Ohm", 40.0)),
        C_uF=float(d.get("C_uF", 2200.0)),
        FR_obj=float(d.get("FR_obj", 0.05)),
    )


def results_to_dict(r: CalcResults) -> dict:
    """Convierte CalcResults a diccionario para serializacion."""
    return {
        # PASO 1
        "Vm": r.Vm,
        "Vm_red": r.Vm_red,
        "f_out": r.f_out,
        "T_out": r.T_out,
        # PASO 2
        "Vo_dc": r.Vo_dc,
        "Io_dc": r.Io_dc,
        # PASO 3
        "Vo_rms": r.Vo_rms,
        "Io_rms": r.Io_rms,
        # PASO 4
        "FF": r.FF,
        "Vr_rms": r.Vr_rms,
        "FR": r.FR,
        # PASO 5
        "ID_prom": r.ID_prom,
        "ID_rms": r.ID_rms,
        "VPR": r.VPR,
        "P_diodo": r.P_diodo,
        # PASO 6
        "Po_dc": r.Po_dc,
        "Po_ca": r.Po_ca,
        "eta": r.eta,
        # PASO 7
        "fourier_freqs": r.fourier_freqs,
        "fourier_amps": r.fourier_amps,
        # PASO 8
        "RT": r.RT,
        "Io_dc_RL": r.Io_dc_RL,
        "V_carga_RL": r.V_carga_RL,
        "Z_RL_arms": r.Z_RL_arms,
        "IL_arms": r.IL_arms,
        "aten_RL": r.aten_RL,
        "Ir_rms_RL": r.Ir_rms_RL,
        "FRi_RL": r.FRi_RL,
        # PASO 9
        "Vr_pp": r.Vr_pp,
        "Vo_dc_C": r.Vo_dc_C,
        "Vr_rms_C": r.Vr_rms_C,
        "Ir_rms_C": r.Ir_rms_C,
        "FR_C": r.FR_C,
        "FRi": r.FRi,
        "C_min_uF": r.C_min_uF,
    }


# =============================================================================
# EJEMPLO DE USO (cuando se ejecuta directamente)
# =============================================================================

if __name__ == "__main__":
    # Demostrar uso sin GUI
    params = InputParams(Vs_rms=12.0, f_red=60.0, Vd=0.7, R_carga=10.0)

    is_valid, error = validate_params(params)
    if not is_valid:
        print(f"Error: {error}")
        exit(1)

    results = calcular_todo(params)

    print("=" * 60)
    print("RESULTADOS DE CALCULO - Rectificador Puente Graetz")
    print("=" * 60)
    print(f"\nPASO 1 - Transformador:")
    print(f"  Vm = {results.Vm:.3f} V")
    print(f"  Vm_red = {results.Vm_red:.3f} V")
    print(f"  f_out = {results.f_out:.0f} Hz")

    print(f"\nPASO 2 - DC Promedio:")
    print(f"  Vo_dc = {results.Vo_dc:.3f} V")
    print(f"  Io_dc = {results.Io_dc:.3f} A")

    print(f"\nPASO 4 - Factor de forma y rizo:")
    print(f"  FF = {results.FF:.4f}")
    print(f"  FR = {results.FR * 100:.2f}%")

    print(f"\nPASO 6 - Potencias:")
    print(f"  Po_dc = {results.Po_dc:.3f} W")
    print(f"  eta = {results.eta:.2f}%")

    print(f"\nPASO 9 - Filtro capacitivo:")
    print(f"  FRi = {results.FRi:.2f}%")
    print(f"  C_min = {results.C_min_uF:.0f} uF")
