# Instrucciones de Ejecución — Practica 1 (Calculadora)

Este documento describe los pasos necesarios para ejecutar la calculadora interactiva de la Práctica 1 en entornos locales y remotos (como GitHub Codespaces).

---

## 1. Configuración del Entorno Virtual

Antes de ejecutar el script, asegúrese de tener activado el entorno virtual con las dependencias instaladas.

**En Windows (PowerShell):**
```powershell
& ".venv\Scripts\Activate.ps1"
```

**En Linux / GitHub Codespaces:**
```bash
source .venv/bin/activate
```

---

## 2. Configuración de la Interfaz Gráfica (GUI)

El script `practica1_calculadora.py` utiliza **Tkinter** y **Matplotlib (TkAgg)**, por lo que requiere un servidor de visualización activo.

### En GitHub Codespaces / Entornos sin Monitor
Para visualizar la ventana en su navegador, debe redirigir el tráfico a un servidor VNC.

1.  **Exportar el Display:**
    ```bash
    export DISPLAY=:1
    ```

2.  **Iniciar el entorno noVNC (si no está activo):**
    En GitHub Codespaces, el entorno suele estar preconfigurado. Si necesita invocarlo manualmente para abrir el puerto **6080**, use:
    ```bash
    # Comando estándar para iniciar noVNC en el puerto 6080 conectado al display :1
    /usr/share/novnc/utils/launch.sh --vnc localhost:5901 --listen 6080 &
    ```
    *Nota: En Codespaces, puede simplemente ir a la pestaña **Puertos (Ports)** y buscar el puerto etiquetado como "Desktop" o "noVNC" (6080).*

---

## 3. Ejecución del Script

Una vez configurado el entorno y el display, ejecute la calculadora desde la raíz del repositorio:

```bash
python "topics/01-circuitos-diodos/Notas/PRACTICA 1/practica1_calculadora.py"
```

O directamente desde la carpeta de la práctica:
```bash
cd "topics/01-circuitos-diodos/Notas/PRACTICA 1/"
python practica1_calculadora.py
```

---

## 4. Solución de Problemas

-   **Error: `TclError: no display name and no $DISPLAY environment variable`**
    Asegúrese de haber ejecutado `export DISPLAY=:1`.
-   **Dependencias faltantes:**
    Si recibe errores de `numpy` o `matplotlib`, reinstale los requisitos:
    ```bash
    pip install numpy==2.4.2 matplotlib==3.10.8 schemdraw==0.22 pillow==12.1.0 scipy
    ```
