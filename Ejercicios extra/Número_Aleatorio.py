import random

numero_aleatorio=random.randint(1,100)
intentos=1

print("el numero aleatorio es",numero_aleatorio)
print("La máquina ha elegido un número del 1 al 100, adivinar cuál es, tienes 3 oportunidades. SUERTE!")

while intentos<=3:
    if intentos==1:
        respuesta=int(input("El primer número elegido es: "))
    elif intentos==2:  
        respuesta=int(input("El segundo número elegido es: "))
    elif intentos==3:
        respuesta=int(input("El tercer número elegido es: "))
    
    if respuesta > numero_aleatorio :
        print("El número aleatorio es mas chico que",respuesta)
    elif respuesta < numero_aleatorio:
        print("El número aleatorio es mas grande que",respuesta)
    else:
        print("Adivinaste!")
        break

    intentos+=1

if numero_aleatorio!=respuesta:
    print("Perdiste, el número aleatorio era",numero_aleatorio)

