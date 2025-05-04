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