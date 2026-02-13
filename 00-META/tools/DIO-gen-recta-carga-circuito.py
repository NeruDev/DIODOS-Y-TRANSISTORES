"""
DIO-gen-recta-carga-circuito.py
───────────────────
Genera un esquemático base para el análisis de recta de carga en un circuito
serie con diodo (fuente DC + resistencia + diodo), incluyendo:

- Sentido de corriente horario.
- Delimitación de la rama del diodo.
- Leyenda de voltaje del diodo como V_D.
- Gráfica de recta de carga por puntos extremos.
- Circuito AC+CD (6 V, 270 Ω) y punto Q.

::SCRIPT_METADATA::
script_id: DIO-gen-recta-carga-circuito
module: DIO
generates:
  - dio-recta-carga-circuito-vd.png
  - dio-recta-carga-extremos.png
  - dio-circuito-ac-cd-6v-270ohm-vd.png
  - dio-recta-carga-q-6v-270ohm.png
  - dio-recta-carga-q-objetivo-19ma-1v5.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota2.md
last_updated: 2026-02-13

Salida:
  - 01-Circuitos-Diodos/media/generated/dio-recta-carga-circuito-vd.png
  - 01-Circuitos-Diodos/media/generated/dio-recta-carga-extremos.png
  - 01-Circuitos-Diodos/media/generated/dio-circuito-ac-cd-6v-270ohm-vd.png
  - 01-Circuitos-Diodos/media/generated/dio-recta-carga-q-6v-270ohm.png
  - 01-Circuitos-Diodos/media/generated/dio-recta-carga-q-objetivo-19ma-1v5.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-recta-carga-circuito.py
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm

schemdraw.use('matplotlib')


OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)

output_circuit = os.path.join(OUTPUT_DIR, "dio-recta-carga-circuito-vd.png")
output_graph = os.path.join(OUTPUT_DIR, "dio-recta-carga-extremos.png")
output_circuit_acdc = os.path.join(OUTPUT_DIR, "dio-circuito-ac-cd-6v-270ohm-vd.png")
output_graph_q = os.path.join(OUTPUT_DIR, "dio-recta-carga-q-6v-270ohm.png")
output_graph_q_target = os.path.join(OUTPUT_DIR, "dio-recta-carga-q-objetivo-19ma-1v5.png")

with schemdraw.Drawing(file=output_circuit, show=False, dpi=150) as d:
    d.config(fontsize=14)

    # Rama izquierda: fuente DC (de abajo hacia arriba)
    d += (source := elm.SourceV().up().label('$E$', loc='left', ofst=0.3))

    # Rama superior: resistencia en serie
    d += elm.Line().right(1)
    d += (rload := elm.Resistor().right().label('$R$', loc='top', ofst=0.15))
    d += elm.CurrentLabelInline(direction='in').at(rload).label('$I_D$', loc='top', ofst=0.6)
    d += elm.Line().right(1)

    # Rama derecha: diodo hacia abajo
    d += (diode := elm.Diode().down().label('$D$', loc='right', ofst=0.3))

    # Rama inferior: cierre de malla
    d += elm.Line().left().tox(source.start)

    # Delimitación de la rama del diodo y leyenda de voltaje V_D
    d += elm.Line().right(1.8).at(diode.start)
    d += elm.Dot(open=True).label('$+$', loc='right')
    d += elm.Gap().down().label([' ', '$V_D$', ' '])
    d += elm.Dot(open=True).label('$-$', loc='right')
    d += elm.Line().left(1.8)

    print("✅ Generada: dio-recta-carga-circuito-vd.png")


    # Parámetros de ejemplo para la recta de carga
    E_val = 5.0      # Voltaje de la fuente [V]
    R_val = 1000.0   # Resistencia [ohm]

    # Recta: R*I_D + V_D = E  ->  I_D = (E - V_D)/R
    v_d = np.linspace(0.0, E_val, 200)
    i_d = (E_val - v_d) / R_val

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(v_d, i_d * 1e3, 'r-', linewidth=2.5, label=r'$I_D = \frac{E - V_D}{R}$')

    # Puntos extremos
    i_max_ma = (E_val / R_val) * 1e3
    ax.plot(0, i_max_ma, 'ko', markersize=8)
    ax.plot(E_val, 0, 'ko', markersize=8)

    ax.annotate(r'$V_D=0\Rightarrow I_D=\frac{E}{R}$',
        xy=(0, i_max_ma), xytext=(0.35, i_max_ma * 0.82),
        arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=11)
    ax.annotate(r'$I_D=0\Rightarrow V_D=E$',
        xy=(E_val, 0), xytext=(E_val * 0.55, i_max_ma * 0.2),
        arrowprops=dict(arrowstyle='->', lw=1.5), fontsize=11)

    ax.set_xlabel('Voltaje del diodo $V_D$ (V)', fontsize=12)
    ax.set_ylabel('Corriente del diodo $I_D$ (mA)', fontsize=12)
    ax.set_title('Recta de carga por puntos extremos', fontsize=13)
    ax.set_xlim(-0.1, E_val + 0.35)
    ax.set_ylim(-0.2, i_max_ma + 1.0)
    ax.grid(True, linestyle='--', alpha=0.45)
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.savefig(output_graph, dpi=150)
    plt.close(fig)

    print("✅ Generada: dio-recta-carga-extremos.png")


    # ============================================================
    # Circuito para análisis de pequeña señal
    # E = 6V en serie con v_s(t)=2sen(wt), R=270Ω y diodo
    # ============================================================
    with schemdraw.Drawing(file=output_circuit_acdc, show=False, dpi=150) as d:
      d.config(fontsize=14)

      # Rama izquierda: fuente DC + fuente AC en serie
      d += (source_dc := elm.SourceV().up().label(r'$E=6\,V$', loc='left', ofst=0.3))
      d += elm.SourceSin().up().label(r'$v_s(t)=2\,\mathrm{sen}(\omega t)$', loc='left', ofst=0.3)

      # Rama superior: resistencia de 270 ohms
      d += elm.Line().right(1)
      d += (rload_acdc := elm.Resistor().right().label(r'$R=270\,\Omega$', loc='top', ofst=0.15))
      d += elm.CurrentLabelInline(direction='in').at(rload_acdc).label('$I_D$', loc='top', ofst=0.6)
      d += elm.Line().right(1)

      # Rama derecha: diodo
      d += (diode_acdc := elm.Diode().down().label('$D$', loc='right', ofst=0.3))

      # Rama inferior: cierre de malla
      d += elm.Line().down().toy(source_dc.start)
      d += elm.Line().left().tox(source_dc.start)

      # Leyenda de voltaje del diodo V_D
      d += elm.Line().right(1.8).at(diode_acdc.start)
      d += elm.Dot(open=True).label('$+$', loc='right')
      d += elm.Gap().down().label([' ', '$V_D$', ' '])
      d += elm.Dot(open=True).label('$-$', loc='right')
      d += elm.Line().left(1.8)

    print("✅ Generada: dio-circuito-ac-cd-6v-270ohm-vd.png")


    # ============================================================
    # Recta de carga CD + curva I-V + límites instantáneos AC
    # Caso: E=6V, v_s(t)=2sen(wt), R=270Ω
    # ============================================================
    E_q = 6.0
    R_q = 270.0
    V_ac_amp = 2.0
    E_max = E_q + V_ac_amp
    E_min = E_q - V_ac_amp
    Is = 1e-12
    n = 1.0
    Vt = 0.026

    # Curva I-V del diodo
    v_d_iv = np.linspace(0.0, 1.0, 1200)
    i_d_iv = Is * (np.exp(v_d_iv / (n * Vt)) - 1.0)

    # Recta de carga CD
    v_d_line = np.linspace(0.0, E_q, 300)
    i_d_line = (E_q - v_d_line) / R_q

    # Rectas límite instantáneas por señal AC
    v_d_line_max = np.linspace(0.0, E_max, 300)
    i_d_line_max = (E_max - v_d_line_max) / R_q
    v_d_line_min = np.linspace(0.0, E_min, 300)
    i_d_line_min = (E_min - v_d_line_min) / R_q

    # Punto Q por búsqueda de cruce
    def f_q(v):
      return Is * (np.exp(v / (n * Vt)) - 1.0) - (E_q - v) / R_q

    low, high = 0.0, 1.0
    for _ in range(80):
      mid = 0.5 * (low + high)
      if f_q(low) * f_q(mid) <= 0:
        high = mid
      else:
        low = mid

    v_q = 0.5 * (low + high)
    i_q = (E_q - v_q) / R_q

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(v_d_iv, i_d_iv * 1e3, 'b-', linewidth=2.5, label='Curva I-V del diodo')
    ax.plot(v_d_line, i_d_line * 1e3, 'r-', linewidth=2.5, label=r'Recta CD: $E=6\,V$')
    ax.plot(v_d_line_max, i_d_line_max * 1e3, color='darkgreen', linestyle='--', linewidth=1.8,
      label=r'Límite instantáneo: $E_{\max}=8\,V$')
    ax.plot(v_d_line_min, i_d_line_min * 1e3, color='purple', linestyle='--', linewidth=1.8,
      label=r'Límite instantáneo: $E_{\min}=4\,V$')

    ax.plot(v_q, i_q * 1e3, 'ko', markersize=8, label='Punto Q')
    ax.annotate(
      rf'$Q(V_D={v_q:.3f}\,V,\ I_D={i_q*1e3:.2f}\,mA)$',
      xy=(v_q, i_q * 1e3),
      xytext=(v_q + 0.35, i_q * 1e3 + 2.0),
      arrowprops=dict(arrowstyle='->', lw=1.5),
      fontsize=10
    )

    ax.plot(0, (E_q / R_q) * 1e3, 'ks', markersize=6)
    ax.plot(E_q, 0, 'ks', markersize=6)

    ax.annotate(r'$I_{D,\max}\approx 29.63\,mA$ (ideal)',
                xy=(0, (E_max / R_q) * 1e3),
                xytext=(0.25, (E_max / R_q) * 1e3 + 1.2),
                fontsize=9, color='darkgreen')
    ax.annotate(r'$I_{D,\min}\approx 14.81\,mA$ (ideal)',
                xy=(0, (E_min / R_q) * 1e3),
                xytext=(0.25, (E_min / R_q) * 1e3 - 2.0),
                fontsize=9, color='purple')

    ax.set_xlabel('Voltaje del diodo $V_D$ (V)', fontsize=12)
    ax.set_ylabel('Corriente del diodo $I_D$ (mA)', fontsize=12)
    ax.set_title('Recta de carga: CD (Q) y límites instantáneos por AC', fontsize=13)
    ax.set_xlim(-0.05, E_max + 0.35)
    ax.set_ylim(-0.5, (E_max / R_q) * 1e3 + 3.0)
    ax.grid(True, linestyle='--', alpha=0.45)
    ax.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.savefig(output_graph_q, dpi=150)
    plt.close(fig)

    print("✅ Generada: dio-recta-carga-q-6v-270ohm.png")


    # ============================================================
    # Gráfica del ejemplo adicional con ajuste de E
    # Ajuste de la recta: E*=6.63V (R=270Ω)
    # Q objetivo nueva: intersección real recta + curva I-V
    # ============================================================
    E_target = 6.63

    v_d_line_target = np.linspace(0.0, E_target, 300)
    i_d_line_target = (E_target - v_d_line_target) / R_q

    # Intersección real con la curva I-V para E ajustada
    def f_target(v):
      return Is * (np.exp(v / (n * Vt)) - 1.0) - (E_target - v) / R_q

    low_t, high_t = 0.0, 1.0
    for _ in range(80):
      mid_t = 0.5 * (low_t + high_t)
      if f_target(low_t) * f_target(mid_t) <= 0:
        high_t = mid_t
      else:
        low_t = mid_t

    v_q_target = 0.5 * (low_t + high_t)
    i_q_target = (E_target - v_q_target) / R_q

    fig2, ax2 = plt.subplots(figsize=(9, 6))
    ax2.plot(v_d_iv, i_d_iv * 1e3, 'b-', linewidth=2.5, label='Curva I-V del diodo')
    ax2.plot(v_d_line_target, i_d_line_target * 1e3, 'darkorange', linewidth=2.5,
             label=r'Recta objetivo: $E^*=6.63\,V$')
    ax2.plot(v_q_target, i_q_target * 1e3, 'ko', markersize=8, label=r'$Q^*$ ajustada')

    ax2.annotate(
      rf'$Q^*(V_D={v_q_target:.3f}\,V,\ I_D={i_q_target*1e3:.2f}\,mA)$',
      xy=(v_q_target, i_q_target * 1e3),
      xytext=(v_q_target + 0.35, i_q_target * 1e3 + 1.2),
      arrowprops=dict(arrowstyle='->', lw=1.5),
      fontsize=10
    )

    ax2.set_xlabel('Voltaje del diodo $V_D$ (V)', fontsize=12)
    ax2.set_ylabel('Corriente del diodo $I_D$ (mA)', fontsize=12)
    ax2.set_title(r'Ejemplo ajustado: intersección real con $E^*=6.63\,V$', fontsize=13)
    ax2.set_xlim(-0.05, E_target + 0.35)
    ax2.set_ylim(-0.5, (E_target / R_q) * 1e3 + 3.0)
    ax2.grid(True, linestyle='--', alpha=0.45)
    ax2.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.savefig(output_graph_q_target, dpi=150)
    plt.close(fig2)

    print("✅ Generada: dio-recta-carga-q-objetivo-19ma-1v5.png")
