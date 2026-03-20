<!--
::METADATA::
type: reference
topic_id: control-scripts
file_id: Control_Scripts
status: active
audience: ai_context
last_updated: 2026-02-23
-->

# 📋 Control de Scripts de Generación de Gráficos

> Registro centralizado de todos los scripts Python en `00-meta/tools/`, las imágenes que generan y los documentos que las referencian.
>
> **Regla:** al crear, modificar o eliminar un script, este archivo DEBE actualizarse de inmediato.

---

## Módulo 01 — Circuitos con Diodos (`DIO`)

### DIO-gen-curva-iv.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-curva-iv.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Curva I-V completa del diodo (directa, inversa, ruptura) + zoom región inversa |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-iv-01-general.png` | `topics/01-circuitos-diodos/assets/` | [DIO-01-Teoria-Diodo.md](../../topics/01-circuitos-diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-iv-02-zoom-inversa.png` | `topics/01-circuitos-diodos/assets/` | [DIO-01-Teoria-Diodo.md](../../topics/01-circuitos-diodos/theory/DIO-01-Teoria-Diodo.md) |

---

### DIO-gen-curva-temperatura.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-curva-temperatura.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Efecto de temperatura en el diodo (gráfica combinada) |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-temp-01-combinada.png` | `topics/01-circuitos-diodos/assets/` | [image-metadata.json](../../topics/01-circuitos-diodos/assets/image-metadata.json) |

---

### DIO-gen-curva-temperatura-split.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-curva-temperatura-split.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Efecto de temperatura (split): directa, inversa, ruptura por separado |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `DIO-curva-temp-02-directa.png` | `topics/01-circuitos-diodos/assets/` | [DIO-01-Teoria-Diodo.md](../../topics/01-circuitos-diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-temp-03-inversa.png` | `topics/01-circuitos-diodos/assets/` | [DIO-01-Teoria-Diodo.md](../../topics/01-circuitos-diodos/theory/DIO-01-Teoria-Diodo.md) |
| `DIO-curva-temp-04-ruptura.png` | `topics/01-circuitos-diodos/assets/` | [DIO-01-Teoria-Diodo.md](../../topics/01-circuitos-diodos/theory/DIO-01-Teoria-Diodo.md) |

---

### DIO-gen-esquematico-pequena-senal.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-esquematico-pequena-senal.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemáticos y gráficas para análisis de pequeña señal del diodo |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `circuito_dc_diodo.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `modelo_pequena_senal.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `circuito_ac_superpuesto.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `recta_de_carga_punto_q.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `diodo_pequena_senal.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `formas_de_onda_temporal.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |

---

### DIO-gen-pequena-senal.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-pequena-senal.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Gráfica de linealización del punto Q y modelo de pequeña señal |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `diodo_pequena_senal.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |

---

### DIO-gen-recta-carga-circuito.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-recta-carga-circuito.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemáticos y gráficas de recta de carga (genérico + caso 6 V / 270 Ω, incluyendo límites instantáneos $E_{\max}$ y $E_{\min}$ en la gráfica de punto Q) |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `dio-recta-carga-circuito-vd.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |
| `dio-recta-carga-extremos.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |
| `dio-circuito-ac-cd-6v-270ohm-vd.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |
| `dio-recta-carga-q-6v-270ohm.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |
| `dio-recta-carga-q-objetivo-19ma-1v5.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) *(ejemplo ajustado con $E^*=6.63V$ y $Q^*$ por intersección real)* |

---

### DIO-gen-ejercicio-recta-carga.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-ejercicio-recta-carga.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Ejercicio de recta de carga con curva I-V ajustada al modelo de Shockley ($n=1.40$, $I_S=7.24\times10^{-11}\,A$). Circuito: $E=0.8\,V$, $R=250\,\Omega$, $e=0.15\,\mathrm{sen}(\omega t)$. Intersección numérica vía `fsolve`. v2: reemplazó modelo lineal a tramos por exponencial. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|------------------|
| `dio-ejercicio-circuito-08v-250ohm.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |
| `dio-ejercicio-recta-carga-08v-250ohm.png` | `topics/01-circuitos-diodos/assets/` | [Nota2.md](../../topics/01-circuitos-diodos/Notas/Nota2.md) |

---

### DIO-gen-ejemplo-circuito-ps.py *(pendiente — actualmente dentro de DIO-gen-esquematico-pequena-senal.py)*

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `ejemplo_circuito_ps.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |
| `ejemplo_formas_onda_ps.png` | `topics/01-circuitos-diodos/assets/` | [Nota1.md](../../topics/01-circuitos-diodos/Notas/Nota1.md) |

---

### DIO-gen-rectificador-media-onda-esquema.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-rectificador-media-onda-esquema.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Diagrama esquemático de un rectificador de media onda básico |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `rectificador_media_onda_esquema.png` | `topics/01-circuitos-diodos/assets/` | [Nota3.md](../../topics/01-circuitos-diodos/Notas/Nota3.md) |

### DIO-gen-rectificador-media-onda-formas-onda.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-rectificador-media-onda-formas-onda.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Formas de onda $v_s$, $v_o$, $v_D$ para rectificador media onda |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `rectificador_media_onda_ondas.png` | `topics/01-circuitos-diodos/assets/` | [Nota3.md](../../topics/01-circuitos-diodos/Notas/Nota3.md) |

---
### DIO-gen-nota4-rectificador-transformador.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota4-rectificador-transformador.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemático y formas de onda del rectificador de media onda con transformador reductor 10:1. Genera: (1) esquemático schemdraw, (2) formas de onda con diodo real ($V_D = 0.7\,V$) + tabla, (3) los tres voltajes principales ($v_s$, $v_o$, $v_D$) en eje $\omega t$ con diodo ideal y todas las anotaciones de valores clave. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------||
| `nota4_circuito.png` | `topics/01-circuitos-diodos/assets/` | [Nota4.md](../../topics/01-circuitos-diodos/Notas/Nota4.md) |
| `nota4_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota4.md](../../topics/01-circuitos-diodos/Notas/Nota4.md) |
| `nota4_voltajes_ideales.png` | `topics/01-circuitos-diodos/assets/` | [Nota4.md](../../topics/01-circuitos-diodos/Notas/Nota4.md) |

---

### DIO-gen-nota5-rectificador-onda-completa-central.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota5-rectificador-onda-completa-central.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemático y formas de onda del rectificador monofásico de onda completa con transformador de derivación central. Genera: (1) esquemático schemdraw con transformador center-tap, dos diodos y $R_L$, (2) formas de onda ($v_{s1}$, $v_{s2}$, $v_o$, $v_{D1}$) con anotaciones de PIV, $V_{DC}$, indicación de diodo en conducción y tabla resumen. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `nota5_circuito.png` | `topics/01-circuitos-diodos/assets/` | [Nota5.md](../../topics/01-circuitos-diodos/Notas/Nota5.md) |
| `nota5_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota5.md](../../topics/01-circuitos-diodos/Notas/Nota5.md) |
| `nota5_diodos_ac.png` | `topics/01-circuitos-diodos/assets/` | [Nota5.md](../../topics/01-circuitos-diodos/Notas/Nota5.md) |

---

### DIO-gen-nota6-rectificador-puente.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota6-rectificador-puente.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemático del rectificador monolítico tipo H (puente de Graetz) con transformador de devanado simple, cuatro diodos en configuración de puente y carga $R_L$. Incluye anotaciones de pares de conducción por semiciclo. Formas de onda: $v_s$, $v_o$ (ideal y real), tensión inversa en $D_3$ y $D_1$ (PIV). |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `nota6_circuito.png` | `topics/01-circuitos-diodos/assets/` | [Nota6.md](../../topics/01-circuitos-diodos/Notas/Nota6.md) |
| `nota6_flujo_corriente.png` | `topics/01-circuitos-diodos/assets/` | [Nota6.md](../../topics/01-circuitos-diodos/Notas/Nota6.md) |
| `nota6_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota6.md](../../topics/01-circuitos-diodos/Notas/Nota6.md) |

---

### DIO-gen-nota7-fourier-armonicos.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota7-fourier-armonicos.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Descomposición en serie de Fourier del voltaje de salida del rectificador tipo puente. Armónicos individuales, reconstrucción progresiva y espectro de amplitudes. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `nota7_armonicos_individuales.png` | `topics/01-circuitos-diodos/assets/` | [Nota7.md](../../topics/01-circuitos-diodos/Notas/Nota7.md) |
| `nota7_reconstruccion_fourier.png` | `topics/01-circuitos-diodos/assets/` | [Nota7.md](../../topics/01-circuitos-diodos/Notas/Nota7.md) |
| `nota7_espectro_armonicos.png` | `topics/01-circuitos-diodos/assets/` | [Nota7.md](../../topics/01-circuitos-diodos/Notas/Nota7.md) |
| `nota7_espectro_frecuencia.png` | `topics/01-circuitos-diodos/assets/` | [Nota7.md](../../topics/01-circuitos-diodos/Notas/Nota7.md) |

---

### DIO-gen-nota7-filtro-inductivo.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota7-filtro-inductivo.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemático de rectificador puente con filtro inductivo (inductor en serie con la carga). |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `nota7_filtro_inductivo.png` | `topics/01-circuitos-diodos/assets/` | [Nota7.md](../../topics/01-circuitos-diodos/Notas/Nota7.md) |

---

### DIO-gen-nota8-recortadores.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/DIO-gen-nota8-recortadores.py` |
| **Módulo** | `DIO` — 01-Circuitos-Diodos |
| **Descripción** | Esquemáticos y formas de onda de recortadores paralelos positivos: (1) simple y (2) con polarización $V_{DC}$. Genera esquemáticos schemdraw y formas de onda con zonas de recorte sombreadas y anotaciones. |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|------------------|
| `nota8_recortador_paralelo_pos.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |
| `nota8_recortador_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |
| `nota8_recortador_polarizado.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |
| `nota8_recortador_polarizado_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |
| `nota8_recortador_serie.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |
| `nota8_recortador_serie_formas_onda.png` | `topics/01-circuitos-diodos/assets/` | [Nota8.md](../../topics/01-circuitos-diodos/Notas/Nota8.md) |

---
## Módulo 02 — Transistor BJT (`BJT`)

### BJT-gen-curvas-caracteristicas.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/BJT-gen-curvas-caracteristicas.py` |
| **Módulo** | `BJT` — topics/02-transistor-bjt |
| **Descripción** | Familia IC-VCE, recta de carga DC, regiones de operación |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `bjt_familia_curvas_ic_vce.png` | `topics/02-transistor-bjt/media/generated/` | Sin referencia actual |
| `bjt_recta_carga_dc.png` | `topics/02-transistor-bjt/media/generated/` | Sin referencia actual |
| `bjt_regiones_operacion.png` | `topics/02-transistor-bjt/media/generated/` | Sin referencia actual |

---

## Módulo 03 — Transistor FET (`FET`)

### FET-gen-curva-transferencia.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/FET-gen-curva-transferencia.py` |
| **Módulo** | `FET` — topics/03-transistor-fet |
| **Descripción** | Transferencia, salida, autopolarización gráfica JFET |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `fet_curva_transferencia.png` | `topics/03-transistor-fet/media/generated/` | Sin referencia actual |
| `fet_familia_curvas_id_vds.png` | `topics/03-transistor-fet/media/generated/` | Sin referencia actual |
| `fet_autopolarizacion_grafica.png` | `topics/03-transistor-fet/media/generated/` | Sin referencia actual |

---

## Módulo 04 — Amplificadores (`AMP`)

### AMP-gen-respuesta-frecuencia.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/AMP-gen-respuesta-frecuencia.py` |
| **Módulo** | `AMP` — topics/04-amplificadores |
| **Descripción** | Bode, comparativa EC/BC/CC, efecto de carga RL |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `amp_bode_emisor_comun.png` | `topics/04-amplificadores/media/generated/` | Sin referencia actual |
| `amp_comparativa_ec_bc_cc.png` | `topics/04-amplificadores/media/generated/` | Sin referencia actual |
| `amp_efecto_rl_ganancia.png` | `topics/04-amplificadores/media/generated/` | Sin referencia actual |

---

## Módulo 05 — Proyecto Final (`PRO`)

### PRO-gen-fuente-alimentacion.py

| Campo | Valor |
|-------|-------|
| **Script** | `00-meta/tools/PRO-gen-fuente-alimentacion.py` |
| **Módulo** | `PRO` — topics/05-proyecto-final |
| **Descripción** | Rectificación, filtrado, regulador LM317 |

| Imagen generada | Ruta | Referenciada en |
|----------------|------|-----------------|
| `pro_formas_onda_rectificacion.png` | `topics/05-proyecto-final/media/generated/` | Sin referencia actual |
| `pro_efecto_filtrado_capacitor.png` | `topics/05-proyecto-final/media/generated/` | Sin referencia actual |
| `pro_diseno_lm317.png` | `topics/05-proyecto-final/media/generated/` | Sin referencia actual |

---

## Resumen

| Módulo | Scripts | Imágenes | Con referencia | Sin referencia |
|--------|---------|----------|---------------|----------------|
| DIO | 13 | 38 | 38 | 0 |
| BJT | 1 | 3 | 0 | 3 |
| FET | 1 | 3 | 0 | 3 |
| AMP | 1 | 3 | 0 | 3 |
| PRO | 1 | 3 | 0 | 3 |
| **Total** | **17** | **50** | **38** | **12** |
