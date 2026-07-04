hab_101_ocupada = False
hab_102_ocupada = False
hab_103_ocupada = False

hab_201_ocupada = False
hab_202_ocupada = False
hab_203_ocupada = False

hab_301_ocupada = False
hab_302_ocupada = False
hab_303_ocupada = False

hab_401_ocupada = False
hab_402_ocupada = False

hay_alguna = False

def calcular_ocupacion():
    ocupadas = 0
    total = 11
    
    if hab_101_ocupada == True: ocupadas +=1
    if hab_102_ocupada == True: ocupadas +=1
    if hab_103_ocupada == True: ocupadas +=1
    if hab_201_ocupada == True: ocupadas +=1
    if hab_202_ocupada == True: ocupadas +=1
    if hab_203_ocupada == True: ocupadas +=1
    if hab_301_ocupada == True: ocupadas +=1
    if hab_302_ocupada == True: ocupadas +=1
    if hab_303_ocupada == True: ocupadas +=1
    if hab_401_ocupada == True: ocupadas +=1
    if hab_402_ocupada == True: ocupadas +=1

    porcentaje = ocupadas/total * 100
    print("En total hay", ocupadas, "habitaciones ocupadas de 11")
    print("Porcentaje de ocupacion:", porcentaje)


def mostrar_disponibles(cantidad_huespedes):
    if cantidad_huespedes == 1:
        if not hab_101_ocupada:
            print("Habitación 101 (Simple) - disponible")
            hay_alguna = True
        if not hab_102_ocupada:
            print("Habitación 102 (Simple) - disponible")
            hay_alguna = True
        if not hab_103_ocupada:
            print("Habitación 103 (Simple) - disponible")
            hay_alguna = True
        
    elif cantidad_huespedes == 2:
        if not hab_201_ocupada:
            print("Habitación 201 (Doble) - disponible")
            hay_alguna = True
        if not hab_202_ocupada:
            print("Habitación 202 (Doble) - disponible")
            hay_alguna = True
        if not hab_203_ocupada:
            print("Habitación 203 (Doble) - disponible")
            hay_alguna = True

    elif cantidad_huespedes == 3:
        if not hab_301_ocupada:
            print("Habitación 301 (Triple) - disponible")
            hay_alguna = True
        if not hab_302_ocupada:
            print("Habitación 302 (Triple) - disponible")
            hay_alguna = True
        if not hab_303_ocupada:
            print("Habitación 303 (Triple) - disponible")
            hay_alguna = True
        
    elif cantidad_huespedes == 4:
        if not hab_401_ocupada:
            print("Habitación 401 (Cuádruple) - disponible")
            hay_alguna = True
        if not hab_402_ocupada:
            print("Habitación 402 (Cuádruple) - disponible")
            hay_alguna = True
       
    else:
        print("No hay habitaciones para esa cantidad de huéspedes")
        hay_alguna = False
    if not hay_alguna and (cantidad_huespedes == 1 or cantidad_huespedes == 2 or cantidad_huespedes == 3 or cantidad_huespedes == 4):
        print("No hay habitaciones disponibles de ese tipo en este momento")
    
    return hay_alguna

opcion = 0

while opcion != 4:
    print("=== MENÚ HOTEL ===")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Estadísticas de ocupación")
    print("4. Salir")
    
    try:
        opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: debe ingresar un número")
        opcion = 0  # para que no rompa el while ni confunda con una opción válida
        continue    # vuelve al inicio del while, salteando el resto
    
    if opcion == 1:
        try:
            cantidad_huespedes = int(input("Ingrese cantidad de huéspedes: "))
        except ValueError:
            print("Debe ingresar un número válido")
            continue
        mostrar_disponibles(cantidad_huespedes)
        if hay_alguna == False:
            continue
        else:
            # llamar a la función de check-in
    elif opcion == 2:
        # llamar a la función de check-out
        pass
    elif opcion == 3:
        calcular_ocupacion #función de estadísticas
        pass
    elif opcion == 4:
        print("Saliendo del sistema...")
    else:
        print("Opción inválida, intente de nuevo")
