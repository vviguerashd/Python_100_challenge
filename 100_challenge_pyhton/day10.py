## Primer ejercicio
#print (suma)
#suma = 4 + 3
  
#resta = 6 - 3
#print (resta)
  
#division = 21/2
#print(division)
  
  #elevar el numero a una potencia, en este caso es a la potencia dos o al cuadrado
#potencia = 5**2
#print (potencia)
  
  # modulo o residuo de una division, en este caso sobra 1 unidad de dividir 21 entre 4
#modulo = 21%4
#print (modulo)
  
  # la divisionEntera descarta la parte decimal del cociente, en este caso 21//4 es igual a 5
#divisionEntera = 21//4
#print (divisionEntera)

## Acá comienza el "Fix my Code"
# Solve the following problems with my code
# Your goal is to print the solution of all 3 calculations to the screen.

# multiplication
#multiplication = 3.4 * 6.8
#print (multiplication)

# division
#division = 2467 / 4673
#print (division)

#raise 10 to the power of 2
#potencia = 10**2
#print (potencia)

# print the remainder when 343 is divided by 4
#modulo = 343%4
#print(modulo)

## Ejercicio 2 - Reto del día 10
laCuenta = float(input("De cuanto es tu cuenta?"))
porcentaje = float(input("¿Qué porcentaje de propina quieres dejar? (lo recomendado es 10%)"))
propina = (laCuenta * porcentaje) / 100
numeroDePersonsas = int(input("Cuantas personas son?"))
respuesta=(laCuenta/numeroDePersonsas)+(propina/numeroDePersonsas)
respuesta = round(respuesta,2)
print("Cada persona debe pagar: $",respuesta, " con la propina incluida")
