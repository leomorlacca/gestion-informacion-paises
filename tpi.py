# Trabajo Practico Integrador de Programación - Leonardo Morlacca y Nahuel Montero
# Sistema de Gestión de Información sobre Paises

import csv
import os

DATASET = "dataset.csv"

def mostrar_menu(menu):
    print("\n")
    for opcion in menu:
        print(opcion)

def cargar_dataset(nombre_archivo=DATASET):
    # Carga el dataset de paises desde el archivo CSV
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
    # Guarda la informacion de paises en el archivo CSV
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

def check_pais_repetido(dataset, pais):
    # UNICIDAD: Verifica si un pais ya existe en el dataset (ignorando mayúsculas y espacios extra)
    pais_normalizado = " ".join(pais.lower().split())
    for pais in dataset:
        if " ".join(pais["NOMBRE"].lower().split()) == pais_normalizado:
            return True
    return False

def check_existencia(catalogo):
    if len(catalogo) == 0:
        print("No hay paises cargados.")
        return False
    return True

def pedir_valor_entero(tipo):
    # Pide al usuario una cantidad entera positiva y la devuelve
    while True:
        cantidad = input(f"{tipo} -> ")
        if cantidad.isdigit() and int(cantidad) > 0:
            return int(cantidad)
        print("Ingrese un número entero mayor a 0.")

def pedir_continente():
    continentes_validos = ["África", "América", "Asia", "Europa", "Oceanía"]

    while True:
        continente_input = input("Continente (África, América, Asia, Europa, Oceanía) -> ").strip().lower()

        for continente in continentes_validos:
            if continente_input == continente.lower():
                return continente

        print("Continente inválido. Ingrese el continente nuevamente.")


"""Funciones del menu principal"""

def agregar_paises(dataset):
    print("\n=== Ingreso de Paises ===\n")

    while True:
        cantidad_paises = input("¿Cuántos paises desea agregar? -> ")
        if cantidad_paises.isdigit() and int(cantidad_paises) > 0:
            cantidad_paises = int(cantidad_paises)
            break
        else:
            print("Ingrese un número entero mayor a 0.")

    for i in range(cantidad_paises):
        print(f"\nPaís {i+1} de {cantidad_paises}")

        # pedir pais con validaciones
        while True:
            pais = input("Nombre -> ").strip()
            if pais == "":
                print("El nombre no puede estar vacío.")
            elif check_pais_repetido(dataset, pais):
                print("Error: Ese país ya existe en la base de datos.")
            else:
                break

        poblacion = pedir_valor_entero("Población")
        superficie = pedir_valor_entero("Superficie (km²)")
        continente = pedir_continente()

        # agregar pais al dataset
        dataset.append({
            "NOMBRE": pais,
            "POBLACION": poblacion,
            "SUPERFICIE": superficie,
            "CONTINENTE": continente
        })

        print(f"'{pais}' añadido correctamente. ✅ ")

    print("\nCarga de Paises finalizada ✅")

def actualizar_pais(dataset):
    print("\n=== Actualizar País ===\n")

    if not check_existencia(dataset):
        return

    nombre = input("Ingrese el nombre del país a actualizar -> ").strip().lower()
    encontrado = False

    for pais in dataset:
        if pais["NOMBRE"].lower().strip() == nombre:
            encontrado = True
            print(f"\nPaís encontrado: {pais['NOMBRE']}")
            print(f"   Población actual: {pais['POBLACION']}")
            print(f"   Superficie actual: {pais['SUPERFICIE']} km²")

            nueva_superficie = pedir_valor_entero("Nueva Superficie (km²)")
            nueva_poblacion = pedir_valor_entero("Nueva Población")

            pais["SUPERFICIE"] = nueva_superficie
            pais["POBLACION"] = nueva_poblacion

            print(f"\n✅ Datos actualizados correctamente para '{pais['NOMBRE']}'")
            print(f"   Nueva Superficie: {pais['SUPERFICIE']} km²")
            print(f"   Nueva Población: {pais['POBLACION']}")
            break

    if not encontrado:
        print(f"No se encontró el país '{nombre}'.")


def buscar_pais_por_nombre(dataset):
    print("\n=== Búsqueda de País ===\n")

    if not check_existencia(dataset):
        return

    busqueda = input("Buscar -> ").strip().lower()
    resultados = []

    for pais in dataset:
        if busqueda in pais["NOMBRE"].lower():
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"No se encontro ningun pais para la busqueda '{busqueda}'.")
    else:
        print(f"\nSe encontró {len(resultados)} resultado(s):\n")
        for p in resultados:
            print(f"{p['NOMBRE']}")
            print(f"   -Población: {p['POBLACION']}")
            print(f"   -Superficie: {p['SUPERFICIE']} km²")
            print(f"   -Continente: {p['CONTINENTE']}\n")

def filtrar_paises(dataset):
    pass
def ordenar_paises(dataset):
    pass
def mostrar_estadisticas(dataset):
    pass


def main():
    dataset = cargar_dataset()
    eleccion = 0
    menu = [
        "[1] Agregar un País",
        "[2] Actualizar Poblacion/Superficie de un País",
        "[3] Buscar País por Nombre",
        "[4] Filtrar Paises",
        "[5] Ordenar Paises",
        "[6] Mostrar Estadísticas",
        "[7] Salir"
    ]

    while eleccion != 7:
        mostrar_menu(menu)
        entrada = input("-> ")

        if not entrada.isdigit():
            print("\nIngrese solo números para elegir una opción.")
            continue
        eleccion = int(entrada)

        match eleccion:
            case 1:
                agregar_paises(dataset)
                guardar_dataset(dataset)
            case 2:
                actualizar_pais(dataset)
                guardar_dataset(dataset)
            case 3:
                buscar_pais_por_nombre(dataset)
            case 4:
                filtrar_paises(dataset)
            case 5:
                ordenar_paises(dataset)
                guardar_dataset(dataset)
            case 6:
                mostrar_estadisticas(dataset)
main()