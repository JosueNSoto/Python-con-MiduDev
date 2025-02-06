

"""
Acá está el repositorio de Github: https://github.com/midudev/curso-python
"""
#minúsculas y para separar con guiones bajos: snake_case
#mayúsculas y sin separar: CamelCase
#mayúsculas y separar con guiones bajos: SNAKE_CASE

print("Hola Mundo :)")
#print es una función que recibe parametros y los imprime en la consola

print("Podemos", "escribir", "varios parámetros", "después de la coma")

print("Modificaremos el final de esta impresión","A menos que tenga un separador en el string", sep="---")
#En lugar de un espacio, colocará tres guiones
print("Funciona en un string",end=" -> ")#En lugar de un salto de línea va a colocar una flecha
print("Este es un test para el salto")

nombre = "josve"
edad = 28#sera un int
fecha_de_nacimiento = "2000-01-28"#sera un string

print(type(fecha_de_nacimiento))
print(type(edad))