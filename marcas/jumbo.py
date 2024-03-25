import json
import re
from csv_uploader import *

datos_nuevos = []

with open('jumbo.json', 'r') as file:
    json_data = json.load(file)

productos = json_data['products']

for producto in productos:
    nombre = producto['productName']
    marca = producto['brand']
    precio = producto['items'][0]["sellers"][0]['commertialOffer']['PriceWithoutDiscount']
    cantidad = re.findall(r'\d+', nombre)
    print(f"""Nombre: {nombre}
Marca: {marca}
Precio: {precio}
Cantidad: {cantidad[0]}
{"-"*30}""")
    datos_nuevos.append([nombre, precio, cantidad[0], marca, "Jumbo"])

agregar_datos_csv("../huevos.csv", datos_nuevos)
    
