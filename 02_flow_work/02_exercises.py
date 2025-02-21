###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
print("Ejercicio 1 ----------------------------")
"""num1, num2 = input("Ingresa el primer número, deja un espacio e ingresa el segundo número: ").split()
print(f"El número 1 es: {num1}, el número 2 es: {num2}")
num1=int(num1)
num2=int(num2)
if num1 != num2:
    if num1>num2:
        print(f"el número {num1}, es mayor que {num2}")
    else:
        print(f"el número {num2}, es mayor que {num1}")
else: print("Los números son iguales")"""

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("Ejercicio 2 ----------------------------")
"""num1, num2 = input("Ingresa el primer número, deja un espacio e ingresa el segundo número: ").split()
num1=int(num1)
num2=int(num2)
operacion = input("Ingresa el operador que deseas (+, -, *, /): ")
if operacion == "+":
    print(f"El resultado de la suma es: {num1+num2}")
elif operacion =="-":
    print(f"El resultado de la resta es: {num1-num2}")
elif operacion =="*":
    print("El resultado de la multiplicación es: ",num1*num2)
elif operacion =="/":
    if num2==0:
        print("No podemos realizar la división entre 0")
    else: print(f"El resultado de la división es: {num1/num2}")
else:print("Operación no reconocida")"""

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print("Ejercicio 3 ----------------------------")
"""año = input("Ingresa un año: ")
año = int(año)
print(f"El año es: {año}")
if año%100==0 and año%400!=0:
    print("El año NO es bisiesto")
elif (año%4==0 and año%100!=0) or año%400==0:
    print("El año es bisiesto")
else: print("El año NO es bisiesto")"""

anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"{anio} es un año bisiesto.")
else:
    print(f"{anio} no es un año bisiesto.")
        

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)
print("Ejercicio 4 ----------------------------")
age = input("Ingresa una edad: ")
age = int(age)
print(f"La edad es de : {age}, usted es: ",end="")
if age >= 65:
    print("Adulto mayor")
elif age >= 18:
    print("Adulto")
elif age >= 13:
    print("Adolescente")
elif age >= 3:
    print("Niño")
else: print("Bebé")