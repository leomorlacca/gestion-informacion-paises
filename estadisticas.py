from validaciones import check_existencia

def mostrar_estadisticas(dataset):
    print("\n=== Estadísticas del Dataset ===\n")

    if not check_existencia(dataset):
        return

    pais_mayor_pob = max(dataset, key=lambda p: p["POBLACION"])
    pais_menor_pob = min(dataset, key=lambda p: p["POBLACION"])

    print(f"País con mayor población: {pais_mayor_pob['NOMBRE']} - ({pais_mayor_pob['POBLACION']} hab.)")
    print(f"País con menor población: {pais_menor_pob['NOMBRE']} - ({pais_menor_pob['POBLACION']} hab.)")

    suma_poblacion = 0
    suma_superficie = 0
    for pais in dataset:
        suma_poblacion += pais["POBLACION"]
        suma_superficie += pais["SUPERFICIE"]

    promedio_poblacion = suma_poblacion / len(dataset)
    promedio_superficie = suma_superficie / len(dataset)

    print(f"\nPromedio de poblacion: {promedio_poblacion:,.0f} hab.")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")

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
