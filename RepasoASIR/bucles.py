no_salir=True

while no_salir: # salida = True
    opcion=0
    num1=0
    num2=0
    resultado=0
    print("Menu")
    print("1 - Sumar.")
    print("2 - Restar.")
    print("q - Salir.")
    opcion=input("Ingrese un número: ") # -> str
    if opcion=="1":
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese un número: "))
        resultado=num1+num2
        print(resultado)
        input("Pulse ENTER para continuar . . .")
    elif opcion=="2":
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese un número: "))
        print(num1-num2)
        input("Pulse ENTER para continuar . . .")
    elif opcion=="q":
        no_salir=False
        print("Gracias por usar el programa :D")
    else:
        print("Operacion no válida :(")
        # no_salir=False en caso de querer salir del programa.