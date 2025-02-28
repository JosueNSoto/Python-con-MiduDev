#Vamos a trabajar con búcles, repetidamente mientras se cumpla una condición
#Para automatizar, necesitamos que se cumpla una condición, si no se cumple, el bucle se detiene
#While: mientras se cumpla la condición, se ejecuta el bucle
#En algunos casos, primero se evalúa la condición y luego se ejecuta el bucle, también se puede ejecutar el código y al final se evalúia la condición para ver si se ejecuta nuevamente el bucle
#En el caso de que la condición no se cumpla, el bucle se detiene
import os
os.system("cls")
#Sintaxis
#while condición:
#    código a ejecutar si se cumple la condición

print("Inicio del programa")
contador = 1
while contador <= 5: #Mientras el contador sea menor o igual a 5, se ejecuta el bucle
    print(contador) #Se imprime del 1al 5
    contador += 1 #Es importante que la condición se pueda cumplir, si no, el bucle se ejecutará infinitamente
    
print("----------------------")

print("Bucle while con break")
#Este tipo de bucles se hacen dado que no conoces el número de iteraciones que se van a realizar
#En este caso, se va a ejecutar el bucle hasta que el contador llegue a 5
contador = 0
while True: #Bucle infinito
    print(contador)
    contador += 1
    if contador == 5:
        break #Se detiene el bucle cuando el contador llega a 5
    
print("----------------------")

print("Uso de bucle con break")
#Este tipo de bucles se hacen dado que no conoces el número de iteraciones que se van a realizar
#Queremos buscar el primer múltiplo de 5
contador = 0
while True: #Bucle infinito
    print(contador)
    contador += 1
    if contador % 105 == 0:
        print(f"El número {contador} es múltiplo de 5")
        break #Se detiene el bucle cuando el contador llega a 5
    
print("----------------------")

print("Vamos a usar el 'continue'")
#Lo que hace es saltar esa iteración y continuar con la siguiente
#Break: detiene el bucle
#Continue: salta la iteración 
contador = 0
while contador <= 100: #Bucle infinito
    contador += 1
    if contador % 2 == 0: #Si el contador es par, se salta la iteración
        continue #Salta la iteración
        #print("Test") #No se ejecuta
    print(contador) #Llega a esta parte si el contador es divisible entre dos, ya que ignora la anterior
    
print("----------------------")

print("Vamos a usar el 'else'")
contador = 0
while contador <=5:
    print(contador)
    contador += 1
    #break # Podemos ocupar break, sin embargo, si la condición se cumple, el bucle se detiene y no llegaríamos al else
else:#El else va a ejecutar el código cuando la condición del while no se cumpla
    print("Fin del bucle")#El else sirve para confirmar que el bucle se ha detenido y se ha cumplido la condición