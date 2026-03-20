# Mapa del Repositorio

> Arquitectura estructural de DIODOS-Y-TRANSISTORES

---

## Jerarquía de Autoridad

Al consultar información de un módulo, el orden de prioridad es:

1. `manifest.json` (metadatos y estado del módulo)
2. `directives.md` (instrucciones específicas del módulo)
3. `AGENTS.md` (directiva general para IAs)
4. `README.md` (descripciones generales)

---

## Estructura de Directorios

```
DIODOS-Y-TRANSISTORES/
├── AGENTS.md                  → Fuente de verdad centralizada para IAs
├── CLAUDE.md                  → Contexto específico para Claude
├── GEMINI.md                  → Contexto específico para Gemini
├── README.md                  → Punto de entrada del repositorio
├── WIKI_INDEX.md              → Mapa de navegación centralizado
├── glossary.md                → Glosario de términos técnicos
├── CHANGELOG.md               → Registro de cambios
│
├── .github/
│   └── copilot-instructions.md → Contexto específico para Copilot
│
├── 00-meta/                   → Centro de control
│   ├── repo-map.md            → Este archivo
│   ├── naming-conventions.md  → Estándares de nomenclatura
│   ├── standards.md           → Directivas técnicas (schemdraw, LaTeX)
│   ├── bibliography.md        → Fuentes bibliográficas
│   ├── study-guide.md         → Guía de estudio
│   ├── temario.md             → Temario oficial de la materia
│   ├── tools/                 → Scripts de generación
│   │   ├── Control_Scripts.md → Registro de scripts e imágenes
│   │   └── *.py               → Scripts Python
│   └── templates/             → Plantillas para futuros repos
│
├── topics/                    → Contenido educativo estructurado
│   ├── 01-circuitos-diodos/   → Módulo DIO
│   ├── 02-transistor-bjt/     → Módulo BJT
│   ├── 03-transistor-fet/     → Módulo FET
│   ├── 04-amplificadores/     → Módulo AMP
│   └── 05-proyecto-final/     → Módulo PRO
│
├── audits/                    → Sistema de auditorías
│   ├── logs/                  → Logs de ejecución
│   ├── reports/               → Reportes de estado
│   └── snapshots/             → Snapshots estructurales
│
└── sandbox/                   → Zona de trabajo libre
```

---

## Directorios Principales

| Directorio | Propósito | Indexado |
|------------|-----------|----------|
| `topics/` | Contenido educativo estructurado | Sí |
| `00-meta/` | Configuración, herramientas y estándares | Sí |
| `sandbox/` | Zona de trabajo libre | No |
| `audits/` | Logs, reportes y snapshots de validación | No |

---

## Estructura de Módulos

Cada módulo en `topics/` sigue esta estructura:

```
topics/xx-nombre-modulo/
├── README.md          → Punto de entrada del módulo
├── manifest.json      → Metadatos y estado
├── directives.md      → Instrucciones para IA
├── theory/            → Desarrollo teórico
├── methods/           → Procedimientos paso a paso
├── problems/          → Ejercicios
├── solutions/         → Soluciones desarrolladas
├── formularios/       → Resúmenes de fórmulas
├── assets/            → Imágenes generadas por scripts
└── Notas/             → Material de clase pendiente de migrar
```

---

## Módulos y Prefijos

| # | Prefijo | Módulo | Carpeta |
|---|---------|--------|---------|
| 01 | `DIO` | Circuitos con Diodos | `topics/01-circuitos-diodos/` |
| 02 | `BJT` | Transistor Bipolar | `topics/02-transistor-bjt/` |
| 03 | `FET` | Transistor Unipolar | `topics/03-transistor-fet/` |
| 04 | `AMP` | Amplificadores | `topics/04-amplificadores/` |
| 05 | `PRO` | Proyecto Final | `topics/05-proyecto-final/` |

---

## Sistema de Estados

| Estado | Significado |
|--------|-------------|
| `draft` | En desarrollo, incompleto, desorden aceptado |
| `review` | Estructura completa, contenido parcial |
| `stable` | Listo para consulta confiable |
| `deprecated` | Obsoleto, mantener solo por referencia |

---

## Dependencias entre Módulos

```
01-Diodos ──► 02-BJT ──► 04-Amplificadores ──► 05-Proyecto Final
01-Diodos ──► 03-FET ──► 04-Amplificadores ──► 05-Proyecto Final
```

---

## Documentos Clave

| Documento | Propósito |
|-----------|-----------|
| [AGENTS.md](../../AGENTS.md) | Directiva general para IAs |
| [naming-conventions.md](naming-conventions.md) | Estándares de nomenclatura |
| [standards.md](standards.md) | Directivas técnicas |
| [bibliography.md](bibliography.md) | Fuentes bibliográficas |
| [tools/Control_Scripts.md](tools/Control_Scripts.md) | Registro de scripts e imágenes |
| [glossary.md](../../glossary.md) | Glosario de términos |
| [WIKI_INDEX.md](../../WIKI_INDEX.md) | Mapa de navegación |
