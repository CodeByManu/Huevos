import requests
from bs4 import BeautifulSoup
import json

def eggScripScraper(url):
    html_huevo = requests.get(url).text
    soup = BeautifulSoup(html_huevo, "html.parser")
    script = soup.find_all('script', type='application/ld+json')
    data = json.loads(script[1].string)
    precio = data['offers']['price']
    nombre = data['name']
    print(f"""
        Nombre: {nombre}
        Precio: {precio}
    """)

jumbo = 'https://www.jumbo.cl/lacteos/huevos'
lider = 'https://www.lider.cl/supermercado/category/Frescos_y_L%C3%A1cteos/Huevos_y_Mantequillas/Huevos'
unimarc = "https://www.unimarc.cl/category/lacteos-huevos-y-refrigerados/huevos"

#LIDER

# html_lider = requests.get(lider).text
# soup_lider = BeautifulSoup(html_lider, 'lxml')
# script_lider = soup_lider.find('script', type='application/ld+json')
# data_lider = json.loads(script_lider.string)

# for item in data_lider['itemListElement']:
#     print(f"Nombre del producto: {item['item']['name']}")
#     print(f"Precio del producto: {item['item']['offers']['price']}")
#     print(f"URL del producto: {item['item']['url']}")
#     print()

#JUMBO

# html_jumbo = requests.get(jumbo).text
# soup_jumbo = BeautifulSoup(html_jumbo, 'html.parser')
# script_jumbo = soup_jumbo.find_all('script', type='application/ld+json')
# huevos_jumbo = script_jumbo[1]
# data_jumbo = json.loads(huevos_jumbo.string)

# for item in data_jumbo['itemListElement']:
#     eggScripScraper(item['url'])

#UNIMARC

html_unimarc = requests.get(unimarc).text
soup_unimarc = BeautifulSoup(html_unimarc, "html.parser")
script_unimarc = soup_unimarc.find("script", type="application/json")
data_unimarc = json.loads(script_unimarc.string)

for item in data_unimarc["props"]["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["data"]["availableProducts"]:
    print(f"""
    nombre: {item["name"]}
    precio: {item["sellers"][0]["listPrice"]}
    unidades: {item["netContent"]}

""")