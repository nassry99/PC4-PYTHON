

import requests
import csv
from datetime import datetime

def precio_real_b():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa (código de estado diferente de 200)
        data = response.json()
        precio = data["bpi"]["USD"]["rate_float"]
        return precio
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None
    
def save_price(precio, archivo):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(archivo, 'a') as file:
        file.write(f"{timestamp}: {precio} USD\n")

def main():
    precio_bitcoin = precio_real_b()
    if precio_bitcoin is not None:
        archivo = 'bitcoin_prices.txt'
        save_price(precio_bitcoin, archivo)
        print(f"Precio de Bitcoin guardado en '{archivo}'")

if __name__ == "__main__":
    main()