"""
::SCRIPT_METADATA::
Prefix: DIO
Description: Genera el esquema de un regulador de voltaje básico con diodo Zener y carga rectangular.
"""
import schemdraw
import schemdraw.elements as elm
import matplotlib
import os

# Configurar backend no interactivo
matplotlib.use('Agg')

# Configuración de salida
output_dir = '01-Circuitos-Diodos/media/generated'
os.makedirs(output_dir, exist_ok=True)

# Paleta de colores didáctica
COLOR_CONEXION = '#374151'
COLOR_RESISTOR = '#EA580C'
COLOR_DIODO = '#DC2626'
COLOR_VOLTAJE = '#7C3AED'
COLOR_CARGA = '#16A34A'
COLOR_FUENTE = '#2563EB'

with schemdraw.Drawing(show=False) as d:
    # Estilo general
    d.config(unit=3.0, fontsize=13, color=COLOR_CONEXION, lw=2.0)
    
    # Fuente DC de entrada
    V_s = d.add(elm.SourceV().up().label('$V_s$', loc='left', color=COLOR_FUENTE))
    top_left = d.add(elm.Dot())
    
    # Resistencia en serie
    R_s = d.add(elm.Resistor().right().color(COLOR_RESISTOR).label('$R_S$', loc='top').label(r'$I_S \rightarrow$', loc='bot', color=COLOR_CONEXION))
    top_node = d.add(elm.Dot())
    
    # Diodo Zener (polarización inversa: cátodo arriba, ánodo a tierra)
    d.push()
    # down().reverse() lo dibuja descendiendo en la pantalla pero apuntando hacia arriba
    Z = d.add(elm.Zener().down().reverse().color(COLOR_DIODO).label('Zener\n$V_Z$', loc='bot').label(r'$I_Z \downarrow$', loc='top', color=COLOR_CONEXION))
    bot_node = d.add(elm.Dot())
    d.pop()
    
    # Indicador de voltaje Vo paralelo al Zener
    d.push()
    x_gap = top_node.start[0] + 1.2
    d.add(elm.Gap().down().at((x_gap, top_node.start[1])).to((x_gap, bot_node.start[1])).label(['+', '$V_o$', '-'], color=COLOR_VOLTAJE, loc='bot'))
    d.pop()
    
    # Conexión hacia la carga
    L_conn = d.add(elm.Line().right().length(3.0).label(r'$I_L \rightarrow$', loc='top', color=COLOR_CONEXION))
    top_load = d.add(elm.Dot())
    
    # Bloque Rectangular de la CARGA (construido con líneas para asegurar estilo geométrico)
    d.add(elm.Resistor(type='iec').down().color(COLOR_CARGA).label('CARGA', loc='bottom'))
    
    # Retorno a tierra y cierre del circuito
    bot_load = d.add(elm.Dot())
    d.add(elm.Line().left().tox(bot_node.start))
    d.add(elm.Ground())
    d.add(elm.Line().left().tox(V_s.start))
    
    # Guardar esquema
    d.save(f'{output_dir}/DIO-esquema-zener-regulador.png', dpi=300)