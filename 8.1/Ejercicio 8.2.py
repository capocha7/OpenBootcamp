
class Vehiculo:
    def Ruedas(x):
        return str(x)

    def Puertas(x):
        return str(x)

    def Ventanas(x):
        return str(x)

ruedas=Vehiculo.Ruedas(4)
puertas=Vehiculo.Puertas(5)
ventanas=Vehiculo.Ventanas(6)

f=open("8.1\\Prueba2.txt","w")
f.write("Cantidad de ruedas: "+ruedas+"\n")
f.write("Cantidad de puertas: "+puertas+"\n")
f.write("Cantidad de ventanas: "+ventanas)
f.close()
