numero=0
numero=int(input("Ingrese un numero: "))
if numero>100:
    print("El numero es muy grande.")
elif numero>=50 and numero<=100:
    print("El numero es mediano.")
elif numero>=20 and numero<50:
    print("El numero es pequeño.")
else:
    print("El numero es muy pequeño.")