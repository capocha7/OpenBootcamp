"""
def nombre():
    print("nombre")
    print("apellido")
    for i in range(1,6):
        print(i,")",i)

print("antes")
nombre()
print("despues")


def mifuncion(nombre):
    print("Hola,",nombre)

mifuncion("Victor")



def matematica(a,b):
    def suma(a,b):
        print(a+b)
    def resta(a,b):
        print(a-b)

    (suma(a,b))
    (resta(a,b))

matematica(5,3)


temperatura=12.0
def mifuncion(nombre):
    hoyhace=6.0
    print("temperatura:",temperatura)
    print("Hola,",nombre,"la temperatura es de ",hoyhace)

mifuncion("Victor")

hoyhace=12.0
def mifuncion(nombre):
    hoyhace=6.0
    print("temperatura:",hoyhace)
    print("Hola,",nombre,"la temperatura es de ",hoyhace)

print("temphoy",hoyhace)
mifuncion("Victor")
print("todavia temp",hoyhace)


hoyhace=12.0
def mifuncion(nombre):
    global hoyhace
    hoyhace=6.0
    hoyhace=6.0+1
    print("Hola,",nombre,"la temperatura es de ",hoyhace)

print(hoyhace)
mifuncion("Victor")
print("todavia temp",hoyhace)


def funcion(nombre="juan"):
    print("hola",nombre)

funcion()
funcion("Alan")


# CUANDO LE DECLARO VALOR A UN PARAMETRO DE LA FUNCION
# EN ESTE CASO SUMA, SI O SI SE DECLARA DE DERECHA A IZQUIERDA
# NO SE PUEDE DECLARAR "a" SIN HACERLO EN "b" y "c"
# COMO TAMBIEN NO SE PUEDE DECLARAR "b" sin "c"
def suma (a=1,b=2,c=3):
    print(a+b+c)

suma()
suma(2)
suma(2,4)
suma(1,1,1)

def suma (c=5,a=1,b=3):
    print("A es",a,"B es",b,"C es",c," ",a+b+c)

suma(5,1,1)

def suma (b=1,c=2,a=3):
    print("A es",a,"B es",b,"C es",c," ",a+b+c)

suma(10,5,1)
suma(10,5)
suma(10)
suma()


def suma (c,a,b=3):
    print("A es",a,"B es",b,"C es",c," ",a+b+c)

suma(a=5,c=2)



def suma(*args):
    resultado=0

    for arg in args:
        resultado+=arg

    print(resultado)

suma(1,2)
suma(10,5)
suma()

def suma(**kwargs):
    print(kwargs)

suma(vivienda="piso",coche="rojo")

def suma(**kwargs):
    #print(kwargs)
    for key, value in kwargs.items():
        print(key, "=", value)

suma(vivienda="piso",coche="rojo")

def suma(**kwargs):
    if kwargs["coche"] =="bonito":
        print("Tu coche es bonito")
    elif kwargs["coche"]=="feo":
        print("tu coche es feo")

suma(coche="feo")




def suma(**kwargs):
    if "coche" in kwargs and kwargs["coche"] =="bonito":
        print("Tu coche es bonito")
    else:
        print("no")
    print(kwargs)

suma(coche="auto")
suma(coche="bonito")
suma(coche="auto",bombo="bonito")



def suma(**kwargs):
    if "coche" not in kwargs:
        return
    if kwargs["coche"]=="bonito":
        print("Tu coche es bonito")
    
suma()
suma(auto="bonito")
suma(coche="bonito")


def suma(a,b):
    return a+b

resultado=suma(2,4)
print(resultado)


def operaciones(a,b):
    return a+b,a-b,a*b,a/b

resultado=operaciones(2,4)
print(resultado)
print(resultado[0])
print(resultado[2])



def operaciones(a,b):
    return a+b,a-b,a*b,a/b

suma,resta,multi=operaciones(2,4)
print(suma)
print(resta)
print(multi)



def operaciones(a,b):
    return a+b,a-b,a*b,a/b

suma,resta,multi,divi=operaciones(2,4)
print(suma)
print(resta)
print(multi)
print(divi)


def sumador(**kwargs):
    inicial=kwargs["inicial"]
    final=kwargs["final"]

    resultado=0
    for x in range(inicial, final+1):
        resultado+=x

    return resultado

print(sumador(inicial=15,final=30))



def sumador(**kwargs):
    inicial=kwargs["inicial"] if "inicial" in kwargs else 0
    final=kwargs["final"] if "final" in kwargs else inicial

    resultado=0
    for x in range(inicial, final+1):
        resultado+=x

    return resultado

print(sumador(inicial=15))
print(sumador(inicial=15,final=30))
print(sumador(final=30))
"""
"""
# FUNCIONES ANONIMAS

anonima= lambda:print("hola")
anonima()


anonima= lambda nombre,nombre2:print("hola",nombre,"adios",nombre2)
anonima("pepe","jose")


def sumatoria(x):
    return print(x+x)

sumatoria(2)

sumatoria=lambda x: x+x
print(sumatoria(2))
"""











