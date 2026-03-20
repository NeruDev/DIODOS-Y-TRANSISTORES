<!--
::METADATA::
type: reference
topic_id: amp-directives
file_id: AMP-directives
status: active
audience: ai_context
last_updated: 2026-03-20
-->

# Directivas — Módulo 04: Amplificadores (AMP)

> Hereda reglas de [AGENTS.md](../../AGENTS.md).

---

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (AMP-01 a AMP-03) |
| `methods/` | Procedimientos paso a paso |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `assets/` | Imágenes PNG generadas por scripts Python |
| `Notas/` | Material de clase pendiente de migrar a `theory/` |

---

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `AMP-01-Teoria-Introduccion-Pequena-Senal.md` | 4.1 Introducción a amplificadores en pequeña señal | draft |
| `AMP-02-Teoria-Amplificador-BJT.md` | 4.2 Amplificador con BJT (modelo re, híbrido, 2 puertos) | draft |
| `AMP-03-Teoria-Amplificador-JFET.md` | 4.3 Amplificador con JFET y MOSFET | draft |

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
- **Prerrequisitos:** Módulo 02 (BJT), Módulo 03 (FET)
