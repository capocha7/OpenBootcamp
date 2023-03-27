
#Valores int,str
a=5
b="5"
c="c"

"""         
                                Listas[,]            Tuplas (,)       Conjuntos{,}         Diccionarios{:,:}         
"""
"""
print(type (b))
print(type (c))
print(id(a))
print(id(b))
print(id(c))
"""

#Vectores/listas y Tuplas: Vectores almacenan numeros,letras, utiliza corchetes y a diferencia de tuplas son inamobibles los valores, y utiliza parentesis
#Agregar y remover valores en el vector
vector=["a","4","b"]
tupla=("a","4","b")

"""
print(type(tupla))
print(type(vector))

vector.append("Y")
vector.append("Z")
vector.append(9)
vector.append(10)
vector.remove("4")
vector.remove("b")
tuple.append(9)  # LA TUPLA NO SE PUEDE AGERGAR VALORES, SON FIJOS
tupla.remove("4") # Tampoco se puede remover valores
print(vector)
"""

#Concatenar Vectores/Listas
abc=["a","b","c"]
xyz=["x","y","z"]

"""
print(abc.append(xyz))
print(abc)
print(abc.append(xyz[0]))
print(abc)
"""
udc=[1,2,3]
ccs=[4,5,6]

"""
print(udc+ccs)
udc.append(ccs)
print(udc)
"""
# Diccionario, almacena un valor dentro de un indice, 
# en este caso el indice es la izquierda, y te devuelve la derecha
diccionario={
    "clave":"valor","clave2":15,10:5,20:"res"
}
"""
print(diccionario)
print(diccionario["clave2"])
print(diccionario[10])
print(diccionario[20])
#print(diccionario["valor"]) #En diccionario, llamas el int o str de la izquierda y devuelve la derecha.
diccionario["clave2"]=100
print(diccionario["clave2"])
print(diccionario)
"""

dicc={"clave1":1,"clave2":2,"clave3":3,"clave4":4}

"""
print(dicc)
import pprint
pprint.pprint(dicc)

print(dicc.pop("clave1"))
print(dicc)
#print(dicc.del("clave2"))
print(dicc)
"""

lista=[1,2,3,1,2,3]
"""
print(lista)
"""
"""
# Conjunto no puede tener valores DUPLICADOS, 
    a diferencia de la lista, que si#"""

"""
conjunto={1,2,3,1,2,3,1,2,3}
print(conjunto)
conjunto.add(4)
conjunto.remove(2)
print(conjunto)
"""

a={0,2,4,6,8}
b={1,2,3,4,5}
c={"a","b","c","a","b","c"}
"""
print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(b ^ a)
print(c)
"""

numeros=5
cadenas="hola"
booleano=True
float=5.4
listas=["a","b","c"]
tuplas=("a","b","c")
Diccionarios={"a":1,"b":2,"c":3}
set={"a","b","c"} #conjuntos

"""
mitexto="hola, esto es un textO"
print(mitexto.capitalize())
print(mitexto.title())
print(mitexto.lower())
print(mitexto.upper())
print(mitexto.replace("e","o"))
print(mitexto.replace("o","e"))
print(mitexto.find("e"))
print(mitexto.find("to"))
print(mitexto.split())
print(mitexto.split(","))
print(mitexto.replace(","," "))
"""

listatexto=['hola,', 'esto', 'es', 'un', 'textO']
"""
print(listatexto)
print(" ".join(listatexto))
print("-_-".join(listatexto))
"""
"""
mivarcompleta=" ".join(listatexto)
print(mivarcompleta)

print(type(listatexto))
print(type(mivarcompleta))
print(mivarcompleta.isnumeric())
mivarcompleta="5"
print(mivarcompleta.isnumeric())
"""
"""
a=5
b=4
c=0
print("RESTA", a-b)  # RESTA
print("MULTIPLICACION",a*b)  # MULTIPLICACION
print("SUMA",a+b)  # SUMA
print("DIVISION",a/b)  # DIVISION
print("MODULO",a%b)  # MODULO
print("POTENCIA",a**b) # POTENCIA
c=a
a=b
b=c
print("INTERCAMBIO DE VARIABLES",a,b)  # INTERCAMBIO DE VALORES
a=5
b=4
a+=a
print("SUMA 'a' por si mismo",a)
a=5
a+=2
print("SUMA 'a' con dos",a)
a=5
a-=2
print("RESTA 'a' con dos",a)
a=5
a**=a
print("POTENCIA de 'a' por a",a)
"""
"""
comparacion: ==, !=, >, >=, <, <=
identidad: is, is not
membresia: in, not in
bit: &, | , ^, ~, >>, <<
"""

