print("==Un login seguro== y muy básico :p ")

userName = input("Ingresa tu nombre de usuario: ")
password = input("Ingresa tu contraseña: ")
if userName == "admin" and password == "admin":
  print("""
  Bienvenido admin al sistema

  Te recuerdo que como admin tienes acceso a todos los datos y eso debe de ser 
  de mucho cuidado, sé precavido con lo que haces porque no queremos que rompas nada.

  Ve por un café y comienza el día.

  No olvides que eres genial
  """)
elif userName == "vico" and password == "vico":
  print("""
  Bienvenido vico al sistema

  Siéntete orgulloso del trabajo que haces, no dudes en lanzarte a hacer algo nuevo ni a dejar de aprender.

  Ve por un café y comienza el día.

  No tengas duda de que eres un campeón :p
  """)
elif userName == "fer" and password == "fer":
  print("""
  Bienvenide fer al sistema

  Sueles traer a tu entorno felicidad y eso es genial en todos los sentidos, no dejas de sorprendernos con tu espontaneidad y capacidad de generar buenos momentos.

  Ve por un café y comienza el día.

  Sigue siendo genial
  """)
else:
    print("Usuario o contraseña incorrectos")