import requests
from bs4 import BeautifulSoup
import json
import re
from csv_uploader import *

datos_nuevos = []

coliumo = "https://huevoscoliumo.cl/tienda/?products-per-page=all"

html_coliumo = requests.get(coliumo).text
soup_coliumo = BeautifulSoup(html_coliumo, "html.parser")
script_coliumo = soup_coliumo.find_all("script", type="text/javascript")

script = script_coliumo[3].string
match = re.search(r'tvc_pgc=(\{.*?\});', script)
if match:
    tvc_pgc_str = match.group(1)
    tvc_pgc = json.loads(tvc_pgc_str)
    for url, data in tvc_pgc.items():
        unidades = re.findall(r'\d+', data['tvc_n'])
        print(f"Nombre: {data['tvc_n']}")
        print(f"Precio: {data['tvc_p']}")
        print(f"Unidades: {unidades[0]}")
        print("-"*30)
        datos_nuevos.append([data['tvc_n'], data['tvc_p'], unidades[0], "Coliumo", "Coliumo"])


agregar_datos_csv("../huevos.csv", datos_nuevos)