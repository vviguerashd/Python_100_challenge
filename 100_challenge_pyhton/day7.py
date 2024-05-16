#order = input("What would you like to order: pizza or hamburger?")
#if order == "hamburger":
  #print("Thank you.")
  #cheese = input("Do you want cheese?")
  #if cheese == "yes":
   #print("You got it.")
  #else: 
    #print("No cheese it is.")
#elif order == "pizza":
  #print("Pizza coming up.")
  #toppings = input("Do you want pepperoni on that?")
  #if toppings == "yes":
    #print("We will add pepperoni.")
#  else:
    #print("Your pizza will not have pepperoni.")

fan = input("¿Eres una verdadera fan de de Toy Story?")
if fan == "si":
  print("Genial, aquí 5 preguntas para fans")
  hermanos = input("¡A ver, cuántos hermanos tiene andy!")
  #primer pregunta
  if hermanos == "1":
    print("¡Eres fan! pero vamos iniciando")
  else:
    print("¡No Eres fan! bye")
  print("Siguiente:")
   #segunda pregunta
  buzz = input("¿Cómo se llama el astronauta del espacio?")
  if buzz == "buzz":
    print("Correcto, pero no deja de ser fácil, continuemos!")
  else:
    print("¡No Eres fan! bye")
   #tercer pregunta
  al = input("¿Cómo se llama el villano de Toy Story 2?")
  if al == "Al":
    print("Correcto, el cabeza de pollo!")
  else:
    print("¡No Eres fan! bye")
    #cuarta pregunta
  ojos = input("¿Cuántos ojos tienen los marcianitos?")
  if ojos == "tres":
      print("Correcto, tienen 3 ojitos y son adorables")
  else:
      print("¡No Eres fan! bye")
  #quinta pregunta
  año = input("¿En qué año se estrenó Toy Story 1?")
  if año == "1995":
      print("No hay duda, eres una verdadera fan")
  else:
      print("¡No Eres fan! bye")
elif fan == "no":
  print("Nos vemos en otro cuestionario")