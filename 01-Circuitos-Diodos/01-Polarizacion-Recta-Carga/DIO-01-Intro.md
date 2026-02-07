<!--
::METADATA::
type: index
topic_id: dio-01-intro
file_id: DIO-01-Intro
status: active
audience: both
last_updated: 2026-02-07
-->

> 🏠 **Navegación:** [← Módulo 01](../00-Index.md) | [📋 Índice Wiki](../../WIKI_INDEX.md) | [📚 Glosario](../../glossary.md)

# DIO-01 — Polarización y Recta de Carga del Diodo

> **Subtema 1.1 del temario** | Dificultad: Básico | Tiempo estimado: 2-3 horas

---

## Objetivo de Aprendizaje

Comprender el funcionamiento fundamental del diodo semiconductor, su ecuación característica (Shockley), las tres regiones de operación, los efectos de la temperatura y la determinación del punto de operación mediante la recta de carga.

---

## Mapa de Recursos

| Recurso | Enlace | Descripción |
|---------|--------|-------------|
| 📖 Teoría | [DIO-01-Teoria-Diodo.md](theory/DIO-01-Teoria-Diodo.md) | Ecuación de Shockley, regiones de operación, efectos térmicos, ejemplos de cálculo |
| 🔧 Métodos | *(pendiente)* | Procedimiento para análisis con recta de carga |
| 📝 Problemas | *(pendiente)* | Ejercicios de polarización |
| ✅ Soluciones | *(pendiente)* | Soluciones desarrolladas paso a paso |

---

## Conceptos Clave

- [Diodo](../../glossary.md#diodo) y [unión PN](../../glossary.md#unión-pn)
- [Ecuación de Shockley](../../glossary.md#ecuación-de-shockley)
- [Voltaje de umbral](../../glossary.md#voltaje-de-umbral) ($V_K \approx 0.7V$ para Si)
- [Corriente de saturación inversa](../../glossary.md#corriente-de-saturación-inversa) ($I_S$)
- [Voltaje térmico](../../glossary.md#voltaje-térmico) ($V_T = kT/q$)
- [Recta de carga](../../glossary.md#recta-de-carga) y [punto de operación](../../glossary.md#punto-de-operación)

---

## Visualizaciones Disponibles

Las siguientes gráficas fueron generadas computacionalmente con Python:

| Gráfica | Archivo | Script |
|---------|---------|--------|
| Curva I-V completa | [curva_diodo_general.png](media/generated/curva_diodo_general.png) | [curva_diodo.py](media/generated/curva_diodo.py) |
| Zoom región inversa | [curva_diodo_zoom_inversa.png](media/generated/curva_diodo_zoom_inversa.png) | [curva_diodo.py](media/generated/curva_diodo.py) |
| Efecto temperatura (directa) | [curva_temp_directa.png](media/generated/curva_temp_directa.png) | [grafica_temperatura_split.py](media/generated/grafica_temperatura_split.py) |
| Efecto temperatura (inversa) | [curva_temp_inversa.png](media/generated/curva_temp_inversa.png) | [grafica_temperatura_split.py](media/generated/grafica_temperatura_split.py) |
| Efecto temperatura (ruptura) | [curva_temp_ruptura.png](media/generated/curva_temp_ruptura.png) | [grafica_temperatura_split.py](media/generated/grafica_temperatura_split.py) |
