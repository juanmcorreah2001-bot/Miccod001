# Gestor de Archivos con Google Drive (LPII 2026)

Módulo en Python estructurado que monta Google Drive en Google Colab, explora un directorio configurado mediante constantes y procesa archivos de datos `.json` y `.csv`.

## 🎯 Objetivo

Desarrollar un módulo modular que:

- Monte Google Drive.
- Explore un directorio definido por constantes.
- Filtre y procese archivos de datos.
- Retorne un diccionario estructurado, listo para ser consumido por una API.

## 📋 Ponderación

| Concepto | Valor |
|---|---|
| Escala | 0 a 20 puntos |
| Ponderación en planificación | 10% de la nota final |
| Aporte neto a la nota definitiva | 2.0 puntos |

## ✅ Requisitos implementados

1. **Filtrado selectivo:** solo se listan archivos con extensión `.json` o `.csv` (constante `EXTENSIONES_PERMITIDAS`).
2. **Metadatos:** tamaño en KB (`os.path.getsize`) y fecha de última modificación (`os.path.getmtime`).
3. **Parseo estructurado:** si existe `inventario.json`, se lee con `json.load()` y se valida que sea una lista de registros.
4. **Retorno modular:** la función `list_files_in_directory()` devuelve un diccionario en memoria.

## 📁 Estructura

```
.
├── gestor_archivos.py   # Módulo principal
└── README.md
```

## ⚙️ Configuración

Las constantes están al inicio de `gestor_archivos.py`:

```python
PUNTO_MONTAJE = '/content/drive'
DIRECTORIO = '/content/drive/My Drive/LPII_2026'
EXTENSIONES_PERMITIDAS = ('.json', '.csv')
ARCHIVO_INVENTARIO = 'inventario.json'
```

## 🚀 Uso

### En Google Colab

1. Sube `gestor_archivos.py` a Colab (o clona el repositorio).
2. Crea en tu Drive la carpeta `LPII_2026` con tus archivos `.json` / `.csv`.
3. Ejecuta:

```python
from gestor_archivos import main
resultado = main()
```

También puedes llamar solo a la función:

```python
from gestor_archivos import montar_drive, list_files_in_directory, DIRECTORIO

montar_drive()
resultado = list_files_in_directory(DIRECTORIO)
```

## 📤 Estructura del diccionario retornado

```json
{
  "directorio": "/content/drive/My Drive/LPII_2026",
  "estado": "ok",
  "mensaje": "2 archivo(s) encontrado(s).",
  "extensiones_filtradas": [".json", ".csv"],
  "total_archivos": 2,
  "archivos": [
    {
      "nombre": "inventario.json",
      "extension": ".json",
      "tamano_kb": 1.25,
      "ultima_modificacion": "2026-11-13 10:30:00"
    }
  ],
  "inventario": {
    "encontrado": true,
    "valido": true,
    "total_registros": 5,
    "registros": [],
    "error": null
  }
}
```

## 🛡️ Manejo de excepciones

- `FileNotFoundError`: directorio inexistente.
- `NotADirectoryError`: la ruta no es un directorio.
- `PermissionError`: sin permisos de lectura.
- `json.JSONDecodeError`: `inventario.json` mal formado.
- `ImportError`: ejecución fuera de Colab (se omite el montaje).

## 👩‍💻 Autora

Elianny — UNEFA, Núcleo Apure — Lenguaje de Programación II
