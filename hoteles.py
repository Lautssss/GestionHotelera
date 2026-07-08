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


def calcular_ocupacion():
    ocupadas = 0
    total = 11

    if hab_101_ocupada: ocupadas += 1
    if hab_102_ocupada: ocupadas += 1
    if hab_103_ocupada: ocupadas += 1
    if hab_201_ocupada: ocupadas += 1
    if hab_202_ocupada: ocupadas += 1
    if hab_203_ocupada: ocupadas += 1
    if hab_301_ocupada: ocupadas += 1
    if hab_302_ocupada: ocupadas += 1
    if hab_303_ocupada: ocupadas += 1
    if hab_401_ocupada: ocupadas += 1
    if hab_402_ocupada: ocupadas += 1

    porcentaje = ocupadas / total * 100

    print("En total hay", ocupadas, "habitaciones ocupadas de 11")
    print("Porcentaje de ocupación:", porcentaje)


def mostrar_disponibles(cantidad_huespedes):
    hay_alguna = False

    if cantidad_huespedes == 1:
        if not hab_101_ocupada:
            print("101 disponible")
            hay_alguna = True
        if not hab_102_ocupada:
            print("102 disponible")
            hay_alguna = True
        if not hab_103_ocupada:
            print("103 disponible")
            hay_alguna = True

    elif cantidad_huespedes == 2:
        if not hab_201_ocupada:
            print("201 disponible")
            hay_alguna = True
        if not hab_202_ocupada:
            print("202 disponible")
            hay_alguna = True
        if not hab_203_ocupada:
            print("203 disponible")
            hay_alguna = True

    elif cantidad_huespedes == 3:
        if not hab_301_ocupada:
            print("301 disponible")
            hay_alguna = True
        if not hab_302_ocupada:
            print("302 disponible")
            hay_alguna = True
        if not hab_303_ocupada:
            print("303 disponible")
            hay_alguna = True

    elif cantidad_huespedes == 4:
        if not hab_401_ocupada:
            print("401 disponible")
            hay_alguna = True
        if not hab_402_ocupada:
            print("402 disponible")
            hay_alguna = True

    else:
        print("No hay habitaciones para esa cantidad")
        return False

    if not hay_alguna:
        print("No hay habitaciones disponibles de ese tipo")

    return hay_alguna


def hacer_checkin(numero_habitacion):
    global hab_101_ocupada, hab_102_ocupada, hab_103_ocupada
    global hab_201_ocupada, hab_202_ocupada, hab_203_ocupada
    global hab_301_ocupada, hab_302_ocupada, hab_303_ocupada
    global hab_401_ocupada, hab_402_ocupada

    if numero_habitacion == 101:
        if not hab_101_ocupada:
            hab_101_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 102:
        if not hab_102_ocupada:
            hab_102_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 103:
        if not hab_103_ocupada:
            hab_103_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 201:
        if not hab_201_ocupada:
            hab_201_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 202:
        if not hab_202_ocupada:
            hab_202_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 203:
        if not hab_203_ocupada:
            hab_203_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 301:
        if not hab_301_ocupada:
            hab_301_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 302:
        if not hab_302_ocupada:
            hab_302_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 303:
        if not hab_303_ocupada:
            hab_303_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 401:
        if not hab_401_ocupada:
            hab_401_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    elif numero_habitacion == 402:
        if not hab_402_ocupada:
            hab_402_ocupada = True
            print("Check-in realizado, muchas gracias.")
        else:
            print("Esta habitación ya está ocupada")

    else:
        print("La habitación seleccionada no existe")

def hacer_checkout(numero_habitacion):
    global hab_101_ocupada, hab_102_ocupada, hab_103_ocupada
    global hab_201_ocupada, hab_202_ocupada, hab_203_ocupada
    global hab_301_ocupada, hab_302_ocupada, hab_303_ocupada
    global hab_401_ocupada, hab_402_ocupada

    if numero_habitacion == 101:
        if hab_101_ocupada:
            hab_101_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 102:
        if hab_102_ocupada:
            hab_102_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 103:
        if hab_103_ocupada:
            hab_103_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 201:
        if hab_201_ocupada:
            hab_201_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 202:
        if hab_202_ocupada:
            hab_202_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 203:
        if hab_203_ocupada:
            hab_203_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 301:
        if hab_301_ocupada:
            hab_301_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 302:
        if hab_302_ocupada:
            hab_302_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 303:
        if hab_303_ocupada:
            hab_303_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 401:
        if hab_401_ocupada:
            hab_401_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    elif numero_habitacion == 402:
        if hab_402_ocupada:
            hab_402_ocupada = False
            print("Check-out realizado, muchas gracias.")
        else:
            print("Esta habutación no fue ocupada.")

    else:
        print("La habitación seleccionada no existe")


opcion = 0

while opcion != 4:
    print("\n=== MENÚ HOTEL ===")
    print("1. Check-in")
    print("2. Check-out")
    print("3. Estadísticas")
    print("4. Salir")

    try:
        opcion = int(input("Ingrese opción: "))
    except:
        print("Error")
        continue

    if opcion == 1:
        try:
            cant = int(input("Cantidad huéspedes: "))
        except:
            print("Error")
            continue

        if mostrar_disponibles(cant):
            try:
                hab = int(input("Número habitación: "))
                hacer_checkin(hab)
            except:
                print("Error número habitación")

    elif opcion == 2:
        try:
            hab = int(input("Número de habitación: "))
            hacer_checkout(hab)
        except:
            print("Error")

    elif opcion == 3:
        calcular_ocupacion()

    elif opcion == 4:
        print("Saliendo...")

    else:
        print("Opción inválida")