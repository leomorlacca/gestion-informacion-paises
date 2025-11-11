import csv
import os

DATASET = "dataset.csv"

def cargar_dataset(nombre_archivo=DATASET):
    dataset = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                dataset.append({
                    "NOMBRE": fila["NOMBRE"],
                    "POBLACION": int(fila["POBLACION"]),
                    "SUPERFICIE": int(fila["SUPERFICIE"]),
                    "CONTINENTE": fila["CONTINENTE"]
                })
        print("\n=== Paises cargados desde archivo CSV. ✅ ===")
    else:
        print("\n=== No se encontró el archivo CSV. Se iniciará un dataset vacío. ===")
    return dataset

def guardar_dataset(dataset, nombre_archivo=DATASET):
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["NOMBRE", "POBLACION", "SUPERFICIE", "CONTINENTE"])
        escritor.writeheader()
        for pais in dataset:
            escritor.writerow({
                "NOMBRE": pais["NOMBRE"],
                "POBLACION": pais["POBLACION"],
                "SUPERFICIE": pais["SUPERFICIE"],
                "CONTINENTE": pais["CONTINENTE"]
            })
    print("Informacion guardada correctamente en el archivo CSV. ✅")
