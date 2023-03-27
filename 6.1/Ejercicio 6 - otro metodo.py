class Color:
    coloracion="verde"

class Ruedas:
    cantidad=4

class Puertas:
    cantidad=5

class Vehiculo:
    color=Color()
    ruedas=Ruedas()
    puertas=Puertas()

#vehiculo=Vehiculo()
#print("El color del auto es: ",vehiculo.color.coloracion)
#print("El auto tiene",vehiculo.ruedas.cantidad,"ruedas")
#print("El auto tiene",vehiculo.puertas.cantidad,"puertas")

class Coche(Vehiculo):
    velocidad=200
    cilindrada=250
    vehiculo=Vehiculo()

coche=Coche()
print("El auto tiene una velocidad de",coche.velocidad,"Km/h")
print("El auto tiene una cilindrada de",coche.cilindrada,"cc")
print("El color del auto es: ",coche.color.coloracion)
print("El auto tiene",coche.ruedas.cantidad,"ruedas")
print("El auto tiene",coche.puertas.cantidad,"puertas")




"""
coche=Coche()
print("El auto tiene una velocidad de",coche.velocidad,"Km/h")
print("El auto tiene una cilindrada de",coche.cilindrada,"cc")

print("El color del auto es: ",coche.vehiculo.color.coloracion)
print("El auto tiene",coche.vehiculo.ruedas.cantidad,"ruedas")
print("El auto tiene",coche.vehiculo.puertas.cantidad,"puertas")
"""