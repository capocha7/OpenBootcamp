import time

hora=time.strftime("%H")
cuantofalta=19-int(hora)

if hora>="19":
    print("Hora de irse")
else:
    print("Te faltan",cuantofalta,"horas para irte a casa")



