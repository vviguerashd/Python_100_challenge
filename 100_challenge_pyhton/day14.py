from getpass import getpass as input

print("Bienvenid@ al juego de Piedra, Papel o Tijera")
print("")
print("Escribe una opción, comienza el jugador 1 y después el jugador 2:")
jugador1 = input("Jugador 1: ¿Piedra, Papel o Tijera? ")
print("")
jugador2 = input("Jugador 2: ¿Piedra, Papel o Tijera? ")
print("")
if jugador1 == "Piedra" and jugador2 == "Piedra":
  print("empate de Piedras!")
elif jugador1 == "Piedra" and jugador2 == "Papel":
  print("gana Jugador 2, porque Papel envuelve a Piedra")
elif jugador1 == "Piedra" and jugador2 == "Tijera":
  print("gana Jugador 1, porque Piedra aplasta Tijera")

elif jugador1 == "Tijera" and jugador2 == "Tijera":
  print("empate de Tijeras!")
elif jugador1 == "Tijera" and jugador2 == "Piedra":
  print("gana Jugador 2, porque Piedra aplasta Tijera")
elif jugador1 == "Tijera" and jugador2 == "Papel":
  print("gana Jugador 1, porque Tijera corta Papel")

elif jugador1 == "Papel" and jugador2 == "Papel":
  print("empate de Papeles!")
elif jugador1 == "Papel" and jugador2 == "Piedra":
  print("gana Jugador 1, porque Piedra aplasta Papel")
elif jugador1 == "Papel" and jugador2 == "Tijera":
  print("gana Jugador 1, porque Tijera corta Papel")
else:
  print("Error, prueba escribir la primer letra en mayúscula")