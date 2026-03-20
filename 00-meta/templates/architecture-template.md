<!--
::METADATA::
type: reference
topic_id: repo-template
file_id: plantilla-arquitectura
status: stable
audience: both
last_updated: 2026-01-05
-->

# 🏗️ Plantilla de Arquitectura Modular para Repositorios Educativos

> **Propósito:** Plantilla universal para crear repositorios de conocimiento estructurado siguiendo el patrón "Jardín Digital". Adaptable a cualquier dominio educativo (Matemáticas, Física, Programación, Idiomas, etc.).

---

## 📖 INTRODUCCIÓN

### ¿Qué es un "Jardín Digital"?

Un **Jardín Digital** es un sistema de gestión de conocimiento que combina:

1. **Estructura modular:** Cada tema es una unidad autónoma y completa
2. **Interconexión:** Términos enlazados entre sí como una wiki
3. **Doble audiencia:** Navegable por humanos y procesable por IA
4. **Validación:** Contenido respaldado por fuentes académicas
5. **Automatización:** Scripts que mantienen la integridad sin intervención manual

### Principios Fundamentales

| Principio | Descripción | Beneficio |
|-----------|-------------|-----------|
| **Encapsulamiento** | Cada subtema contiene TODO lo necesario | No hay dependencias rotas |
| **Identidad Única** | Sistema de prefijos identifica cada módulo | Organización automática |
| **Separación Semántica** | Distinguir teoría de procedimientos | Respuestas precisas |
| **Automatización** | Scripts validan y enlazan contenido | Mantenimiento mínimo |
| **Escalabilidad** | Estructura replicable infinitamente | Crece sin caos |

---

## 🏛️ ARQUITECTURA DE TRES NIVELES

### Diagrama Conceptual

```
REPOSITORIO (Nivel 0)
│
├── ARCHIVOS RAÍZ ────────────► Navegación + Identidad + Glosario
├── 00-META/ ─────────────────► Reglas + Herramientas + Estándares
│
└── MÓDULOS (Nivel 1)
    └── SUBTEMAS (Nivel 2)
        ├── Configuración ────► manifest.json + _directives.md
        ├── Contenido ────────► theory/ + methods/ + problems/ + solutions/
        └── Recursos ─────────► media/ + applications/ + diagnostic/
```

---

## 📂 NIVEL 0: RAÍZ DEL REPOSITORIO

### Estructura Obligatoria

```
[NOMBRE-REPOSITORIO]/
│
├── 📄 NAVEGACIÓN PRINCIPAL
│   ├── README.md                    # Portada del proyecto
│   ├── WIKI_INDEX.md                # Tabla de contenidos maestra
│   └── glossary.md                  # Diccionario de términos
│
├── 📄 DOCUMENTACIÓN
│   ├── Guía de Arquitectura.md      # Documentación técnica
│   └── AUDITORIA_ESTADO_REPO.md     # Reporte de salud auto-generado
│
├── 🎛️ 00-META/                      # Centro de control
│   └── [Ver sección siguiente]
│
└── 📚 MÓDULOS DE CONTENIDO
    ├── 01-[Módulo-1]/
    ├── 02-[Módulo-2]/
    └── NN-[Módulo-N]/
```

### Descripción de Archivos Raíz

#### 1. `README.md` — Portada del Repositorio

**Función:** Primera impresión. Define la identidad del proyecto.

**Contenido obligatorio:**
- Nombre y descripción del proyecto
- Tabla de módulos con estados
- Instrucciones diferenciadas (humanos vs IAs)
- Diagrama de dependencias (skill tree)
- Enlaces rápidos a recursos principales

**Plantilla:**

```markdown
<!--
::METADATA::
type: index
topic_id: repo-readme
file_id: README
status: stable
audience: both
-->

# 📚 [Nombre del Repositorio]

> **[Descripción breve del propósito]**

## 🧭 Navegación Rápida

| Para... | Ir a... |
|---------|---------|
| 📖 Estudiantes | [Guía de Estudio](00-META/study-guide.md) |
| 🤖 Asistentes IA | [Contrato IA](00-META/ia-contract.md) |
| 📋 Contenido completo | [Índice Wiki](WIKI_INDEX.md) |
| 📚 Definiciones | [Glosario](glossary.md) |

## 📊 Módulos Disponibles

| # | Prefijo | Módulo | Estado | Subtemas |
|---|---------|--------|--------|----------|
| 01 | `XX` | Nombre | ✅ Activo | Lista... |
| 02 | `YY` | Nombre | 🔄 En progreso | Lista... |

## 🗺️ Mapa de Dependencias

[Diagrama Mermaid mostrando prerrequisitos entre módulos]
```

---

#### 2. `WIKI_INDEX.md` — Tabla de Contenidos Maestra

**Función:** Mapa de navegación centralizado. Permite encontrar CUALQUIER recurso desde un solo lugar.

**Estructura:**

```markdown
# 📑 Índice Wiki

## Módulo 01: [Nombre]
- **Subtema 1.1:** [Nombre](ruta/Intro.md)
  - [Teoría](ruta/theory/archivo.md)
  - [Métodos](ruta/methods/archivo.md)
  - [Problemas](ruta/problems/archivo.md)
  - [Soluciones](ruta/solutions/archivo.md)
```

---

#### 3. `glossary.md` — Diccionario Centralizado

**Función:** Vocabulario común con definiciones consistentes. Destino de enlaces automáticos.

**Estructura de cada término:**

```markdown
### [término]

> **Definición formal:** [Definición técnica precisa]
> 
> **Analogía/Intuición:** [Explicación accesible con metáforas]
> 
> **Ver también:** [enlaces a términos relacionados]
```

**Ejemplo:**

```markdown
### función

> **Definición formal:** Una regla que asigna a cada elemento de un conjunto A 
> exactamente un elemento del conjunto B.
> 
> **Analogía:** Piensa en una máquina expendedora: insertas una moneda (entrada) 
> y siempre obtienes el mismo producto (salida).
>
> **Ver también:** [dominio](#dominio), [rango](#rango)
```

---

## 🎛️ CARPETA `00-META` — CENTRO DE CONTROL

### Estructura Completa

```
00-META/
│
├── 🤖 DIRECTIVAS PARA IA
│   ├── ia-contract.md           # LEY SUPREMA - Reglas fundamentales
│   └── ai-directives.md         # Reglas técnicas complementarias
│
├── 📏 ESTÁNDARES Y NORMAS
│   ├── nomenclatura-estandar.md # Convenciones de nombrado
│   ├── notation-cheatsheet.md   # Símbolos y notación estándar
│   └── bibliografia-general.md  # Fuentes académicas autorizadas
│
├── 🔍 HERRAMIENTAS DE AUDITORÍA
│   ├── audit-file-list.md       # Lista de archivos obligatorios
│   ├── audit-table-issues.md    # Registro de problemas
│   ├── directory-tree.md        # Árbol de directorios ideal
│   └── repo-tests.md            # Pruebas de integridad
│
├── 🎓 RECURSOS PARA USUARIOS
│   ├── study-guide.md           # Guía de navegación
│   ├── prompts-for-students.md  # Prompts prediseñados para IA
│   └── plantilla-respuestas.md  # Modelo para soluciones
│
└── 🔧 tools/                    # Scripts de automatización
    ├── validate_repo.py         # Auditor de estructura
    ├── link_knowledge_base.py   # Auto-vinculador al glosario
    ├── check_tables.py          # Validador de tablas
    └── graphics/                # Subsistema gráfico (opcional)
```

---

### Archivos Críticos de `00-META`

#### `ia-contract.md` — La Ley Suprema

**Propósito:** Documento OBLIGATORIO para cualquier IA. Define las reglas que gobiernan toda interacción.

**Contenido obligatorio:**

```markdown
# Contrato IA — [Nombre del Repositorio]

## 1. Estructura del Repositorio

| # | Prefijo | Módulo | Descripción |
|---|---------|--------|-------------|
| 01 | `XX` | Nombre | Descripción breve |

## 2. Sistema de Nomenclatura

Patrón: `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`

- **PREFIJO:** 2-3 letras del módulo
- **XX:** Número del subtema (01, 02...)
- **Contenido:** Nombre descriptivo
- **Tipo:** Teoria, Metodos, Problemas, Respuestas, Intro

## 3. Estructura Obligatoria por Subtema

Cada subtema DEBE contener:
- `manifest.json` — Metadatos y mapa de recursos
- `_directives.md` — Instrucciones específicas
- `[PREFIX]-XX-*-Intro.md` — Punto de entrada
- `theory/` — Desarrollo teórico
- `methods/` — Procedimientos
- `problems/` — Ejercicios
- `solutions/` — Respuestas y desarrollos

## 4. Reglas de Generación de Contenido

- SIEMPRE dar contexto antes de resolver
- Usar notación estándar según `notation-cheatsheet.md`
- Validar contra bibliografía en `bibliografia-general.md`
- Formato de soluciones: "**N)** *Contexto:* [explicación]"
```

---

#### `nomenclatura-estandar.md` — Convenciones de Nombrado

**Define:**
- Patrón de nombres de archivos
- Excepciones documentadas
- Sintaxis de enlaces internos
- Estructura de bloques `::METADATA::`

**Ejemplo de patrón:**

```
[PREFIJO]-[XX]-[Contenido]-[Tipo].md

Ejemplos válidos:
- FIS-01-Cinematica-Intro.md
- PROG-03-Funciones-Teoria.md
- ING-02-Gramatica-Problemas.md
```

---

## 📚 NIVEL 1: MÓDULOS PRINCIPALES

### Estructura de un Módulo

```
XX-[Nombre-Modulo]/
├── 00-Index.md              # Índice del módulo
├── 01-[Subtema-1]/          # Primer subtema
├── 02-[Subtema-2]/          # Segundo subtema
└── NN-[Subtema-N]/          # Subtemas adicionales
```

### `00-Index.md` — Índice del Módulo

**Contenido:**
- Descripción del módulo
- Lista de subtemas con enlaces
- Prerrequisitos
- Tiempo estimado de estudio

---

## 📖 NIVEL 2: SUBTEMAS (Unidad Atómica)

### Estructura Completa de un Subtema

```
XX-[Nombre-Subtema]/
│
├── 📋 CONFIGURACIÓN
│   ├── manifest.json            # Metadatos para IA
│   └── _directives.md           # Instrucciones específicas
│
├── 📚 CONTENIDO PRINCIPAL
│   ├── [PREFIX]-XX-*-Intro.md   # Punto de entrada
│   └── [PREFIX]-XX-Resumen-Formulas.md  # Cheatsheet
│
├── 📖 CARPETAS SEMÁNTICAS
│   ├── theory/                  # EL "QUÉ" — Definiciones, teoremas
│   ├── methods/                 # EL "CÓMO" — Procedimientos
│   ├── problems/                # PRÁCTICA — Ejercicios
│   └── solutions/               # VALIDACIÓN — Respuestas
│       ├── [PREFIX]-XX-Respuestas.md          # Nivel 1: Solo resultados
│       ├── [PREFIX]-XX-Soluciones-Desarrolladas.md  # Nivel 2: Con contexto
│       └── prob-XX/                           # Nivel 3: Individual extenso
│
├── 📁 OPCIONALES
│   ├── applications/            # Casos de uso reales
│   ├── diagnostic/              # Evaluaciones previas
│   └── media/                   # Recursos visuales
│       └── generated/           # Auto-generados
│
└── 🔓 SANDBOX (Zona libre)
    └── Notas/                   # 📝 Recursos sin clasificar
        └── README.md            # Directiva de excepción
```

---

## 🔓 CARPETA `Notas/` — ZONA SANDBOX

### Concepto

Cada subtema debe incluir una carpeta `Notas/` que funciona como **buzón temporal** para recursos sin clasificar. Esta zona está **completamente exenta** de todas las reglas del repositorio.

### Propósito

| Característica | Descripción |
|----------------|-------------|
| **Almacenamiento temporal** | Guardar recursos antes de clasificarlos |
| **Flexibilidad total** | Cualquier tipo de archivo y formato |
| **Sin validación** | La IA no aplica reglas ni sugiere correcciones |
| **Clasificación diferida** | El contenido se organiza cuando el usuario tenga tiempo |

### Contenido Permitido

- 📄 Apuntes, borradores, resúmenes personales
- 🖼️ Imágenes, capturas, diagramas externos
- 💻 Código de cualquier lenguaje, experimentos
- 📎 PDFs, referencias, material complementario
- 📝 Cualquier formato sin restricción

### Comportamiento de la IA

| Acción | Comportamiento |
|--------|----------------|
| Validar nomenclatura | ⛔ OMITIR |
| Sugerir correcciones | ⛔ OMITIR |
| Solicitar metadatos | ⛔ OMITIR |
| Leer contenido | ✅ COMPLETO |
| Integrar información | ✅ Como contexto |

### README de Notas — Plantilla

```markdown
<!--
::METADATA::
type: sandbox
topic_id: notas-usuario
file_id: Notas-README
status: exempt
scope: local_only
ai_directive: READ_FULL_CONTEXT
validation: NONE
rules_exempt: true
-->

# 📝 Notas del Usuario — Zona Libre

Esta carpeta es una **zona sandbox** exenta de todas las reglas del repositorio.

## ⚠️ DIRECTIVA PARA IA

**NO VALIDAR** ningún contenido dentro de esta carpeta.
**NO SUGERIR** correcciones de nomenclatura ni formato.
**LEER COMPLETO** cualquier archivo si se solicita contexto.

## Contenido Permitido

- Cualquier tipo de archivo
- Cualquier formato
- Sin metadatos obligatorios
- Sin nomenclatura estándar
```

### Flujo de Trabajo

```
1. Usuario guarda recurso útil en Notas/ del subtema más cercano
2. Cuando tenga tiempo, lo clasifica:
   - Teoría → theory/
   - Ejercicio → problems/
   - Multimedia → media/
3. Al mover, aplica nomenclatura y metadatos estándar
```

### Patrón de Excepción

```
Ruta detectada como SANDBOX: */Notas/*

La IA desactiva automáticamente todas las validaciones
para cualquier archivo dentro de carpetas Notas/
```

---

### `manifest.json` — El Contrato Central del Subtema

**El archivo MÁS IMPORTANTE para la IA.** Define qué contiene el subtema y cómo interactuar con él.

**Plantilla completa:**

```json
{
  "id": "[prefijo]-[xx]-[nombre]",
  "topic": "[Nombre legible]",
  "type": "learning_module",
  "status": "active",
  "last_updated": "YYYY-MM-DD",
  
  "human_purpose": "[Descripción del objetivo de aprendizaje]",
  "tags": ["tag1", "tag2", "tag3"],
  "difficulty": "básico|intermedio|avanzado",
  "estimated_time": "X-Y horas",
  
  "resource_map": {
    "entry_point": "[PREFIX]-XX-*-Intro.md",
    "main_theory": "theory/[PREFIX]-XX-Teoria-*.md",
    "cheat_sheet": "[PREFIX]-XX-Resumen-Formulas.md",
    "methods": ["methods/[PREFIX]-XX-Metodos-*.md"],
    "problems": ["problems/[PREFIX]-XX-Problemas.md"],
    "answers": "solutions/[PREFIX]-XX-Respuestas.md",
    "solutions": ["solutions/[PREFIX]-XX-Soluciones-Desarrolladas.md"]
  },
  
  "subtopics": [
    {"id": "X.1", "title": "[Nombre]", "concepts": ["concepto1", "concepto2"]}
  ],
  
  "ai_contract": {
    "default_output": "markdown",
    "allowed_tasks": ["explain_concept", "generate_problems", "verify_solution"],
    "solution_guidelines": {
      "require_context": true,
      "step_by_step": true
    }
  },
  
  "references": [
    {
      "citation": "[Autor]. ([Año]). [Título]. [Editorial].",
      "mapping": {"Capítulo X": "Tema cubierto"}
    }
  ]
}
```

**Campos obligatorios:** `id`, `topic`, `type`, `status`, `tags`

---

### `_directives.md` — Instrucciones Específicas

**Hereda** las reglas globales de `ia-contract.md` y añade reglas específicas del subtema.

**Plantilla:**

```markdown
# Directivas — [Nombre del Subtema]

## Clasificación del Contenido

| Carpeta | Archivo Principal | Descripción |
|---------|-------------------|-------------|
| `theory/` | `[PREFIX]-XX-Teoria-*.md` | Teoría completa |
| `methods/` | `[PREFIX]-XX-Metodos-*.md` | Procedimientos |
| `problems/` | `[PREFIX]-XX-Problemas.md` | Ejercicios |
| `solutions/` | `[PREFIX]-XX-Respuestas.md` | Soluciones |

## Subtemas

1. **X.1** [Nombre] — [Conceptos clave]
2. **X.2** [Nombre] — [Conceptos clave]

## Directivas Específicas para IA

- **Audiencia:** [Nivel educativo]
- **Formato de salida:** Markdown con [notación específica]
- **Tareas permitidas:** [Lista de tareas]
- **Al generar soluciones:** [Instrucciones específicas]
```

---

## ✅ SISTEMA DE METADATOS `::METADATA::`

Todo archivo `.md` debe comenzar con un bloque de metadatos:

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

| type | Descripción | Ubicación |
|------|-------------|-----------|
| `theory` | Desarrollo teórico | `theory/*.md` |
| `method` | Procedimiento | `methods/*.md` |
| `problem` | Enunciados | `problems/*.md` |
| `solution` | Soluciones | `solutions/*.md` |
| `index` | Punto de entrada | `*-Intro.md` |
| `cheatsheet` | Resumen | `*-Resumen-*.md` |
| `answer-key` | Tabla de respuestas | `*-Respuestas.md` |

---

## 🔧 SCRIPTS DE AUTOMATIZACIÓN

### 1. `validate_repo.py` — El Auditor

**Función:** Recorre el repositorio verificando que se cumpla el contrato IA.

**Valida:**
- Existencia de `manifest.json` en cada subtema
- Nomenclatura correcta de archivos
- Prefijos válidos por módulo
- Bloques `::METADATA::` en archivos `.md`
- Enlaces internos no rotos

**Configuración clave a adaptar:**

```python
PREFIXES = {
    "01-[Modulo]": "[XX]",
    "02-[Modulo]": "[YY]",
    # Añadir según módulos del nuevo repositorio
}

REQUIRED_MANIFEST_FIELDS = ["id", "topic", "type", "status", "tags"]
```

---

### 2. `link_knowledge_base.py` — El Bibliotecario

**Función:** Transforma el repositorio en un wiki interconectado.

**Proceso:**
1. Extrae términos del `glossary.md`
2. Escanea archivos de contenido
3. Vincula automáticamente la primera mención de cada término

**Configuración a adaptar:**

```python
CONTENT_FOLDERS = [
    "01-[Modulo]",
    "02-[Modulo]",
    # Lista de módulos a escanear
]

CONTENT_SUBFOLDERS = ["theory", "problems", "methods", "applications", "solutions"]
```

---

### 3. `check_tables.py` — Validador de Tablas

**Función:** Detecta tablas Markdown con columnas desalineadas.

**Problema que resuelve:** El símbolo `|` en notación (ej. valor absoluto) interfiere con separadores de columnas.

---

## 🔗 SISTEMA DE ENLACES

### Sintaxis Obligatoria

```markdown
[Texto visible](ruta/relativa/archivo.md)
[Texto visible](ruta/relativa/archivo.md#ancla)
```

### Ejemplos

| Tipo | Sintaxis |
|------|----------|
| Mismo directorio | `[Intro](PREFIX-XX-Intro.md)` |
| Subdirectorio | `[Teoría](theory/PREFIX-XX-Teoria.md)` |
| Al glosario | `[término](../../glossary.md#termino)` |
| Entre módulos | `[Tema](../02-Modulo/01-Subtema/)` |

### Header de Navegación Estándar

```markdown
> 🏠 **Navegación:** [← Volver al Índice](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)
```

---

## 📋 CHECKLIST PARA CREAR UN NUEVO REPOSITORIO

### Fase 1: Estructura Base
- [ ] Crear `README.md` con tabla de módulos
- [ ] Crear `WIKI_INDEX.md` vacío
- [ ] Crear `glossary.md` con términos iniciales (mínimo 20)
- [ ] Crear carpeta `00-META/` con:
  - [ ] `ia-contract.md` — Definir prefijos y reglas
  - [ ] `nomenclatura-estandar.md` — Convenciones
  - [ ] `bibliografia-general.md` — Fuentes académicas
  - [ ] `study-guide.md` — Guía para estudiantes

### Fase 2: Definir Módulos
- [ ] Listar módulos principales (01-XX/ a NN-XX/)
- [ ] Asignar prefijos únicos de 2-3 letras por módulo
- [ ] Crear `00-Index.md` en cada módulo
- [ ] Documentar prerrequisitos entre módulos

### Fase 3: Crear Subtemas
- [ ] Para cada subtema crear estructura de carpetas
- [ ] Crear `manifest.json` con campos obligatorios
- [ ] Crear `_directives.md` heredando de `ia-contract.md`
- [ ] Crear `*-Intro.md` como punto de entrada

### Fase 4: Poblar Contenido
- [ ] Desarrollar `theory/` con definiciones y teoremas
- [ ] Crear `methods/` con procedimientos paso a paso
- [ ] Crear `problems/` con ejercicios (mínimo 10 por subtema)
- [ ] Implementar sistema de 3 niveles en `solutions/`

### Fase 5: Automatización
- [ ] Adaptar `validate_repo.py` con nuevos prefijos
- [ ] Configurar `link_knowledge_base.py` con carpetas
- [ ] Ejecutar validación inicial
- [ ] Generar `AUDITORIA_ESTADO_REPO.md`

---

## 🎯 EJEMPLOS DE ADAPTACIÓN POR DOMINIO

### Ejemplo 1: Repositorio de Física

```python
PREFIXES = {
    "01-Mecanica": "MEC",
    "02-Termodinamica": "TER",
    "03-Electromagnetismo": "EM",
    "04-Optica": "OPT",
    "05-Fisica-Moderna": "MOD",
}
```

**Estructura de subtema:**
```
01-Mecanica/01-Cinematica/
├── manifest.json
├── _directives.md
├── MEC-01-Cinematica-Intro.md
├── MEC-01-Resumen-Formulas.md
├── theory/MEC-01-Teoria-Cinematica.md
├── methods/MEC-01-Metodos-Cinematica.md
├── problems/MEC-01-Problemas.md
└── solutions/
    ├── MEC-01-Respuestas.md
    └── MEC-01-Soluciones-Desarrolladas.md
```

---

### Ejemplo 2: Repositorio de Programación

```python
PREFIXES = {
    "01-Fundamentos": "FUND",
    "02-POO": "POO",
    "03-Estructuras-Datos": "ED",
    "04-Algoritmos": "ALG",
    "05-Bases-Datos": "BD",
}
```

**Adaptaciones específicas:**
- `theory/` → Conceptos y paradigmas
- `methods/` → Patrones de código y buenas prácticas
- `problems/` → Ejercicios de programación
- `solutions/` → Código completo con explicación

---

### Ejemplo 3: Repositorio de Idiomas

```python
PREFIXES = {
    "01-Gramatica": "GRAM",
    "02-Vocabulario": "VOC",
    "03-Lectura": "LECT",
    "04-Escritura": "ESC",
    "05-Conversacion": "CONV",
}
```

**Adaptaciones específicas:**
- `theory/` → Reglas gramaticales
- `methods/` → Técnicas de aprendizaje
- `problems/` → Ejercicios de práctica
- `solutions/` → Respuestas con explicaciones
- `media/audio/` → Pronunciación (carpeta adicional)

---

### Ejemplo 4: Repositorio de Historia

```python
PREFIXES = {
    "01-Prehistoria": "PRE",
    "02-Antigüedad": "ANT",
    "03-Medieval": "MED",
    "04-Moderna": "MOD",
    "05-Contemporanea": "CON",
}
```

**Adaptaciones específicas:**
- `theory/` → Contexto histórico y análisis
- `methods/` → Metodología de investigación
- `problems/` → Preguntas de análisis
- `solutions/` → Ensayos modelo
- `media/timelines/` → Líneas de tiempo

---

## 📚 BIBLIOGRAFÍA DE DISEÑO

Esta arquitectura está inspirada en:

| Concepto | Descripción | Aplicación |
|----------|-------------|------------|
| **Zettelkasten** | Sistema de notas interconectadas | Enlaces entre términos |
| **Digital Gardens** | Conocimiento en crecimiento orgánico | Estructura wiki |
| **Docs as Code** | Documentación versionable | Git + Markdown |
| **Atomic Design** | Componentes reutilizables | Módulos independientes |
| **Single Source of Truth** | Una fuente de verdad | `manifest.json` |

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### Para el Creador del Repositorio

```
1. Definir dominio y módulos principales
           ↓
2. Crear estructura base (Fase 1)
           ↓
3. Definir prefijos en ia-contract.md
           ↓
4. Crear subtemas con estructura completa
           ↓
5. Poblar contenido progresivamente
           ↓
6. Ejecutar validación automática
           ↓
7. Iterar y expandir
```

### Para el Usuario (Estudiante)

```
1. Leer README.md para contexto
           ↓
2. Consultar study-guide.md para ruta de aprendizaje
           ↓
3. Navegar a módulo de interés via WIKI_INDEX.md
           ↓
4. Entrar por *-Intro.md del subtema
           ↓
5. Estudiar theory/ → methods/ → problems/
           ↓
6. Verificar con solutions/
           ↓
7. Consultar glossary.md para términos
```

### Para la IA Asistente

```
1. SIEMPRE leer ia-contract.md primero
           ↓
2. Navegar a subtema via manifest.json
           ↓
3. Leer _directives.md del subtema
           ↓
4. Consultar resource_map para localizar archivos
           ↓
5. Generar contenido siguiendo reglas
           ↓
6. Validar contra bibliografía
```

---

**Versión:** 1.0 — Plantilla Universal  
**Basada en:** Repositorio de Matemáticas v5.0  
**Última actualización:** 2026-01-05  
**Licencia:** Libre para uso educativo
