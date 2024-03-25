import json
import requests
from bs4 import BeautifulSoup
from csv_uploader import *

datos_nuevos = []

url = "https://ecoterra.cl/collections/huevos"

page_ecoterra = requests.get(url).text
soup_ecoterra = BeautifulSoup(page_ecoterra, "html.parser")
huevos_eco = soup_ecoterra.find_all("div", class_="product-card__info")

for huevo in huevos_eco:
    if "clara" in huevo.find("a").text.lower() or "polvo" in huevo.find("a").text.lower():
        continue
    nombre = huevo.find("a").text
    precio = huevo.find("sale-price").text.strip().replace("Precio de oferta", "").replace("Desde ", "")
    unidades = int(''.join(filter(str.isdigit, nombre)))
    print(f"""
    Nombre: {nombre}
    Precio: {precio}
    Unidades: {unidades}
    """)
    datos_nuevos.append([nombre, precio, unidades, "Ecoterra", "Ecoterra"])

agregar_datos_csv("../huevos.csv", datos_nuevos)