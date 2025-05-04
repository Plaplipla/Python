codigo="salida"
intentos=3

print("Tienes 3 intentos para encontrar el código secreto")
print(f"La palabra tiene {len(codigo)} caracteres")
print("es el resultado de un proceso")

palabra_usuario=input("Ingrese la palabra que cree es la indicada: ")

if len(palabra_usuario)<=len(codigo) and palabra_usuario.isalpha:
    intentos-=1
    if palabra_usuario==codigo:
        print(f"Felicidades!!, encontraste la palabra {codigo}")
    else:
        print("Te equivocaste, aquí van algunas pistas")
        print("Es un concepto que indica los datos que salen del sistema al usuario")
        print(f"{codigo[0]} _ _ _ _ _")

        palabra_usuario=input("Ingrese la palabra que cree es la indicada: ")

        if len(palabra_usuario)<=len(codigo) and palabra_usuario.isalpha:
            intentos-=1
            if palabra_usuario==codigo:
                print(f"Felicidades!!, encontraste la palabra {codigo}")
            else:
                print("Te equivocaste, aquí van algunas pistas")
                print(f"{codigo[0]} _ _ _ _ {codigo[-1]}")
                palabra_usuario=input("Ingrese la palabra que cree es la indicada: ")

                if len(palabra_usuario)<=len(codigo) and palabra_usuario.isalpha:
                    intentos-=1
                    if palabra_usuario==codigo:
                        print(f"Felicidades!!, encontraste la palabra {codigo}")
                    else:
                        print("Te equivocaste, aquí van algunas pistas")
                        print(f"{codigo[0]} {codigo[1]} _ _ _ {codigo[-1]}")
                        
                        palabra_usuario=input("Ingrese la palabra que cree es la indicada: ")

                        if len(palabra_usuario)<=len(codigo) and palabra_usuario.isalpha:
                            intentos-=1
                            if palabra_usuario==codigo:
                                print(f"Felicidades!!, encontraste la palabra {codigo}")
                            else:
                                print("Lo sentimos. No pudiste adivinar la palabra")
                                print(f"la palabra secreta era {codigo}")
                                
                        else:
                            print("La palabra debe tener más de 6 caracteres y no contener números")
                            
        
        else:
            print("La palabra debe tener más de 6 caracteres y no contener números")
            
    
            #if intentos<=0 and len(palabra_usuario)!=len(codigo):
             #   print("Lo sentimos. No pudiste adivinar la palabra")
              #  print(f"la palabra secreta era {codigo}")

else:
    print("La palabra debe tener no más de 6 caracteres y no contener números")
    