import requests
import json
from bs4 import BeautifulSoup
from csv_uploader import *

datos_nuevos = []

marta_blanco = "https://www.huevossantamarta.cl/productos/linea/1/huevos-blancos"
marta_color = "https://www.huevossantamarta.cl/productos/linea/2/huevos-color"
marta_libre = "https://www.huevossantamarta.cl/productos/linea/3/huevos-gallina-libre"

def huevos_marta(url):
    page = requests.get(url).text
    soup_marta = BeautifulSoup(page, "html.parser")
    detail = soup_marta.find_all("div", class_="detail")

    for d in detail:
        nombre = d.find("a", class_="name").text
        unidades = nombre.split("-")[1].replace("UNIDADES", "").strip()
        print(f"""
        Nombre: {d.find("div", class_="cat").text}
        Detalle: {d.find("a", class_="name").text}
        Precio: {d.find("span").text.strip()}
        Tipo: {url.split("/")[-1].split("-")[-1].capitalize()}
        Unidades: {unidades}
        """)
        datos_nuevos.append([nombre, d.find("span").text.strip(), unidades, "Santa Marta", "Santa Marta"])

for url in [marta_blanco, marta_color, marta_libre]:
    huevos_marta(url)

agregar_datos_csv("../huevos.csv", datos_nuevos)