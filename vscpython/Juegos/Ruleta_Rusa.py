from random import *
Jugador = str(input("Ingresa tu nombre: "))
print("Bienvenido ", Jugador," Has ingresado al juego de la\n=========Ruleta Rusa========")
jugar = input("====¿Desea jugar?====")

if jugar == "No" or jugar == "no":
    print("...Cobarde")

else:
    partida = True
    while partida == True:  
        print(" ")
        print("...")
        print(" ")
        Cantidad_Balas = int(input("===¿Cuantas balas desea insertar?:"))       
        print("...")
        print(" ")
        Bala = 1
        while Bala <= Cantidad_Balas and partida == True:
            apretar = (input("===Apriete el gatillo (Ingrese cualquier tecla)==="))
            print(" ")
            Disparo = (randint(1, 2))
            print(" ")
           
            if Disparo == 1 and Bala <= Cantidad_Balas:
                print("Numero de Bala: ", Bala, " Suerte")
                print(" ")
                print(" ")
                print("La bala era falsa")
                print(" ")
                if Bala < Cantidad_Balas:
                    print(" Felicidades ", Jugador, " sigue jugando... Por ahora")
                Bala = Bala + 1 

            if Disparo == 2:
                print("Numero de Bala: ", Bala," Suerte")
                print("La bala estaba cargada")
                print(" ")
                print(" -Disparo- ")   
                print("::::::::::::::::::::::::::::::::::::::", Jugador," Usted Falleció:::::::::::::::::::::::::::::::::::")
                partida = False
                
        if Bala > Cantidad_Balas:
            print("Ha superado todas las balas")
            Bala = Bala-1
            print("Numero de balas superadas: (", Bala, ")")
            print(" ===Felicidades", Jugador,"ha ganado la ruleta===")
            print(" ")
            print(" ")
            
        Jugar_Nuevamente = (input("¿Desea volver a jugar?: "))
        if Jugar_Nuevamente == "No" or Jugar_Nuevamente == "no":
            Partida = False
            print(" ")
            print("Nos vemos a la próxima", Jugador)
            print(" ")
            break
        else:
            partida = True