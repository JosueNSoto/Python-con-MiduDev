#Vamos a hablar sobre los métodos que tienen las listas y que con estos se pueden hacer los ejercicios de una manera más eficiente
import os
os.system("clear")

#Métodos de las listas
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