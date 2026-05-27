# Guía de Personalización de Formatos en Pandoc

Pandoc utiliza diferentes metodologías de estilo dependiendo del formato de destino. A continuación se detalla cómo configurar márgenes, tipografías e interlineado tanto para exportaciones a Word (`.docx`) como a PDF.

---

## 1. Modificar Formato para Word (.docx)

La exportación a Microsoft Word no acepta variables de estilo por línea de comandos. En su lugar, Pandoc emplea un **Documento de Referencia** o "plantilla base" de la cual hereda el diseño de página, márgenes y todos los estilos tipográficos (Título 1, Texto normal, etc.).

### Proceso de Configuración:

1.  **Extraer la plantilla base:**
    Abre la terminal en la carpeta de tu proyecto y extrae el documento maestro de Pandoc:
    ```powershell
    pandoc -o plantilla_estilos.docx --print-default-data-file reference.docx
    ```

2.  **Modificar la plantilla en Microsoft Word:**
    *   Abre `plantilla_estilos.docx` en Microsoft Word.
    *   **Márgenes:** Ve a *Disposición* o *Diseño de Página* y modifica los márgenes de la página (ej. 3 cm).
    *   **Fuente e Interlineado:** Haz clic derecho en el estilo **"Normal"** dentro de la galería de Estilos y selecciona **Modificar**. Selecciona fuente Arial, tamaño 12, e interlineado 1.5. 
    *   Guarda y cierra el archivo.

3.  **Compilar usando la plantilla personalizada:**
    Al momento de renderizar tus archivos Markdown, instruye a Pandoc para que utilice tu archivo de referencia con la bandera `--reference-doc`:
    ```powershell
    pandoc "archivo.md" -o "archivo_final.docx" --reference-doc="plantilla_estilos.docx"
    ```

---

## 2. Modificar Formato para PDF

Para exportar a PDF (cuyo motor interno predeterminado es LaTeX), Pandoc **sí permite** ajustar estos valores directamente en el comando de ejecución mediante la bandera de variables `-V` o `--variable`.

### A. Ajustar Márgenes, Tamaño de Letra e Interlineado (Estándar)

Puedes inyectar las configuraciones en la terminal:

```powershell
pandoc "archivo.md" -o "archivo.pdf" -V geometry:"margin=2.5cm" -V fontsize=12pt -V linestretch=1.5
```
*   **`geometry:"margin=2.5cm"`:** Define un margen parejo. (Alternativa avanzada: `geometry:"top=2cm, bottom=2cm, left=3cm, right=3cm"`).
*   **`fontsize=12pt`:** Tamaño base de la fuente (limitado a 10pt, 11pt, 12pt en LaTeX básico).
*   **`linestretch=1.5`:** Interlineado (espaciado entre líneas).

### B. Cambiar el Tipo de Letra (Arial, Times New Roman, etc.)

El motor predeterminado de LaTeX (`pdflatex`) no soporta cargar fuentes del sistema operativo (como Arial o Calibri) de forma directa. Para cambiar la fuente, debes utilizar el motor **`xelatex`** y especificar la variable `mainfont`.

```powershell
pandoc "archivo.md" -o "archivo.pdf" --pdf-engine=xelatex -V mainfont="Arial" -V geometry:"margin=2.5cm" -V fontsize=12pt -V linestretch=1.5
```

> **Nota:** Para que `mainfont` funcione, debes tener instalado el motor XeLaTeX en tu distribución (MiKTeX en Windows generalmente lo incluye por defecto) y la fuente especificada ("Arial") debe estar instalada en tu sistema.
