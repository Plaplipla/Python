#Ejercicio 1    |   Ordenar los códigos para que el sistema muestre por consola el siguiente resultado:
#-----Detalle Anualidad Colegio-----
#Nombre alumno: Esteban Garcia
#Rut apoderado: 10743568-2
#Curso matriculado: 8C
#Valor matricula: 25000
#Valor mensualidad: 30000
#Valor total a pagar: 325000

rut = input("Ingrese RUT apoderado: ")
nomAlum = input("Ingrese nombre del alumno")
curso = input("Ingrese el curso al cual el alumno debe matricularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad*10)+matricula

print(f"-----Detalle Anualidad Colegio-----")
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRICULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")


#Ejercicio 2    |   Valor Neto de un Producto

producto = input ("Ingrese el nombre del producto: ")
valorProd = int(input("Ingrese el valor del producto: "))
valorNeto = float(0.81)
valorSinIVA = float(valorProd * valorNeto)

print(f"-----Detalle producto-----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProd}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIVA}")

#P: ¿Por qué se debe ocupar tipo de dato FLOAT para calcular el IVA?
#R: Los datos tipo FLOAT permiten calcular números con décimales, mientras que los datos tipo INT solo permiten calcular números enteros.

#Ejercicio 3    |   Determinar la secuencia generada x el siguiente programa:
num = 0
print(num)
next = 1
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
num = num + next
print(num)
next = num + next
print(next)
#R: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610
#Secuencia de Fibonacci como Lateralus de Tool