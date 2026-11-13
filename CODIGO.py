

import json
import os
from datetime import datetime

PUNTO_MONTAJE = '/content/drive'
DIRECTORIO = '/content/drive/My Drive/LPII_2026'
EXTENSIONES_PERMITIDAS = ('.json', '.csv')
ARCHIVO_INVENTARIO = 'inventario.json'
FORMATO_FECHA = '%Y-%m-%d %H:%M:%S'

def montar_drive():
    """Monta Google Drive si se ejecuta en Google Colab."""
    try:
        from google.colab import drive
        drive.mount(PUNTO_MONTAJE)
        return True
    except ImportError:
        print('Aviso: no se está ejecutando en Google Colab; se omite el montaje.')
        return False

def obtener_metadatos(ruta):
    """Devuelve el tamaño en KB y la fecha de última modificación de un archivo."""
    tamano_kb = round(os.path.getsize(ruta) / 1024, 2)
    fecha = datetime.fromtimestamp(os.path.getmtime(ruta)).strftime(FORMATO_FECHA)
    return tamano_kb, fecha


def validar_inventario(ruta):
    """
    Lee inventario.json con json.load() y valida que sea una lista de
    registros (cada registro debe ser un diccionario).
    """
    resultado = {
        'encontrado': True,
        'valido': False,
        'total_registros': 0,
        'registros': [],
        'error': None,
    }
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            datos = json.load(f)

        if not isinstance(datos, list):
            resultado['error'] = 'El contenido debe ser una lista de registros.'
        elif not all(isinstance(r, dict) for r in datos):
            resultado['error'] = 'Todos los elementos de la lista deben ser registros (objetos JSON).'
        else:
            resultado['valido'] = True
            resultado['registros'] = datos
            resultado['total_registros'] = len(datos)

    except json.JSONDecodeError as e:
        resultado['error'] = f'JSON mal formado: {e}'
    except (OSError, UnicodeDecodeError) as e:
        resultado['error'] = f'No se pudo leer el archivo: {e}'

    return resultado


def list_files_in_directory(directorio, extensiones=EXTENSIONES_PERMITIDAS):
    """
    Explora un directorio, filtra por extensión, calcula metadatos y valida
    inventario.json.

    Retorna un diccionario estructurado:
    {
        'directorio': str,
        'estado': 'ok' | 'error',
        'mensaje': str,
        'extensiones_filtradas': list,
        'total_archivos': int,
        'archivos': [
            {'nombre', 'extension', 'tamano_kb', 'ultima_modificacion'}, ...
        ],
        'inventario': {
            'encontrado', 'valido', 'total_registros', 'registros', 'error'
        }
    }
    """
    respuesta = {
        'directorio': directorio,
        'estado': 'ok',
        'mensaje': '',
        'extensiones_filtradas': list(extensiones),
        'total_archivos': 0,
        'archivos': [],
        'inventario': {
            'encontrado': False,
            'valido': False,
            'total_registros': 0,
            'registros': [],
            'error': None,
        },
    }

    try:
        nombres = sorted(os.listdir(directorio))
    except FileNotFoundError:
        respuesta['estado'] = 'error'
        respuesta['mensaje'] = 'Directorio no encontrado.'
        print(respuesta['mensaje'])
        return respuesta
    except NotADirectoryError:
        respuesta['estado'] = 'error'
        respuesta['mensaje'] = 'La ruta indicada no es un directorio.'
        print(respuesta['mensaje'])
        return respuesta
    except PermissionError:
        respuesta['estado'] = 'error'
        respuesta['mensaje'] = 'Sin permisos para leer el directorio.'
        print(respuesta['mensaje'])
        return respuesta

    print(f'Archivos {", ".join(extensiones)} en {directorio}:')

    for nombre in nombres:
        ruta = os.path.join(directorio, nombre)
        extension = os.path.splitext(nombre)[1].lower()

        # Filtrado selectivo: solo archivos .json o .csv
        if not os.path.isfile(ruta) or extension not in extensiones:
            continue

        try:
            tamano_kb, fecha = obtener_metadatos(ruta)
        except OSError as e:
            print(f' └── {nombre} (no se pudieron leer los metadatos: {e})')
            continue

        respuesta['archivos'].append({
            'nombre': nombre,
            'extension': extension,
            'tamano_kb': tamano_kb,
            'ultima_modificacion': fecha,
        })
        print(f' └── {nombre} | {tamano_kb} KB | Última modificación: {fecha}')

    respuesta['total_archivos'] = len(respuesta['archivos'])

    if respuesta['total_archivos'] == 0:
        respuesta['mensaje'] = 'No se encontraron archivos con las extensiones indicadas.'
        print(respuesta['mensaje'])
    else:
        respuesta['mensaje'] = f'{respuesta["total_archivos"]} archivo(s) encontrado(s).'

    # Parseo estructurado de inventario.json (si existe)
    ruta_inventario = os.path.join(directorio, ARCHIVO_INVENTARIO)
    if os.path.isfile(ruta_inventario):
        respuesta['inventario'] = validar_inventario(ruta_inventario)
        inv = respuesta['inventario']
        if inv['valido']:
            print(f'\n{ARCHIVO_INVENTARIO} válido: {inv["total_registros"]} registro(s).')
        else:
            print(f'\n{ARCHIVO_INVENTARIO} inválido: {inv["error"]}')

    return respuesta

def main():
    montar_drive()
    resultado = list_files_in_directory(DIRECTORIO)
    # Vista del diccionario listo para una API
    print('\nResultado (JSON):')
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    return resultado


if __name__ == '__main__':
    main()
