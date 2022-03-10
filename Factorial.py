from functools import reduce    
lista = []
limite = int(input("ingrese el numero limite: "))
for n in range(limite):
    lista.append(n)

def factorial(numero):
    if numero < 0: 
        pass

    else: 
        factorial = 1
        while(numero > 1): 
            factorial *= numero
            numero -= 1
        return 1/factorial

lista = list(map(factorial,lista))

def suma(a,b):
    return a+b
resultado = reduce(suma,lista)
print(resultado)


