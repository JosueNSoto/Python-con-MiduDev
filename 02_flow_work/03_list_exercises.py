###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".
"""mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
palabra1=mensaje[7:14] #palabra1=mensaje[7:], también es otra solución
print(palabra1)"""

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

#Otra solución es: numeros[0], numeros[-1] = numeros[-1], numeros[0], conocido como asignación múltiple
#Primero se evalúan los valores de la derecha, y luego se asignan a los valores de la izquierda
"""numeros = [10, 20, 30, 40, 50]
print(numeros)
numeros[0]=numeros[-1]
print(numeros)
numeros[-1]=10
print(numeros)"""

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.
"""pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
sandwich = []
sandwich += pan + ingredientes + pan_abajo #Otra solución es: sandwich = pan + ingredientes + pan_abajo, donde solamente metemos los elementos en una variable
print(sandwich)"""

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]
"""lista = [1, 2, 3]
#duplicada = lista * 2 
#print(duplicada)
lista_duplicada = lista + lista
print(lista_duplicada)"""


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30
lista = [10, 20, 30, 40, 50]
#print(lista[2]), Solución pedorra, poco eficiente
centro = len(lista)//2
print(centro)
print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
"""lista = [1, 2, 3, 4, 5, 6]
mitad = len(lista)//2#Nos devuelve un entero, si fuera una sola /, nos devolvería un flotante
primera_mitad = lista[:mitad][::-1] + lista[mitad:]#La parte de [::-1], automáticamente efectúa el cambio sobre la lista previa, que en este caso es la primera mitad. Después estamos concatenando la primera mitad invertida con la segunda mitad
print(primera_mitad)"""