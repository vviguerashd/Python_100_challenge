print ("Bienvenido a la creadora de buenos días de pepe")
name = input("¿Cuál es tu nombre?")
if name == "pepe" or name == "Pepe":
  print ("Hola " + name + "!")
  dia = input("Qué día de la semana es hoy?")
  if dia =="lunes":
    print("Te deseo " + name + " que hoy tengas un día bueno, comienza con todo")
  elif dia =="martes":
    print("Hoy " + dia + " deseo que " + name + " sea una persona afortunada")
  elif dia =="miercoles":
    print("Que hoy siendo " + dia + " mitad de semana, disfrutes tu día")
  elif dia =="jueves":
    print(name + " hoy es jueves, es día de ponerle ganas a tus amigos")
  elif dia =="viernes":
    print("Hoy es viernes, es día de llamar a tus amigos, no lo olvides " + name)
else:
  print("Esta creadora solo funciona para pepe, bye "+ name + "!")