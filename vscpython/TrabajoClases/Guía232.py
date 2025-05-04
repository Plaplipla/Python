#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad > 0 and edad < 18:
    print(f"Edad: {edad}, tiene descuento de un 50%")
elif edad >= 18 and edad < 30:
    print(f"Edad: {edad}, tiene descuento de un 20%")
elif edad >= 60:
    print(f"Edad: {edad}, tiene descuento de un 90%")
else:
    print(f"Edad: {edad}, no aplica descuento")

#Feedback: Los códigos en programación deben siempre considerar el orden de:
#   Entrada -> Proceso -> Salida

#En Python y cualquier otro lenguaje de prog debemos programar en el orden:
#       1.- Solicitar datos de entrada
#       2.- Procesar la información (ej: operaciones aritméticas, sentencias de lógica
#       3.- Mostrar datos de salida

#Ejercicio 2    |   Falta una sentencia

#Validación user y pass
user = input("Ingrese su user")
pwd = input("Ingrese su pass")

if user == "admin" and pwd =="admin123":
    print("Bienvenido")
else:
    print("Error en contraseña")
#Feedback: Cuando debemos validar accesos, es muy relevante que las igualdades consideren como obligatorio solicitar todos los datos, esto se consigue con la cláusula "and", que valida que ambas variables (user y pass) sean verdaderas.
