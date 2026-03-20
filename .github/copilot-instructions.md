# Instrucciones de Contexto para GitHub Copilot

> **Hereda de:** [AGENTS.md](../AGENTS.md) — Fuente de verdad centralizada
> **Última sincronización:** 2026-03-20

---

## Instrucciones para Copilot

1. **Leer** [AGENTS.md](../AGENTS.md) como primera acción obligatoria.
2. **Consultar** `manifest.json` del módulo objetivo.
3. **Seguir** las directivas específicas en `directives.md` del módulo.

---

## Referencias Rápidas

| Documento | Propósito |
|-----------|-----------|
| [AGENTS.md](../AGENTS.md) | Directiva general completa |
| [00-meta/repo-map.md](../00-meta/repo-map.md) | Mapa estructural |
| [00-meta/naming-conventions.md](../00-meta/naming-conventions.md) | Estándares de nomenclatura |
| [00-meta/standards.md](../00-meta/standards.md) | Directivas técnicas |
| [00-meta/tools/Control_Scripts.md](../00-meta/tools/Control_Scripts.md) | Registro de scripts |

---

## Extensiones Específicas para Copilot

### Arquitectura (Resumen)

```
topics/
├── 01-circuitos-diodos/  (DIO)
├── 02-transistor-bjt/    (BJT)
├── 03-transistor-fet/    (FET)
├── 04-amplificadores/    (AMP)
└── 05-proyecto-final/    (PRO)
```

### Símbolos LaTeX estándar

| Símbolo | Notación | Descripción |
|---------|----------|-------------|
| $V_T$ | `$V_T$` | Voltaje térmico |
| $I_S$ | `$I_S$` | Corriente de saturación inversa |
| $V_{BR}$ | `$V_{BR}$` | Voltaje de ruptura |
| $V_K$ | `$V_K$` | Voltaje de umbral/rodilla |
| $V_Z$ | `$V_Z$` | Voltaje Zener |
| $\beta$ | `$\beta$` | Ganancia de corriente (BJT) |
| $g_m$ | `$g_m$` | Transconductancia |
| $r_e$ | `$r_e$` | Resistencia dinámica de emisor |

---

## Reglas Anti-Solapamiento de Etiquetas en schemdraw

Reglas derivadas de la práctica con esquemáticos de rectificadores y transformadores:

### 1. No usar `\n` en `.label()` para dos datos distintos

Usar dos llamadas `.label()` separadas con `loc=` distintos:

```python
# INCORRECTO — solapamiento con etiquetas vecinas
elm.Inductor2(loops=3).down().label('$N_2$\n$V_s = 12\\,V_{rms}$', loc='right')

# CORRECTO — etiquetas independientes en diferentes anclajes
elm.Inductor2(loops=3).down() \
    .label('$N_2$',                 loc='right', ofst=0.15) \
    .label('$V_s = 12\\,V_{rms}$', loc='bot',   ofst=0.15)
```

### 2. Etiqueta sobre el núcleo del transformador

Elevarla al menos `+0.70 u` sobre `prim.start[1]`:

```python
d += elm.Label().at((cx_nucleo, prim.start[1] + 0.70)).label('$10:1$')
```

### 3. `SourceSin()` con voltaje y frecuencia

Usar `ofst ≥ 0.55` para que el texto no tape el conductor superior:

```python
elm.SourceSin().up().label(
    '$V_p = 120\\,V_{rms}$\n$f = 60\\,Hz$', loc='left', ofst=0.55
)
```

### 4. Transformador simétrico

El secundario usa `.flip()` para que sus bumps apunten hacia el núcleo; separación mínima primario–secundario de **2.5 u**:

```python
prim = elm.Inductor2(loops=3).down()  # bumps a la derecha
sec  = elm.Inductor2(loops=3).down().flip().at((prim.start[0] + 2.5, prim.start[1]))
```

### 5. Backend sin GUI

Añadir siempre antes de cualquier otro import de matplotlib/schemdraw:

```python
import matplotlib
matplotlib.use('Agg')  # backend sin GUI — evita TclError de tkinter
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements as elm
```

### 6. No usar `.label()` sobre `Inductor2` para voltajes

Los bumps de la bobina tapan el texto. Usar `elm.Label()` con coordenadas explícitas offset `+1.1 u` del lado limpio:

```python
# INCORRECTO — texto tapado por bumps
sec = elm.Inductor2(loops=3).down().label('$V_m$', loc='right')

# CORRECTO — Label externo posicionado
sec = elm.Inductor2(loops=3).down().flip()
d += elm.Label().at((sec.start[0] + 1.1, (sec.start[1]+sec.end[1])/2)).label('$V_m$')
```

### 7. $R_L$ en rectificadores con derivación central

Colocar **horizontalmente** a la altura media del secundario (`sec_mid_y`), entre el nodo de cátodos y CT:

```python
sec_mid_y = (sec_top.start[1] + sec_bot.end[1]) / 2
d += elm.Line().at(cathode_junction).down().to((cathode_junction[0], sec_mid_y))
d += elm.Resistor().left().to((ct_x, sec_mid_y)).label('$R_L$', loc='bot')
```

### 8. Gap de polaridad cerca de inductores

`elm.Gap()` colisiona con bumps de `Inductor2`. Usar `elm.Label()` explícito para indicadores de polaridad junto a bobinas.

### 9. Espacio vertical entre ramas paralelas

Si se necesita alojar componentes entre D1 y D2, aumentar `loops` del primario (≥ 4):

```python
prim = elm.Inductor2(loops=4).down()       # más loops = más separación vertical
sec_top = elm.Inductor2(loops=3).down().flip()
sec_bot = elm.Inductor2(loops=3).down().flip()
```

---

## Sintaxis PowerShell para Windows

El entorno es **PowerShell (pwsh)**. Su sintaxis difiere de bash:

```powershell
# Patrón canónico — cambiar directorio y ejecutar script Python
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
& ".venv\Scripts\python.exe" "00-meta/tools/SCRIPT.py"

# En una sola línea
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"; & ".venv\Scripts\python.exe" "00-meta/tools/SCRIPT.py" 2>&1
```

### Errores frecuentes y correcciones

| Problema | Incorrecto (bash) | Correcto (PowerShell) |
|----------|-------------------|-----------------------|
| Ejecutar path como comando | `"ruta/python.exe" "script.py"` | `& "ruta/python.exe" "script.py"` |
| Cambiar directorio | `cd "ruta"` | `Set-Location "ruta"` |
| Encadenar comandos | `cmd1 && cmd2` | `cmd1; cmd2` |
| Capturar stderr | `cmd 2>/dev/null` | `cmd 2>&1` |
| Activar venv | `source .venv/bin/activate` | `& ".venv\Scripts\Activate.ps1"` |

> **Regla:** En PowerShell, cualquier ruta de ejecutable pasada como cadena **requiere** el operador `&` para ser invocada. Sin él, PowerShell lanza `ParserError: Unexpected token`.

### Directivas técnicas para gráficos

- **Escalas dispares:** Componentes electrónicos tienen zonas con magnitudes extremadamente diferentes (ej. Amperios en directa vs. Nanoamperios en inversa). Usar gráficas separadas o insets (gráficas insertadas) para manejar esto; nunca una sola escala lineal.
- **Ecuación de Shockley:** Incluir el término de ruptura si se desea visualizar el diodo completo: `i_breakdown = -Is * np.exp(-(V - Vbr) / (n * Vt))`
- **Formato de salida:** PNG a 100 DPI como mínimo.
- **Estilo:** Incluir grid, etiquetas de ejes, título, leyenda y anotaciones de las regiones de operación.

### Directivas para esquemáticos de circuitos complejos

Para circuitos con múltiples componentes (multiplicadores, fuentes reguladas, amplificadores multietapa, etc.), aplicar las siguientes reglas:

1. **Especificaciones estándar H3 (recomendadas para circuitos complejos):**
   ```python
   # Parámetros estándar H3 — usar como base para circuitos complejos
   unit_size = 3.5       # Espaciado amplio entre componentes
   comp_length = 3.5     # Longitud de componentes para buena proporción
   separation = 2.0      # Separación generosa entre secciones del circuito
   fontsize = 13         # Etiquetas legibles a cualquier tamaño
   dpi = 300             # Alta resolución para impresión y pantalla
   ```
   - Usar `unit=3.5` o superior en `schemdraw.Drawing()` para espaciado adecuado
   - Usar `dpi=300` o superior para alta resolución y legibilidad
   - Usar `fontsize=13` o superior para etiquetas visibles
   - Usar coordenadas absolutas para posicionamiento preciso de componentes

2. **Layout horizontal (flujo L→R) para circuitos complejos:**
   - **Línea superior única:** conexiones de nodos y componentes activos (positivos)
   - **Línea inferior única:** referencia a tierra física (negativos/GND)
   - Este estándar facilita la lectura del flujo de señal de izquierda a derecha

3. **Colores diferenciados para fines didácticos:**
   - Usar una paleta de colores consistente para distinguir tipos de componentes:
     ```python
     COLOR_FUENTE = '#2563EB'       # Azul - fuentes AC/DC y transformadores
     COLOR_DIODO = '#DC2626'        # Rojo - diodos y semiconductores
     COLOR_CAPACITOR = '#16A34A'    # Verde - capacitores
     COLOR_RESISTOR = '#EA580C'     # Naranja - resistencias
     COLOR_CONEXION = '#374151'     # Gris oscuro - líneas, nodos y tierra
     COLOR_VOLTAJE = '#7C3AED'      # Violeta - indicadores de voltaje
     COLOR_NODO = '#111827'         # Negro - puntos de nodo
     ```
   - Aplicar colores con `.color(COLOR_X)` en cada elemento de schemdraw

4. **Posicionamiento de etiquetas (CRÍTICO para legibilidad):**
   - **Las etiquetas NUNCA deben solaparse** con líneas de conexión, componentes ni otras etiquetas
   - **Etiquetas en línea superior:** usar `loc='top'` con `ofst=0.3` o superior
   - **Etiquetas en línea inferior:** usar coordenadas absolutas desplazadas (`x - 0.5, y`) para evitar solapamiento con GND
   - **Etiquetas de voltaje:** ubicar en espacio libre, nunca sobre componentes
   - **Aprovechar el espacio extra:** el tamaño ampliado del diagrama permite colocar etiquetas fuera de cualquier elemento
   - Ejemplo de etiqueta desplazada:
     ```python
     # Mal: etiqueta sobre línea de tierra
     d += elm.Label().at(nodo_B).label('B', loc='bot', ofst=0.3)

     # Bien: etiqueta desplazada a la izquierda
     d += elm.Label().at((nodo_B[0] - 0.5, nodo_B[1])).label('B')
     ```

5. **Anotación de voltajes importantes:**
   - Etiquetar voltajes clave del circuito ($V_m$, $V_o$, $V_{C1}$, $V_{C2}$, etc.)
   - Usar `elm.Gap()` con etiquetas `['+', '$V_o$', '−']` para indicadores de polaridad
   - Usar `elm.Label()` para voltajes en nodos específicos
   - Identificar nodos críticos con letras (A, B, C, ...) cuando sea necesario

6. **Espaciado y organización:**
   - Usar transformador compacto: separación primario-secundario de `0.8` a `1.0` unidades
   - Usar coordenadas absolutas `(x, y)` para posicionamiento preciso y evitar solapamientos
   - Usar tres niveles verticales: `y_top`, `y_mid`, `y_bot` para organización clara
   - Usar líneas de conexión explícitas en lugar de superposición de terminales

### Política de scripts de generación

Cada gráfico generado debe cumplir las siguientes reglas:

1. **Un script por gráfico (o conjunto temático coherente).** Cada script Python en `00-meta/tools/` produce una o varias imágenes estrechamente relacionadas. No mezclar gráficos de temas distintos en un mismo script.
2. **Referencia cruzada obligatoria.** Toda imagen generada debe estar referenciada en:
   - La **nota o documento** `.md` donde se utiliza (enlace Markdown estándar).
   - El archivo de control **[Control_Scripts.md](00-meta/tools/Control_Scripts.md)**, donde se lleva el registro centralizado de todos los scripts, sus imágenes y las notas que las consumen.
3. **Metadatos en cada script.** Todo script `.py` debe incluir un bloque `::SCRIPT_METADATA::` en sus comentarios iniciales con al menos:
   - `script_id`: nombre del archivo sin extensión.
   - `module`: prefijo del módulo (`DIO`, `BJT`, `FET`, `AMP`, `PRO`).
   - `generates`: lista de imágenes PNG que produce.
   - `referenced_by`: lista de archivos `.md` que enlazan las imágenes.
   - `last_updated`: fecha de última modificación.
4. **Actualización del registro.** Al crear, modificar o eliminar un script, actualizar `Control_Scripts.md` de forma inmediata.

### Gestión de imágenes generadas (limpieza de `media/generated/`)

Cuando una imagen nueva **reemplace** a una imagen anterior:

- Actualizar las referencias del repo para apuntar al archivo vigente.
- Eliminar del repositorio la imagen anterior que ya no se usa.
- Verificar que no existan enlaces rotos después del reemplazo.

**Regla operativa:** `media/generated/` debe contener solo imágenes con uso actual en documentación o flujo de generación vigente. No se permiten archivos huérfanos.

---

## Sincronización

Este archivo hereda de `AGENTS.md`. Ante cambios estructurales, actualizar primero `AGENTS.md` y luego propagar a este archivo.
