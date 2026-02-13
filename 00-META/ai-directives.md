<!--
::METADATA::
type: reference
topic_id: ai-directives
file_id: ai-directives
status: stable
audience: ai_context
last_updated: 2026-02-13
-->

# 🔧 Directivas Técnicas para IA — Diodos y Transistores

> Reglas técnicas complementarias al [Contrato IA](ia-contract.md).

Este documento recopila las mejores prácticas, correcciones y observaciones técnicas derivadas del desarrollo del material didáctico del repositorio.

## 1. Generación de Gráficas en Python

Para la creación de curvas características de componentes electrónicos (como diodos y transistores), se deben seguir las siguientes pautas para asegurar claridad y precisión técnica:

### Manejo de Escalas Dispares
Los componentes electrónicos suelen tener zonas de operación con magnitudes extremadamente diferentes (ej. Amperios en directa vs Nanoamperios en inversa).
*   **Problema:** Una escala lineal simple oculta los detalles de las corrientes de fuga ($I_S$).
*   **Solución Recomendada:** Generar dos visualizaciones separadas o usar "Insets" (gráficas insertadas).
    *   **Gráfica Global:** Para ver el comportamiento general (ruptura y conducción).
    *   **Gráfica de Zoom:** Específica para la región cercana al origen para mostrar que $I \neq 0$.

### Simulación de Ecuaciones
*   Al modelar la ecuación de Shockley, incluir términos para la **Región de Ruptura** si se desea visualizar el componente completo, ya que la ecuación estándar solo cubre directa e inversa ideal sin ruptura.
*   Código ejemplo para ruptura simplificada:
    ```python
    i_breakdown = -Is * np.exp(-(V - Vbr) / (n * Vt))
    ```

## 2. Formato LaTeX en Documentación Markdown

El proyecto utiliza renderizado de fórmulas matemáticas mediante LaTeX.

### Sintaxis
*   **Inline (en línea):** Usar un solo signo de dólar `$ E = mc^2 $`.
*   **Bloque (centrado):** Usar doble signo de dólar `$$` al inicio y final de la línea.

### ⚠️ Escritura Automatizada (Terminal/Bash)
Un error común al generar documentación automáticamente desde la terminal es la **desaparición de fórmulas LaTeX**.

*   **El Problema:** Al usar comandos como `cat >> archivo <<EOF`, la terminal (bash) interpreta los símbolos `$` como variables de entorno (ej. `$V_T` intenta buscar la variable `V_T`). Si no existe, la reemplaza por vacío.
*   **La Solución:** Siempre usar comillas simples en el delimitador del *Heredoc* (`'EOF'`) para evitar la interpolación de variables.

**Incorrecto (destruye LaTeX):**
```bash
cat >> archivo.md <<EOF
El voltaje es $V_T$
EOF
# Resultado en archivo: "El voltaje es "
```

**Correcto (preserva LaTeX):**
```bash
cat >> archivo.md <<'EOF'
El voltaje es $V_T$
EOF
# Resultado en archivo: "El voltaje es $V_T$"
```

## 3. Gestión de Imágenes Generadas (Limpieza de `media/generated/`)

Cuando una imagen nueva **reemplace** a una imagen anterior:

*   Actualizar las referencias del repo para apuntar al archivo vigente.
*   Eliminar del repositorio la imagen anterior que ya no se usa.
*   Verificar que no existan enlaces rotos después del reemplazo.

Regla operativa: `media/generated/` debe contener solo imágenes con uso actual en documentación o flujo de generación vigente.

## 4. Política de Scripts de Generación de Gráficos

Cada gráfico generado debe cumplir las siguientes reglas:

1. **Un script por gráfico (o conjunto temático coherente).** Cada script Python en `00-META/tools/` produce una o varias imágenes estrechamente relacionadas. No mezclar gráficos de temas distintos en un mismo script.
2. **Referencia cruzada obligatoria.** Toda imagen generada debe estar referenciada en:
   - La **nota o documento** `.md` donde se utiliza (enlace Markdown estándar).
   - El archivo de control **[Control_Scripts.md](tools/Control_Scripts.md)**, donde se lleva el registro centralizado de todos los scripts, sus imágenes y las notas que las consumen.
3. **Metadatos en cada script.** Todo script `.py` debe incluir un bloque de comentarios con metadatos al inicio (dentro del docstring o inmediatamente después) con al menos:
   - `script_id`: nombre del archivo sin extensión.
   - `module`: prefijo del módulo (`DIO`, `BJT`, `FET`, `AMP`, `PRO`).
   - `generates`: lista de imágenes PNG que produce.
   - `referenced_by`: lista de archivos `.md` que enlazan las imágenes.
   - `last_updated`: fecha de última modificación.
4. **Actualización del registro.** Al crear, modificar o eliminar un script, actualizar `Control_Scripts.md` de forma inmediata.
