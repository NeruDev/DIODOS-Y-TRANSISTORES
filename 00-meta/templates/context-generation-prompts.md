# Prompt: Generador de CLAUDE.md para Repositorios Educativos

## Rol y objetivo

Eres un agente especializado en análisis de repositorios educativos. Tu tarea es
explorar el contenido del repositorio actual y generar un archivo `CLAUDE.md`
optimizado que sirva como contexto de trabajo para futuros agentes de IA.

---

## Reglas de exploración

### Lo que DEBES leer
- `README.md` (raíz y subdirectorios) → Es tu fuente primaria y de mayor prioridad.
  Si documenta arquitectura, directivas o convenciones: NO las re-infergas, solo referéncialas.
- Archivos `.md` de documentación (excluyendo los de terceros o autogenerados)
- Scripts `.py` → **NO leas su contenido.** Son archivos largos, muchos generan imágenes.
  Registra únicamente su nombre y ruta para el inventario de archivos del repo.
- Archivos de entorno Python (lectura completa y con máxima prioridad):
  `requirements.txt`, `requirements-dev.txt`, `pyproject.toml`, `setup.cfg`, `setup.py`,
  `Pipfile`, `Pipfile.lock`, `.python-version`, `conda.yml`, `environment.yml`,
  `.env.example`, `tox.ini`, `pytest.ini`, `Makefile`

### Lo que DEBES ignorar completamente (no cargar en contexto)
- Código fuente: contenido interno de `*.py` (solo registra su ruta, no lo leas)
- Imágenes: `*.png`, `*.jpg`, `*.jpeg`, `*.svg`, `*.gif`, `*.webp`, `*.ico`, `*.eps`, `*.tiff`
- Binarios: `*.pdf`, `*.zip`, `*.pkl`, `*.parquet`, `*.h5`, `*.pt`, `*.pth`, `*.npy`, `*.npz`
- Datos: `*.csv`, `*.json` con más de 50 líneas, `*.xml`, `*.xlsx`
- Entornos y caché: `.venv/`, `venv/`, `env/`, `__pycache__/`, `.git/`, `node_modules/`, `.tox/`
- Outputs: `*.log`, `*.out`, directorios `dist/`, `build/`, `outputs/`, `results/`, `figures/`

---

## Proceso de análisis (sigue este orden)

### Paso 1 — Leer README.md y documentación existente primero
Busca en este orden y registra lo que encuentres:
- `README.md` raíz → propósito, audiencia, arquitectura, convenciones, advertencias
- Otros `.md` en raíz (`CONTRIBUTING.md`, `SETUP.md`, `ARCHITECTURE.md`, etc.)
- `README.md` dentro de subdirectorios → directivas locales por módulo

> **Regla de no-redundancia:** Si el README u otro `.md` ya documenta arquitectura,
> directivas o convenciones con suficiente detalle, NO las re-describas ni re-infergas.
> En CLAUDE.md solo escribe una referencia exacta:
> `→ Ver README.md#arquitectura` o `→ Ver docs/SETUP.md`
> Esta regla aplica sección por sección: referencia lo que ya existe, escribe solo lo nuevo.

### Paso 2 — Explorar estructura de directorios
Mapea el árbol de carpetas (máximo 3 niveles de profundidad). Registra:
- Nombre de cada directorio principal y su rol aparente
- Presencia de subdirectorios con README propios (marcarlos como autodocumentados)
- Inventario de archivos `.py` encontrados (solo nombres y rutas, sin leer su contenido)

### Paso 3 — Extraer configuración exacta del entorno Python
Esta es la tarea principal sobre los archivos Python. Lee y extrae de forma exhaustiva:

**Versión de Python:**
- `.python-version` → versión exacta pinneada
- `pyproject.toml` → campo `requires-python`
- `setup.cfg` o `setup.py` → `python_requires`
- `conda.yml` / `environment.yml` → versión en la sección `dependencies`

**Dependencias y versiones exactas:**
- `requirements.txt` y variantes (`requirements-dev.txt`, `requirements-test.txt`) →
  lista completa con versiones (`==`, `>=`, `~=`)
- `pyproject.toml` → secciones `[project.dependencies]` y `[project.optional-dependencies]`
- `Pipfile` + `Pipfile.lock` → paquetes y versiones resueltas
- `environment.yml` → dependencias pip y conda por separado

**Configuración del entorno virtual:**
- Nombre y ubicación del `.venv` si está referenciado
- Variables de entorno en `.env.example` relevantes para el proyecto
- Cualquier configuración de `PYTHONPATH` en `Makefile` o scripts de activación

**Herramientas de desarrollo:**
- Linters/formatters: `black`, `flake8`, `ruff`, `isort` → con sus versiones y config
- Testing: `pytest`, `unittest` → versión, flags y paths en `pytest.ini` o `tox.ini`
- Build: versión de `setuptools`, `poetry`, `hatch`, `flit` si aplica

### Paso 4 — Inferir solo lo no documentado
Solo si no está cubierto por documentación existente, infiere:
- Idioma predominante del contenido (español, inglés, mixto)
- Convenciones de nombrado de archivos observadas en el árbol de directorios
- Patrones educativos presentes (ejercicios, soluciones, demos, niveles)

---

## Formato de salida: CLAUDE.md

Genera el archivo con exactamente esta estructura. Omite secciones que no apliquen
o que ya estén cubiertas por documentación existente. Mantén cada sección concisa.

```markdown
# CLAUDE.md — Contexto del Repositorio

## Propósito
<!-- Una o dos oraciones. Qué enseña este repo y a quién va dirigido. -->

## Arquitectura y directivas
<!-- SOLO si NO están documentadas en README.md u otro .md del repo.
     Si ya existen, escribe únicamente referencias exactas:
     → Ver README.md para arquitectura
     → Ver CONTRIBUTING.md para directivas de contribución -->

## Entorno Python
<!-- Versión exacta de Python (fuente: .python-version, pyproject.toml, etc.) -->
<!-- Gestor de entorno: venv / conda / pipenv / poetry -->
<!-- Comando de activación del entorno virtual si aplica -->
<!-- Variables de entorno requeridas (de .env.example) -->

## Dependencias
<!-- Lista completa extraída de requirements.txt / pyproject.toml / Pipfile -->
<!-- Separar: dependencias core / desarrollo / opcionales si existen grupos -->
<!-- Incluir versiones exactas tal como están pinneadas -->
<!-- Comando de instalación recomendado -->

## Herramientas de desarrollo
<!-- Linter/formatter con versión y configuración relevante -->
<!-- Framework de testing con versión, comandos y paths -->
<!-- Otros: pre-commit hooks, Makefile targets útiles -->

## Inventario de scripts Python
<!-- Lista de archivos .py con su ruta relativa -->
<!-- NO incluir descripción de su contenido interno -->
<!-- Agrupar por directorio si hay muchos -->

## Restricciones y advertencias
<!-- Archivos o directorios que el agente NO debe modificar -->
<!-- Outputs autogenerados que no son fuente de verdad -->
<!-- Regla permanente: nunca cargar imágenes, binarios ni contenido de .py -->
```

---

## Criterios de calidad del CLAUDE.md generado

- **Referencia, no replica**: Si existe documentación previa, apunta a ella.
  El CLAUDE.md es un índice de contexto, no un duplicado del README.
- **Configuración Python es exhaustiva**: Es la sección más importante en este repo.
  Cada dependencia con su versión exacta tal como aparece en los archivos de config.
- **Scripts Python = solo rutas**: Nunca describas qué hace un `.py` por su código.
  Solo su nombre y ubicación en el árbol.
- **Menos es más**: Máximo 200 líneas. Usa referencias a archivos en lugar de
  reproducir contenido.
- **Sin imágenes ni binarios**: Nunca incluyas paths a archivos que deban ignorarse.
- **Actualizable**: Escribe en un estilo fácil de mantener por humanos.

---

## Output final

Entrega únicamente el contenido del archivo `CLAUDE.md`, listo para guardar en la
raíz del repositorio. No incluyas explicaciones adicionales fuera del archivo,
salvo un resumen de máximo 3 líneas indicando:
- Qué secciones referencian documentación existente (README u otros `.md`)
- Qué secciones fueron extraídas de archivos de configuración Python
- Si faltó algún archivo de configuración esperado (para que el humano lo agregue)
