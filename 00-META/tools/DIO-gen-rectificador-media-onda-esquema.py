"""
DIO-gen-rectificador-media-onda-esquema.py
───────────────────
Genera el diagrama esquemático de un rectificador de media onda.

Salida:
  - 01-Circuitos-Diodos/media/generated/rectificador_media_onda_esquema.png

::SCRIPT_METADATA::
script_id: DIO-gen-rectificador-media-onda-esquema
module: DIO
generates:
  - rectificador_media_onda_esquema.png
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

filename = os.path.join(OUTPUT_DIR, 'rectificador_media_onda_esquema.png')

# Configuración de dibujo
with schemdraw.Drawing(file=filename, show=False, dpi=150) as d:
    # Fuente AC
    d += (source := elm.SourceSin().up().label('$v_s(t)$', loc='bot')
                                      .label('$V_m \sin(\omega t)$', loc='top'))
    
    # Diodo Rectificador
    d += elm.Diode().right().label('D').label('Ideal', loc='bot', fontsize=10)
    
    # Resistencia de Carga down
    d += (res := elm.Resistor().down().label('$R_{L}$', loc='bot')
                         .label('$+$', loc='top', ofst=(-0.5, -0.2))
                         .label('$-$', loc='bot', ofst=(-0.5, 0.2))
                         .label('$v_o(t)$', loc='top', ofst=(0.5, -0.5)))
    
    # Cierre de malla (tierra común o línea de retorno)
    d += elm.Line().left().to(source.start)
    
    # Tierra referencia (opcional, pero buena práctica)
    d += elm.Ground().at(source.start)

print(f"Generado: {filename}")
