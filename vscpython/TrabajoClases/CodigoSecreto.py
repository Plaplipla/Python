# Configuración inicial
secretCode = "salida"
intentos_restantes = 3
longitudCode = len(secretCode)

# Pista inicial
pista_actual = "_" * longitudCode

# Interacción con el jugador
print("¡Bienvenido al juego 'Adivina el código secreto'!\n\n1.-\tTienes solo 3 intentos para descubrirlo.")
print(f"2.-\tEl código tiene {longitudCode} letras.")
#print(f"La palabra tiene {len(secretCode)} caracteres")
print("\n------Pista: Es el resultado de un proceso.------")

userword = input("\nIngrese la palabra que cree indicada: ")

# Validación de intento
if len(userword) <= len(secretCode) and userword.isalpha:
    intentos_restantes -= 1
    if userword == secretCode:
        print(f"\n¡Muy bien! Adivinaste el código secreto: {secretCode}\n")
    else:
        print("\nERROR. Es un concepto que indica los datos que salen del sistema al usuario.")
        print(f"\nAquí tienes una pista:\n {secretCode[0]}_ _ _ _ _")

        userword = input("\nIngrese la palabra que cree indicada: ")

        if len(userword) <= len(secretCode) and userword.isalpha:
            intentos_restantes -= 1
            if userword == secretCode:
                print(f"\n¡Muy bien! Adivinaste el código secreto: {secretCode}\n")
            else:
                print("\nERROR. Es un concepto que indica los datos que salen del sistema al usuario.")
                print(f"\nAquí tienes una pista:\n {secretCode[0]}_ _ _ _ {secretCode[-1]}")

                userword = input("\nIngrese la palabra que cree indicada: ")

                if len(userword) <= len(secretCode) and userword.isalpha:
                    intentos_restantes -= 1
                    if userword == secretCode:
                        print(f"\n¡Muy bien! Adivinaste el código secreto: {secretCode}\n")
                    else:
                        print("\nERROR. Es un concepto que indica los datos que salen del sistema al usuario.")
                        print(f"\nAquí tienes una pista:\n {secretCode[0]} {secretCode[1]} _ _ _ {secretCode[-1]}")

                        userword = input("\nIngrese la palabra que cree indicada: ")

                        if len(userword) <= len(secretCode) and userword.isalpha:
                            intentos_restantes -= 1
                            if userword == secretCode:
                                print(f"\n¡Muy bien! Adivinaste el código secreto: {secretCode}\n")
                            else:
                                print(f"\n¡Te has quedado sin intentos! El código secreto era: {secretCode}\n")
                        else:
                            print("\nLa palabra debe tener 6 caracteres y no debe contener números.\n")
        else:
            print("\nLa palabra debe tener más de 6 caracteres y no debe contener números.\n")

else:
    print("\nLa palabra debe tener 6 caracteres y no debe contener números.\n")










#------ [ ctrl + } ] Para comentar PY ------

# while intentos > 0:
#     print(f"\nPista actual: {pista_actual}")
#     print(f"Intentos restantes: {intentos}")
#     intento = input("Ingresa tu intento: ").upper()

#     #Validación del intento con isalpha() y len()
#     if not intento.isalpha() or len(intento) != longitudCode:
#         print("ERROR: Debes ingresar una palabra con el mismo número de letras que el código secreto y solo letras.")
#         intentos -= 1
#         continue
    
#     #Comparación con el código secreto
#     if intento == secretCode:
#         print(f"Muy bien! Adivinaste el código secreto: {secretCode}")
#         break
#     else:
#         #Generar pistas para el jugador x cada intento fallido
#         newTrack = ""
#.....