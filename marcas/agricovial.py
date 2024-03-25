import requests
import json
from bs4 import BeautifulSoup
from csv_uploader import *

datos_nuevos = []

def huevos_agrico(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    card_body = soup.find_all("div", class_="card-body")
    for card in card_body:
        if card.find("h2", class_="card-text") is None:
            continue
        name = card.find("h2", class_="card-text").text
        price = card.find("bdi").text
        print(f"Nombre: {name}")
        print(f"Precio: {price}")
        print("-"*30)
        unidades = name.split(" ")[-3]
        datos_nuevos.append([name, price, unidades, "Agricovial", "Agricovial"])

vial_blanco = "https://www.agricovial.cl/categoria-producto/huevo-blanco/"
vial_color = "https://www.agricovial.cl/categoria-producto/huevo-color/"

urls_agrico = [vial_blanco, vial_color]

for url in urls_agrico:
    huevos_agrico(url)

agregar_datos_csv("../huevos.csv", datos_nuevos)
