import re

input_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1.md'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1-completo.md'

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Pequeña señal
text = text.replace(
    r'$$' + '\n' + r'  \hat{v}_d \ll n V_T \quad (\text{típicamente } \hat{v}_d < 5\text{ mV})' + '\n' + r'  $$',
    r'$$' + '\n' + r'  \hat{v}_d \ll n V_T' + '\n' + r'  $$' + '\n\n> [!NOTE]\n> **Criterio de pequeña señal**: $\hat{v}_d < 5\text{ mV}$ (o a veces $10\text{ mV}$) es un "criterio conservador típico" aceptado habitualmente.'
)
# fallback inline replacement if my newline guess is wrong
text = text.replace(
    r'\hat{v}_d \ll n V_T \quad (\text{típicamente } \hat{v}_d < 5\text{ mV})',
    r'\hat{v}_d \ll n V_T' + '\n$$' + '\n\n> [!NOTE]\n> **Criterio de pequeña señal**: $\hat{v}_d < 5\text{ mV}$ (o a veces $10\text{ mV}$) es un "criterio conservador típico" aceptado.'
)

# 2. Potencia Reactiva
text = text.replace(
    'potencia reactiva o ruido armónico de AC',
    'potencia en componente AC, potencia armónica o potencia no útil (no es potencia reactiva pura, ya que la carga es resistiva)'
)
text = text.replace(
    'potencia reactiva o ruido armónico de AC',
    'potencia en componente AC, potencia armónica o potencia no útil'
)
text = text.replace(
    'potencia reactiva o ruido armónico',
    'potencia en componente AC o potencia no útil'
)

# 3. Rectificadores Reales
vrms_note = '\n\n> [!NOTE]\n> **Aproximación**: Este es un modelo aproximado válido cuando $V_m \gg V_D$. La forma exacta requiere integración angular porque el diodo no conduce todo el semiciclo:\n> $$\n> V_{rms} = \sqrt{\\frac{1}{2\pi} \\int_{\\theta_{on}}^{\\pi-\\theta_{on}} (v_s - V_D)^2 d\\theta}\n> $$\n> donde $\\theta_{on} = \\arcsin\\left(\\frac{V_D}{V_m}\\right)$.'

text = text.replace(
    r'V_{rms} = \frac{V_{s,\text{pico}} - V_D}{2}',
    r'V_{rms} = \frac{V_{s,\text{pico}} - V_D}{2}' + vrms_note
)
text = text.replace(
    r'V_{rms} = \frac{V_m - 2V_D}{\sqrt{2}}',
    r'V_{rms} \approx \frac{V_m - 2V_D}{\sqrt{2}}' + vrms_note
)

# 4. PIV Puente
text = text.replace(
    r'\text{PIV} = V_m - V_D',
    r'\text{PIV} \approx V_m' + '\n\n> [!NOTE]\n> *Más exactamente $\text{PIV} = V_m - V_D$, pero en la práctica se diseña con $V_m$ para conservar el margen.*'
)

# 5. Fourier Warning
fourier_warning = '\n\n> [!WARNING]\n> **Validez de la Serie**: Esta serie es correcta SOLO para rectificación de onda completa ideal, con carga resistiva pura y SIN filtro. Con un capacitor en paralelo, la serie cambia completamente (aparecen picos de corriente y cambia la función temporal).'
text = text.replace(
    r'a_n = \frac{-4 V_m}{\pi (4n^2 - 1)}',
    r'a_n = \frac{-4 V_m}{\pi (4n^2 - 1)}' + fourier_warning
)

# 6. Nuevos temas
nuevos_temas = """

---

## Tema Adicional: Multiplicadores, Sujetadores y Diodos Especiales

### 1. Multiplicadores de Voltaje

Permiten elevar el voltaje pico de entrada mediante arreglos de diodos y capacitores.

* **Ecuación Ideal (sin carga)**:
  $$
  V_o \approx n \cdot V_m
  $$
  > [!WARNING]
  > **Modelo ideal sin carga**: En la práctica, las cascadas tipo Cockcroft-Walton se desploman brutalmente al conectarles carga debido al rizo y la caída acumulada en los diodos.

### 2. Sujetadores (Clampers)

Desplazan el nivel de DC de la señal de entrada.

* **Sujetador Positivo**:
  $$
  v_o(t) \approx v_i(t) + V_m
  $$
* **Sujetador Negativo**:
  $$
  v_o(t) \approx v_i(t) - V_m
  $$
* **Condición Clave de Diseño**: Para que el capacitor mantenga la carga durante el semiciclo de no conducción:
  $$
  R C \gg T
  $$

### 3. Diodo Zener

* **Porcentaje de Regulación de Línea**:
  $$
  \%Reg = \frac{V_{NL} - V_{FL}}{V_{FL}} \times 100\%
  $$
* **Condición de Regulación**: Para que el Zener mantenga el voltaje estable, la corriente debe permanecer dentro de los límites seguros:
  $$
  I_{Z(min)} < I_Z < I_{Z(max)}
  $$

### 4. Diodos Especiales

* **Diodo Schottky**: Presenta conmutación muy rápida y poca carga almacenada.
  $$
  V_D \approx 0.2\text{ V} - 0.3\text{ V}
  $$
* **Diodo Varactor**: Su capacitancia de unión varía de forma inversamente proporcional a la tensión inversa. Todo gira alrededor de esta capacitancia variable inversa.
  $$
  C_j \propto \frac{1}{(V_R)^n}
  $$
* **Diodo Túnel**: Presenta una **región de resistencia negativa** en su curva característica. Gráficamente siempre se pide identificar esta zona inestable.

---

## Método Rápido de Análisis (Estrategia Práctica para Exámenes)

Este método universal te resolverá la gran mayoría de los ejercicios sin perderte en integrales innecesarias.

### 1. El Método Universal (ON/OFF)
Siempre empieza suponiendo los estados de los diodos en DC:
1. **Supón**: Diodo ON o diodo OFF.
2. **Reemplaza**:
   * **ON** $\\rightarrow$ Cortocircuito (o fuente de $0.7\\text{V}$).
   * **OFF** $\\rightarrow$ Circuito abierto.
3. **Resuelve** el circuito lineal resultante (Mallas/Nodos).
4. **Verifica**:
   * Si asumiste ON, la corriente debe salir $I_D > 0$. Si sale $I_D < 0$, tu suposición inicial era falsa.
   * Si asumiste OFF, el voltaje debe salir $V_D < 0.7\\text{V}$.

### 2. Para Gráficas (Recortadores y Sujetadores)
1. Identifica las regiones temporales (divide el tiempo en **ON** y **OFF**).
2. Construye funciones por tramos.
3. Dibuja qué parte de la onda pasa y qué parte se recorta o desplaza.

### 3. Aproximaciones Memorizadas (¡Claves!)
* **Media Onda**:
  $$ V_{DC} \approx 0.318 V_m $$
  $$ V_{rms} \approx 0.500 V_m $$
  $$ \eta \approx 40.6\% $$
* **Onda Completa**:
  $$ V_{DC} \approx 0.636 V_m $$
  $$ V_{rms} \approx 0.707 V_m $$
  $$ \eta \approx 81.2\% $$

### 4. Análisis de Rectificadores (Paso Obligado)
**SIEMPRE** dibuja qué pasa en el semiciclo positivo y negativo:
* Indica claramente qué diodo conduce y cuál se bloquea.
* Traza el recorrido de la corriente en la carga.
*(Sin esto, acabarás inventando corrientes fantasma).*

### 5. Fourier Rápido
No expandas series completas salvo que te lo exijan. Memoriza:
* La componente DC ($a_0/2$).
* El primer armónico ($a_1$).
* La frecuencia fundamental del rizo ($2f$ para onda completa).

### 6. Relaciones Rápidas para Filtros
* **Capacitor grande** $\\implies$ Rizo baja ($r \\downarrow$).
* **Frecuencia grande** $\\implies$ Rizo baja ($r \\downarrow$).
* **Carga mayor (menor $R_L$)** $\\implies$ Rizo sube ($r \\uparrow$).

---
"""

# Extract the Glossary
glossary_marker = '## Glosario de Variables\n\n'
parts = text.split(glossary_marker)

if len(parts) == 2:
    main_text = parts[0]
    glossary = parts[1]
    
    # Append the new topics to main_text
    main_text += nuevos_temas
    
    # We should add any new variables to the glossary.
    new_vars = {
        '$V_{NL}$': 'Voltaje en vacío (No-Load) (V).',
        '$V_{FL}$': 'Voltaje a plena carga (Full-Load) (V).',
        '$C_j$': 'Capacitancia de la unión del varactor (F).',
        '$V_R$': 'Tensión inversa aplicada al varactor (V).',
        '$\\theta_{on}$': 'Ángulo de encendido o conducción (rad).'
    }
    
    # parse existing glossary
    lines = glossary.strip().split('\n')
    var_dict = {}
    for line in lines:
        m = re.match(r'^\*\s*\*\*(.*?)\*\*:\s*(.*)', line)
        if m:
            var_dict[m.group(1)] = m.group(2)
            
    # merge new vars
    for k, v in new_vars.items():
        var_dict[k] = v
        
    # rebuild glossary
    final_glossary = glossary_marker
    for k in sorted(var_dict.keys()):
        final_glossary += f'* **{k}**: {var_dict[k]}\n'
        
    final_text = main_text + final_glossary
else:
    # If something fails, just append
    final_text = text + nuevos_temas

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_text)

print("File generated successfully.")
