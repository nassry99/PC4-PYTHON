

import pyfiglet
import random

def aleatorio():
    disponible = pyfiglet.FigletFont.getFonts()
    _aleatoria = random.choice(disponible)
    return _aleatoria

def main():
    fuente = aleatorio()
    texto = input("Ingrese el texto: ")
    
    try:
        fig = pyfiglet.Figlet(font=fuente)
        resultado = fig.renderText(texto)
        print(resultado)
    except pyfiglet.FontNotFound:
        print(f"La fuente '{fuente}' no fue encontrada.")
if __name__ == "__main__":
    main()