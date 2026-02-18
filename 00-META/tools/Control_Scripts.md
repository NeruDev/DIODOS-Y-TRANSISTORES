<!--
::METADATA::
type: reference
topic_id: control-scripts
file_id: Control_Scripts
status: active
audience: ai_context
last_updated: 2026-02-13
-->

# 📋 Control de Scripts de Generación de Gráficos

> Registro centralizado de todos los scripts Python en `00-META/tools/`, las imágenes que generan y los documentos que las referencian.
>
> **Regla:** al crear, modificar o eliminar un script, este archivo DEBE actualizarse de inmediato.

---

## Módulo 01 — Circuitos con Diodos (`DIO`)

### DIO-gen-curva-iv.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-curva-iv.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Curva I-V completa del diodo (directa, inversa, ruptura) + zoom región inversa |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-iv-01-general.png` | `01-Circuitos-Diodos/media/generated/` | [DIO-01-Teoria-Diodo.md](../../01-Circuitos-Diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-iv-02-zoom-inversa.png` | `01-Circuitos-Diodos/media/generated/` | [DIO-01-Teoria-Diodo.md](../../01-Circuitos-Diodos/theory/DIO-01-Teoria-Diodo.md) |

---

### DIO-gen-curva-temperatura.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-curva-temperatura.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Efecto de temperatura en el diodo (gráfica combinada) |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-temp-01-combinada.png` | `01-Circuitos-Diodos/media/generated/` | [image-metadata.json](../../01-Circuitos-Diodos/media/generated/image-metadata.json) |

---

### DIO-gen-curva-temperatura-split.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-curva-temperatura-split.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Efecto de temperatura (split): directa, inversa, ruptura por separado |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-temp-02-directa.png` | `01-Circuitos-Diodos/media/generated/` | [DIO-01-Teoria-Diodo.md](../../01-Circuitos-Diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-temp-03-inversa.png` | `01-Circuitos-Diodos/media/generated/` | [DIO-01-Teoria-Diodo.md](../../01-Circuitos-Diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-temp-04-ruptura.png` | `01-Circuitos-Diodos/media/generated/` | [DIO-01-Teoria-Diodo.md](../../01-Circuitos-Diodos/theory/DIO-01-Teoria-Diodo.md) |

---

### DIO-gen-esquematico-pequena-senal.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-esquematico-pequena-senal.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemáticos y gráficas para análisis de pequeña señal del diodo |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `circuito_dc_diodo.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `modelo_pequena_senal.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `circuito_ac_superpuesto.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `recta_de_carga_punto_q.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `diodo_pequena_senal.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `formas_de_onda_temporal.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |

---

### DIO-gen-pequena-senal.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-pequena-senal.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Gráfica de linealización del punto Q y modelo de pequeña señal |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `diodo_pequena_senal.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |

---

### DIO-gen-recta-carga-circuito.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-recta-carga-circuito.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemáticos y gráficas de recta de carga (genérico + caso 6 V / 270 Ω, incluyendo límites instantáneos $E_{\max}$ y $E_{\min}$ en la gráfica de punto Q) |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `dio-recta-carga-circuito-vd.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |
| `dio-recta-carga-extremos.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |
| `dio-circuito-ac-cd-6v-270ohm-vd.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |
| `dio-recta-carga-q-6v-270ohm.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |
| `dio-recta-carga-q-objetivo-19ma-1v5.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) *(ejemplo ajustado con $E^*=6.63V$ y $Q^*$ por intersección real)* |

---

### DIO-gen-ejercicio-recta-carga.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-ejercicio-recta-carga.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Ejercicio de recta de carga con curva I-V ajustada al modelo de Shockley ($n=1.40$, $I_S=7.24\times10^{-11}\,A$). Circuito: $E=0.8\,V$, $R=250\,\Omega$, $e=0.15\,\mathrm{sen}(\omega t)$. Intersección numérica vía `fsolve`. v2: reemplazó modelo lineal a tramos por exponencial. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|------------------|
| `dio-ejercicio-circuito-08v-250ohm.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |
| `dio-ejercicio-recta-carga-08v-250ohm.png` | `01-Circuitos-Diodos/media/generated/` | [Nota2.md](../../01-Circuitos-Diodos/Notas/Nota2.md) |

---

### DIO-gen-ejemplo-circuito-ps.py *(pendiente — actualmente dentro de DIO-gen-esquematico-pequena-senal.py)*

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `ejemplo_circuito_ps.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |
| `ejemplo_formas_onda_ps.png` | `01-Circuitos-Diodos/media/generated/` | [Nota1.md](../../01-Circuitos-Diodos/Notas/Nota1.md) |

---

### DIO-gen-rectificador-media-onda-esquema.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-rectificador-media-onda-esquema.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Diagrama esquemático de un rectificador de media onda básico |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `rectificador_media_onda_esquema.png` | `01-Circuitos-Diodos/media/generated/` | [Nota3.md](../../01-Circuitos-Diodos/Notas/Nota3.md) |

### DIO-gen-rectificador-media-onda-formas-onda.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/DIO-gen-rectificador-media-onda-formas-onda.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Formas de onda $v_s$, $v_o$, $v_D$ para rectificador media onda |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `rectificador_media_onda_ondas.png` | `01-Circuitos-Diodos/media/generated/` | [Nota3.md](../../01-Circuitos-Diodos/Notas/Nota3.md) |

---

## Módulo 02 — Transistor BJT (`BJT`)

### BJT-gen-curvas-caracteristicas.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/BJT-gen-curvas-caracteristicas.py` |
| **Módulo** | `BJT` — 02-Transistor-BJT |
| **Descripción** | Familia IC-VCE, recta de carga DC, regiones de operación |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `bjt_familia_curvas_ic_vce.png` | `02-Transistor-BJT/media/generated/` | Sin referencia actual |
| `bjt_recta_carga_dc.png` | `02-Transistor-BJT/media/generated/` | Sin referencia actual |
| `bjt_regiones_operacion.png` | `02-Transistor-BJT/media/generated/` | Sin referencia actual |

---

## Módulo 03 — Transistor FET (`FET`)

### FET-gen-curva-transferencia.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/FET-gen-curva-transferencia.py` |
| **Módulo** | `FET` — 03-Transistor-FET |
| **Descripción** | Transferencia, salida, autopolarización gráfica JFET |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `fet_curva_transferencia.png` | `03-Transistor-FET/media/generated/` | Sin referencia actual |
| `fet_familia_curvas_id_vds.png` | `03-Transistor-FET/media/generated/` | Sin referencia actual |
| `fet_autopolarizacion_grafica.png` | `03-Transistor-FET/media/generated/` | Sin referencia actual |

---

## Módulo 04 — Amplificadores (`AMP`)

### AMP-gen-respuesta-frecuencia.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/AMP-gen-respuesta-frecuencia.py` |
| **Módulo** | `AMP` — 04-Amplificadores |
| **Descripción** | Bode, comparativa EC/BC/CC, efecto de carga RL |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `amp_bode_emisor_comun.png` | `04-Amplificadores/media/generated/` | Sin referencia actual |
| `amp_comparativa_ec_bc_cc.png` | `04-Amplificadores/media/generated/` | Sin referencia actual |
| `amp_efecto_rl_ganancia.png` | `04-Amplificadores/media/generated/` | Sin referencia actual |

---

## Módulo 05 — Proyecto Final (`PRO`)

### PRO-gen-fuente-alimentacion.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-META/tools/PRO-gen-fuente-alimentacion.py` |
| **Módulo** | `PRO` — 05-Proyecto-Final |
| **Descripción** | Rectificación, filtrado, regulador LM317 |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `pro_formas_onda_rectificacion.png` | `05-Proyecto-Final/media/generated/` | Sin referencia actual |
| `pro_efecto_filtrado_capacitor.png` | `05-Proyecto-Final/media/generated/` | Sin referencia actual |
| `pro_diseno_lm317.png` | `05-Proyecto-Final/media/generated/` | Sin referencia actual |

---

## Resumen

| Módulo | Scripts | Imágenes | Con referencia | Sin referencia |
|--------|---------|----------|---------------|----------------|
| DIO | 7 | 18 | 18 | 0 |
| BJT | 1 | 3 | 0 | 3 |
| FET | 1 | 3 | 0 | 3 |
| AMP | 1 | 3 | 0 | 3 |
| PRO | 1 | 3 | 0 | 3 |
| **Total** | **11** | **30** | **18** | **12** |
