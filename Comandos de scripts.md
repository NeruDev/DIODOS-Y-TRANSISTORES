# 📜 Registro de Comandos de Scripts

Este documento sirve como referencia rápida para la ejecución de scripts interactivos y herramientas de generación visual dentro del repositorio, especialmente aquellos que requieren configuraciones específicas en entornos Headless o en **GitHub Codespaces**.

---

## ⚙️ Requisitos Globales Previos

### 1. Entorno de Ventanas (VNC / X11)
Para ejecutar cualquier script que requiera una interfaz gráfica de usuario (GUI) utilizando librerías como `tkinter`, es estrictamente necesario configurar la redirección del Display hacia el servidor VNC asociado al contenedor de desarrollo.

**Comando obligatorio antes de ejecutar cualquier script GUI:**
```bash
export DISPLAY=:1
```
*(Nota: Este comando configura la sesión actual de la terminal. Debe ejecutarse cada vez que se abre una terminal nueva si no se ha añadido globalmente al archivo `.bashrc`).*

---

## 🧮 Calculadoras Interactivas (GUI)

Estos scripts lanzan interfaces gráficas de usuario para resolver problemas, validar gráficas o explorar respuestas de forma dinámica. Requieren que el entorno VNC esté configurado previamente y se deben visualizar a través del puerto "Desktop" o "noVNC" en la pestaña "Puertos / Ports" de VS Code.

### 1. Calculadora Interactiva - Práctica 1 (Diodos)
Herramienta de cálculo y validación gráfica para los circuitos tratados en la Práctica 1.

- **Ruta relativa del script:** `01-Circuitos-Diodos/Notas/PRACTICA 1/practica1_calculadora.py`
- **Comando de ejecución:**
  ```bash
  python "01-Circuitos-Diodos/Notas/PRACTICA 1/practica1_calculadora.py"
  ```
