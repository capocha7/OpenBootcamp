lista =[]

paises=input("Ingresar pais: ")

while paises!="0":
    lista.append(paises)
    paises=input("Ingresar pais: ")

lista=list(set(lista))
ordenada=sorted(lista)
separar=",".join(ordenada)

print(separar)



































