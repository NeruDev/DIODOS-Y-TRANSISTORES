"""
DIO-gen-ejercicio-rectificador-transformador.py
───────────────────
Genera el diagrama esquemático para el ejercicio de rectificador de media onda con transformador.

Salida:
  - 01-Circuitos-Diodos/media/generated/ejercicio_rectificador_transformador.png

::SCRIPT_METADATA::
script_id: DIO-gen-ejercicio-rectificador-transformador
module: DIO
generates:
  - ejercicio_rectificador_transformador.png
referenced_by:
  - 01-Circuitos-Diodos/Notas/Nota3.md
last_updated: 2026-02-18
"""

import schemdraw
import schemdraw.elements as elm
import os

# Directorio de salida
OUTPUT_DIR = os.path.join("01-Circuitos-Diodos", "media", "generated")
os.makedirs(OUTPUT_DIR, exist_ok=True)
filename = os.path.join(OUTPUT_DIR, 'ejercicio_rectificador_transformador.png')

# Configuración de dibujo
with schemdraw.Drawing(file=filename, show=False, dpi=150) as d:
    # 1. Malla Primaria
    d += (source := elm.SourceSin().up().label(('$120 V_{rms}$', '$60 Hz$'), loc='left'))
    d += elm.Line().right(2)
    
    # Transformador (dibujado manualmente con inductores para control preciso)
    # Primario
    d += (prim := elm.Inductor2().down().label('$N_1$', loc='left'))
    d += elm.Line().left().to(source.start)

    # Núcleo magnético
    core_x = prim.start[0] + 0.5
    d += elm.Line().at((core_x, prim.start[1])).to((core_x, prim.end[1])).linestyle('--').color('gray')
    d += elm.Line().at((core_x + 0.2, prim.start[1])).to((core_x + 0.2, prim.end[1])).linestyle('--').color('gray')

    # Secundario (desplazado a la derecha)
    # Importante: anchor en el start del secundario alineado con el start del primario
    d += (sec := elm.Inductor2().down().at((prim.start[0] + 1.5, prim.start[1])).label('$N_2$', loc='right'))
    
    # Etiqueta de relación de vueltas
    d += elm.Label().at((prim.start[0] + 0.75, prim.start[1])).label('10:1', loc='top')

    # 2. Malla Secundaria
    # Parte superior: Diodo y conexión
    d += elm.Line().right(1.5).at(sec.start)
    d += (D := elm.Diode().right().label('D'))
    
    d += elm.Line().right(1)
    
    # Rama de carga (Resistencia)
    d += (res := elm.Resistor().down().label('$R_L = 5 \Omega$', loc='bot'))

    # Etiquetas de voltaje Vo (usando Gap para no encimar)
    d += elm.Gap().at(res.start).to(res.end).label(['+', '$V_o$', '-'], loc='right', ofst=0.6)
    
    # Corriente Io (flecha al lado de la resistencia)
    d += elm.CurrentLabel(top=True, ofst=1.2, length=1.5).at(res).label('$I_o$')

    # Retorno (parte inferior)
    # Desde el final de la resistencia hasta el final del secundario
    d += elm.Line().left().to(sec.end) # Cierra el circuito visualmente

print(f"Generado: {filename}")
