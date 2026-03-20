<!--
::METADATA::
type: reference
topic_id: dio-directives
file_id: DIO-directives
status: active
audience: ai_context
last_updated: 2026-03-20
-->

# Directivas — Módulo 01: Circuitos de Aplicación con Diodos

> Hereda reglas de [AGENTS.md](../../AGENTS.md).

---

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (DIO-01 a DIO-08) |
| `methods/` | Procedimientos paso a paso (compartidos por todo el módulo) |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `assets/` | Imágenes PNG generadas por scripts Python |
| `Notas/` | Material de clase pendiente de migrar a `theory/` |

---

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `DIO-01-Teoria-Diodo.md` | 1.1 Polarización y recta de carga | review |
| `DIO-02-Teoria-Circuitos-Serie-Paralelo.md` | 1.2 Circuitos serie, paralelo, serie-paralelo | draft |
| `DIO-03-Teoria-Rectificacion-Filtrado.md` | 1.3.1 Rectificación y filtrado | draft |
| `DIO-04-Teoria-Recortadores.md` | 1.3.2 Recortadores | draft |
| `DIO-05-Teoria-Sujetadores.md` | 1.3.3 Sujetadores | draft |
| `DIO-06-Teoria-Multiplicadores.md` | 1.3.4 Multiplicadores | draft |
| `DIO-07-Teoria-Diodo-Zener.md` | 1.4 Diodo Zener y reguladores | draft |
| `DIO-08-Teoria-Otros-Diodos.md` | 1.5 Otros diodos | draft |

---

## Directiva de Migración de Contenido: Notas/ → theory/

> **IMPORTANTE:** El contenido de `Notas/` debe clasificarse y migrar a sus respectivos archivos en `theory/`.

### Mapeo de archivos

| Archivo en Notas/ | Contenido Principal | Destino en theory/ |
|-------------------|--------------------|--------------------|
| `Nota1.md` | Polarización, modelo del diodo, recta de carga | `DIO-01-Teoria-Diodo.md` |
| `Nota2.md` | Circuitos con múltiples diodos | `DIO-02-Teoria-Circuitos-Serie-Paralelo.md` |
| `Nota3.md` | Pequeña señal, modelo lineal | `DIO-01-Teoria-Diodo.md` (sección avanzada) |
| `Nota4.md` | Rectificador de media onda | `DIO-03-Teoria-Rectificacion-Filtrado.md` |
| `Nota5.md` | Rectificador de onda completa (derivación central) | `DIO-03-Teoria-Rectificacion-Filtrado.md` |
| `Nota6.md` | Rectificador puente | `DIO-03-Teoria-Rectificacion-Filtrado.md` |
| `Nota7.md` | Filtros (inductivo, capacitivo, RC, Fourier) | `DIO-03-Teoria-Rectificacion-Filtrado.md` |
| `Nota8.md` | Recortadores y sujetadores | `DIO-04-Teoria-Recortadores.md`, `DIO-05-Teoria-Sujetadores.md` |

### Proceso de migración

Al migrar contenido de Notas/ a theory/:

1. **Extraer** teoría validada, ecuaciones y fórmulas
2. **Preservar** referencias a imágenes generadas (actualizar rutas a `assets/`)
3. **Incluir** ejemplos resueltos como secciones de aplicación
4. **Mantener** formato estándar con bloque `::METADATA::`
5. **Eliminar** la nota original solo cuando todo su contenido esté migrado

### Criterio de completitud

Un subtema se considera migrado cuando:
- [ ] Toda la teoría relevante está en `theory/`
- [ ] Las ecuaciones están en formato LaTeX correcto
- [ ] Las imágenes están referenciadas desde `assets/`
- [ ] El estado en `manifest.json` cambia a `review` o `stable`

---

## Directivas Específicas para IA

- **Audiencia:** Ingeniería (universitario)
- **Formato de salida:** Markdown con LaTeX para ecuaciones
- **Tareas permitidas:** Explicar conceptos, generar problemas, verificar soluciones, generar gráficas
- **Al generar gráficas:** Usar matplotlib, guardar en `assets/`, documentar parámetros
- **Al generar soluciones:** Siempre paso a paso con unidades y contexto físico
- **Reemplazo de imágenes:** Si una imagen nueva sustituye a otra, actualizar referencias y eliminar la imagen anterior

---

## Lecciones Aprendidas — Esquemáticos schemdraw

Errores documentados durante la generación del esquemático del rectificador de derivación central. Estas reglas complementan [00-meta/standards.md](../../00-meta/standards.md).

### Transformadores con derivación central

1. **Etiquetas de voltaje sobre inductores:** Nunca usar `.label()` directamente sobre `Inductor2`. Los bumps del componente tapan el texto. Usar `elm.Label()` con coordenadas explícitas desplazadas al menos `+1.1 u` horizontalmente.

2. **Conexión de $R_L$ a la toma central:** $R_L$ debe conectarse **horizontalmente** entre el nodo de unión de cátodos y la toma central (CT), a la altura media del secundario (`sec_mid_y`).

3. **Dimensionamiento del transformador:** Si la carga u otros componentes deben caber **entre** las ramas de salida, aumentar `loops` del primario (≥ 4) para ganar altura vertical suficiente.

4. **Indicadores de polaridad:** Usar `elm.Gap()` solo para componentes compactos. Para voltajes del secundario, usar `elm.Label()` en lugar de Gap para evitar solapamiento con los bumps.
