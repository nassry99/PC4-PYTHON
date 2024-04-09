import requests

def precio_real():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        precio = data["bpi"]["USD"]["rate_float"]
        return precio
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    n = input("Ingrese la cantidad de Bitcoins que posee: ")
    try:
        n = float(n)
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    bitcoin = precio_real()
    if bitcoin is not None:
        costo_en_usd = n*bitcoin
        print(f"El costo actual de {n:.4f} Bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
