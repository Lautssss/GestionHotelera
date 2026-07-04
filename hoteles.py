from datetime import date

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
        # llamar a la función de check-in
        pass
    elif opcion == 2:
        # llamar a la función de check-out
        pass
    elif opcion == 3:
        # llamar a la función de estadísticas
        pass
    elif opcion == 4:
        print("Saliendo del sistema...")
    else:
        print("Opción inválida, intente de nuevo")
