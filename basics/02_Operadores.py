
# Operadores matematicos con enteros (int)
print(3 + 4) # Suma -> +
print(3 - 4) # Resta -> -
print(3 * 4) # Multiplicacion -> *
print(10 / 3) # Division exacta, incluye decimas -> /
print(10 // 3) # Division pero aproximandose siempre al numero entero mas cercano, evitamos las decimas -> //

# (%) Devuleve el residuo de una divion
print(10 % 3) # Da como resultado 9 es decir queda 1 sobrando ese uno sera lo que imprima ya que es lo que sobro
# en caso de que una divison sea exacta osea no deja residuo imprimira 0

#Aqui calculamos exponentes | En este caso 2 elevado a 3 (es lo mismo que decir 2x2x2 =8)
print(2 ** 3) 

#---------------------------------------------------------------------------------------------------------------------

# Podemos hacer operaciones con cadenas de texto:
# Podemos sumar cadenas de texto
print("Hola " + "Python " + "¿Qué tal?") # Y se imprime uno detras del otro, como si fuera una oracion normal
# Podemos multiplicar cadenas de texto
print("Hola " * 5) # Le decimos que imprima 5 veces el hola, tambien valido

#---------------------------------------------------------------------------------------------------------------------

# Solo se pueden operar datos del mismo tipo -> str con str o int con int o etc...
# Por ende si queremos operar un str con un int debemos convertir uno al tipo del otro como en este ejemplo
print("Hola " + str(5)) # Covertimos el int en string y asi quedan una operacion de dos string valida

#---------------------------------------------------------------------------------------------------------------------

# Importante:
mi_float = 2.5 * 2 # Aqui hacemos un operacion que nos da de resultado 5.0 el cual seria un float
'''Si queremos concatenar una cadena de texto propia con un tipo float, hacemos lo siguiente:
No podemos operar floats con cadenas de texto por lo que convertimos el float a int y ahora si podemos'''
print("Hola " * int(mi_float))  # Escribimos int() y dentro de los parentesis el nombre de la variable y listo ahora es int
# Importante si el float no es exacto como 5.0 si no que es 5.2 o 5.8 al cambiarlo a int queda en 5, su numero entero original

#---------------------------------------------------------------------------------------------------------------------

#Operadores Comparativas con enteros 
print(3 > 4) # Mayor que
print(3 < 4) # Menor que
print(3 >= 4) # Mayor o igual que
print(4 <= 4) # Menor o igual que
print(3 == 4) # Igual que
print(3 != 4) # Diferente que
# Estos daran como resultado un boolean (true o false) es como una pregunta de, este es mayor que este? y asi con todos

#---------------------------------------------------------------------------------------------------------------------

# Operaciones con cadenas de texto. Compara en orden alfabetico 
'''Compara la letra inicial de cada palabra y ahi decide cual es mayor o menor en orden alfabetico, aunque si todo 
es igual pero una palabra es más corta como: hola - holanda | entonces la mas corta es menor y la larga es mayor
Si son exactamente iguales: no es ni mayor ni menor, son iguales
*Importante* Las mayúsculas son “menores” que las minúsculas'''
print("Hola" > "Python") # Es mayor Hola que Python? -> La h esta primero que la P = true/verdadero
print("Hola" < "Python") # Es menor Hola que Python? -> La h esta primero que la P = false/falso
print("aaaa" >= "abaa")  # Es mayor o igual Hola que Python? -> La h esta primero que la P = true/verdadero
print("Hola" <= "Python") # Es menor o igual Hola que Python? -> La h esta primero que la P = false/falso
print("Hola" == "Hola") # Es igual Hola que Python? -> La h esta primero que la P = false/falso
print("Hola" != "Python") # Es diferente Hola que Python? -> La h esta primero que la P = true/verdadero

#---------------------------------------------------------------------------------------------------------------------

# Usando el len() comparamos por cantidad de caracteres osea por int, no por orden alfabetico
# El len() compara por cantidad caracteres en cada palabra 
print(len("aaaa") >= len("abaa")) # Es mayor o igual aaaa(4) que abaa(4) -> Son iguales tienen 4 caracteres = true

#---------------------------------------------------------------------------------------------------------------------

# Operadores Lógicos 
''' Estos son complementos y son:
and = y
or = o
not = niega
'''
# Con (and) ambas condiciones se deben cumplir para ser true sino seran false
print(3 > 4 and "Hola" > "Python") # 3 es mayor que 4 y (and) Hola es mayor que Python -> False
# Es false porque 3 no es mayor que 4 aunque Hola si sea mayor que Python, solo se cumple una de las dos.

# Usando (or) con tan solo que se cumpla una de las condiciones sera true
print(3 < 4 or 4 == 5) # 3 es menor que 4 o(or) 4 es igual a 4 -> true
# Es true porque se cumple una de las condiciones, 3 si es menor que 4 aunque 4 no sea igual que 5

#Aqui combinamos y decimos:
'''   3 es menor que 4 o(or) 4 es igual 4    | Esa es la primera condicion y luego dice otra: 
  y(and) 1 es igual a 1 o(or) 2 es menor a 3 | esta es la segunda condicion.
tan solo se debe cumplir una condicion en ambas para que sea true de no ser asi sera false 
'''
print(3 < 4 or 4 == 4 and 1 == 1 or 2 < 3)

# not() niega la condicion, es deir, aqui 3 es mayor que 4? Pues NO -> false, pero el not niega eso, el resultado da true. Como que lo contradice
print(not (3 > 4))  