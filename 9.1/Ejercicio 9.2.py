from functools import reduce

def suma(a,b):
    return a+b

def TomarImpares(numeros):
    if (numeros in lista):
        return True
    else:
        return False

lista=[1,2,3,4,5]

print("Primer lista",lista)

for i in lista:
    if i%2==0:
        lista.remove(i)

print("Segunda lista, filtrando pares",lista)

filtro = filter(TomarImpares, lista)

print("Las letras filtradas son:")

for i in filtro:
    print(i)

reducir=reduce(suma,lista)
print("La suma de los elementos filtrados es: ",reducir)











