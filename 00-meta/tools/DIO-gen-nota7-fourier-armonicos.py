"""
DIO-gen-nota7-fourier-armonicos.py
───────────────────
Genera gráficas de la descomposición en serie de Fourier del voltaje
de salida de un rectificador monofásico de onda completa tipo puente (H).

Salida:
  - topics/01-circuitos-diodos/assets/nota7_armonicos_individuales.png
  - topics/01-circuitos-diodos/assets/nota7_reconstruccion_fourier.png
  - topics/01-circuitos-diodos/assets/nota7_espectro_armonicos.png
  - topics/01-circuitos-diodos/assets/nota7_espectro_frecuencia.png

Ejecutar desde la raíz del repositorio:
  python 00-META/tools/DIO-gen-nota7-fourier-armonicos.py

::SCRIPT_METADATA::
script_id: DIO-gen-nota7-fourier-armonicos
module: DIO
generates:
  - nota7_armonicos_individuales.png
  - nota7_reconstruccion_fourier.png
  - nota7_espectro_armonicos.png
  - nota7_espectro_frecuencia.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota7.md
last_updated: 2026-03-04
"""

import matplotlib
matplotlib.use('Agg')  # backend sin GUI
import matplotlib.pyplot as plt
import numpy as np
import os

# ── Directorio de salida ──
OUTPUT_DIR = os.path.join("topics", "01-circuitos-diodos", "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Parámetros del circuito ──
Vm = 15.57       # V  (Vm - 2Vd con Vm=16.97, Vd=0.7)
f = 60           # Hz
omega = 2 * np.pi * f
T = 1 / f        # periodo de la señal de entrada

# ── Eje temporal: 2 periodos completos de la entrada ──
t = np.linspace(0, 2 * T, 2000)
theta = omega * t  # ángulo en radianes

# ── Señal rectificada exacta ──
vo_exact = Vm * np.abs(np.sin(theta))

# ── Coeficientes de Fourier ──
def Cn(n, Vm):
    """Amplitud pico del n-ésimo armónico (n >= 1)."""
    return -4 * Vm / (np.pi * (4 * n**2 - 1))

def Vdc(Vm):
    """Componente DC."""
    return 2 * Vm / np.pi

# ── Construir componentes individuales ──
N_harmonics = 5
dc = Vdc(Vm) * np.ones_like(t)
harmonics = {}
for n in range(1, N_harmonics + 1):
    harmonics[n] = Cn(n, Vm) * np.cos(2 * n * omega * t)

# ── Colores para los armónicos ──
colors = {
    'dc':  '#2196F3',   # azul
    1:     '#F44336',    # rojo
    2:     '#4CAF50',    # verde
    3:     '#FF9800',    # naranja
    4:     '#9C27B0',    # púrpura
    5:     '#00BCD4',    # cyan
}

labels_es = {
    'dc': f'DC = $2V_m/\\pi$ = {Vdc(Vm):.2f} V',
    1:    f'$n=1$: $2f = 120$ Hz  (Amp = {abs(Cn(1,Vm)):.2f} V)',
    2:    f'$n=2$: $4f = 240$ Hz  (Amp = {abs(Cn(2,Vm)):.2f} V)',
    3:    f'$n=3$: $6f = 360$ Hz  (Amp = {abs(Cn(3,Vm)):.2f} V)',
    4:    f'$n=4$: $8f = 480$ Hz  (Amp = {abs(Cn(4,Vm)):.2f} V)',
    5:    f'$n=5$: $10f = 600$ Hz (Amp = {abs(Cn(5,Vm)):.2f} V)',
}

t_ms = t * 1000  # tiempo en milisegundos

# ═══════════════════════════════════════════════════════════════
# FIGURA 1: Armónicos individuales
# ═══════════════════════════════════════════════════════════════
fig1, axes = plt.subplots(N_harmonics + 1, 1, figsize=(12, 14),
                          sharex=True, gridspec_kw={'hspace': 0.35})
fig1.suptitle('Componentes de Fourier del rectificador tipo puente\n'
              f'($V_m\' = {Vm}$ V, $f = {f}$ Hz, diodos Si)',
              fontsize=14, fontweight='bold', y=0.98)

# DC
axes[0].axhline(Vdc(Vm), color=colors['dc'], linewidth=2, label=labels_es['dc'])
axes[0].fill_between(t_ms, 0, Vdc(Vm), alpha=0.15, color=colors['dc'])
axes[0].set_ylabel('$V_{DC}$ (V)')
axes[0].set_ylim(-1, Vm + 1)
axes[0].legend(loc='upper right', fontsize=9)
axes[0].grid(True, alpha=0.3)
axes[0].set_title('Componente DC (valor promedio)', fontsize=10, loc='left')

# Armónicos 1 a 5
for n in range(1, N_harmonics + 1):
    ax = axes[n]
    ax.plot(t_ms, harmonics[n], color=colors[n], linewidth=1.5, label=labels_es[n])
    ax.axhline(0, color='gray', linewidth=0.5, linestyle='--')
    ax.fill_between(t_ms, 0, harmonics[n], alpha=0.12, color=colors[n])
    ax.set_ylabel(f'$C_{n}$ (V)')
    amp = abs(Cn(n, Vm))
    ax.set_ylim(-amp * 1.5, amp * 1.5)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)
    freq = 2 * n * f
    ax.set_title(f'Armónico $n={n}$: frecuencia = ${2*n}f$ = {freq} Hz',
                 fontsize=10, loc='left')

axes[-1].set_xlabel('Tiempo (ms)')
axes[-1].set_xlim(0, 2 * T * 1000)

fig1.savefig(os.path.join(OUTPUT_DIR, 'nota7_armonicos_individuales.png'),
             dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig1)
print("Generada: nota7_armonicos_individuales.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 2: Reconstrucción progresiva de la señal
# ═══════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(12, 7))
fig2.suptitle('Reconstrucción progresiva de $v_o(t)$ mediante serie de Fourier\n'
              f'Rectificador tipo puente — $V_m\' = {Vm}$ V, $f = {f}$ Hz',
              fontsize=13, fontweight='bold')

# Señal exacta
ax2.plot(t_ms, vo_exact, 'k-', linewidth=2.5, alpha=0.35, label='$|V_m\\sin(\\omega t)|$ (exacta)')

# Reconstrucciones parciales
reconstruction_colors = ['#F44336', '#4CAF50', '#FF9800', '#9C27B0', '#00BCD4']
for N in range(1, N_harmonics + 1):
    partial = dc.copy()
    for n in range(1, N + 1):
        partial += harmonics[n]
    style = '-' if N == N_harmonics else '--'
    lw = 2.0 if N == N_harmonics else 1.2
    alpha = 1.0 if N == N_harmonics else 0.6
    ax2.plot(t_ms, partial, linestyle=style, linewidth=lw, alpha=alpha,
             color=reconstruction_colors[N - 1],
             label=f'DC + {N} armónico{"s" if N > 1 else ""}')

# Solo DC
ax2.axhline(Vdc(Vm), color=colors['dc'], linewidth=1.5, linestyle=':',
            alpha=0.7, label=f'Solo DC = {Vdc(Vm):.2f} V')

ax2.set_xlabel('Tiempo (ms)', fontsize=12)
ax2.set_ylabel('$v_o(t)$ (V)', fontsize=12)
ax2.set_xlim(0, 2 * T * 1000)
ax2.set_ylim(-1, Vm + 2)
ax2.legend(loc='upper right', fontsize=9, ncol=2)
ax2.grid(True, alpha=0.3)

# Anotación del error residual
partial_5 = dc.copy()
for n in range(1, 6):
    partial_5 += harmonics[n]
error_max = np.max(np.abs(vo_exact - partial_5))
ax2.annotate(f'Error máx. (5 armónicos) = {error_max:.3f} V ({error_max/Vm*100:.2f}%)',
             xy=(0.02, 0.02), xycoords='axes fraction', fontsize=10,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='gray'))

fig2.savefig(os.path.join(OUTPUT_DIR, 'nota7_reconstruccion_fourier.png'),
             dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig2)
print("Generada: nota7_reconstruccion_fourier.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 3: Espectro de amplitudes (diagrama de barras)
# ═══════════════════════════════════════════════════════════════
fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(14, 6),
                                   gridspec_kw={'width_ratios': [3, 2]})
fig3.suptitle('Espectro de Fourier del voltaje de salida — Rectificador tipo puente\n'
              f'$V_m\' = {Vm}$ V, $f = {f}$ Hz',
              fontsize=13, fontweight='bold')

# (a) Barras de amplitud
freqs = [0] + [2 * n * f for n in range(1, N_harmonics + 1)]
amps_pico = [Vdc(Vm)] + [abs(Cn(n, Vm)) for n in range(1, N_harmonics + 1)]
bar_colors = [colors['dc']] + [colors[n] for n in range(1, N_harmonics + 1)]
bar_labels = ['DC'] + [f'$n={n}$\n({2*n*f} Hz)' for n in range(1, N_harmonics + 1)]

bars = ax3a.bar(range(len(freqs)), amps_pico, color=bar_colors, edgecolor='black',
                linewidth=0.5, width=0.65)

# Etiquetas de valor sobre cada barra
for i, (bar, amp) in enumerate(zip(bars, amps_pico)):
    ax3a.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
              f'{amp:.3f} V', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3a.set_xticks(range(len(freqs)))
ax3a.set_xticklabels(bar_labels, fontsize=9)
ax3a.set_ylabel('Amplitud pico (V)', fontsize=11)
ax3a.set_title('(a) Amplitudes absolutas', fontsize=11, loc='left')
ax3a.grid(True, axis='y', alpha=0.3)
ax3a.set_ylim(0, max(amps_pico) * 1.25)

# (b) Amplitudes relativas a DC (%)
amps_rel = [100 * amp / Vdc(Vm) for amp in amps_pico]
bars_b = ax3b.bar(range(len(freqs)), amps_rel, color=bar_colors, edgecolor='black',
                  linewidth=0.5, width=0.65)

for i, (bar, rel) in enumerate(zip(bars_b, amps_rel)):
    ax3b.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
              f'{rel:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3b.set_xticks(range(len(freqs)))
ax3b.set_xticklabels(bar_labels, fontsize=9)
ax3b.set_ylabel('Amplitud relativa a DC (%)', fontsize=11)
ax3b.set_title('(b) Porcentaje respecto a $V_{DC}$', fontsize=11, loc='left')
ax3b.grid(True, axis='y', alpha=0.3)
ax3b.set_ylim(0, 115)

fig3.tight_layout(rect=[0, 0, 1, 0.90])
fig3.savefig(os.path.join(OUTPUT_DIR, 'nota7_espectro_armonicos.png'),
             dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig3)
print("Generada: nota7_espectro_armonicos.png")

# ═══════════════════════════════════════════════════════════════
# FIGURA 4: Espectro en frecuencia con referencia a 60 Hz
# ═══════════════════════════════════════════════════════════════
fig4, ax4 = plt.subplots(figsize=(12, 6))
fig4.suptitle('Espectro de Fourier del voltaje de salida — Rectificador tipo puente\n'
              f'$V_m\' = {Vm}$ V, $f = {f}$ Hz — Eje en frecuencia (Hz)',
              fontsize=13, fontweight='bold')

# Posiciones en el eje de frecuencia (Hz real)
freqs_hz = [0] + [2 * n * f for n in range(1, N_harmonics + 1)]
amps_abs = [Vdc(Vm)] + [abs(Cn(n, Vm)) for n in range(1, N_harmonics + 1)]

# Colores para cada componente
stem_colors = [colors['dc']] + [colors[n] for n in range(1, N_harmonics + 1)]

for i, (freq, amp, col) in enumerate(zip(freqs_hz, amps_abs, stem_colors)):
    # Línea vertical (stem)
    ax4.vlines(freq, 0, amp, colors=col, linewidth=3, zorder=3)
    # Marcador circular en la punta
    ax4.plot(freq, amp, 'o', color=col, markersize=10, zorder=4,
             markeredgecolor='black', markeredgewidth=0.8)
    # Anotación con valor
    if i == 0:
        label_text = f'DC\n{amp:.2f} V'
    else:
        label_text = f'{amp:.3f} V\n({amp/Vdc(Vm)*100:.1f}% DC)'
    y_offset = 0.35 if amp > 1 else 0.15
    ax4.annotate(label_text, xy=(freq, amp + y_offset),
                 ha='center', va='bottom', fontsize=9, fontweight='bold',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                           edgecolor=col, alpha=0.9))

# Marcar las frecuencias de referencia (múltiplos de 60 Hz)
for mult in range(0, 12):
    freq_ref = mult * f
    ax4.axvline(freq_ref, color='gray', linewidth=0.3, linestyle=':', alpha=0.5)

# Etiquetas del eje x: múltiplos de f (0f a 10f = 0 a 600 Hz)
n_multiples = 11  # 0 a 10
xtick_positions = [m * f for m in range(n_multiples)]
ax4.set_xticks(xtick_positions)
ax4.set_xticklabels([f'{x}' for x in xtick_positions], fontsize=8)

# Eje x secundario: múltiplos de f
ax4_top = ax4.secondary_xaxis('top')
ax4_top.set_xticks(xtick_positions)
ax4_top.set_xticklabels([f'{m}$f$' for m in range(n_multiples)], fontsize=9, color='#555')
ax4_top.set_xlabel('Múltiplos de $f$ = 60 Hz', fontsize=10, color='#555')

ax4.set_xlabel('Frecuencia (Hz)', fontsize=12)
ax4.set_ylabel('Amplitud pico (V)', fontsize=12)
ax4.set_xlim(-20, 10.5 * f)
ax4.set_ylim(0, Vdc(Vm) * 1.35)
ax4.grid(True, axis='y', alpha=0.3)

# Sombrear zona de armónicos impares (ausentes) para resaltar que solo hay pares
for mult in [1, 3, 5, 7, 9]:
    center = mult * f
    ax4.axvspan(center - 15, center + 15, alpha=0.06, color='red', zorder=0)

# Leyenda explicativa
ax4.annotate('Zonas rojas claras = armónicos impares\n(ausentes por simetría de onda completa)',
             xy=(0.98, 0.95), xycoords='axes fraction', fontsize=8,
             ha='right', va='top', style='italic', color='#888',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#ccc'))

fig4.tight_layout(rect=[0, 0, 1, 0.90])
fig4.savefig(os.path.join(OUTPUT_DIR, 'nota7_espectro_frecuencia.png'),
             dpi=150, bbox_inches='tight', facecolor='white')
plt.close(fig4)
print("Generada: nota7_espectro_frecuencia.png")

print("\n✅ Todas las imágenes de Nota7 (Fourier) generadas correctamente.")
