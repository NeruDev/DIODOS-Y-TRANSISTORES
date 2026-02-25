<!--
::METADATA::
type: reference
topic_id: dio-directives
file_id: DIO-directives
status: active
audience: ai_context
last_updated: 2026-02-13
-->

# Directivas — Módulo 01: Circuitos de Aplicación con Diodos

> Hereda reglas de [ia-contract.md](../00-META/ia-contract.md).

## Clasificación del Contenido

| Carpeta | Descripción |
|---------|-------------|
| `theory/` | Un archivo `.md` por cada subtema del temario (DIO-01 a DIO-08) |
| `methods/` | Procedimientos paso a paso (compartidos por todo el módulo) |
| `problems/` | Ejercicios del módulo |
| `solutions/` | Soluciones desarrolladas |
| `media/generated/` | Gráficas y scripts Python |

## Subtemas (archivos en `theory/`)

| Archivo | Tema | Estado |
|---------|------|--------|
| `DIO-01-Teoria-Diodo.md` | 1.1 Polarización y recta de carga | 🔄 En progreso |
| `DIO-02-Teoria-Circuitos-Serie-Paralelo.md` | 1.2 Circuitos serie, paralelo, serie-paralelo | 📝 Pendiente |
| `DIO-03-Teoria-Rectificacion-Filtrado.md` | 1.3.1 Rectificación y filtrado | 📝 Pendiente |
| `DIO-04-Teoria-Recortadores.md` | 1.3.2 Recortadores | 📝 Pendiente |
| `DIO-05-Teoria-Sujetadores.md` | 1.3.3 Sujetadores | 📝 Pendiente |
| `DIO-06-Teoria-Multiplicadores.md` | 1.3.4 Multiplicadores | 📝 Pendiente |
| `DIO-07-Teoria-Diodo-Zener.md` | 1.4 Diodo Zener y reguladores | 📝 Pendiente |
| `DIO-08-Teoria-Otros-Diodos.md` | 1.5 Otros diodos | 📝 Pendiente |

## Directivas Específicas para IA

- **Audiencia:** Ingeniería (universitario)
- **Formato de salida:** Markdown con LaTeX para ecuaciones
- **Tareas permitidas:** Explicar conceptos, generar problemas, verificar soluciones, generar gráficas
- **Al generar gráficas:** Usar matplotlib, guardar en `media/generated/`, documentar parámetros
- **Al generar soluciones:** Siempre paso a paso con unidades y contexto físico
- **Reemplazo de imágenes:** Si una imagen nueva sustituye a otra, actualizar referencias y eliminar la imagen anterior sin uso para mantener `media/generated/` limpio.

## Lecciones Aprendidas — Esquemáticos schemdraw (Módulo DIO)

Errores documentados durante la generación iterativa del esquemático del rectificador de derivación central (`DIO-gen-nota5-rectificador-onda-completa-central.py`). Estas reglas complementan las directivas generales de `ai-directives.md` §5.

### Transformadores con derivación central

1. **Etiquetas de voltaje sobre inductores:** Nunca usar `.label()` directamente sobre `Inductor2`. Los bumps del componente tapan el texto. Usar `elm.Label()` con coordenadas explícitas desplazadas al menos `+1.1 u` horizontalmente (ver `ai-directives.md` §5.6).

2. **Conexión de $R_L$ a la toma central:** $R_L$ debe conectarse **horizontalmente** entre el nodo de unión de cátodos y la toma central (CT), a la altura media del secundario (`sec_mid_y`). NO trazar el camino de retorno por rutas externas que rodeen el circuito (ver `ai-directives.md` §5.8).

3. **Dimensionamiento del transformador:** Si la carga u otros componentes deben caber **entre** las ramas de salida (ej. entre D1 y D2), aumentar `loops` del primario (≥ 4) para ganar altura vertical suficiente (ver `ai-directives.md` §5.9).

4. **Indicadores de polaridad:** Usar `elm.Gap()` solo para componentes compactos (resistores, diodos). Para voltajes del secundario del transformador, usar `elm.Label()` en lugar de Gap para evitar solapamiento con los bumps (ver `ai-directives.md` §5.7).
