numero = 10
texto ="quijote"
otromas=1.2

# FORMA ANTIGUA
# %d significa digit, %s significa string, %f significa float
"""
print("el numero es %d y el texto es %s y tiene %f" % (numero,texto,otromas))

print("Valor flotante: %f" % otromas)
print("Valor flotante: %.2f" % otromas)
"""

# FORMA SIGUIENTE A LA ANTIGUA
"""
print("el numero es {} y el texto es {} y tiene {}"
      .format(numero,texto,otromas))

print("el numero es {} y el texto es {} y tiene {}"
      .format(otromas,numero,texto))
"""
"""
print("el numero es {0} y el texto es {1} y tiene {2}"
      .format(numero,texto,otromas))

print("el numero es {1} y el texto es {2} y tiene {0}"
      .format(numero,texto,otromas))

print("el numero es {1} y el texto es {2} y tiene {0}"
      .format(otromas,numero,texto))

print("el numero es {n1} y el texto es {texto} y tiene {otro}"
      .format(n1=numero,texto=texto,otro=otromas))
"""
"""
print(f"el numero es {numero} y el texto es {texto} y tiene {otromas}")
print(f"el numero es {numero} y el texto es {texto.upper()} y tiene {otromas}")

txt=f"el numero es {numero} y el texto es {texto.upper()} y tiene {otromas}"
print(txt)


def suma(a,b):
    return a+b

print(f"el numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}")


txt=f"el numero es {suma(numero,numero)} y el texto es {texto.upper()} y tiene {otromas}"
print(txt)
"""
"""
num=511
print(type(num))
print(type(str(num)))
numtxt=str(num)
print(type(num),type(numtxt),num,numtxt)

print(repr(num))
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

j1=Juguete("Potato",10.5)
print((j1))
print(str(j1))
print(repr(j1))
"""

"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def __str__(self): # Para lograr un valor humano, sin el nombre tecnico
        return f"mi nombre es {self.nombre} y mi precio {self.precio}"
     
j1=Juguete("Potato",10.5)
print((j1))
print(str(j1))
print(repr(j1))

demo=j1
print(demo)
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def __str__(self): # Para lograr un valor humano, sin el nombre tecnico
        return f"mi nombre es {self.nombre} y mi precio {self.precio}"
     
j1=Juguete("Potato",10.5)
print((j1))
print(str(j1))
print(repr(j1))

demo=str(j1)
print(type(demo))
print(demo)
"""

"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def __str__(self): # Para lograr un valor humano, sin el nombre tecnico
        return f"mi nombre es {self.nombre} y mi precio {self.precio}"
     
    def __repr__(self):
        return f"Potat0 ({self.nombre},{self.precio})"


j1=Juguete("Potato",10.5)
print(repr(j1))
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
   
    def __repr__(self): # Salidas Tecnicas
        return f"Potat0 ({self.nombre},{self.precio})"

j1=Juguete("Potato",10.5)
print(repr(j1))
print(str(j1))
print(j1)
"""
"""

class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
   
    def __str__(self): # Para lograr un valor humano, sin el nombre tecnico
        return f"mi nombre es {self.nombre} y mi precio {self.precio}"
   
j1=Juguete("Potato",10.5)
print(repr(j1))
print(str(j1))
print(j1)
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def __str__(self): # Para lograr un valor humano, sin el nombre tecnico
        return f"mi nombre es {self.nombre} y mi precio {self.precio}"
     
    def __repr__(self):
        return f"Potat0 ({self.nombre},{self.precio})"


j1=Juguete("Potato",10.5)
j2= Juguete("dino",4.5)


print(Juguete("Lui",33))
print(j1)
print(j2)

representaciontextual=str(j1)
print(representaciontextual)
"""
"""
import pprint
pprint.pprint(dir(""))
"""
cadena="en un lugar de la manchA"
numero= "5"
num=5
caracter="a5"
"""
print(cadena.capitalize())
print(cadena.title())
print(cadena.count("a"))
print(cadena.lower())
print(cadena.upper())
print(cadena.lower().count("a"))
print(cadena.lower(),"hola".upper())
print(cadena.lower(),cadena.upper())
"""
"""
print(cadena.isdigit())
print(numero.isdigit())
#print(num.isdigit())  NO LO TOMA XQE ES INT y NO STRING
print(numero.isalnum())
print(numero.isalpha())
print(caracter.isalpha())
print(caracter.isalnum())
print(cadena.isalpha())
"""
cadena="       en un lugar de la manchA         "
numero= "5"
num=5
caracter="a5"
 
"""
print(cadena)
print(cadena.strip())
print(cadena.lstrip())
print(cadena.rstrip())
"""
"""
cadena="       en un lugar de la manchA         "
print(cadena.split())
print(cadena.split("un"))
"""
"""
cadena="en un lugar de la manchA"
print(cadena.startswith("en"))
print(cadena.startswith("mancha"))
print(cadena.lower().startswith("mancha"))
print(cadena.lower().endswith("mancha"))
"""

# r : lectura
# a : append - agregar
# w : escritura
# x : create

# t : texto
# b : binary

"""
f = open("C:\\Users\\Fede\\Desktop\\Practica python\\Ejercicios extra\\Practica.py")
datos= f.read()
f.close()
print(datos)
"""

"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.read()
f.close()
print(datos)
"""

"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.read(16)
f.close()
print(datos)
"""

"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.read(32)
f.close()
print(datos)
"""

"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.readline()
datos= f.readline()
datos= f.readline()
f.close()
print(datos)


f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.readline()
f.close()
print(datos)

f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.readline()
datos= f.readline()
f.close()
print(datos)
"""
"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")

datos=None
while datos !="":
    datos=f.readline()
    print(datos)


f.close()
print(datos)
"""
"""
f = open("c:\\Users\\Fede\\Desktop\\musik.txt")
datos= f.readlines()
f.close()
print(datos)
"""
"""
def main():
    usuarios = listarUsuarios()
    #print(usuarios)

def listarUsuarios():
    f=open("c:\\Users\\Fede\\Desktop\\musik.txt","r")
    datos = f.readlines()
    f.close()

    resultado=[]
    for linea in datos:
        if linea [0]=="\n":
            continue

        partes=linea.split("-")
        print(linea)
        print(partes)
        print(partes[0])


if __name__ =="__main__":
    main()
"""
"""
def main():
    usuarios = listarUsuarios()


def listarUsuarios():
    f=open("c:\\Users\\Fede\\Desktop\\musik.txt","r")
    datos = f.readlines()
    f.close()

    resultado=[]
    for linea in datos:
        if linea [0]=="\n":
            continue
        
        partes=linea.split("-")
        resultado.append(partes[0])
        print(partes)

if __name__ =="__main__":
    main()
"""
"""
def main():
    usuarios = listarUsuarios()
    for usuario in usuarios:
        print(f"usuario: {usuario}")

def listarUsuarios():
    f=open("c:\\Users\\Fede\\Desktop\\musik.txt","r")
    datos = f.readlines()
    f.close()

    resultado=[]
    for linea in datos:
        if linea [0]=="\n":
            continue
        
        partes=linea.split("-")
        resultado.append(partes[0])
    return resultado

if __name__ =="__main__":
    main()
"""
"""
f = open("8.1\\mifichero.txt","w")  #Escribe reemplazando los datos adentro
f.write("datos\n")
f.write("datos2\n")
f.close()
"""
"""
f = open("8.1\\mifichero.txt","a")  #Escribe agregando al texto existente
f.write("datos\n")
f.write("datos2\n")
f.close()
"""
"""
f = open("8.1\\mifichero.txt","w")  

lista= [
    "una linea\n",
    "dos lineas\n",
    "tres lineas\n"
]

f.writelines(lista)
f.close()
"""

"""
def escribe(fichero,datos):
    f = open(fichero,"w")  

    for linea in datos:
        f.write(linea)

    f.close()

lista= [
    "una linea\n",
    "dos lineas\n",
    "tres lineas\n"
]

escribe("8.1\\mifichero.txt",lista)
"""
"""
def escribe(fichero,datos):
    f = open(fichero,"w")  

    for linea in datos:


        f.write(linea)

    f.close()

lista= [
    "una linea\n",
    "dos lineas\n",
    "tres lineas"
]

escribe("8.1\\mifichero.txt",lista)
"""
"""
def escribe(fichero,datos):
    f = open(fichero,"w")  

    for linea in datos:
        if not linea.endswith("\n"):
            linea=linea+"\n"

        f.write(linea)

    f.close()

lista= [
    "una linea",
    "dos lineas",
    "tres lineas"
]

escribe("8.1\\mifichero.txt",lista)
"""
"""
def escribe(fichero,datos):
    f = open(fichero,"w")  

    for linea in datos:
        if not linea.endswith("\n"):
            print("Linea sin \\n ",linea)
            linea=linea+"\n"

        f.write(linea)

    f.close()

lista= [
    "una linea",
    "dos lineas\n",
    "tres lineas"
]

escribe("8.1\\mifichero.txt",lista)
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre
    
j1=Juguete("Potato",10.5)
print(type(j1))
print(j1.getNombre())
"""
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre
    
j1=Juguete("Potato",10.5)
print(j1.getNombre())
"""
"""
import pickle

class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre
    
j1=Juguete("Potato",10.5)
f=open("8.1\\datos.bin","wb")
pickle.dump(j1,f)
f.close()
"""

import pickle
"""
class Juguete:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def getNombre(self):
        return self.nombre
    

f=open("8.1\\datos.bin","rb")
potato=pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(),"precio",potato.precio)
"""
# GUARDAR JUEGO
"""
class Estado:
    players=Players()
    status=Status()
    life_remaining=12
    armor=False

f=open("gamestatuis.dat","wb")
e=Estado()
pickle.dump(f,e)
f.close()
"""
# CARGAR JUEGO
"""
class Estado:
    players=Players()
    status=Status()
    life_remaining=12
    armor=False

f=open("gamestatuis.dat","wb")
e=pickle.load(f)
f.close()
"""








