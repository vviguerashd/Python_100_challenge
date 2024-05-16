#challenge
#ejercicio para calcular cuántos segundos tiene este año
bisiesto = input ("¿Este año es bisiesto? ¿si o no?")
segundos = 60 * 60 * 24 * 365
segundosBisiesto = 60 * 60 * 24 * 366

if bisiesto == "si":
  print ("Este año tiene" , segundosBisiesto ," segundos")
else:
  print ("Este año tiene" , segundos ," segundos")

