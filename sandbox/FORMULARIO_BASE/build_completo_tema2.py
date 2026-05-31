import re

input_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2.md'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2-completo.md'

with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Aproximación no marcada I_C \approx \beta I_B
text = text.replace(
    r'| **Región Activa** | Polarización Directa | Polarización Inversa | Amplificador lineal de corriente ($I_C \approx \beta I_B$). |',
    r'| **Región Activa** | Polarización Directa | Polarización Inversa | Amplificador lineal de corriente ($I_C \approx \beta I_B$, válido si $I_{CEO} \ll \beta I_B$). |'
)
text = text.replace(
    r'$$' + '\n' + r'    I_C = \beta I_B' + '\n' + r'    $$',
    r'$$' + '\n' + r'    I_C \approx \beta I_B' + '\n' + r'    $$' + '\n' + r'    > [!NOTE]' + '\n' + r'    > **Aproximación**: Válido cuando $I_{CEO} \ll \beta I_B$. Rigurosamente $I_C = \beta I_B + I_{CEO}$.'
)

# 2. Problema conceptual de linealidad (Efecto Early)
text = text.replace(
    r'La corriente de salida es lineal e independiente de $V_{CE}$, gobernada por:',
    r'La corriente de salida es casi lineal y depende ligeramente de $V_{CE}$ (Efecto Early), gobernada aproximadamente por:'
)
# Add early equation into the Early Effect section
text = text.replace(
    r'1. Un incremento sutil en las corrientes $I_E$ e $I_C$ para un voltaje $V_{BE}$ constante en las curvas de entrada.',
    r'1. Un incremento sutil en las corrientes $I_E$ e $I_C$ para un voltaje $V_{BE}$ constante en las curvas de entrada. Matemáticamente: $I_C = \beta I_B \left(1 + \frac{V_{CE}}{V_A}\right)$ donde $V_A$ es el Voltaje Early.'
)

# 3. Saturación V_BE(sat)
text = text.replace(
    r'| **Saturación** | Polarización Directa | Polarización Directa | Interruptor cerrado ($V_{CE(\text{sat})} \approx 0.2\text{ V}$). |',
    r'| **Saturación** | Polarización Directa | Polarización Directa | Interruptor cerrado ($V_{CE(\text{sat})} \approx 0.2\text{ V}$ y $V_{BE(\text{sat})} \approx 0.8\text{ V}$). |'
)

# 4. Fórmula peligrosa en diseño de switch
text = text.replace(
    r'$$' + '\n' + r'I_{B(\text{sat},\min)} = \frac{I_{C(\text{sat})}}{\beta}' + '\n' + r'$$',
    r'$$' + '\n' + r'I_{B(\text{sat},\min)} = \frac{I_{C(\text{sat})}}{\beta}' + '\n' + r'$$' + '\n' + r'Para asegurar una conmutación robusta en diseño real, se sobrediseña inyectando una corriente mayor utilizando un $\beta_{\text{forzado}}$ (ej. $\beta / 5$ o $\beta = 10$):' + '\n' + r'$$' + '\n' + r'I_B \ge \frac{I_{C(\text{sat})}}{\beta_{\text{forzado}}}' + '\n' + r'$$'
)


nuevos_temas = r"""

---

## Tema Adicional: Modelos Físicos, Parámetros AC y Otras Configuraciones

### 1. Ecuación de Shockley del BJT
La ecuación exponencial fundamental que relaciona la corriente de colector con la tensión base-emisor:
$$
I_C = I_S e^{\frac{V_{BE}}{V_T}}
$$
Derivadas importantes para pequeña señal:
* **Transconductancia ($g_m$):**
  $$
  g_m = \frac{I_C}{V_T}
  $$
* **Resistencia dinámica de emisor ($r_e$):**
  $$
  r_e = \frac{V_T}{I_E} \approx \frac{V_T}{I_C}
  $$

### 2. Parámetros Básicos de Pequeña Señal (AC) en Emisor Común
* **Ganancia de voltaje ($A_v$):**
  $$
  A_v \approx -\frac{R_C}{r_e}
  $$
* **Ganancia de corriente ($A_i$):**
  $$
  A_i \approx \beta
  $$
* **Impedancia de entrada en la base ($Z_{in(\text{base})}$):**
  $$
  Z_{in(\text{base})} \approx \beta r_e
  $$

### 3. Características Clave por Configuración
* **Base Común (B-com):**
  * Ganancia de corriente: $A_i \approx \alpha < 1$
  * Ganancia de voltaje: Alta
  * Impedancia de entrada: Muy baja
  * Impedancia de salida: Alta
* **Colector Común (C-com) o Seguidor de Emisor:**
  * Ganancia de voltaje: $A_v \approx 1$
  * Ganancia de corriente: Alta ($\beta + 1$)
  * Impedancia de entrada: Alta
  * Impedancia de salida: Baja

### 4. Estabilidad Matemática Térmica
El factor de estabilidad evalúa cuánto se desvía la corriente de colector ante variaciones térmicas en la corriente de fuga.
$$
S = \frac{\partial I_C}{\partial I_{CBO}}
$$
> [!NOTE]
> **Deriva Térmica**: Si la temperatura sube ($T \uparrow$), entonces $V_{BE} \downarrow$ y las fugas $I_{CBO} \uparrow$, lo cual fuerza a $I_C \uparrow$. La resistencia de emisor ($R_E$) es fundamental porque introduce realimentación negativa para compensar y frenar este incremento.

---

## Método Rápido de Análisis (Estrategia Práctica para Exámenes)

Este compendio de métodos prácticos te permitirá sobrevivir al 90% de los ejercicios analíticos sin perder tiempo en derivaciones físicas.

### 1. Método Universal de Polarización DC
Sigue estos pasos en orden para resolver casi cualquier circuito BJT en activa:
1. **Paso 1:** Asume siempre $V_{BE} \approx 0.7\text{ V}$ para transistores de silicio.
2. **Paso 2:** Calcula $I_B$ resolviendo la malla de entrada. Luego calcula $I_C = \beta I_B$.
3. **Paso 3:** Calcula $V_{CE}$ resolviendo la malla de salida.
4. **Paso 4:** Verifica la región analizando los voltajes obtenidos:
   * **Corte:** $V_{BE} < 0.7\text{ V}$
   * **Activa:** $V_C > V_B$
   * **Saturación:** $V_C \le V_B$ o $V_{CE} \approx 0.2\text{ V}$

### 2. Método Rápido de Recta de Carga
El examen típico exige dibujar la recta y situar el punto Q.
1. **Punto de Corte (Eje X):** Haz $I_C = 0 \implies V_{CE} = V_{CC}$
2. **Punto de Saturación (Eje Y):** Haz $V_{CE} = 0 \implies I_C = \frac{V_{CC}}{R_C + R_E}$
3. **Punto Q:** Sitúa las coordenadas $(V_{CEQ}, I_{CQ})$ halladas en el Paso 3 del método universal sobre la línea recta.

### 3. Estados de Conmutación (Switching)
Memoriza esta tabla visual para circuitos digitales:

| Estado | $I_B$ | $I_C$ | $V_{CE}$ |
|--------|-------|-------|----------|
| **Corte** (OFF) | $0$ | $0$ | $V_{CC}$ |
| **Activa** (Amp) | Media | $\beta I_B$ | Intermedio |
| **Saturación** (ON) | Alta | Máxima | $\approx 0.2\text{ V}$ |

### 4. Memorización de Gráficas
Los profesores evalúan mucho el entendimiento visual:
* **Curva de Entrada ($I_B$ vs $V_{BE}$):** Es idéntica a la curva de un diodo polarizado en directa.
* **Curva de Salida ($I_C$ vs $V_{CE}$):** Es una "familia de curvas horizontales" separadas por escalones de $I_B$.
  * **Saturación:** La pared casi vertical a la izquierda ($V_{CE} < 0.2\text{ V}$).
  * **Activa:** Las líneas horizontales en el centro.
  * **Ruptura (Breakdown):** El quiebre abrupto hacia arriba a la derecha extrema.

---
"""

glossary_marker = '## Glosario de Variables\n\n'
parts = text.split(glossary_marker)

if len(parts) == 2:
    main_text = parts[0]
    glossary = parts[1]
    
    main_text += nuevos_temas
    
    new_vars = {
        '$A_v$': 'Ganancia de voltaje en pequeña señal (adimensional o V/V).',
        '$A_i$': 'Ganancia de corriente en pequeña señal (adimensional o A/A).',
        '$g_m$': 'Transconductancia del transistor BJT (S o A/V).',
        '$I_S$': 'Corriente de saturación inversa intrínseca de la unión base-emisor (A).',
        '$r_e$': 'Resistencia dinámica diferencial de emisor en el modelo $\\pi$ o T ($\\Omega$).',
        '$S$': 'Factor de estabilidad térmica (adimensional).',
        '$V_A$': 'Voltaje de Early, proyecta la convergencia de las curvas de salida en la región activa (V).',
        '$V_{BE(\\text{sat})}$': 'Voltaje de saturación base-emisor, requerido para forzar la conducción plena (V).',
        '$Z_{in(\\text{base})}$': 'Impedancia de entrada vista desde el terminal de base ($\\Omega$).',
        '$\\beta_{\\text{forzado}}$': 'Ganancia de corriente degradada o asumida forzosamente para asegurar saturación en diseño de switch (adimensional).'
    }
    
    lines = glossary.strip().split('\n')
    var_dict = {}
    for line in lines:
        m = re.match(r'^\*\s*\*\*(.*?)\*\*:\s*(.*)', line)
        if m:
            var_dict[m.group(1)] = m.group(2)
            
    for k, v in new_vars.items():
        var_dict[k] = v
        
    final_glossary = glossary_marker
    for k in sorted(var_dict.keys()):
        final_glossary += f'* **{k}**: {var_dict[k]}\n'
        
    final_text = main_text + final_glossary
else:
    final_text = text + nuevos_temas

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(final_text)

print("File generated successfully.")
