<!--
::METADATA::
type: reference
topic_id: fet-directives
file_id: FET-directives
status: active
audience: ai_context
last_updated: 2026-03-20
-->

# Directivas — Módulo 03: Transistor Unipolar (FET)

> Hereda reglas de [AGENTS.md](../../AGENTS.md).

---

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (FET-01 a FET-06) |
| `methods/` | Procedimientos paso a paso |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `assets/` | Imágenes PNG generadas por scripts Python |
| `Notas/` | Material de clase pendiente de migrar a `theory/` |

---

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `FET-01-Teoria-Polarizacion-Fija.md` | 3.1.1 Polarización fija | draft |
| `FET-02-Teoria-Autopolarizacion.md` | 3.1.2 Autopolarización (curva universal) | draft |
| `FET-03-Teoria-Divisor-Voltaje.md` | 3.2 Divisor de voltaje (curva universal) | draft |
| `FET-04-Teoria-Compuerta-Drenador-Comun.md` | 3.3 Compuerta y drenador común | draft |
| `FET-05-Teoria-Polarizacion-MOSFET.md` | 3.4 Polarización de MOSFET | draft |
| `FET-06-Teoria-Redes-Combinadas.md` | 3.5 Redes combinadas | draft |

---

## Directiva de Migración de Contenido: Notas/ → theory/

> **IMPORTANTE:** Cuando exista contenido en `Notas/`, debe clasificarse y migrar a sus respectivos archivos en `theory/`.

### Proceso de migración

Al migrar contenido de Notas/ a theory/:

1. **Extraer** teoría validada, ecuaciones y fórmulas
2. **Preservar** referencias a imágenes generadas (actualizar rutas a `assets/`)
3. **Incluir** ejemplos resueltos como secciones de aplicación
4. **Mantener** formato estándar con bloque `::METADATA::`
5. **Eliminar** la nota original solo cuando todo su contenido esté migrado

---

## Directivas Específicas para IA

- **Audiencia:** Ingeniería (universitario)
- **Formato de salida:** Markdown con LaTeX para ecuaciones
- **Al generar gráficas:** Usar matplotlib, guardar en `assets/`, documentar parámetros
- **Al generar soluciones:** Paso a paso con unidades y contexto físico
- **Prerrequisito:** Módulo 01 (Diodos)
