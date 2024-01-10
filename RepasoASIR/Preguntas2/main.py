# todos los numeros primos entre 1 y 100
def es_primo(numero):
    divisores=[]
    for n in range(2,numero):
        if numero%n==0:
            divisores.append(n)
    if not divisores:
        return numero # Si es primo


def main():
    primos=[]
    for n in range(1,100):
        if es_primo(n)!=None:
            primos.append(es_primo(n))
    print(primos)

if __name__=='__main__':
    main()