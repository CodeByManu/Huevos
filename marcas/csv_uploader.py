import csv

def agregar_datos_csv(archivo_csv, datos_nuevos):
    with open(archivo_csv, 'r', newline='') as file:
        reader = csv.reader(file)
        cabeceras = next(reader)
        datos_existentes = list(reader)
    datos_completos = datos_existentes + datos_nuevos
    with open(archivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(cabeceras)
        writer.writerows(datos_completos)
