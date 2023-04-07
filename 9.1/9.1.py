"""
import _thread
import time

def horaActual(nombre_thread,tiempo_de_espera):
    count =0

    while count <5:

        time.sleep(tiempo_de_espera)
        count +=1
        print(f"Hilo: {nombre_thread} - {time.ctime(time.time())}")

_thread.start_new_thread(horaActual,("thread uno",1))
_thread.start_new_thread(horaActual,("thread dos",2))

print("he disparado ya los hilos")

while True:
    pass
"""

"""
import logging 


logging.basicConfig(level=logging.INFO)  # nos muestra el nivel y los mas criticos dsp de ese
logging.info("Arrancando programa")
logging.warning("Hace Calor")
logging.error("test")
logging.critical("adios")
"""
"""
import logging 


logging.basicConfig(level=logging.ERROR)
logging.info("Arrancando programa")
logging.warning("Hace Calor")
logging.error("test")
logging.critical("adios")
"""
"""
import logging 


logging.basicConfig(level=logging.DEBUG)
logging.info("Arrancando programa")
logging.warning("Hace Calor")
logging.error("test")
logging.critical("adios")
"""
"""
# La sintaxis basica
numeros=[1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    return True

filter(FUNCION,numeros)
"""
"""
numeros=[1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2==0:
        return True
    
    return False

resultado=filter(mifuncion,numeros)
print(list(resultado))
""""""
numeros=[1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if x % 2==0:
        return True
    
    return False

resultado=filter(lambda x:x%2==0,numeros) # PARES
print(list(resultado))
resultado=filter(lambda x:x%2,numeros) # IMPARES
print(list(resultado))
"""
"""
numeros=[1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if str(x).startswith("pep"):
        return True
    
    return False

resultado=filter(mifuncion,["pepe","pepito","juan"]) # PARES
print(list(resultado))
"""
"""
numeros=[1,2,3,4,5,6,7,8,9,10]

def mifuncion(x):
    if str(x).startswith("pep"):
        return True
    
    return False

resultado=filter(lambda x:str(x).startswith("pep"),["pepe","pepito","juan"]) # PARES
print(list(resultado))
"""

"""# FUNCION ""MAP"" FUNCIONA CON LISTAS"""
"""resultado = map(FUNCION,LISTA)"""

"""
def cuadrado(x):
    return x*x

resultado=map(cuadrado,[1,2,3,4,5,6,7,8,9,10])
print(list(resultado))
"""
"""
resultado=map(lambda x: x * x,[1,2,3,4,5,6,7,8,9,10])
print(list(resultado))
"""

""" # COMO USAR REDUCE
from functools import reduce

reduce(FUNCION,LISTA)
""""""
from functools import reduce

def multiplicacion(a,b):
    return a*b

res=reduce(multiplicacion,[1,2,3,4,5])
print(res)
"""
"""
from functools import reduce

def suma(a,b):
    return a+b

res=reduce(suma,[1,2,3,4,5])
print(res)
""""""
from functools import reduce

def suma(a,b):
    print(f"a={a}, b={b}")
    return a+b

res=reduce(suma,[1,2,3,4,5])
print(res)
"""
"""
cursos=["java","python","git"]
asistentes=[15,20,4]

demo=zip(cursos,asistentes)

print(list(demo))
""""""
cursos=["java","python"]
asistentes=[15,20,4]

demo=zip(cursos,asistentes)

print(list(demo))
""""""
cursos=["java","python","git","jose"]
asistentes=[15,20,4]

demo=zip(cursos,asistentes)

print(list(demo))
"""
"""
cursos=["java","python","git"]
asistentes=[15,20,4]

demo=zip(cursos,asistentes)

print(list(demo))
"""
"""
listaA=[1==1,2==2,3==4]

res=any(listaA)
print(res)

res=all(listaA)
print(res)
"""
"""
listaA=[1==1,2==2,3==3]

res=any(listaA)
print(res)

res=all(listaA)
print(res)
"""
"""# REDONDEAR, .5 PARA ARRIBA, .4 PARA ABAJO, FUNCION ROUND#"""
"""
a=5.5
b=5.4
c=5.6

print(round(a))
print(round(b))
print(round(c))
"""
"""# NUMERO MINIMO#"""
"""
print(min(2,3,4,5,9,3,1))
"""
"""# EXPONENCIAl #"""
"""
print(pow(2,4))
"""
"""
lista=["z","c","d","a"]
ordenada=sorted(lista)
print(ordenada)
"""
"""
lista=["z","c","d","a"]
ordenada=sorted(lista,reverse=True)
print(ordenada)
"""
"""
lista=["z","c","d","a"]
ordenada=sorted(lista,reverse=True, key=lambda x: str(x).startswith("a"))
print(ordenada)
"""
"""
a= input("¿Como te llamas?")
print(f"hola, {a}")
"""
"""
user= input("usuario")
passwd=   input("password")
print("usuario",user,"\npassword",passwd)
"""
"""
from getpass import getpass

user= input("Usuario: ")
passwd=  getpass("Password: ")
print("Usuario",user,"Password",passwd)
"""

secreto=50
valor=0

while valor != secreto:
    valor = int(input("introduce un numero: "))

    if valor>secreto:
        print("muy alto")
        continue

    if valor <secreto:
        print("muy bajo")
        continue

print("acertaste")

"""
vari=input()
if type(vari)==str:
    print("error")
"""











