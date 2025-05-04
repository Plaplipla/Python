# Ejercicio 1   |   Ingresar notas
print("Bienvenido al sistema de promedios DUOCUC\nIngrese las notas: ")

nota1 = input("Ingresa la nota de la EA1: ")
nota1 = round(float(nota1), 2)

nota2 = input("Ingresa la nota de la EA2: ")
nota2 = round(float(nota2), 2)

nota3 = input("Ingresa la nota de la EA3: ")
nota3 = round(float(nota3), 2)

nota_ponderada1 = nota1 * 0.3
nota_ponderada2 = nota2 * 0.4
nota_ponderada3 = nota3 * 0.3
nota_presentacion = nota_ponderada1 + nota_ponderada2 + nota_ponderada3
print(f"El promedio de presentación final es: {nota_presentacion}")

# Calcular promedio final
notaET = input("Ingrese la nota del examen: ")
if notaET.isnumeric():
    notaET = round(float(notaET), 2)                             #Otra forma:   notaFinal = nota_presentacion*0.6 + notaET*0.4
    notaFinal = round(nota_presentacion * 0.6 + notaET * 0.4, 2) #              notaFinal = round(notaFinal, 2)
    print(f"\nEl promedio final es: {notaFinal}")
else:
    print("Debe ingresar un valor numérico")



#Ejercicio 2    |   Números pares
print("Identificar números pares e impares")
num = input("Ingrese un número: ")
num2 = input("Ingrese otro número: ")
num3 = input("Ingrese otro número: ")
contadorPar = 0
contadorImpar = 0

if num % 2 == 0:
    contadorPar+=1
    print("El número1 es par")
else:
    contadorImpar+=1
    print("El número1 es impar")

if num2 % 2 == 0:
    contadorPar+=1
    print("El número2 es par")
else:
    contadorImpar+=1
    print("El número2 es impar")

if num3 % 2 == 0:
    contadorPar+=1
    print("El número3 es par")
else:
    contadorImpar+=1
    print("El número3 es impar")

print(f"Se ingresaron {contadorPar} números pares.")
print(f"Se ingresaron {contadorImpar} números impares.")

suma = num + num2 + num3
if sum > 100 and sum % 2 == 0:
    print("La suma es mayor a 100")
    print("La suma es par")
else:
    print("La suma no es mayor a 100")
    print("La suma es impar")