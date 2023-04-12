lista =[]

paises=input("Ingresar pais: ")

while paises!="0":
    lista.append(paises)
    paises=input("Ingresar pais: ")

lista=list(set(lista))
ordenada=sorted(lista)
separar=",".join(ordenada)

print(separar)

""" ## OTRA MANERA DE HACERLO
items = input("Introduce países separados por comas:\n")

paises = [pais for pais in items.split(",")]

print(",".join(sorted(list(set(paises)))))
"""































