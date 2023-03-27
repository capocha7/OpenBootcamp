"""
class Dino:
    encendido=False

    def enciende(self):
        pass

enciende()

class Dino:
    encendido=False

    def enciende(self):
        pass

d=Dino()
d.enciende()
print(d.encendido)
"""


class Dino:
    _encendido=True

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido


"""
d=Dino()
d.apaga()
print(d.isencendido())
print(d._encendido)


d1=Dino()
d1.apaga()
print(d1.isencendido())

d2=Dino()
d2.enciende()
print(d2.isencendido())
print(d1.isencendido())
"""
"""
class estatica:
    numero=1
    def incrementa():
        estatica.numero+=1

estatica.incrementa()
print(estatica.numero)

estatica.incrementa()
print(estatica.numero)

estatica.incrementa()
print(estatica.numero)
"""
"""
class juguete:
    _encendido=True

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido

class potato(juguete):
    _encendido=True

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido

    
class miclase(Dino):
    def oreja(self):
        return self._encendido

    def verescamas(self):
        pass

class Dino(potato,juguete):
    _encendido=True

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido

p=Dino()
p.enciende()
print(p.isencendido())
p.apaga()
print(p.isencendido())
#print(dir(p))
"""

"""
class Dino():

    color=None
    nobmre=None

    def __init__ (self,nombre):
        print("estoy en el constructor",nombre)
        self.color="verde"
        self.nombre=nombre

    def __del__ (self):
        print("estoy en el destructor",self.__class__)

class juguete:
    _encendido=True

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido


p=Dino("midinosaurito")


print(p.color)
print(p.nombre)

del(p)
print("a")
print("b")

print("a")
del(p)
print("b")
"""
"""
class juguete:
    _encendido=True

    def __init__ (self,x):      #def __init__ (self):
        print("estoy en la calse juguete, en su constructor",x)

    def enciende(self):
        self._encendido=True

    def apaga(self):
        self._encendido=False

    def isencendido(self):
        return self._encendido

class Dino(juguete):

    color=None
    nobmre=None

    def __init__ (self,nombre):       # def __init__ (self,nombre):
        super().__init__(nombre)             #juguete.__init__(self,nombre)
        print("estoy en el constructor",nombre)         
"""
"""
    def __del__ (self):
        print("estoy en el destructor",self.__class__)

p=Dino("midinosaurito")
"""

"""
def enciende():
    print("invocoa enciende")
    global _encendido
    _encendido=True

def apaga():
    global _encendido
    _encendido=False

def isEncendido():
    return _encendido

diccionario={
    "_encendido":False,"enciende":enciende,"apaga":apaga
}

diccionario["enciende"]()
print(diccionario["_encendido"])
"""

"""
def enciende(nombre):
    print("invocoa enciende",nombre)
    global _encendido
    _encendido=True

def apaga():
    global _encendido
    _encendido=False

def isEncendido():
    return _encendido

diccionario={
    "enciende":enciende
}

diccionario["enciende"]("hola")
#print(diccionario["enciende"])
"""
"""
from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def dihola(self):
        print("hola")

class perro(animal):
    def sonido(self):
        print("guau")

class gato(animal):
    def sonido(self):
        print("miau")

p= perro()
p.sonido()
p.dihola()

g=gato()
g.sonido()
g.dihola()
"""



"""
class ventanas:
    cantidad=5

    def cambiarcantidad(self,valor):
        self.cantidad=valor

class ruedas:
    cantidad=4

class motor:
    tipo="diesel"

class carroceria:
    Ventanas=ventanas()
    Ruedas=ruedas()
    
class coche():
    Motor=motor()
    Carroceria=carroceria()

c=coche()
print("motor es",c.Motor.tipo)
print("ventanas: ",c.Carroceria.Ventanas.cantidad)

c.Carroceria.Ventanas.cambiarcantidad(3)
print("ventanas: ",c.Carroceria.Ventanas.cantidad)
"""


class categoria:
    idcategoria=0
    nombre=""

class proveedores:
    idproveedor=0
    nombre=0

class productos:
    idproducto=0
    categoriaproducto=categoria()
    precio=0
    tamaño=0
    tipodeproducto=0
    cifproveedor=proveedores()

p=productos()

print(p.cifproveedor.nombre)
p.categoriaproducto.idcategoria













