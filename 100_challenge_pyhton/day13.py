print ("Este programa te da la calificación de un examen según su puntaje")
print ("")
print ("Para lo cual necesitamos que contestes algunas preguntas")
nombreExamen = input("¿Cuál es el nombre del examen?")
puntMax = int(input("¿Cuál es el puntaje máximo del examen?"))
puntos = int(input("¿Cuál es el puntaje que obtuviste en el exámen?"))
porcentaje = float((puntos/puntMax)*100)
#print (porcentaje)

if porcentaje >= 90 and porcentaje <=100:
  print("Obtuviste un porcentaje de", porcentaje, "% que equivale a una A+")
elif  porcentaje >= 80 and porcentaje <90:
    print("Obtuviste un porcentaje de", porcentaje, "%que equivale a una A-")
elif  porcentaje >= 70 and porcentaje <80:
  print("Obtuviste un porcentaje de", porcentaje, "% que equivale a una B")
elif porcentaje >= 60 and porcentaje <70:
  print("Obtuviste un porcentaje de", porcentaje, "% que equivale a una C")
elif porcentaje >= 50 and porcentaje <60:
  print("Obtuviste un porcentaje de", porcentaje, "% que equivale a una D")
elif porcentaje >0 and porcentaje < 50:
  print("Obtuviste un porcentaje de", porcentaje, "% que equivale a una horrible F")
else:
  print("Por favor ingresa un puntaje válido")