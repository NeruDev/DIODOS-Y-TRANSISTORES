<!--
::METADATA::
type: reference
topic_id: bjt-directives
file_id: BJT-directives
status: active
audience: ai_context
last_updated: 2026-03-20
-->

# Directivas — Módulo 02: Transistor Bipolar (BJT)

> Hereda reglas de [AGENTS.md](../../AGENTS.md).

---

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (BJT-01 a BJT-06) |
| `methods/` | Procedimientos paso a paso |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `assets/` | Imágenes PNG generadas por scripts Python |
| `Notas/` | Material de clase pendiente de migrar a `theory/` |

---

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `BJT-01-Teoria-Caracteristicas-Parametros.md` | 2.1 Características, parámetros y punto de operación | draft |
| `BJT-02-Teoria-Polarizacion-Emisor-Comun.md` | 2.2.1 Emisor común (fija, emisor, divisor, realimentación) | draft |
| `BJT-03-Teoria-Polarizacion-Base-Comun.md` | 2.2.2 Base común | draft |
| `BJT-04-Teoria-Polarizacion-Colector-Comun.md` | 2.2.3 Colector común | draft |
| `BJT-05-Teoria-Conmutacion.md` | 2.3 Conmutación | draft |
| `BJT-06-Teoria-Estabilidad.md` | 2.4 Estabilidad | draft |

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
