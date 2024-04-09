import requests
import zipfile
import os

def descargar_imagen(link, archivo):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            with open(archivo, 'wb') as f:
                f.write(response.content)
            print(f"Imagen descargada como '{archivo}'")
        else:
            print("Error al descargar la imagen:", response.status_code)
    except Exception as e:
        print("Error al descargar la imagen:", e)

def comprimir(name_zip1, archi_comprimiri):
    with zipfile.ZipFile(name_zip1, 'w') as zipf:
        for archivo in archi_comprimiri:
            zipf.write(archivo)
    print(f"Archivos comprimidos en '{name_zip1}'")

def descomprimir(name_zip1, destino):
    with zipfile.ZipFile(name_zip1, 'r') as zipf:
        zipf.extractall(destino)
    print(f"Archivos descomprimidos en '{destino}'")

def main():
    link_imagen = 'https://i.blogs.es/8acec8/persona-3-reload-analisis-01/original.jpeg'
    nombre_imagen = 'descarga.jpg'
    descargar_imagen(link_imagen, nombre_imagen)

    a_comprimir = [nombre_imagen]
    name_zip1 = 'imagen.zip'
    comprimir(name_zip1, a_comprimir)

    destino = 'imagen_descomprimida'
    descomprimir(name_zip1, destino)

if __name__ == "__main__":
    main()