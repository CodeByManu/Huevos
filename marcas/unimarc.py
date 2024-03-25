import requests
from bs4 import BeautifulSoup
import json
from csv_uploader import *

datos_nuevos = []

unimarc = "https://www.unimarc.cl/category/lacteos-huevos-y-refrigerados/huevos"

html_unimarc = requests.get(unimarc).text
soup_unimarc = BeautifulSoup(html_unimarc, "html.parser")
script_unimarc = soup_unimarc.find("script", type="application/json")
data_unimarc = json.loads(script_unimarc.string)

for item in data_unimarc["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["data"]["availableProducts"]:
    print(f"""
    nombre: {item["name"]}
    precio: {item["sellers"][0]["listPrice"]}
    marca: {item["brand"]}
    unidades: {item["netContent"].replace("unidad", "").strip()}

""")
    datos_nuevos.append([item["name"], item["sellers"][0]["listPrice"], item["netContent"].replace("unidad", "").strip(), item["brand"], "Unimarc"])

agregar_datos_csv("../huevos.csv", datos_nuevos)