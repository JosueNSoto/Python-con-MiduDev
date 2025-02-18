#Se ejecuta un código si se cumple una condición (if, elif, else)

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
nota = 5

if nota >= 9:
    print("Calificación sobresaliente")
elif nota >= 7:
    print("Calificación buena")
elif nota > 5:
    print("Apenas pasaste :)")
else:#Else no es obligatorio, en caso de no cumplir ninguna condición else se ejecuta
    print("Reprobaste :(")