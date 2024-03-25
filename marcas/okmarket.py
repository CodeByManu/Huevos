import requests
from bs4 import BeautifulSoup
import json
from csv_uploader import *

datos_nuevos = []

ok = 'https://www.rappi.cl/tiendas/481-ok-market/lacteos-refrigerados-y-huevos/huevos'

html_ok = requests.get(ok).text
soup_ok = BeautifulSoup(html_ok, 'html.parser')
script_ok = soup_ok.find('script', type='application/json')
data_ok = json.loads(script_ok.string)

for data in data_ok["props"]["pageProps"]["fallback"]["storefront/481-ok-market/lacteos-refrigerados-y-huevos/huevos"]["aisle_detail_response"]["data"]["components"][0]["resource"]["products"]:
    print(f"""
    Nombre: {data["name"]}
    Marca: {data["trademark"]}
    Precio: {data["real_price"]}
    Cantidad: {data["quantity"]}
    """)
    datos_nuevos.append([data["name"], data["real_price"], data["quantity"], "Ok Market", "Ok Market"])

agregar_datos_csv("../huevos.csv", datos_nuevos)