import requests
import json
from csv_uploader import *

datos_nuevos = []

url = "https://apps.lider.cl/supermercado/bff/category"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"122\", \"Not(A:Brand\";v=\"24\", \"Microsoft Edge\";v=\"122\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "tenant": "supermercado",
    "x-channel": "SOD",
    "x-flowid": "3ff39d4b-979a-455c-b81a-8bfc97c1ffcf",
    "x-sessionid": "833587b7-2f31-4223-9a4f-df9f303cf2cc",
    "cookie": "Aquí van tus cookies",
    "Referer": "https://www.lider.cl/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

body = {
    "categories": "Frescos y Lácteos/Huevos y Mantequillas/Huevos",
    "page": 1,
    "facets": [],
    "sortBy": "",
    "hitsPerPage": 64
}

response = requests.post(url, headers=headers, data=json.dumps(body))
response = response.json()


for i,product in enumerate(response['products']):
    Nombre = product["displayName"].split(",")[0]
    if 'blanco' in Nombre.lower():
        Color = 'Blanco'
    elif 'color' in Nombre.lower():
        Color = 'Color'
    elif "feliz" in Nombre.lower() or "libre" in Nombre.lower():
        Color = 'Libre'
    else:
        Color = 'N/A'
    print(f"""
    Nombre: {Nombre}
    Marca: {product["brand"]}
    Precio: {product["price"]["BasePriceReference"]}""")
    if any(char.isdigit() for char in Nombre) and "un" in Nombre.lower():
        unidades = int(''.join(filter(str.isdigit, Nombre)))
        print(f"    Unidades: {unidades}")
    else: 
        unidades = "N/A"
        print("    Unidades: N/A")
    print("    Color: ", Color)
    datos_nuevos.append([Nombre, product["price"]["BasePriceReference"], unidades, product["brand"], "Lider"])

agregar_datos_csv("../huevos.csv", datos_nuevos)