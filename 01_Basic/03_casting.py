#Transformación de tipos
#Convertir el 100 a un string, un 0 a boleano, un 1 a flotante y un 1.0 a entero

print("Vamos a iniciar la conversión de tipos")  

print("De entero a string:")
print(type(100))#Es un entero
print(type(str(100)))#Lo convertimos a string 

print("De string a entero:")
print(type("100"))#Es un string
print(type(int("100")))#Lo convertimos a string

#No podemos sumar un string con un entero
"""
print("100" + 2), esto nos daría un error
"""
#Sin embargo, si podemos multiplicar un string por un entero, nos repetiría el string dado
print("Hola"*2)
#Podemos convertir el tipo de dato y hacer la operación
print(int("100")+2)#La suma es 102
#Podemos convertir el tipo de dato y hacer la contanenación
print("500"+str(2))#La concatenación es 5002

print("Podemos transformar un flotante a entero: ")#Perdemos precisión, pero obtenemos el entero, borra después del punto y queda solo el entero
print(type(3.1416))
print(int(3.1426))
print(type(int(3.1426)))

print("Podemos redondear un flotante a entero con la función round: ")#Redondea al entero más cercano
print(round(2.5))#2 
print(round(3.5))#4
"""
Si está justo en medio .5, hace el redondeo al número par más cercano, por ese 3.5 es 4
"""