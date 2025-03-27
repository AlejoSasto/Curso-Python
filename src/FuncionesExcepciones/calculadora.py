def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return x / y

def calculadora():
    while True:
        print("Seleccione una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Ingrese una opción (1, 2, 3, 4, 5): ")

        if opcion == "5":
            print("Saliendo...")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print("Resultado:", sumar(num1, num2))
            elif opcion == "2":
                print("Resultado:", restar(num1, num2))
            elif opcion == "3":
                print("Resultado:", multiplicar(num1, num2))
            elif opcion == "4":
                print("Resultado:", dividir(num1, num2))
        else:
            print("Opción inválida. Intente de nuevo.")

calculadora()
