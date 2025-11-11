# Trabajo Practico Integrador de Programación - Leonardo Morlacca y Nahuel Montero
# Sistema de Gestión de Información sobre Paises

from datos import cargar_dataset, guardar_dataset
from filtros import filtrar_paises
from ordenamiento import ordenar_paises
from estadisticas import mostrar_estadisticas
from busquedas import buscar_pais_por_nombre
from validaciones import pedir_valor_entero, check_pais_repetido, pedir_continente, check_existencia

def mostrar_menu(menu):
    print("\n")
    for opcion in menu:
        print(opcion)

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

            nueva_superficie = pedir_valor_entero("\nNueva Superficie (km²)")
            nueva_poblacion = pedir_valor_entero("Nueva Población")

            pais["SUPERFICIE"] = nueva_superficie
            pais["POBLACION"] = nueva_poblacion

            print(f"\nDatos actualizados correctamente para '{pais['NOMBRE']}' ✅")
            break

    if not encontrado:
        print(f"No se encontró el país '{nombre}'.")

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
    print("\nPrograma finalizado.")

if __name__ == "__main__":
    main()
