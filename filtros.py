from validaciones import check_existencia, pedir_valor_entero
from validaciones import pedir_continente

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
