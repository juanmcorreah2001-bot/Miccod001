# Gestor de Archivos con Google Drive (LPII 2026)

Módulo en Python estructurado que monta Google Drive en Google Colab, explora un directorio configurado mediante constantes y procesa archivos de datos `.json` y `.csv`.

## 🎯 Objetivo

Desarrollar un módulo modular que:

- Monte Google Drive.
- Explore un directorio definido por constantes.
- Filtre y procese archivos de datos.
- Retorne un diccionario estructurado, listo para ser consumido por una API.



## ✅ Requisitos implementados

1. **Filtrado selectivo:** solo se listan archivos con extensión `.json` o `.csv` (constante `EXTENSIONES_PERMITIDAS`).
2. **Metadatos:** tamaño en KB (`os.path.getsize`) y fecha de última modificación (`os.path.getmtime`).
3. **Parseo estructurado:** si existe `inventario.json`, se lee con `json.load()` y se valida que sea una lista de registros.
4. **Retorno modular:** la función `list_files_in_directory()` devuelve un diccionario en memoria.





