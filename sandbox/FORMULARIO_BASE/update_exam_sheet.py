import re

filepath = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1-examen.md'

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Insertion 1: Diode table and visual rule
diodo_model_str = """### 1.1 Modelo del Diodo en DC"""
diodo_model_replacement = """### 1.1 Modelo del Diodo en DC
* **Caídas Típicas de Voltaje ($V_D$):**

  | Tipo | $V_D$ típico |
  | --- | --- |
  | Silicio | $0.7\\text{ V}$ |
  | Germanio | $0.3\\text{ V}$ |
  | Schottky | $0.2\\text{ V} - 0.3\\text{ V}$ |
  | LED | $1.8\\text{ V} - 3.3\\text{ V}$ |

* **Regla Visual Rápida (Análisis Gráfico):**
  * **Diodo OFF** $\\implies I_D \\approx 0$
  * **Diodo ON** $\\implies V_D \\approx 0.7\\text{ V}$
"""
text = text.replace(diodo_model_str, diodo_model_replacement)


# Insertion 2: Rectifier warning and quick table
rect_str = """## 2. Rectificadores

### 2.1 Transformador"""
rect_replacement = """## 2. Rectificadores

> [!WARNING]
> **Condición de Validez:** Las aproximaciones estandarizadas de $V_{DC}$, $V_{rms}$ y eficiencia son válidas asumiendo **$V_m \\gg V_D$**. Para señales pequeñas, el error se incrementa y se debe usar integración angular.

### Tabla Rápida de Rectificadores
| Circuito | $V_{DC}$ | $f_{\\text{rizo}}$ |
| --- | --- | --- |
| **Media Onda** | $0.318 V_m$ | $f_{in}$ |
| **Onda Completa** | $0.636 V_m$ | $2f_{in}$ |

### 2.1 Transformador"""
text = text.replace(rect_str, rect_replacement)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated Formulario-tema_1-examen.md successfully.")
