#1 Mostrar por pantalla estos mensajes

print("Bienvenido al mundo de la programación")
nom = input("Para comenzar, ingresa tu nombre: ")

#2 Almacenar el nombre en una variable llamada "nom" y luego mostrar el mensaje de bienvenida usando print(f""). Debe imprimir el nombre ingresado por pantalla.

print(f"\nBienvenido {nom}")

#3 Ingreso de variables de tipo numérica Int (input()), solicitar x para resolver la ecuación y mostrar el resultado por pantalla
#Ecuación: f(x) = 3x^2 + 2x - 7

x = int(input("\nA continuación, ingresa un valor para x: "))
resultado = 3*x**2 + 2*x - 7
print(f"El resultado de la ecuación para x={x} es {resultado}")

#4 Consultar datos de personas y mostrarlos
print("\nPara finalizar, por favor ingrese sus datos personales")
nombre = input("Ingresa tu nombre: ")
rut = input("Ingresa tu rut: ")
correo = input("Ingresa tu correo: ")
telefono = input("Ingresa tu telefono: ")
print(f"\nCompruebe la información ingresada:\n NOMBRE:\t{nombre} \n RUT:\t\t{rut} \n CORREO:\t{correo} \n TELEFONO:\t{telefono}")