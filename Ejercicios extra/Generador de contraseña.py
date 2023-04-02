import random
import string

longitud_contraseña = 8
caracteres_contraseña = string.ascii_letters + string.digits
contraseña = ""

for i in range(longitud_contraseña):
    contraseña += random.choice(caracteres_contraseña)

print("Contraseña generada:", contraseña)