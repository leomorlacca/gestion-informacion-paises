from validaciones import check_existencia, pedir_valor_entero

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
