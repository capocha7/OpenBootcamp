lista=[]
contador=1
while contador<=100:
    lista.append(contador)
    contador+=1

print("ordenado de mayor a menor",sorted(lista,reverse=True))
