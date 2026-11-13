# Miccod001
# LGII-T1

## Prácticas de Lenguaje 2 — Conexión Drive & Colab

### 📌 Descripción del Proyecto

Módulo en Python diseñado para **Google Colab** que permite montar unidades de **Google Drive**, explorar directorios específicos configurados mediante constantes y listar el contenido de carpetas de forma modular y segura[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).

---

### ✨ Funcionalidades Principales

| # | Requisito | 🛠️ Implementación |
| :---: | :--- | :--- |
| 1 | **Conexión con Drive** | Montaje de la unidad personal en `/content/drive/MyDrive` dentro del entorno de Google Colab[span_6](start_span)[span_6](end_span). |
| 2 | **Ruta Configurable** | Definición mediante la constante `DIRECTORIO` para apuntar directamente a la carpeta raíz o subcarpetas específicas[span_7](start_span)[span_7](end_span). |
| 3 | **Listado Modular** | Implementación de la función `list_files_in_directory(directorio)` utilizando `os.listdir()` para recorrer e imprimir cada archivo o carpeta[span_8](start_span)[span_8](end_span). |
| 4 | **Salida Estructurada** | Visualización clara en consola de los elementos encontrados dentro de la ruta especificada[span_9](start_span)[span_9](end_span). |

> 🛡️ **Manejo de Excepciones Integrado:** Controla errores comunes de ejecución como rutas inexistentes o unidades no montadas (`FileNotFoundError`), mostrando un mensaje limpio (`Directorio no encontrado.`) sin detener abruptamente el programa[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).

---

### 🗂️ Estructura del Repositorio

```text
📦 LGII-T1
 ├── 📓 practica_drive.ipynb
 ├── 📜 LICENSE
 ├── 🙈 .gitignore
 └── 📘 README.md
