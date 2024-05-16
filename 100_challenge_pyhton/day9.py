#Primer ejercicio
#myScore = int (input("¿Cuál fue tu puntuación?"))
#if myScore >= 90:
 # print("¡Excelente!")
#else:
 # print("¡Sigue trabajando!")

#segundo ejercicio
#miPi = float (input("¿Recuerdas 5 decimales del valor de pi?"))
#if miPi == 3.14159:
#  print("¡Excelente!")
#else:
#  print("¡Tienes que ser más preciso!")

#Extra challenge
#myPi = float (input("What is Pi to 3dp?"))
#if myPi == 3.142 :
#  print("Exactly!")
#else:
#  print("Try again 😭")

#Challenge

print  ("Bienvenida al Identificador de Generaciones")
miNacimiento = int (input("¿En qué año naciste?"))
if miNacimiento >1883 and miNacimiento <= 1900:
  print ("Eres Generación Perdida")
elif miNacimiento > 1901 and miNacimiento <= 1927:
  print ("Eres de La Gran Generación")
elif miNacimiento > 1928 and miNacimiento <= 1945:
  print ("Eres de la Generación Silenciosa")
elif miNacimiento > 1946 and miNacimiento <= 1964:
  print ("Eres de la Generación Baby Boomers")
elif miNacimiento > 1965 and miNacimiento <= 1980:
  print ("Eres de la Generación X")
elif miNacimiento > 1981 and miNacimiento <= 1996:
  print ("Eres de la Generación Millenials")
elif miNacimiento > 1997 and miNacimiento <= 2012:
  print ("Eres de la Generación Z")
elif miNacimiento > 2013 and miNacimiento <= 2025:
  print ("Eres de la Generación Alpha")
else:
  print ("No es una generación válida, ¿eres humano?")