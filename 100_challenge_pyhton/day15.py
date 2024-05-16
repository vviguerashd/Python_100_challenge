#ejercicio 1
#contador = 0
#while contador < 100:
#  print(contador)
#  contador += 2

#ejercicio 2
#fiesta = ""
#while fiesta != "sí":
#  print("¿Qué se acabó la fiesta?: ")
#  fiesta = input("")

#fix the code1
#counter = 0
#while counter <= 100:
#  print(counter)
#  counter +=1

#fix the code2
#counter = 0
#while counter < 25:
#  print(counter)
#  counter +=1

#fix the code3
#counter = 0
#while counter <= 12:
#  print(counter)
#  counter += 1

#fix the code4
#exit = ""
#while exit != ("sí"):
#  print("🥳")
#  exit = input("Terminamos la fiesta?")

#Day challenge
# este es un juego que te dirá cómo suena un animal, considera que son animales de la granja
print ("Bienvenido al juego de animales, por cada animal de la granja que ingreses en minúsculas te daremos un sonido y una frase")
print(" ")
exit = ("")
while exit != ("no"):
  animal = input("Ingresa el animal que quieres saber su sonido y su frase: ")
  if animal == ("perro"):
    print("El perro hace guau guau")
    print("El perrito baila al ritmo de su propio guau-guau.")
    exit = input("Quieres continuar en el juego?")
  elif animal == ("gato"):
    print("El gato hace miau miau")
    print("El gato es un animal domestico")
    exit = input("Quieres continuar en el juego?")
  elif animal == ("pájaro"):
    print("El pájaro hace Pío pío	")
    print("El pajarito dice pío-pío como un pequeño poeta al cantar.")
    exit = input("Quieres continuar en el juego?")
  elif animal == ("elefante"):
    print("El elefante barrita")
    print("El elefante barrita tan fuerte que hace temblar las hojas.")
    exit = input("Quieres continuar en el juego?")
  elif animal == ("león"):
    print("El león ruge")
    print("¡El león rugió tan fuerte que asustó a las nubes!")
    exit = input("Quieres continuar en el juego?")
  elif animal == ("rana"):
    print("La rana hace Croac croac	")
    print("La rana croa una melodía mágica que hace reír a los sapos.")
    exit = input("Quieres continuar en el juego?")
