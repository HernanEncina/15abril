import json
import csv
from datetime import datetime
import sys

def leer_archivo(nombre):
    if nombre.endswith('.txt'):
        with open(nombre, 'r') as f:
            return [{'linea': i, 'contenido': l.strip()} for i, l in enumerate(f.readlines())]
    elif nombre.endswith('.json'):
        with open(nombre, 'r') as f:
            return json.load(f)
    elif nombre.endswith('.csv'):
        datos = []
        with open(nombre, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                datos.append(row)
        return datos
    else:
        raise ValueError("Formato no soportado")

def filtrar_datos(datos, filtro_edad=18):
    if isinstance(datos, list) and len(datos) > 0 and 'edad' in datos[0]:
        return [d for d in datos if int(d['edad']) >= filtro_edad]
    return datos

def generar_resultado(datos_filtrados, nombre_salida='resultado.json'):
    with open(nombre_salida, 'w') as f:
        json.dump(datos_filtrados, f, indent=2)
    return nombre_salida

def registrar_log(archivo_original, resultado, version="v1.0"):
    with open('backup.log', 'a') as log:
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{ahora} | Archivo: {archivo_original} | Resultado: {len(resultado)} registros filtrados | Version: {version}\n")

def main():
    if len(sys.argv) < 2:
        print("Uso: python procesador.py <archivo>")
        return
    
    archivo = sys.argv[1]
    print(f"Procesando {archivo}...")
    
    datos = leer_archivo(archivo)
    print(f"Leidos {len(datos)} registros")
    
    filtrados = filtrar_datos(datos)
    print(f"Filtrados {len(filtrados)} registros (edad >= 18)")
    
    salida = generar_resultado(filtrados)
    print(f"Resultado guardado en {salida}")
    
    registrar_log(archivo, filtrados)
    print("Log guardado en backup.log")

if __name__ == "__main__":
    main()