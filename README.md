# 🏦 Análisis Exploratorio de Datos (EDA) de Campaña de Marketing Bancario

Este repositorio contiene el código fuente y los reportes generados para el **Trabajo Final: Análisis de Dataset de Datos de Marketing de Banca**, desarrollado para el curso de Herramientas Básicas de Programación en Python.

El proyecto se centra en el **Bank Marketing Dataset** (UCI Machine Learning Repository) para caracterizar a los clientes de una entidad bancaria y evaluar la eficacia operativa de una campaña de telemercadeo.

---

## 🎯 Objetivos del Proyecto

El análisis se enfoca en responder las siguientes preguntas de negocio:

* **Perfil Demográfico:** Identificar y caracterizar el perfil de edad principal de los clientes contactados.
* **Engagement:** Determinar qué perfiles laborales muestran mayor **interés (*engagement*)**, utilizando la duración de la llamada como métrica clave.
* **Consistencia Operativa:** Evaluar la **variabilidad** de la duración de las llamadas por mes y estado civil para detectar inconsistencias en el proceso de venta.

---

## 🛠️ Estructura del Repositorio

| Archivo/Directorio | Descripción |
| :--- | :--- |
| `main.py` | Script principal que contiene todas las funciones de ingesta, limpieza, transformación, análisis y visualización. |
| `data/bank-full.csv` | **Dataset original** utilizado para el análisis (Fuente: UCI Machine Learning Repository). |
| `data/processed/` | Directorio que almacena los reportes de salida generados. |
| `data/processed/age_stats.csv` | Reporte de estadísticas descriptivas de la variable `age`. |
| `data/processed/report_average_call_duration_per_job.csv` | Reporte de la duración promedio (mean, median, min, max, std) de las llamadas por ocupación. |

---

## 🚀 Cómo Ejecutar el Análisis

Para replicar el análisis y generar los reportes, sigue estos pasos:

### 1. Requisitos

- **Crear el entorno virtual (solo la primera vez)**

```
python -m venv pr-venv
```

## Instalación y entorno virtual

- Windows CMD:
```cmd
pr-venv\Scripts\activate
```

- Windows PowerShell:
```powershell
.\pr-venv\Scripts\Activate.ps1
```

- Linux / macOS:
```bash
source pr-venv/bin/activate
```

## Instalar dependencias

```
pip install -r requirements.txt
```

### 2. Ejecución

El script main.py está diseñado para ejecutar todo el flujo de trabajo automáticamente:

```bash
python main.py
```
Al finalizar, se generarán tres visualizaciones (Histograma de Edad, Barras de Duración, Heatmap de Variabilidad) y se actualizarán los archivos CSV de salida dentro de la carpeta data/processed/.
