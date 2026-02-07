<!--
::METADATA::
type: reference
topic_id: dio-01-directives
file_id: DIO-01-directives
status: active
audience: ai_context
last_updated: 2026-02-07
-->

# Directivas — Polarización y Recta de Carga del Diodo

> Hereda reglas de [ia-contract.md](../../00-META/ia-contract.md).

## Clasificación del Contenido

| Carpeta | Archivo Principal | Descripción |
|---------|-------------------|-------------|
| `theory/` | `DIO-01-Teoria-Diodo.md` | Teoría del diodo: ecuación de Shockley, regiones de operación, efectos térmicos |
| `methods/` | *(pendiente)* | Procedimientos para análisis con recta de carga |
| `problems/` | *(pendiente)* | Ejercicios de polarización y cálculos |
| `solutions/` | *(pendiente)* | Soluciones desarrolladas |

## Subtemas

1. **1.1.1** Ecuación de Shockley — corriente de saturación, voltaje térmico, factor de idealidad
2. **1.1.2** Regiones de operación — directa, inversa, ruptura
3. **1.1.3** Efectos de la temperatura — coeficientes térmicos, duplicación de $I_S$
4. **1.1.4** Recta de carga — punto de operación, análisis gráfico

## Directivas Específicas para IA

- **Audiencia:** Ingeniería (universitario)
- **Formato de salida:** Markdown con LaTeX para ecuaciones
- **Tareas permitidas:** Explicar conceptos, generar problemas, verificar soluciones, generar gráficas
- **Al generar gráficas:** Usar matplotlib, guardar en `media/generated/`, documentar parámetros
- **Al generar soluciones:** Siempre paso a paso con unidades y contexto físico
