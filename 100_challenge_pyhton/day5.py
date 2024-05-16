# este código es para el ejercicio realizado durante la clase
#miNombre = input("¿Cuál es tu nombre? ")
#if miNombre == "vico":
    #print("Hola vico, bienvenido")
    #print("Estás haciendo un buen esfuerzo en este curso, sigue así ;)")
#else:
    #print("Hola", miNombre, "cuéntame más de ti")
   #miEdad = input("¿Cuál es tu edad? ")
    #print("Ahora sé", miNombre, "que tienes", miEdad, "años, te doy la bienvenida")

#este código es para el reto 5

print("Bienvenido al seleccionador de personajes de la película 'Intensamente'")
print("contesta solo con si o con no a las siguientes preguntas para saber cuál personaje eres:")
alegria = input("¿Te sientes feliz todo el día?")
if alegria == "si":
  print("Entonces tú eres alegría e iluminas todo a tu alrededor")
else:
  print("Entonces no eres alegría, intentemos con otra pregunta:")
  tristeza = input("¿Te sientes muy triste y lloras fácilmente?")
  if tristeza == "si":
    print("Entonces tú eres tristeza y eres capaz de solucionar los problemas de la película")
  else:
    print("Entonces no eres tristeza, intentemos con otra pregunta:")
    desagrado = input("¿Te sientes con el seño fruncido ante personas nuevas y sueles pensar que las personas son payasitas al primer contacto?")
    if desagrado == "si":
      print("Entonces tú eres desagrado y puedes evitar muchos malos momentos por anticipado")
    else:
      print("Entonces no eres desagrado, intentemos con otra pregunta:")
      temor = input("¿Te asusta lo nuevo y sueles paralizarte cuando hablas frente a las personas?")
      if temor == "si":
        print("Entonces tú eres temor y sueles ser muy precavido cuando te sientas en situaciones difíciles")
      else:
        print("Entonces no eres temor, intentemos con otra pregunta:")
        furia = input("¿Te sientes enojado cuando las cosas no salen como quieres?")
        if furia == "si":
          print("Entonces tú eres furia y podrías incendiar un campo completo si te lo propones, relax!")
        else:
          print("Entonces no eres furia, ni ninguno de los personajes de esta película... tal vez aparezcas en la nueva película de 2024.")