#Se ejecuta un código si se cumple una condición (if, elif, else)

import os
os.system("cls")#os.system("clear")#Limpia la consola, el primero es para windows, el segundo para mac

#Ejemplo 1
"""edad = 18
if edad >= 18:#Son necesarios los : y la identación
    print("Eres mayor de edad")"""
    
#Ejemplo 2
"""edad = 17
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")"""
    
#Ejemplo 3
"""nota = 5

if nota >= 9:
    print("Calificación sobresaliente")
elif nota >= 7:
    print("Calificación buena")
elif nota > 5:
    print("Apenas pasaste :)")
else:#Else no es obligatorio, en caso de no cumplir ninguna condición else se ejecuta
    print("Reprobaste :(")"""
    
#Ejemplo 4 
### Operadores lógicos
#and, or, not
edad = 15
carnet = False

if edad >= 18 and carnet == True:
    print("Puedes conducir")
elif edad >= 16 and carnet == True:
    print("Necesitas un adulto para conducir")
else:
    print("No puedes conducir")
    
#Ejemplo 5  
if edad >= 18 or carnet == True:
    print("Puedes conducir")
else:
    print("No puedes conducir")
    
#Ejemplo 6
es_fin_de_semana = False#Acá sabemos que NO es fin de semana
if not es_fin_de_semana:#Nos preguntamos si NO es fin de semana, tenemos que trabajar
    print("Tenemos que chambear :(")
    print(es_fin_de_semana)