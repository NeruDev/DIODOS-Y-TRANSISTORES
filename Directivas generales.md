# Directivas Generales del Proyecto

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
