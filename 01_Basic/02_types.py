"""
Vamos a ver los tipos de datos básicos en Python
"""
#Tenemos strings o cadenas de texto, números enteros, decimales, booleanos, listas, diccionarios, NontType, tuplas y conjuntos
print("int: ")
print("100")#Obtenemos un valor y que es un str
print(type(100))#Obtenemos el tipo de dato 
print("-5")#Obtenemos un valor y que es un str
print(type("-5"))#Obtenemos el tipo de dato
#Podemos sumar a la hora de colocar un print
print(50+1)#Obtenemos un 51

print("float: ")
print("10.5")
print(type("10.5"))
print(1e3)
print(type(1e3)) #notación científica y esto da 1000.0

print("complex: ") #números complejos, tenemos un número real y un número imaginario
print(1 + 5j)
print(type(1 + 5j))

print("String: ")
print("")
print(type(""))
print("""
      Este  es un texto en multilinea
      """)
print(type("""
      Este  es un texto en multilinea
      """))

print("Boolean: ")
print(type(True))
print(type(False))
print(1>2)#debería devolver false, porque 1 no es mayor que 2
print(type(1>2))

#Este tipo de dato describe la ausencia de valor
print("NoneType: ")
print(type(None))