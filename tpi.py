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

def filtrar_por_rango(dataset, campo, descripcion):
    print(f"\nIngrese el rango de {descripcion.lower()}:")
    valor_minimo = pedir_valor_entero("Mínimo")
    valor_maximo = pedir_valor_entero("Máximo")

    if valor_minimo > valor_maximo:
        print("Rango inválido (mínimo mayor que máximo).")
        return

    resultados = []
    for pais in dataset:
        if pais[campo] >= valor_minimo and pais[campo] <= valor_maximo:
            resultados.append(pais)

    if len(resultados) == 0:
        print(f"No se encontraron países con {descripcion.lower()} entre {valor_minimo} y {valor_maximo}.")
    else:
        print(f"\nPaíses filtrados con {descripcion.lower()} entre {valor_minimo} y {valor_maximo}:\n")
        for p in resultados:
            if campo == "POBLACION":
                print(f"{p['NOMBRE']}, {p['POBLACION']} hab.")
            else:
                print(f"{p['NOMBRE']}, {p['SUPERFICIE']} km²")


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
    if not check_existencia(dataset):
        return

    while True:
        print("\n=== Filtrar Países ===")
        print("[1] Por Continente")
        print("[2] Por Rango de Población")
        print("[3] Por Rango de Superficie")
        print("[4] Volver al menú principal")

        opcion = pedir_valor_entero("")

        if opcion == 1:
            continente = input("Ingrese el continente (África, América, Asia, Europa, Oceanía) -> ").strip().lower()
            resultados = [p for p in dataset if p["CONTINENTE"].lower() == continente]

            if len(resultados) == 0:
                print(f"No se encontraron países cargados para el continente '{continente}'.")
            else:
                print(f"\nPaíses en {resultados[0]['CONTINENTE']}:\n")
                for p in resultados:
                    print(f"{p['NOMBRE']} - Población: {p['POBLACION']} - Superficie: {p['SUPERFICIE']} km²")

        elif opcion == 2:
            filtrar_por_rango(dataset, "POBLACION", "Población")

        elif opcion == 3:
            filtrar_por_rango(dataset, "SUPERFICIE", "Superficie")

        elif opcion == 4:
            break
        else:
            print("Opcion inválida. Ingrese una opcion del 1 al 4.")

def ordenar_paises(dataset):
    if not check_existencia(dataset):
        return

    print("\n=== Ordenar Países ===")
    print("[1] Por Nombre")
    print("[2] Por Población")
    print("[3] Por Superficie")
    print("[4] Volver al menu principal")

    opcion = pedir_valor_entero("")

    if opcion == 1:
        paises_ordenados = sorted(dataset, key=lambda p: p["NOMBRE"])
        criterio = "nombre"
    elif opcion == 2:
        paises_ordenados = sorted(dataset, key=lambda p: p["POBLACION"])
        criterio = "población"
    elif opcion == 3:
        paises_ordenados = sorted(dataset, key=lambda p: p["SUPERFICIE"])
        criterio = "superficie"
    elif opcion == 4:
        return
    else:
        print("Opción inválida.")
        return

    print(f"\nPaíses ordenados por {criterio} (de menor a mayor):\n")
    for p in paises_ordenados:
        print(f"{p['NOMBRE']} - {p['POBLACION']} hab. - {p['SUPERFICIE']} km² - {p['CONTINENTE']}")

def mostrar_estadisticas(dataset):
    print("\n=== Estadísticas del Dataset ===\n")

    if not check_existencia(dataset):
        return

    # pais con mayor y menor poblacion
    pais_mayor_pob = max(dataset, key=lambda p: p["POBLACION"])
    pais_menor_pob = min(dataset, key=lambda p: p["POBLACION"])

    print(f"País con mayor población: {pais_mayor_pob['NOMBRE']} - ({pais_mayor_pob['POBLACION']} hab.)")
    print(f"País con menor población: {pais_menor_pob['NOMBRE']} - ({pais_menor_pob['POBLACION']} hab.)")

    # promedios
    suma_poblacion = 0
    suma_superficie = 0
    for pais in dataset:
        suma_poblacion += pais["POBLACION"]
        suma_superficie += pais["SUPERFICIE"]

    promedio_poblacion = suma_poblacion / len(dataset)
    promedio_superficie = suma_superficie / len(dataset)

    print(f"\nPromedio de poblacion: {promedio_poblacion:,.0f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")

    # cant de paises por continente
    continentes = {}
    for pais in dataset:
        continente = pais["CONTINENTE"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nCantidad de países por continente:")
    for cont, cantidad in continentes.items():
        print(f"   - {cont}: {cantidad}")


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
            case 6:
                mostrar_estadisticas(dataset)
main()