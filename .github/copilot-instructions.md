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

> **Regla:** En PowerShell, cualquier ruta de ejecutable pasada como cadena **requiere** el operador `&` para ser invocada.

---

## Directivas Técnicas para Gráficos

- **Escalas dispares:** Usar gráficas separadas o insets; nunca una sola escala lineal.
- **Ecuación de Shockley:** Incluir término de ruptura si se visualiza diodo completo.
- **Formato de salida:** PNG a 100 DPI mínimo.
- **Estilo:** Grid, etiquetas de ejes, título, leyenda y anotaciones de regiones.

---

## Sincronización

Este archivo hereda de `AGENTS.md`. Ante cambios estructurales, actualizar primero `AGENTS.md` y luego propagar a este archivo.
