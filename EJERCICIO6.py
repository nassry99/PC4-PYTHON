def enumerar(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            lineas_code = 0
            for linea in lineas:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_code += 1
        return lineas_code
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return None
def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if ruta_archivo.endswith(".py"):
        num_lineas= enumerar(ruta_archivo)
        if num_lineas is not None:
            print(f"El número de líneas de código en el archivo {ruta_archivo} es: {num_lineas}")
    else:
        print("El archivo no tiene la extensión .py o la ruta es inválida.")

if __name__ == "__main__":
    main()
    