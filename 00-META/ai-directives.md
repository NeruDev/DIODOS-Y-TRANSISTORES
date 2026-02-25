<!--
::METADATA::
type: reference
topic_id: ai-directives
file_id: ai-directives
status: stable
audience: ai_context
last_updated: 2026-02-23
-->

# 🔧 Directivas Técnicas para IA — Diodos y Transistores

> Reglas técnicas complementarias al [Contrato IA](ia-contract.md).

Este documento recopila las mejores prácticas, correcciones y observaciones técnicas derivadas del desarrollo del material didáctico del repositorio.

## 1. Generación de Gráficas en Python

Para la creación de curvas características de componentes electrónicos (como diodos y transistores), se deben seguir las siguientes pautas para asegurar claridad y precisión técnica:

### Manejo de Escalas Dispares
Los componentes electrónicos suelen tener zonas de operación con magnitudes extremadamente diferentes (ej. Amperios en directa vs Nanoamperios en inversa).
*   **Problema:** Una escala lineal simple oculta los detalles de las corrientes de fuga ($I_S$).
*   **Solución Recomendada:** Generar dos visualizaciones separadas o usar "Insets" (gráficas insertadas).
    *   **Gráfica Global:** Para ver el comportamiento general (ruptura y conducción).
    *   **Gráfica de Zoom:** Específica para la región cercana al origen para mostrar que $I \neq 0$.

### Simulación de Ecuaciones
*   Al modelar la ecuación de Shockley, incluir términos para la **Región de Ruptura** si se desea visualizar el componente completo, ya que la ecuación estándar solo cubre directa e inversa ideal sin ruptura.
*   Código ejemplo para ruptura simplificada:
    ```python
    i_breakdown = -Is * np.exp(-(V - Vbr) / (n * Vt))
    ```

## 2. Formato LaTeX en Documentación Markdown

El proyecto utiliza renderizado de fórmulas matemáticas mediante LaTeX.

### Sintaxis
*   **Inline (en línea):** Usar un solo signo de dólar `$ E = mc^2 $`.
*   **Bloque (centrado):** Usar doble signo de dólar `$$` al inicio y final de la línea.

### ⚠️ Escritura Automatizada (Terminal/Bash)
Un error común al generar documentación automáticamente desde la terminal es la **desaparición de fórmulas LaTeX**.

*   **El Problema:** Al usar comandos como `cat >> archivo <<EOF`, la terminal (bash) interpreta los símbolos `$` como variables de entorno (ej. `$V_T` intenta buscar la variable `V_T`). Si no existe, la reemplaza por vacío.
*   **La Solución:** Siempre usar comillas simples en el delimitador del *Heredoc* (`'EOF'`) para evitar la interpolación de variables.

**Incorrecto (destruye LaTeX):**
```bash
cat >> archivo.md <<EOF
El voltaje es $V_T$
EOF
# Resultado en archivo: "El voltaje es "
```

**Correcto (preserva LaTeX):**
```bash
cat >> archivo.md <<'EOF'
El voltaje es $V_T$
EOF
# Resultado en archivo: "El voltaje es $V_T$"
```

## 3. Gestión de Imágenes Generadas (Limpieza de `media/generated/`)

Cuando una imagen nueva **reemplace** a una imagen anterior:

*   Actualizar las referencias del repo para apuntar al archivo vigente.
*   Eliminar del repositorio la imagen anterior que ya no se usa.
*   Verificar que no existan enlaces rotos después del reemplazo.

Regla operativa: `media/generated/` debe contener solo imágenes con uso actual en documentación o flujo de generación vigente.

## 4. Política de Scripts de Generación de Gráficos

Cada gráfico generado debe cumplir las siguientes reglas:

1. **Un script por gráfico (o conjunto temático coherente).** Cada script Python en `00-META/tools/` produce una o varias imágenes estrechamente relacionadas. No mezclar gráficos de temas distintos en un mismo script.
2. **Referencia cruzada obligatoria.** Toda imagen generada debe estar referenciada en:
   - La **nota o documento** `.md` donde se utiliza (enlace Markdown estándar).
   - El archivo de control **[Control_Scripts.md](tools/Control_Scripts.md)**, donde se lleva el registro centralizado de todos los scripts, sus imágenes y las notas que las consumen.
3. **Metadatos en cada script.** Todo script `.py` debe incluir un bloque de comentarios con metadatos al inicio (dentro del docstring o inmediatamente después) con al menos:
   - `script_id`: nombre del archivo sin extensión.
   - `module`: prefijo del módulo (`DIO`, `BJT`, `FET`, `AMP`, `PRO`).
   - `generates`: lista de imágenes PNG que produce.
   - `referenced_by`: lista de archivos `.md` que enlazan las imágenes.
   - `last_updated`: fecha de última modificación.
4. **Actualización del registro.** Al crear, modificar o eliminar un script, actualizar `Control_Scripts.md` de forma inmediata.

## 5. Anti-solapamiento de Etiquetas en Schemdraw

Al generar esquemáticos con `schemdraw`, las etiquetas de los elementos colisionan fácilmente entre sí cuando hay varios componentes próximos. Las siguientes reglas eliminan este problema:

### 5.1 No usar `\n` en `.label()` para múltiples líneas de texto

Cuando un elemento tiene dos datos que mostrar (p.ej. nombre y valor), **no** concatenarlos en un solo `.label()` con salto de línea. En su lugar, usar **dos llamadas `.label()` separadas** con `loc=` distintos:

```python
# INCORRECTO — puede solaparse con etiquetas vecinas
elm.Inductor2().down().label('$N_2$\n$V_s = 12\\,V_{rms}$', loc='right')

# CORRECTO — cada etiqueta en su propio anclaje
elm.Inductor2().down() \
    .label('$N_2$',               loc='right', ofst=0.15) \
    .label('$V_s = 12\\,V_{rms}$', loc='bot',   ofst=0.15)
```

### 5.2 Etiqueta sobre el núcleo del transformador

La etiqueta de relación de vueltas (`10:1`, `n:1`) debe colocarse **elevada** con respecto a la parte superior del núcleo para no colisionar con las cabezas de las bobinas:

```python
# offset vertical mínimo recomendado: +0.70 u sobre prim.start[1]
d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label('$10:1$')
```

Con `+0.35` u la etiqueta queda encima de los bumps del secundario; con `+0.70` u queda libre.

### 5.3 Fuente sinusoidal con dos líneas de texto

Para `SourceSin()` con voltaje y frecuencia indicados, usar `ofst ≥ 0.55` para separar el texto del conductor superior:

```python
elm.SourceSin().up().label(
    '$V_p = 120\\,V_{rms}$\n$f = 60\\,Hz$', loc='left', ofst=0.55
)
```

### 5.4 Transformador simétrico con `.flip()`

El secundario de un transformador debe dibujarse con `.flip()` para que sus bumps apunten **hacia el núcleo** (igual que el primario):

```python
# Primario — bumps a la derecha (dirección natural de .down())
prim = elm.Inductor2(loops=3).down()

# Secundario — bumps a la izquierda (hacia el núcleo)
sec  = elm.Inductor2(loops=3).down().flip().at((prim.start[0] + 2.5, prim.start[1]))
```

Separación mínima entre primario y secundario: **2.5 u**, para dejar espacio al núcleo y sus etiquetas.

### 5.5 Backend matplotlib sin GUI (`Agg`)

En entornos sin display (terminales sin tkinter), `schemdraw` y `matplotlib` fallan con `TclError`. Añadir **siempre** al inicio de cada script, **antes** de cualquier otro import de matplotlib:

```python
import matplotlib
matplotlib.use('Agg')  # backend sin GUI — obligatorio en entornos sin display
import matplotlib.pyplot as plt
import schemdraw
```

### 5.6 No usar `.label()` directamente sobre `Inductor2` para etiquetas de voltaje

> **Origen:** Corrección iterativa del esquemático del rectificador monofásico de derivación central (`DIO-gen-nota5-rectificador-onda-completa-central.py`), iteración 1.

**Problema:** Al colocar etiquetas como `$V_m$` o `$V_s$` con `.label()` directamente sobre un `elm.Inductor2()`, el texto se renderiza **encima de los bumps** (ondulaciones) de la bobina, haciéndolo ilegible. Los bumps del inductor ocupan espacio considerable y `.label()` no puede calcular un offset suficiente automáticamente.

**Solución:** Usar elementos `elm.Label()` independientes posicionados con coordenadas explícitas, desplazados horizontalmente fuera de la zona de los bumps:

```python
# INCORRECTO — texto tapado por los bumps del inductor
sec_top = elm.Inductor2(loops=3).down().label('$V_m$', loc='right')

# CORRECTO — Label externo con coordenadas explícitas
sec_top = elm.Inductor2(loops=3).down().flip()
sec_x = sec_top.start[0]
sec_mid_y = (sec_top.start[1] + sec_top.end[1]) / 2
d += elm.Label().at((sec_x + 1.1, sec_mid_y)).label('$V_m$')
```

El offset horizontal recomendado es `+1.1 u` cuando el inductor tiene `.flip()` (bumps a la izquierda) o `−1.1 u` cuando los bumps apuntan a la derecha.

### 5.7 Elementos `Gap` para indicadores de polaridad de voltaje — offset mínimo

> **Origen:** Iteración 2 del esquemático del rectificador de derivación central.

**Problema:** Al usar `elm.Gap()` como indicador de polaridad (`+`/`−`) para el voltaje sobre un componente, si el Gap queda adyacente a un `Inductor2`, sus etiquetas colisionan igualmente con los bumps de la bobina.

**Solución:** Reservar `elm.Gap()` para componentes con cuerpo compacto (resistores, diodos, fuentes), y usar `elm.Label()` con coordenadas explícitas cuando el indicador de polaridad debe estar cerca de un inductor. Cuando sí se use Gap, asegurar un offset mínimo de `0.55 u` entre el Gap y el borde del inductor.

### 5.8 Carga $R_L$ «interna» vs. «externa» en rectificadores con derivación central

> **Origen:** Iteraciones 2 y 3 del esquemático del rectificador de derivación central.

**Problema:** Al conectar $R_L$ entre el punto de unión de cátodos (nodo de salida) y la toma central (CT) del transformador, la ruta natural en schemdraw tiende a trazar la resistencia por un camino **externo** — bajando desde los cátodos, recorriendo horizontalmente y subiendo hasta CT. Esto produce un esquemático donde $R_L$ aparece «fuera» del circuito, lejos de los diodos.

**Solución:** Colocar $R_L$ **horizontalmente** a la altura del punto medio del secundario (`sec_mid_y`), conectando el nodo de cátodos directamente con CT usando `.left()`:

```python
# sec_mid_y = altura media entre el inicio del secundario superior y el fin del inferior
sec_mid_y = (sec_top.start[1] + sec_bot.end[1]) / 2

# Unir cátodos y bajar hasta sec_mid_y
d += elm.Line().at(cathode_junction).down().to((cathode_junction[0], sec_mid_y))

# RL horizontal hacia la izquierda hasta la coordenada x de CT
d += elm.Resistor().left().to((ct_x, sec_mid_y)).label('$R_L$', loc='bot')
```

Esto coloca $R_L$ visualmente **entre** D1 y D2, dentro de la topología del circuito.

### 5.9 Espacio vertical insuficiente entre ramas de diodos paralelos

> **Origen:** Iteración 3 del esquemático del rectificador de derivación central.

**Problema:** Con `loops=3` en ambos secundarios del transformador, la separación vertical entre D1 (rama superior) y D2 (rama inferior) era insuficiente para alojar $R_L$ horizontalmente sin solapamiento visual.

**Solución:** Aumentar el número de loops del primario a `loops=4` (o más) y mantener `loops=3` en cada mitad del secundario. Esto incrementa la altura total del transformador y proporciona espacio vertical suficiente entre las ramas:

```python
# Primario más alto → más separación vertical total
prim = elm.Inductor2(loops=4).down()       # 4 loops = mayor altura

# Cada mitad del secundario mantiene 3 loops
sec_top = elm.Inductor2(loops=3).down().flip()
sec_bot = elm.Inductor2(loops=3).down().flip()
```

**Regla práctica:** El número de loops del primario debe ser ≥ la suma de loops de ambas mitades del secundario dividida por 1.5, para garantizar espacio interno suficiente.

### 5.10 Resumen de errores — Esquemático rectificador derivación central

| Iteración | Error | Síntoma | Corrección aplicada |
|-----------|-------|---------|---------------------|
| 1 | `.label()` sobre `Inductor2` | Texto tapado por bumps de la bobina | Usar `elm.Label()` con coordenadas explícitas (§5.6) |
| 1 | $R_L$ sin conexión a CT | Resistencia flotante, circuito abierto | Redirigir retorno de $R_L$ al nodo CT del transformador |
| 2 | Gap de voltaje adyacente a inductor | Etiquetas `+`/`−` sobre los bumps | Usar Labels explícitos en lugar de Gap cerca de inductores (§5.7) |
| 2 | $R_L$ por ruta externa | Circuito visualmente incorrecto | Reubicar $R_L$ horizontalmente entre D1 y D2 (§5.8) |
| 3 | $R_L$ fuera de la topología | Resistencia «rodea» al circuito | Colocar $R_L$ con `.left()` a la altura `sec_mid_y` (§5.8) |
| 3 | Espacio vertical insuficiente | $R_L$ solapa con diodos/inductores | Aumentar loops del primario a 4 (§5.9) |

---

## 6. Sintaxis Correcta de PowerShell para Ejecutar Python

El entorno de trabajo usa **PowerShell** (pwsh) en Windows. La sintaxis difiere de bash en puntos críticos.

### 6.1 Operador de llamada `&` — obligatorio

Para ejecutar un ejecutable cuya ruta es una cadena (especialmente con espacios), se **requiere** el operador `&` (call operator). Sin él, PowerShell interpreta la cadena como expresión y lanza `ParserError: Unexpected token`.

```powershell
# INCORRECTO — genera ParserError
"G:/ruta/python.exe" "script.py"

# CORRECTO
& "G:/ruta/python.exe" "script.py"
```

### 6.2 Forma estándar para scripts de este repositorio

```powershell
# Patrón canónico: cambiar directorio + ejecutar script
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
& "G:/REPOSITORIOS GITHUB/DIODOS Y TRANSISTORES/.venv/Scripts/python.exe" "00-META/tools/SCRIPT.py"

# En una sola línea (separar comandos con ;)
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"; & "G:/REPOSITORIOS GITHUB/DIODOS Y TRANSISTORES/.venv/Scripts/python.exe" "00-META/tools/SCRIPT.py"
```

### 6.3 Reglas adicionales

| Regla | Correcto | Incorrecto |
|-------|----------|------------|
| Cambiar directorio | `Set-Location "ruta"` | `cd ruta` (alias, evitar en scripts) |
| Separar comandos en una línea | `cmd1; cmd2` | `cmd1 && cmd2` (sintaxis bash) |
| Capturar salida y errores | `comando 2>&1` | `comando 2>/dev/null` (bash) |
| Variables de entorno | `$env:VAR` | `$VAR` (bash) |
| Activar venv | `& ".venv\Scripts\Activate.ps1"` | `source .venv/bin/activate` (bash) |
