from validaciones import check_existencia

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
