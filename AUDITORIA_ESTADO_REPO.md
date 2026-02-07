<!--
::METADATA::
type: reference
topic_id: auditoria
file_id: AUDITORIA_ESTADO_REPO
status: active
audience: both
last_updated: 2026-02-07
-->

# 🔍 Auditoría de Estado del Repositorio

> **Generado:** 07 de Febrero, 2026  
> **Tipo:** Manual (pendiente automatización)

---

## Resumen General

| Métrica | Valor |
|---------|-------|
| Módulos totales | 5 |
| Subtemas totales (archivos de teoría) | 25 |
| Archivos de teoría con contenido | 1 (DIO-01) |
| Archivos de teoría vacíos (stub) | 24 |
| Formularios por módulo | 5 (en `formularios/`) |
| Scripts de gráficas | 7 (en `00-META/tools/`) |
| Gráficas generadas (DIO) | 6 |
| Gráficas generables (BJT, FET, AMP, PRO) | ~12 (scripts disponibles) |
| Términos en glosario | ~45 |

---

## Estado por Módulo

### 01 — Circuitos con Diodos (`DIO`)

| Componente | Estado |
|------------|--------|
| 00-Index.md | ✅ |
| manifest.json | ✅ |
| _directives.md | ✅ |
| DIO-00-Intro.md | ✅ |
| Notas/README.md | ✅ |

| Archivo de Teoría | Contenido |
|--------------------|-----------|
| DIO-01-Teoria-Diodo.md | ✅ Completo |
| DIO-02-Teoria-Circuitos-Serie-Paralelo.md | 📝 Stub |
| DIO-03-Teoria-Rectificacion-Filtrado.md | 📝 Stub |
| DIO-04-Teoria-Recortadores.md | 📝 Stub |
| DIO-05-Teoria-Sujetadores.md | 📝 Stub |
| DIO-06-Teoria-Multiplicadores.md | 📝 Stub |
| DIO-07-Teoria-Diodo-Zener.md | 📝 Stub |
| DIO-08-Teoria-Otros-Diodos.md | 📝 Stub |

| Carpeta | Archivos |
|---------|----------|
| formularios/ | ✅ DIO-Formulario.md |
| methods/ | ⬜ Vacía |
| problems/ | ⬜ Vacía |
| solutions/ | ⬜ Vacía |
| media/generated/ | ✅ 6 PNGs |

### 02 — Transistor BJT (`BJT`)

| Componente | Estado |
|------------|--------|
| 00-Index.md | ✅ |
| manifest.json | ✅ |
| _directives.md | ✅ |
| BJT-00-Intro.md | ✅ |
| Notas/README.md | ✅ |

| Archivo de Teoría | Contenido |
|--------------------|-----------|
| BJT-01-Teoria-Caracteristicas-Parametros.md | 📝 Stub |
| BJT-02-Teoria-Polarizacion-Emisor-Comun.md | 📝 Stub |
| BJT-03-Teoria-Polarizacion-Base-Comun.md | 📝 Stub |
| BJT-04-Teoria-Polarizacion-Colector-Comun.md | 📝 Stub |
| BJT-05-Teoria-Conmutacion.md | 📝 Stub |
| BJT-06-Teoria-Estabilidad.md | 📝 Stub |

| Carpeta | Archivos |
|---------|----------|
| formularios/ | ✅ BJT-Formulario.md |
| methods/ | ⬜ Vacía |
| problems/ | ⬜ Vacía |
| solutions/ | ⬜ Vacía |
| media/generated/ | 🔧 Script disponible (ejecutar para generar) |

### 03 — Transistor FET (`FET`)

| Componente | Estado |
|------------|--------|
| 00-Index.md | ✅ |
| manifest.json | ✅ |
| _directives.md | ✅ |
| FET-00-Intro.md | ✅ |
| Notas/README.md | ✅ |

| Archivo de Teoría | Contenido |
|--------------------|-----------|
| FET-01-Teoria-Polarizacion-Fija.md | 📝 Stub |
| FET-02-Teoria-Autopolarizacion.md | 📝 Stub |
| FET-03-Teoria-Divisor-Voltaje.md | 📝 Stub |
| FET-04-Teoria-Compuerta-Drenador-Comun.md | 📝 Stub |
| FET-05-Teoria-Polarizacion-MOSFET.md | 📝 Stub |
| FET-06-Teoria-Redes-Combinadas.md | 📝 Stub |

| Carpeta | Archivos |
|---------|----------|
| formularios/ | ✅ FET-Formulario.md |
| methods/ | ⬜ Vacía |
| problems/ | ⬜ Vacía |
| solutions/ | ⬜ Vacía |
| media/generated/ | 🔧 Script disponible (ejecutar para generar) |

### 04 — Amplificadores (`AMP`)

| Componente | Estado |
|------------|--------|
| 00-Index.md | ✅ |
| manifest.json | ✅ |
| _directives.md | ✅ |
| AMP-00-Intro.md | ✅ |
| Notas/README.md | ✅ |

| Archivo de Teoría | Contenido |
|--------------------|-----------|
| AMP-01-Teoria-Introduccion-Pequena-Senal.md | 📝 Stub |
| AMP-02-Teoria-Amplificador-BJT.md | 📝 Stub |
| AMP-03-Teoria-Amplificador-JFET.md | 📝 Stub |

| Carpeta | Archivos |
|---------|----------|
| formularios/ | ✅ AMP-Formulario.md |
| methods/ | ⬜ Vacía |
| problems/ | ⬜ Vacía |
| solutions/ | ⬜ Vacía |
| media/generated/ | 🔧 Script disponible (ejecutar para generar) |

### 05 — Proyecto Final (`PRO`)

| Componente | Estado |
|------------|--------|
| 00-Index.md | ✅ |
| manifest.json | ✅ |
| _directives.md | ✅ |
| PRO-00-Intro.md | ✅ |
| Notas/README.md | ✅ |

| Archivo de Teoría | Contenido |
|--------------------|-----------|
| PRO-01-Teoria-Fuente-Regulador-Transistorizado.md | 📝 Stub |
| PRO-02-Teoria-Fuente-Regulador-CI.md | 📝 Stub |

| Carpeta | Archivos |
|---------|----------|
| formularios/ | ✅ PRO-Formulario.md |
| methods/ | ⬜ Vacía |
| problems/ | ⬜ Vacía |
| solutions/ | ⬜ Vacía |
| media/generated/ | 🔧 Script disponible (ejecutar para generar) |

---

## Archivos Raíz

| Archivo | Estado |
|---------|--------|
| README.md | ✅ Completo |
| WIKI_INDEX.md | ✅ Completo |
| glossary.md | ✅ Completo (~45 términos) |
| Temario.md | ✅ Completo |
| Plantilla de Arquitectura Modular Universal.md | ✅ Referencia |

## 00-META

| Archivo | Estado |
|---------|--------|
| ia-contract.md | ✅ Completo |
| ai-directives.md | ✅ Completo (migrado de Directivas generales) |
| nomenclatura-estandar.md | ✅ Completo |
| bibliografia-general.md | ✅ Completo |
| study-guide.md | ✅ Completo |
| tools/README.md | ✅ Guía de herramientas Python |
| tools/*.py | ✅ 7 scripts de generación de gráficos |

---

## Próximos Pasos Recomendados

1. Desarrollar contenido de teoría para los stubs del Módulo 01 (DIO-02 a DIO-08).
2. Crear archivos de `methods/` y `problems/` para el Módulo 01.
3. Generar scripts de visualización adicionales en `media/generated/`.
4. Avanzar con el contenido del Módulo 02 (BJT) una vez completo el Módulo 01.
5. Poblar progresivamente `solutions/` con resoluciones detalladas.
