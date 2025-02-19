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

"""
AND
TRUE + TRUE = TRUE
TRUE + FALSE = FALSE
FALSE + TRUE = FALSE
FALSE + FALSE = FALSE

OR
TRUE + TRUE = TRUE
TRUE + FALSE = TRUE
FALSE + TRUE = TRUE
FALSE + FALSE = FALSE

NOT
TRUE = FALSE
FALSE = TRUE
"""
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
if not es_fin_de_semana:#Nos preguntamos si NO es fin de semana, lo que hace el not, es cambiar el valor de es_fin_de_semana
    print("Tenemos que chambear :(")
    print(es_fin_de_semana)
    
#Ejemplo 7
#Condición ternaria
#[Código si cumple la condición if] if [condición] else [Código si no cumple
u_love_job = True
print("Sigue trabajando feliz") if u_love_job == True else print("Renuncia al trabajando")
#La primera parte es lo que haría si se cumple la condición, después la evaluación de la condición, y por último lo que haría si no se cumple la condición
#Esto se hace para "simular" que es un dialogo, ya que se lee de izquierda a derecha