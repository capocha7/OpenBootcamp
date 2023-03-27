"""
class juguete:
    nombre=""
    def obtenernombre(self):
        return self.nombre
    
j1=juguete()
j1.nombre="potato"
print(j1.obtenernombre())
"""
"""
import operaciones as o

def main():
    res=o.suma(2,2)
    resResta=o.resta(5,3)
    print("Hola en main():",res,resResta) 


if __name__ =="__main__":
    main()
"""
"""
import operaciones as o

def main():
    #print(o.comomellamo)
    print(o.comomellamo())
    

if __name__ =="__main__":
    main()
"""
"""
import operaciones

def main():
    op=operaciones.operador()
    print(op.multiplicacion(4,2))
    

if __name__ =="__main__":
    main()
"""
"""
import operaciones

def main():
    print(operaciones.PI)
    
    
if __name__ =="__main__":
    main()
"""

"""
import sys
import pprint


def main():
    pprint.pprint(sys.path)
    
    
if __name__ =="__main__":
    main()
"""
"""
import sys
sys.path.append("/Users/Fede/desktop/Practica Python/mismodulos")

import pprint
pprint.pprint(sys.path)
import saluda

def main():
    
    saluda.saluda("victor")
    
if __name__ =="__main__":
    main()
"""
"""   
import operacioness.suma

def main():
    operacioness.suma.suma(2,2) # una suma es del fichero.py otra es de la funcion
    

if __name__ =="__main__":
    main()
"""
"""
import operacioness.suma

def main():
    mp=operacioness.suma.multiplicacion()
    print(mp.multiplica(5,5))

main()
"""
"""
import operacioness.suma

def main():
    mp=operacioness.suma.multiplicacion()
    print(mp.multiplica(5,5))

if __name__ =="__main__":
    main()
"""

"""

import operacioness.restador.resta as r
import operacioness.sumador.suma as s

#from operacioness import restador,sumador

def main():
    resta = r.resta(5,3)
    suma = s.suma(4,2)
    print()

if __name__ =="__main__":
    main()
"""
"""
from operacioness import *

def main():
    resta = restador.resta(5,3)
    suma = sumador.suma(4,2)
    print()

if __name__ =="__main__":
    main()
"""
"""
from operacioness import restador,sumador

def main():
    resta = restador.resta.resta(5,3)
    suma = sumador.resta.suma(4,2)


if __name__ =="__main__":
    main()

"""

"""
import operacioness.sumador

def main():
    print(dir(operacioness.sumador))


if __name__ =="__main__":
    main()
"""
"""

import operacioness.sumador.sumatorio as s
import pprint

def main():
    misuma=s.Sumatorio()
    pprint.pprint(dir(misuma))

if __name__ =="__main__":
    main()
"""

"""
import operacioness.sumador.sumatorio as s
import pprint

def main():
    mivar="a"
    pprint.pprint(dir(mivar))

if __name__ =="__main__":
    main()
"""

"""
import pprint

def main():
    pprint.pprint(dir(1))

if __name__ =="__main__":
    main()
"""

"""
import operacioness.sumador.sumatorio as s
import pprint
import math

def main():
    obj=s.Sumatorio()
    obj.suma(2,2)
    help(obj.suma)

if __name__ =="__main__":
    main()
"""

import operacioness.sumador.sumatorio as s
import pprint

def test():
    print("hola")

numero=4

obj=s.Sumatorio()
obj.suma(2,2)
pprint.pprint(globals())



















