def Calculadora(x,y):
    def Suma(x,y):
        print(f"La suma de {x} + {y} es: ",x+y)
    def Resta(x,y):
        print(f"La resta de {x} - {y} es: ",x-y)
    def Multiplicacion(x,y):
        print(f"La multiplicacion de {x} * {y} es: ",x*y)
    def Division(x,y):
        print(f"La division de {x} / {y} es:",x//y)

    (Suma(x,y))
    (Resta(x,y))
    (Multiplicacion(x,y))
    (Division(x,y))
    
a=int(input("El primer valor a calcular es:"))
b=int(input("El primer valor a calcular es:"))

Calculadora(a,b)






