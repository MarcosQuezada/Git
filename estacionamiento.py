# SIMULADOR DE UN PARQUEADERO AUTOMATICO

limite = 50
vehiculos = []

def registrar_auto(matricula):
    if len(vehiculos) < limite:
        if matricula not in vehiculos:
            vehiculos.append(matricula)
            print("Vehículo", matricula, "ingresado.")
        else:
            print("El vehículo ya está dentro.")
    else:
        print("Parqueadero lleno.")

def retirar_auto(matricula):
    if matricula in vehiculos:
        vehiculos.remove(matricula)
        print("Vehículo", matricula, "salió.")
    else:
        print("Vehículo no encontrado.")

def consultar_espacios():
    libres = limite - len(vehiculos)
    print("Espacios disponibles:", libres)

while True:
    print(" ##### BIENVENIDO AL PARQUEADERO 1 UTC ##### ")
    print("\nOpciones:")
    print("1. Ingresar vehículo")
    print("2. Sacar vehículo")
    print("3. Mostrar espacios")
    print("4. Salir")

    seleccion = input("Elija opción: ")

    if seleccion == "1":
        matricula = input("Ingrese placa: ").upper()
        registrar_auto(matricula)

    elif seleccion == "2":
        matricula = input("Ingrese placa: ").upper()
        retirar_auto(matricula)

    elif seleccion == "3":
        consultar_espacios()

    elif seleccion == "4":
        print("Gracias por utilizar nuestros servicios")
        break

    else:
        print("Opción inválida.")