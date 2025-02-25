#Vamos a hablar sobre los métodos que tienen las listas y que con estos se pueden hacer los ejercicios de una manera más eficiente
import os
os.system("clear")

#Métodos "Añadir" de las listas
print("Métodos para añadir elementos a una lista")
lista = [1, 2, 3, 4, 5]
#append() agrega UN solo elemento al final de la lista, si  tratas de agregar más, no funcionará
lista.append(6)#Recibe un solo argumento
print(lista)

#insert() agrega un elemento en la posición que le indiques, solamente desplaza el elemento
lista_abedecario=["a","b","d","e","f","g"]
lista_abedecario.insert(2,"c")#Recibe dos argumentos, el primero es la posición y el segundo es el elemento a agregar, con este método, no podemos agregar más de un elemento
print(lista_abedecario)

#extend() agrega varios elementos al final de la lista, recibe un solo argumento, que es una lista
lista_extend = ["samsung", "Huawei", "Xiaomi"]
print(f"Nuestra lista original es: {lista_extend}")
lista_extend.extend(["sony", "LG", "Nokia"])#Recibe un solo argumento, que es una lista
print(lista_extend)

#Métodos "Borrar" de las listas
print("Métodos para borrar elementos a una lista")
#Eliminar la primera aparición de un elemento con remove(), el resto las dejas intactas
lista_remove = ["samsung", "Huawei", "Xiaomi"]
lista_remove.remove("samsung")#Recibe un solo argumento, que es el elemento a eliminar
print(lista_remove)

#Eliminar un elemento sabiendo su índice o posición con pop(), el resto las dejas intactas
lista_pop = ["samsung", "Huawei", "Xiaomi", "Nokia","Lumia"]#nos devuelve el elemento que eliminamos
residuo = lista_pop.pop(-2)#Si no le pasamos un argumento, elimina el último elemento de la lista, podemos utulizar un índice negativo para eliminar desde el final
print(residuo)

#Eliminar un elemento con del, el resto las dejas intactas, sin embargo, este no devuelve NADA
#Puedes eliminar un rango de elementos con del, con pop no es posible
lista_del = ["1", "2", "3", "4","5"]
"""del lista_del[2]#Recibe un solo argumento, que es el índice del elemento a eliminar
print(lista_del)
"""
del lista_del[1:5]#no incluye el último índice
print(lista_del)

#Eliminar todos los elementos de una lista con clear()
lista_clear = [1,2,3,4,5,6,7,8,9,10]
lista_clear.clear()#No recibe argumentos
print("Tenemos la lista vacia por el método 'clear': ",lista_clear)

#Métodos "Ordenar" de las listas
print("Métodos para ordenar elementos a una lista")
print("El método 'sort()', ordena los elementos de la lista original, pero no devuelve nada")
number = [10,20,50,60,15,90,80,100,40,30,10]
number.sort()#Eficiente en memoria, no se puede revertir al orden original
#Podemos utilizar number.sort(reverse=True) para ordenar de manera descendente
print(number)

print("El método 'sorted()', ordena los elementos de una copia de la lista original, pero no modifica la lista original y ahora si devuelve la lista ordenada")
numbers = [10,20,50,60,15,90,80,100,40,30,10]
sorted_numbers = sorted (numbers)#Hace una copia de la lista original y la ordena, después la devuelve y la guarda en sorted_numbers
#Podemos utilizar sorted(numbers, reverse=True) para ordenar de manera descendente
print(numbers)

#Existen problemas a la hora de ordenar listas con elementos de diferentes tipos, por ejemplo, números y letras
#Un ejemplo es con cadenas de texto con mayúsculas y minúsculas	
frutas = ["Manzana", "Banana","manzana", "pera", "Pera", "banana"]
#frutas.sort()#Ordena las cadenas de texto de manera ascendente
#print(frutas)#De esta manera ordena primero las mayúsculas y después las minúsculas
frutas.sort(key=str.lower)#Ordena las cadenas de texto de manera ascendente, pero ignora las mayúsculas y minúsculas
print(frutas)

#Más métodos que se pueden utilizar con las listas
"""
len() nos devuelve la longitud de la lista
index() nos devuelve el índice de un elemento en la lista
count() nos devuelve el número de veces que aparece un elemento en la lista
in y not in nos permite saber si un elemento está o no en la lista
"""