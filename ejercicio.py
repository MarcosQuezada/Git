#simulador de cajero automatico
saldo = 0.0
while True:
    print("Bienvenido al simulador de cajero automatico")
    print("Seleccione una opcion:")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    opcion = int(input("Ingrese el numero correspondiente a la opcion que desea realizar: "))
    match opcion:
        case 1:
            print(f"Su saldo actual es: ${saldo:.2f}")
        case 2:
            deposito = float(input("Ingrese el monto a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Deposito exitoso. Su nuevo saldo es: ${saldo:.2f}")
            else:
                 print("el valor debe de ser mayor a 0")    
        case 3:
            retiro = float(input("Ingrese el monto a retirar: "))
            if retiro <= 0:
                print("el valor debe de ser mayor a 0")
            elif retiro > saldo:
                print("Saldo insuficiente para realizar el retiro.")
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
        case 4:
            print("Gracias por usar el simulador de cajero automatico. Hasta luego!")
            break
        case _:
            print("Opcion no valida. Por favor, seleccione una opcion del 1 al 4.")