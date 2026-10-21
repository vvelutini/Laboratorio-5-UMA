"""
EJERCICIO 05: Refactorización de un programa de Cajero Automático

Se tiene un programa que simula un cajero automático. Este es funcional, pero está mal estructurado. 
Debes dividir el código proporcionado en una estructura modular de tres archivos:

    1. auth.py (Módulo de Autenticación):

        - Debe contener una función, por ejemplo, verificar_pin(pin_correcto) que gestione el ciclo de los intentos y 
        retorne True si el usuario acierta o False si agota los intentos.

    2. operaciones.py (Módulo de Lógica Bancaria):

        - Debe contener funciones puras o con parámetros claros para las acciones del cajero, por ejemplo:
            consultar_saldo(saldo)
            depositar(saldo, monto) (retorna el nuevo saldo)
            retirar(saldo, monto) (retorna el nuevo saldo si es posible, o muestra error)

    3. main.py (Script Principal):

        - Debe importar auth y operaciones.
        - Debe inicializar las variables principales (saldo = 1000.0, pin_correcto = "1234").
        - Debe coordinar el flujo del programa principal llamando a las funciones de los módulos importados.

"""

# La solución (código dividido en módulos) está en la carpeta cajero/:
#   cajero/auth.py, cajero/operaciones.py, cajero/main.py
# Se ejecuta con:  python3 cajero/main.py

# Código original (sin modificar, solo como referencia)

saldo = 1000.0
pin_correcto = "1234"

print("CAJERO AUTOMÁTICO")
intentos = 3
acceso = False

while intentos > 0:
    pin = input("Ingrese su PIN de 4 dígitos: ")
    if pin == pin_correcto:
        acceso = True
        break
    else:
        intentos -= 1
        print(f"PIN incorrecto. Te quedan {intentos} intentos.")

if acceso:
    while True:
        print("\n1. Consultar saldo")
        print("\n2. Depositar dinero")
        print("\n3. Retirar dinero")
        print("\n4. Salir")
        
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                print(f"Su saldo actual es: ${saldo}")
            case "2":
                monto = float(input("Ingrese monto a depositar: "))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
                else:
                    print("Monto inválido.")
            case "3":
                monto = float(input("Ingrese monto a retirar: "))
                if 0 < monto <= saldo:
                    saldo -= monto
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                elif monto > saldo:
                    print("Fondos insuficientes")
                else:
                    print("Monto inválido")
            case "4":
                print("Gracias por usar el cajero.")
                break
            case _:
                print("Opción inválida.")
else:
    print("Tarjeta bloqueada por seguridad.")