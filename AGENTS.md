# AGENTS.md — Directiva General para Agentes de IA

> **Fuente de verdad centralizada** para todos los agentes de IA que interactúan con este repositorio.
> Los archivos de contexto específicos (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`) **heredan** de este documento y solo contienen extensiones propias de cada agente.

---

## 1. Propósito del Repositorio

**DIODOS-Y-TRANSISTORES** es un repositorio de conocimiento estructurado ("Jardín Digital") para la materia de **Diodos y Transistores** a nivel universitario (Ingeniería Electrónica).

| Campo | Valor |
|-------|-------|
| Materia | Electrónica Analógica — Diodos y Transistores |
| Audiencia | Estudiantes de Ingeniería Electrónica |
| Nivel académico | Universitario |
| Idioma | Español |
| Tono | Técnico pero accesible, con analogías cuando sean útiles |
| Bibliografía principal | Boylestad & Nashelsky (11ª ed.), Sedra & Smith (7ª ed.), Malvino & Bates (7ª ed.) |

---

## 2. Arquitectura del Repositorio

```
DIODOS-Y-TRANSISTORES/
├── AGENTS.md                       → Este archivo (directiva general para IAs)
├── CLAUDE.md                       → Contexto específico para Claude
├── GEMINI.md                       → Contexto específico para Gemini
├── README.md                       → Punto de entrada del repo
├── WIKI_INDEX.md                   → Mapa de navegación centralizado
├── glossary.md                     → Glosario de términos técnicos
├── CHANGELOG.md                    → Registro de cambios
├── .github/copilot-instructions.md → Contexto específico para GitHub Copilot
│
├── 00-meta/                        → Centro de control
│   ├── repo-map.md                 → Mapa estructural del repositorio
│   ├── naming-conventions.md       → Estándares de nomenclatura
│   ├── standards.md                → Directivas técnicas (schemdraw, LaTeX)
│   ├── bibliography.md             → Fuentes bibliográficas
│   ├── study-guide.md              → Guía de estudio para alumnos
│   ├── temario.md                  → Temario oficial de la materia
│   ├── tools/                      → Scripts de generación de gráficos (Python)
│   │   └── Control_Scripts.md      → Registro centralizado de scripts e imágenes
│   └── templates/                  → Plantillas para futuros repositorios
│
├── topics/                         → Contenido educativo estructurado
│   ├── 01-circuitos-diodos/  (DIO) → Módulo 1
│   ├── 02-transistor-bjt/    (BJT) → Módulo 2
│   ├── 03-transistor-fet/    (FET) → Módulo 3
│   ├── 04-amplificadores/    (AMP) → Módulo 4
│   └── 05-proyecto-final/    (PRO) → Módulo 5
│
├── audits/                         → Sistema de auditorías
│   ├── logs/
│   ├── reports/
│   └── snapshots/
│
└── sandbox/                        → Zona de trabajo libre (no indexada)
```

### 2.1 Estructura interna de cada módulo

```
topics/xx-nombre-modulo/
├── README.md               → Punto de entrada del módulo
├── manifest.json           → Metadatos y estado (JSON)
├── directives.md           → Instrucciones específicas del módulo para IA
├── formularios/            → Formularios de fórmulas clave
├── theory/                 → Desarrollo teórico por subtema
├── methods/                → Procedimientos paso a paso
├── problems/               → Ejercicios
├── solutions/              → Soluciones desarrolladas
├── assets/                 → Imágenes PNG generadas por scripts Python
└── Notas/                  → Material de clase pendiente de migrar a theory/
```

### 2.2 Módulos y prefijos

| # | Prefijo | Módulo | Carpeta | Subtemas |
|---|---------|--------|---------|----------|
| 01 | `DIO` | Circuitos con Diodos | `topics/01-circuitos-diodos/` | Polarización, rectificación, recortadores, sujetadores, multiplicadores, Zener, otros diodos |
| 02 | `BJT` | Transistor Bipolar | `topics/02-transistor-bjt/` | Características, polarización (EC, BC, CC), conmutación, estabilidad |
| 03 | `FET` | Transistor Unipolar | `topics/03-transistor-fet/` | Polarización (fija, auto, divisor), MOSFET, redes combinadas |
| 04 | `AMP` | Amplificadores | `topics/04-amplificadores/` | Pequeña señal, amplificador BJT, amplificador JFET |
| 05 | `PRO` | Proyecto Final | `topics/05-proyecto-final/` | Fuente con regulador transistorizado, fuente con regulador CI |

### 2.3 Jerarquía de autoridad

Orden de prioridad al consultar información de un módulo:

1. `manifest.json` (metadatos y estado)
2. `directives.md` (instrucciones específicas)
3. `AGENTS.md` (este archivo)
4. `README.md` (descripciones generales)

### 2.4 Sistema de estados

| Estado | Significado |
|--------|-------------|
| `draft` | En desarrollo, incompleto, desorden aceptado |
| `review` | Estructura completa, contenido parcial |
| `stable` | Listo para consulta confiable |
| `deprecated` | Obsoleto, mantener solo por referencia |

---

## 3. Entorno de Desarrollo

### 3.1 Python

| Aspecto | Valor |
|---------|-------|
| Versión | Python 3.14.0 |
| Gestor de entorno | venv (`.venv/`) |
| Requisito del sistema (Linux) | `python3-tk` |

**Activación del entorno:**
```bash
# Linux/Codespaces
source .venv/bin/activate
export DISPLAY=:1  # Para GUI

# Windows PowerShell
& ".venv\Scripts\Activate.ps1"
```

### 3.2 Dependencias Python (versiones exactas)

```
numpy==2.4.2
matplotlib==3.10.8
schemdraw==0.22
pillow==12.1.0
packaging==26.0
python-dateutil==2.9.0.post0
six==1.17.0
```

**Instalación:**
```bash
pip install numpy==2.4.2 matplotlib==3.10.8 schemdraw==0.22 pillow==12.1.0 packaging==26.0 python-dateutil==2.9.0.post0 six==1.17.0
```

### 3.3 Backends de Matplotlib

| Modo | Backend | Uso |
|------|---------|-----|
| Headless (PNG) | `Agg` | Scripts en `00-meta/tools/` |
| GUI interactiva | `TkAgg` | Calculadoras en `Notas/` |

```python
# Siempre al inicio del script:
import matplotlib
matplotlib.use('Agg')  # O 'TkAgg' para GUI
```

---

## 4. Scripts de Generación de Gráficos

### 4.1 Ubicación y convención

- **Directorio:** `00-meta/tools/`
- **Patrón de nombre:** `[PREFIJO]-gen-[descripcion].py`
- **Salida:** `topics/xx-modulo/assets/*.png`

### 4.2 Registro centralizado

> Ver [00-meta/tools/Control_Scripts.md](00-meta/tools/Control_Scripts.md) para el inventario completo de scripts, imágenes generadas y referencias cruzadas.

### 4.3 Ejecución

```bash
# Desde la raíz del repositorio:
python 00-meta/tools/DIO-gen-curva-iv.py

# Todos los scripts:
for script in 00-meta/tools/*.py; do python "$script"; done
```

**PowerShell (Windows):**
```powershell
Set-Location "G:\REPOSITORIOS GITHUB\DIODOS Y TRANSISTORES"
& ".venv\Scripts\python.exe" "00-meta/tools/SCRIPT.py"
```

### 4.4 Política de scripts

1. **Un script por conjunto temático coherente.**
2. **Referencia cruzada obligatoria** en el documento `.md` que usa la imagen y en `Control_Scripts.md`.
3. **Metadatos `::SCRIPT_METADATA::`** en cada script con `script_id`, `module`, `generates`, `referenced_by`, `last_updated`.
4. **Actualizar `Control_Scripts.md`** inmediatamente al crear/modificar/eliminar scripts.

---

## 5. Reglas de Generación de Contenido

### 5.1 Nomenclatura de archivos

**Patrón:** `[PREFIJO]-[XX]-[Contenido]-[Tipo].md`

| Campo | Ejemplo |
|-------|---------|
| `PREFIJO` | `DIO`, `BJT`, `FET`, `AMP`, `PRO` |
| `XX` | `01`, `02`, ..., `08` |
| `Contenido` | `Polarizacion`, `Rectificacion` (PascalCase) |
| `Tipo` | `Intro`, `Teoria`, `Metodos`, `Problemas`, `Soluciones` |

### 5.2 Bloque de metadatos obligatorio

```markdown
<!--
::METADATA::
type: [theory|method|problem|solution|reference|index|cheatsheet|answer-key]
topic_id: [id-del-tema]
file_id: [nombre-archivo-sin-extension]
status: [draft|review|stable|deprecated]
audience: [student|ai_context|both]
last_updated: YYYY-MM-DD
-->
```

### 5.3 Formato LaTeX

- **Inline:** `$ expresión $`
- **Bloque:** `$$ expresión $$`

**Precaución en bash:** Usar `<<'EOF'` (comillas simples) para heredocs con LaTeX:
```bash
cat >> archivo.md <<'EOF'
El voltaje térmico es $V_T$
EOF
```

### 5.4 Directiva de mejora de redacción para Notas/

Cuando el usuario proporcione texto informal para `Notas/`, el agente **debe** mejorar automáticamente:
1. **Coherencia:** Conexión lógica entre ideas.
2. **Orden:** Estructura con encabezados y listas.
3. **Contexto:** Definiciones y notación necesarias.

Solo se mejora la forma; los valores técnicos se respetan fielmente.

---

## 6. Restricciones y Prohibiciones

### 6.1 El agente NO debe:

- Leer contenido interno de archivos `.py` (solo registrar rutas)
- Cargar imágenes, binarios o archivos pesados
- Inventar datos; usar solo valores realistas de componentes electrónicos
- Modificar archivos en `Notas/` sin respetar que es zona sandbox
- Usar `sandbox/` como fuente de verdad

### 6.2 Directorios a ignorar:

- `.venv/`, `__pycache__/`, `.git/`, `node_modules/`
- `dist/`, `build/`, `outputs/`, `results/`
- `sandbox/` (no indexar automáticamente)

### 6.3 Archivos autogenerados (no son fuente de verdad):

- `topics/*/assets/*.png`

---

## 7. Flujo de Trabajo para Agentes IA

1. **Leer** este archivo (`AGENTS.md`) como primera acción.
2. **Consultar** `manifest.json` del módulo objetivo.
3. **Revisar** `directives.md` del módulo para instrucciones específicas.
4. **Generar** contenido siguiendo las reglas de este documento.
5. **Si genera gráficas:** crear/modificar script en `00-meta/tools/`, ejecutar desde la raíz, actualizar `Control_Scripts.md`.

---

## 8. Documentos de Referencia Clave

| Documento | Propósito |
|-----------|-----------|
| [00-meta/repo-map.md](00-meta/repo-map.md) | Mapa estructural del repositorio |
| [00-meta/naming-conventions.md](00-meta/naming-conventions.md) | Estándares de nomenclatura completos |
| [00-meta/standards.md](00-meta/standards.md) | Directivas técnicas (schemdraw, LaTeX) |
| [00-meta/bibliography.md](00-meta/bibliography.md) | Fuentes bibliográficas válidas |
| [00-meta/tools/Control_Scripts.md](00-meta/tools/Control_Scripts.md) | Registro de scripts, imágenes y referencias |
| [glossary.md](glossary.md) | Glosario de términos técnicos |
| [WIKI_INDEX.md](WIKI_INDEX.md) | Mapa de navegación centralizado |

---

## 9. Sincronización de Archivos de Contexto

> **OBLIGATORIO:** Mantener sincronizados todos los archivos de contexto de IA ante cambios estructurales.

### 9.1 Archivos de contexto específicos

| Archivo | Agente | Relación con AGENTS.md |
|---------|--------|------------------------|
| `CLAUDE.md` | Claude (Anthropic) | Hereda de AGENTS.md, contiene extensiones específicas |
| `GEMINI.md` | Gemini (Google) | Hereda de AGENTS.md, contiene extensiones específicas |
| `.github/copilot-instructions.md` | GitHub Copilot | Hereda de AGENTS.md, incluye detalles schemdraw |

### 9.2 Eventos que requieren sincronización

| Evento | Acción requerida |
|--------|------------------|
| **Cambio de arquitectura** | Actualizar §2 en todos los archivos |
| **Cambio de dependencias Python** | Actualizar §3.2 en todos los archivos |
| **Nuevo estándar de nomenclatura** | Actualizar §5 en todos los archivos |

### 9.3 Procedimiento de sincronización

1. **Editar primero** `AGENTS.md` como fuente de verdad.
2. **Propagar cambios** a `CLAUDE.md`, `GEMINI.md` y `.github/copilot-instructions.md`.
3. **Documentar** la sincronización en el commit message:
   ```
   sync(agents): Actualizar dependencias Python en archivos de contexto IA
   ```

---

## 10. Versionado

| Versión | Fecha | Cambios |
|---------|-------|---------|
| 2.0.0 | 2026-03-20 | Reestructuración: topics/, 00-meta/, sistema de auditorías |
| 1.0.0 | 2026-03-20 | Creación inicial del archivo AGENTS.md |

---

> **Nota:** Este archivo es la **fuente de verdad centralizada**. Los archivos específicos de cada agente deben referenciar este documento y solo contener extensiones propias de su plataforma.
