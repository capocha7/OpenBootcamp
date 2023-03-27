class Vehiculo:
    color="verde"
    ruedas=4
    puertas=5

class Coche(Vehiculo):
    velocidad=200
    cilindrada=250
    print("El auto tiene una velocidad de",velocidad,"Km/h")
    print("El auto tiene una cilindrada de",cilindrada,"cc")
    print("El color del auto es: ",Vehiculo.color)
    print("El auto tiene",Vehiculo.ruedas,"ruedas")
    print("El auto tiene",Vehiculo.puertas,"puertas")

coche=Coche()

















