def save_tabla_X(numero):
    try:
        with open(f"tabla-{numero}.txt", "w") as archivo:
            for i in range(1, 11):
                archivo.write(f"{numero} x {i} = {numero * i}\n")
        print(f"Tabla de multiplicar del {numero} guardada en tabla-{numero}.txt")
    except Exception as e:
        print("Error al guardar la tabla de multiplicar:", e)

def show_tabla_X(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= linea:
                print(lineas[linea - 1].strip())
            else:
                print(f"No hay suficientes líneas en el archivo tabla-{numero}.txt")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                save_tabla_X(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                show_tabla_X(numero)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            if 1 <= numero <= 10 and linea >= 1:
                mostrar_linea(numero, linea)
            else:
                print("El número debe estar entre 1 y 10, y la línea debe ser mayor o igual a 1.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        
if __name__ == "__main__":
    main()