import requests
url="https://api.apis.net.pe/v1/tipo-cambio-sunat?month=3&year=2024"
response=requests.get(url)


data = response.json()


with open('sunat_info.db', mode='w') as file:

    for registro in data:

        fecha = registro['fecha']
        compra = registro['compra']
        venta = registro['venta']

        file.writelines([f'====== {fecha} =======\n', f'Compra USD: {compra}\n', f'Venta USD: {venta}\n'])