es_primo=True
no_salir=True
cont=1
numero=int(input("Numero: "))

while es_primo and no_salir:
    if numero%cont==0:
        es_primo=False
        no_salir=False
    if cont>(numero//2)+1:
        es_primo=True
        no_salir=False
    cont+=1

if es_primo:
    print(f"El numero {numero} es primo.")
else:
    print(f"El numero {numero} no es primo.")