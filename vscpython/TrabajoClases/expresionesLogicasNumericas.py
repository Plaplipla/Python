from typing import Match

print("------Bienvenido al restaurante------\n")

print("1.- Porotos con riendas")
print("2.- Seitan con papas")
print("3.- Verduras salteadas")
opcion = input("Ingrese la opción que desea: ")

match opcion:
    case "1":
        print("Servir porotos con riendas")
    case "2":
        print("Servir seitan con papas")
    case "3":
        print("Servir verduras salteadas")
    case _:
        print("No tenemos esa opción en el menú")

