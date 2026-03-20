<!--
::METADATA::
type: reference
topic_id: nomenclatura
file_id: nomenclatura-estandar
status: stable
audience: both
last_updated: 2026-03-20
-->

# 📏 Nomenclatura Estándar — Diodos y Transistores

---

## Patrón de Nombres de Archivos

```
[PREFIJO]-[XX]-[Contenido]-[Tipo].md
```

### Componentes

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `PREFIJO` | 3 letras del módulo | `DIO`, `BJT`, `FET`, `AMP`, `PRO` |
| `XX` | Número de subtema (2 dígitos) | `01`, `02`, ..., `08` |
| `Contenido` | Nombre descriptivo | `Polarizacion`, `Rectificacion`, `EmComun` |
| `Tipo` | Clasificación del archivo | `Intro`, `Teoria`, `Metodos`, `Problemas`, `Respuestas`, `Soluciones`, `Resumen` |

### Tabla de Prefijos

| Módulo | Prefijo | Carpeta |
|--------|---------|---------|
| Circuitos con Diodos | `DIO` | `01-Circuitos-Diodos/` |
| Transistor Bipolar | `BJT` | `02-Transistor-BJT/` |
| Transistor Unipolar | `FET` | `03-Transistor-FET/` |
| Amplificadores | `AMP` | `04-Amplificadores/` |
| Proyecto Final | `PRO` | `05-Proyecto-Final/` |

### Ejemplos Válidos

```
DIO-01-Polarizacion-Intro.md
DIO-01-Polarizacion-Teoria.md
DIO-03-Rectificacion-Metodos.md
DIO-07-Zener-Problemas.md
BJT-01-Caracteristicas-Intro.md
BJT-02-EmComun-Teoria.md
FET-02-Autopolarizacion-Metodos.md
AMP-02-AmplificadorBJT-Teoria.md
PRO-01-FuenteTransistorizada-Intro.md
```

---

## Nombres de Carpetas

| Nivel | Convención | Ejemplo |
|-------|------------|---------|
| Módulo | `NN-Nombre-Modulo/` | `01-Circuitos-Diodos/` |
| Subtema | `NN-Nombre-Subtema/` | `03-Rectificacion-Filtrado/` |
| Semántica | minúsculas, sin número | `theory/`, `methods/`, `problems/`, `solutions/` |
| Recursos | minúsculas | `media/`, `media/generated/` |
| Sandbox | PascalCase | `Notas/` |

---

## Bloques `::METADATA::`

Todo archivo `.md` debe comenzar con:

```markdown
<!--
::METADATA::
type: [theory|method|problem|solution|reference|index|cheatsheet|answer-key]
topic_id: [id-del-tema]
file_id: [nombre-archivo-sin-extension]
status: [draft|review|stable|active]
audience: [student|ai_context|both]
last_updated: YYYY-MM-DD
-->
```

### Tipos válidos

| `type` | Descripción | Ubicación típica |
|--------|-------------|------------------|
| `theory` | Desarrollo teórico | `theory/*.md` |
| `method` | Procedimiento | `methods/*.md` |
| `problem` | Enunciados | `problems/*.md` |
| `solution` | Soluciones | `solutions/*.md` |
| `index` | Punto de entrada | `*-Intro.md` |
| `cheatsheet` | Resumen de fórmulas | `*-Resumen-*.md` |
| `answer-key` | Tabla de respuestas | `*-Respuestas.md` |
| `reference` | Documentación | Archivos raíz / 00-META |

---

## Sintaxis de Enlaces

| Tipo | Sintaxis |
|------|----------|
| Mismo directorio | `[Intro](DIO-01-Intro.md)` |
| Subdirectorio | `[Teoría](theory/DIO-01-Teoria.md)` |
| Al glosario | `[término](../../glossary.md#termino)` |
| Entre módulos | `[Tema](../02-Transistor-BJT/01-Caracteristicas/)` |

### Header de Navegación Estándar

```markdown
> 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)
```

---

## Notación Matemática (LaTeX)

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
| $V_{GS}$ | `$V_{GS}$` | Voltaje compuerta-fuente (FET) |
| $I_{DSS}$ | `$I_{DSS}$` | Corriente de drenador en saturación |
