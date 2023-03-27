a=5
b=6
c=5
"""
print(a<b)
print(a>b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)
print(a==c)
print("")

print("COMPARA")

print(a>=c + a<b+a==b)
print(a>=c and a<b)
print(a>=c or a>b)
print((a>b or b>c) and (c>a))
print((a>b or b>c) and ((c>a) or (b<a)))

d=input()

if d<b:
    print("si,pero")
elif b>c:
    print("si")
else:
    print("no")

while False:
    print("hola")
"""
contador=1

"""
while contador<=10:
    print("contador vale", contador)
    contador+=1

print("Fin del while")

while contador<=10:
    print("contador vale", contador)
    
    if contador==5:
        print("Fuera del if")
        break
    contador+=1
print("Fin del while")


while contador<=10:
    print("contador vale", contador)
    
    if contador==5:
        print("Fuera del if")
        continue #BUCLE INFINITO
 #continue reinicia el while sin seguir hasta el final del bucle

    contador+=1
print("Fin del while")

while contador<=10:
    contador+=1
    print("contador vale", contador)
    
    if contador%2==0:
        print("contador vale par", contador)
        continue
    print("Impar, no pasa por el continue")
print("Fin del while")
"""

lista=[1,"2",3,"a",5]
"""
for valoractual in lista:
    print(valoractual,type(valoractual))

for numero in range(11):
    print(numero)

for numero in range(1,6):
    print(numero)

longitud=len(lista)
print("la lista tiene",longitud,"items")

for numero in range(longitud):
    print(lista[numero])

"""
lista=["hola","mensaje","adios"]
"""
for palabra in lista:
    print("Palabra actual:", palabra)
    if palabra=="mensaje":
        print("encontre mensaje")
        break

if "mensaje" in lista:
    print("encontre mensaje")
"""
"""
lista=[3,4,1,2,5]
print(lista)

listaordenada=sorted(lista)
print(listaordenada)

listaordenada=sorted(lista,reverse=True)
print(listaordenada)

lista=["A","a","b","Z","p"]
listaordenada=sorted(lista,reverse=True)
print(listaordenada)
listaordenada=sorted(lista)
print(listaordenada)
"""

valor=5
"""
if(valor==1):
    print("valor es1")
elif valor==2:
    print("valor es 2")
elif valor==3:
    print("valor es 3")
elif valor==4:
    print("valor es 4")
elif valor==5:
    print("valor es 5")
"""

valor=5
"""
match valor:
    case 1:
        print("valor es 1")
    case 2:
        print("valor es 2")
    case 3:
        print("valor es 3")
    case 4:
        print("valor es 4")
    case 5:
        print("valor es 5")
"""

lista=["hola","mensaje","adios"]
"""
for palabra in lista:
    if palabra=="mensaje":
        print("encuentro palabra mensaje")
        continue
else:
    print("no encuentro nada")

for palabra in lista:
    if palabra=="mensaje":
        print("mensaje encuentro ")
        break
else:
    print("encuentro nada")
"""

"""
for palabra in lista:
    print(palabra)
    if palabra=="mensaje":
        encontrado=True
        break
    else:
        encontrado=False

if encontrado:
    print("encontre la palabra")
else:
    print("no la encontre")
"""

for palabra in lista:
    pass
                        # PASS: para saltear un bucle, condicion, etc
                        # para completar luego
if 5<6:
    pass




