
# Que es una variable?
'''Las variables son como de_int_a_str_variables que almacenan datos de cualquier tipo
a las cuales podemos acceder llamandolas por su nombre'''
# Aqui vemos cuatro variables diferentes que almacenan 4 distintos tipos de datos
# Al llamarlas por su nombre usando un print, imprimimos lo que almacenan ellas, que seria lo que esta despues de =

mi_variable = 'Hola' # Variable que almacena un string ("Hola")
print(mi_variable)   # Imprimimos el hola de mi_variable

mi_int_variable = 20 # Variable que almacena un int (20)
print(mi_int_variable) # Imprimimos el 20 de mi_int_variable

mi_float_variable = 20.5 # Variable que almacena un float (20.5)
print(mi_float_variable) # Imprimimos el 20.5 de mi_int_variable

my_boolean_variable = False # Variable que almacena un bolean (False)
print(my_boolean_variable) # Imprimimos el boolean de mi_boolean _variable

#---------------------------------------------------------------------------------------------------------------------

'''Podemos transformar variables, por ejemplo una que almacenaba un str, en una que ahora almacene un int
sin tener que cambiar lo el valor de la variable, me explico:  '''
mi_int_variable = 20 # Aqui "mi_int_variable" almacena un int el cual es 20
bolsa_de_str = str(mi_int_variable) # Decimos que el int(20) cambie a ser un str() y ahora my_int_variablese se llama bolsa_de_str
# Imprimimos a bolsa_de_str y no a mi_int_variable por que le cambiamos el nombre, importante
print(bolsa_de_str) # Al imprimir vemos que sigue dando el numero 20 a pesar de que ahora es tipo str
print(type(bolsa_de_str)) # Podemos comprobar que ahora 20 es de tipo str con type, vemos que perdio su funcion de int
'''Al 20 ser un str y ya no ser un int deja de ser tratado como numero y pasa a ser tratado como un texto
por lo que no podemos realizar operaciones matematicas con el. Visualmente vemos que es un numero pero 
al convertirlo en str el sistema lo trata como texto'''

#---------------------------------------------------------------------------------------------------------------------

# Podemos combinar para imprimir variables en una linea, a esto se le llama 'concatenacion de variables'
Saludo = "Hola "
Despedida = "Adios "
print(Saludo, Despedida) # Los unimos y se imprimen ambos en orden y en la misma linea
# Tambien podemos combinar una cadena de texto nuestra, con una combinacion de variables
print(Saludo + " soy Joseph, como estas? " + Despedida) 

#---------------------------------------------------------------------------------------------------------------------

# Distintas Variables en una linea (no es muy buena practica pero se puede hacer)
'''El valor se asigna segun el orden | la bolsa_de_str 1(name) guardara el valor 1(Joseph), la bolsa_de_str 2(surname)
guardara el valor 2(Elizondo) y asi sucesivamente'''
name, surname, alias, age = "Joseph", "Elizondo", "Tote", 22
print(name, surname, alias, age) # Imprimimos para comprobar
# Podemos imprimirlas en el orden que queramos de primera a ultima 
# Incluso como vimos antes podemos meter cadenas de texto propias entre ellas para darles mas sentido
print("Me llamo ", name, surname, "mi apodo es ", alias, "y tengo ", age, "años")
print(name)# O usarlas por separado, dandole uso solo a una o solo dos etc...

#---------------------------------------------------------------------------------------------------------------------

# Funcion Input(), esta permite que el usuario sea el que digite que va almacenar una variable
primer_nombre = input("Cual es tu nombre?: ") # Lo que digite el usuario sera lo que se almacene en primer_nombre
print(primer_nombre) # vemos que digito el usario

#---------------------------------------------------------------------------------------------------------------------

#Funcionalidad de 'len()'
#Esta cuenta la cantidad de caracteres de lo que almacena una variable que le demos(incluye o cuenta espacios)
bolsa_de_str = "Hola"
print(len(bolsa_de_str)) # imprime 4 ya que es la cantidad de caracteres que guarda bolsa_de_str con el "H-o-l-a" -> 4
# Da error con los de tipo numericos eje: 200 -> no daria 3 ni 200 porque es un numero sino que daria error