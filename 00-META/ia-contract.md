<!--
::METADATA::
type: reference
topic_id: ia-contract
file_id: ia-contract
status: stable
audience: ai_context
last_updated: 2026-02-07
-->

# 🤖 Contrato IA — Diodos y Transistores

> **DOCUMENTO OBLIGATORIO.** Toda IA que interactúe con este repositorio DEBE leer este archivo primero.

---

## 1. Estructura del Repositorio

| # | Prefijo | Módulo | Descripción |
|---|---------|--------|-------------|
| 01 | `DIO` | Circuitos con Diodos | Polarización, rectificación, recortadores, sujetadores, multiplicadores, Zener, otros diodos |
| 02 | `BJT` | Transistor Bipolar | Características, polarización (EC, BC, CC), conmutación, estabilidad |
| 03 | `FET` | Transistor Unipolar | Polarización (fija, auto, divisor), MOSFET, redes combinadas |
| 04 | `AMP` | Amplificadores | Pequeña señal, amplificador BJT, amplificador JFET |
| 05 | `PRO` | Proyecto Final | Fuentes de alimentación reguladas |

---

## 2. Sistema de Nomenclatura

**Patrón:** `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`

- **PREFIJO:** 3 letras del módulo (`DIO`, `BJT`, `FET`, `AMP`, `PRO`)
- **XX:** Número del subtema (01, 02, ..., 08)
- **Contenido:** Nombre descriptivo en PascalCase
- **Tipo:** `Intro`, `Teoria`, `Metodos`, `Problemas`, `Respuestas`, `Soluciones`, `Resumen`

**Ejemplos válidos:**
```
DIO-01-Polarizacion-Intro.md
DIO-03-Rectificacion-Teoria.md
BJT-02-EmComun-Metodos.md
FET-05-MOSFET-Problemas.md
AMP-02-AmplificadorBJT-Soluciones.md
```

---

## 3. Estructura Obligatoria por Subtema

Cada subtema DEBE contener:

```
XX-[Nombre-Subtema]/
├── manifest.json            — Metadatos y mapa de recursos
├── _directives.md           — Instrucciones específicas del subtema
├── [PREFIX]-XX-*-Intro.md   — Punto de entrada
├── theory/                  — Desarrollo teórico ("el QUÉ")
├── methods/                 — Procedimientos paso a paso ("el CÓMO")
├── problems/                — Ejercicios y enunciados
├── solutions/               — Respuestas y desarrollos
├── media/generated/         — Recursos visuales auto-generados
└── Notas/                   — Zona sandbox (sin validación)
```

---

## 4. Reglas de Generación de Contenido

### Generales
- **SIEMPRE** dar contexto antes de resolver un problema.
- Usar notación estándar según [nomenclatura-estandar.md](nomenclatura-estandar.md).
- Validar contra bibliografía en [bibliografia-general.md](bibliografia-general.md).
- Formato de soluciones: paso a paso con explicación de cada operación.

### Formato Matemático
- **Inline:** `$ expresión $`
- **Bloque:** `$$ expresión $$`
- Usar notación de ingeniería eléctrica estándar.

### Audiencia
- **Nivel:** Ingeniería (universitario).
- **Idioma:** Español.
- **Tono:** Técnico pero accesible, con analogías cuando sean útiles.

### Gráficas y Visualizaciones
- Generar con Python (matplotlib/numpy).
- Guardar en `media/generated/` del subtema correspondiente.
- Incluir código fuente junto a la gráfica.
- Ver [Directivas técnicas](ai-directives.md) para detalles sobre escalas y simulaciones.

---

## 5. Tareas Permitidas para IA

| Tarea | Permitida | Notas |
|-------|-----------|-------|
| Explicar conceptos | ✅ | Con contexto y ejemplos |
| Generar problemas | ✅ | Indicar dificultad |
| Verificar soluciones | ✅ | Paso a paso |
| Generar gráficas | ✅ | Python + matplotlib |
| Crear resúmenes | ✅ | Con fórmulas clave |
| Modificar Notas/ | ⛔ | Zona sandbox exenta |
| Inventar datos | ⛔ | Solo valores realistas |

---

## 6. Zona Sandbox (Notas/)

Cada subtema contiene una carpeta `Notas/` que es **zona libre**:
- **NO VALIDAR** nomenclatura ni formato.
- **NO SUGERIR** correcciones.
- **LEER COMPLETO** si se solicita contexto.
- Cualquier archivo, cualquier formato.
