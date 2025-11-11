def check_pais_repetido(dataset, pais):
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
