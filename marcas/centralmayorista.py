import json
from csv_uploader import *

datos_nuevos = []

with open('central.json', 'r') as file:
    json_data = json.load(file)

productos = json_data[0]['data']['getProductsByCategory']['category']['products']

for producto in productos:
    nombre = producto['name']
    precio = producto['price']
    print(f"""Nombre: {nombre}
Precio: {precio}""")
    if any(char.isdigit() for char in nombre) and "un" in nombre.lower():
        unidades = int(''.join(filter(str.isdigit, nombre)))
        print(f"Unidades: {unidades}")
    else: 
        unidades = "N/A"
        print("Unidades: N/A")
    print("-"*50)
    datos_nuevos.append([nombre, precio, unidades, "Central Mayorista", "Central Mayorista"])

agregar_datos_csv("../huevos.csv", datos_nuevos)