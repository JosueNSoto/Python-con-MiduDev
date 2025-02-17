#Función input() para poder pedir datos en consola al usuario
#SIEMPRE que se pida un dato, se guardará como un string

"""print("Ingresa tu nombre:")
nombre = input()

#Existe una forma más corta de hacer esto
apellido = input("Cuál es tu apellido? ")#Puedes agregar un salto de linea \n

print(f"Tu nombre es: {nombre}, mientras que tu apellido es: {apellido}")#Puedes agregar un salto de linea \n"""

age = int(input("Cuál es tu edad? "))#Transformamos el string a un entero
print(f"Tu edad es: {age + 20}")

nombre, apellido = input("Escribe uno de tus nombres y tu primer apellido: ").split()
print(f"El nombre ingresado es: {nombre} y tu apellido es: {apellido}")

#Podemos obtener múltiples datos en una sola línea
"""city, state = input("Dame tu ciudad y estado: ").split()#Por defecto, split separa por espacios 
print(f"La ciudad donde vives es: {city} y el estado es: {state}, ¿verdad?")"""