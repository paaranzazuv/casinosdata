# 📃 Proceso de Consolidación de Datos

Este proyecto automatiza el procesamiento de archivos Excel provenientes de máquinas, extrayendo información clave y consolidándola en un solo archivo. Está pensado para usarse con Power BI o herramientas de análisis posteriores.

## 📦 Estructura del Proyecto

```
proceso/
├── data/
│   ├── input/            # Carpeta donde se cargan los archivos nuevos (.xlsx)
│   └── procesados/       # Carpeta donde se guarda el archivo final consolidado
├── proceso/
│   └── preprocesador.py  # Lógica principal de lectura, limpieza y escritura
├── main.py               # Ejecuta el proceso de carga de archivos
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Este archivo
```

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/proceso.git
cd proceso
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno

* En Windows:

```bash
.venv\Scripts\activate
```

* En macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el script

Asegúrate de tener archivos `.xlsx` dentro de `data/input/`. Luego ejecuta:

```bash
python main.py
```

Los datos procesados se consolidarán automáticamente en:
📁 `data/procesados/data.xlsx`

## 📌 Requisitos

* Python 3.8 o superior
* Librerías: `pandas`, `openpyxl`, `shutil`, `os`
