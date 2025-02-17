#Sirven para guardar datos y poder utilizarlos en el futuro
#Darles un nombre y referirnos a ellos

my_name="Josve"
print(my_name)

#Las variables en python son dinámicas, no necesitamos especificar el tipo de dato que vamos a guardar.
#Podemos cambiar el tipo de dato de una variable en cualquier momento, conforme avanza el programa

age=25
print(type(age))#Es un int
#Como se observa, es la misma variable, pero dinámica
"""age="Veinti cinto"
print(type(age))#Es un string"""

#También podemos usar una cadena con un número, usando una cadena formateada
#También llamadadas f-strings
print(f"Mi nombre es '{age}' y mi nombre es {my_name}")
#También podemos hacer operaciones dentro de esta evaluación
print(f"Mi nombre es '{age+25}' y mi nombre es {my_name}") #En la edad sería 25, edad inicial + lo que le agreguemos

#No se recomienda declarar variables en un mismo renglón, es confuso
name, city, age = "Josve", "EDOMEX", 25
#Estoy es confuso y no se recomienda

#Convención de nombres de variables, usar snake_case
mi_nombre="josve"
mi_nombre_de_mi_variable="ñangos"

MI_CONSTANTE = 3.1416#Las constantes se declaran en mayúsculas

