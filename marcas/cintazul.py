import requests
import json
from bs4 import BeautifulSoup
from csv_uploader import *

datos_nuevos = []

def huevos_cintazul(url):
    page = requests.get(url).text
    soup_cintazul = BeautifulSoup(page, "html.parser")
    precio = soup_cintazul.find_all("div", class_="product_content_info")
    for p in precio:
        detalle = p.find("a")
        print(f"""
        Nombre: {detalle.text}
        Precio: {p.find("span", class_="price").text}
        Marca: Cintazul
        Unidades: {detalle.text.split(" ")[-2].strip("(") if any(char.isdigit() for char in detalle.text) else "N/A"}
        Tipo: {url.split("/")[-2].split("-")[-1].capitalize()}
        """)
        datos_nuevos.append([detalle.text, p.find("span", class_="price").text, detalle.text.split(" ")[-2].strip("(") if any(char.isdigit() for char in detalle.text) else "N/A", "Cintazul", "Cintazul"])

cintazul_blanco = "https://tienda.cintazul.cl/categoria-producto/huevos-blancos/"
cintazul_color = "https://tienda.cintazul.cl/categoria-producto/huevos-color/"
cintazul_libre = "https://tienda.cintazul.cl/categoria-producto/huevos-gallina-libre/"

url_cintazul = [cintazul_blanco, cintazul_color, cintazul_libre]

for url in url_cintazul:
    huevos_cintazul(url)

agregar_datos_csv("../huevos.csv", datos_nuevos)