import requests
from csv_uploader import *

datos_huevos = []

url = "https://websites-api.getjusto.com/graphql?operationName=getCategoryProducts&variables=%7B%22page%22%3A1%2C%22limit%22%3A12%2C%22categoryId%22%3A%22yFcFkSTjmbCuFKekJ%22%2C%22menuId%22%3A%22ykRQoXpkdPqkXbKJF%22%2C%22format%22%3A%22webp%22%2C%22filter%22%3A%22%22%2C%22productFilters%22%3A%5B%5D%2C%22priceFilters%22%3A%5B%5D%2C%22storeId%22%3Anull%2C%22deliverAt%22%3Anull%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%228331df29c66a81acc9325174d102ba4746b591295fb9c041cf5460b01a043872%22%7D%7D"

headers = {
    "accept": "*/*",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "apollographql-client-name": "websites",
    "apollographql-client-version": "local",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "x-orion-deviceid": "WHnZBV8xTdwkopCCJhI3BKkxT7DA3B53fgiglaI62GpsVsuSfj",
    "x-orion-domain": "delivery.oxxo.cl",
    "x-orion-fp": "f532090578625371bf76cd6dcc988c13",
    "x-orion-pathname": "/pedir/category/yFcFkSTjmbCuFKekJ",
    "x-orion-referrer": "",
    "x-orion-timezone": "America/Santiago",
    "x-orion-web-version": "2"
}

response = requests.get(url, headers=headers)
response = response.json()

products = response['data']['category']['paginatedProducts']['items']
print(products)

# Filtra los productos para obtener solo los huevos
huevos = [product for product in products if 'HUEVO' in product['name'].upper()]

# Imprime los datos de los huevos
for huevo in huevos:
    cantidad = huevo['name'].split(" ")[-2]
    print(f"Nombre: {huevo['name']}")
    print(f"Precio: {huevo['availabilityAt']['finalPrice']}")
    print(f"Cantidad: {cantidad}")
    print("-"*30)
    datos_huevos.append([huevo['name'], huevo['availabilityAt']['finalPrice'], cantidad, "Oxxo", "Oxxo"])

agregar_datos_csv("../huevos.csv", datos_huevos)