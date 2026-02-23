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
