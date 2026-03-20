<!--
::METADATA::
type: reference
topic_id: pro-directives
file_id: PRO-directives
status: active
audience: ai_context
last_updated: 2026-03-20
-->

# Directivas — Módulo 05: Proyecto Final (PRO)

> Hereda reglas de [AGENTS.md](../../AGENTS.md).

---

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (PRO-01 a PRO-02) |
| `methods/` | Procedimientos paso a paso |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `assets/` | Imágenes PNG generadas por scripts Python |
| `Notas/` | Material de clase pendiente de migrar a `theory/` |

---

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `PRO-01-Teoria-Fuente-Regulador-Transistorizado.md` | 5.1.1 Fuente con regulador transistorizado | draft |
| `PRO-02-Teoria-Fuente-Regulador-CI.md` | 5.1.2 Fuente con regulador de CI | draft |

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
- **Enfoque:** Diseño práctico e integrador
- **Al generar gráficas:** Usar matplotlib, guardar en `assets/`, documentar parámetros
- **Al generar soluciones:** Paso a paso con unidades, simulaciones y justificación de componentes
- **Prerrequisitos:** Todos los módulos anteriores (01-04)

---

## Enfoque del Proyecto

Este módulo es **integrador**. El proyecto final debe demostrar:

1. Comprensión de rectificación y filtrado (Módulo 01)
2. Uso de transistores como reguladores (Módulos 02-03)
3. Análisis de pequeña señal para estabilidad (Módulo 04)
