def calcular_beca(quintil, tiene_aporte):
    if quintil in [1, 2]:
        return 250000 if not tiene_aporte else 80000
    elif quintil == 3:
        return 150000 if not tiene_aporte else 70000
    else:
        return 0  # Quintiles 4 y 5 no tienen beca

# Solicitar datos al usuario
try:
    quintil = int(input("Ingrese su quintil (1 a 5): "))
    if quintil < 1 or quintil > 5:
        print("Error: El quintil debe estar entre 1 y 5.")
    else:
        aporte_input = input("¿Tiene aporte económico? (si/no): ").strip().lower()
        if aporte_input not in ["si", "no"]:
            print("Error: Debe ingresar 'si' o 'no'.")
        else:
            tiene_aporte = True if aporte_input == "si" else False
            monto_beca = calcular_beca(quintil, tiene_aporte)
            print(f"\nResultado:")
            print(f"Quintil: {quintil}")
            print(f"Tiene aporte: {'Sí' if tiene_aporte else 'No'}")
            print(f"Beca asignada: ${monto_beca}")
except ValueError:
    print("Error: Entrada no válida. Asegúrese de ingresar números enteros para el quintil.")

#segundo
try:
    quintil = int(input("Ingrese su quintil (1 a 5): "))
    
    if quintil < 1 or quintil > 5:
        print("Error: El quintil debe estar entre 1 y 5.")
    else:
        aporte_input = input("¿Tiene aporte económico? (si/no): ").strip().lower()
        
        if aporte_input not in ["si", "no"]:
            print("Error: Debe ingresar 'si' o 'no'.")
        else:
            tiene_aporte = True if aporte_input == "si" else False

            # Calcular monto de beca según condiciones
            if quintil in [1, 2]:
                if not tiene_aporte:
                    monto_beca = 250000
                else:
                    monto_beca = 80000
            elif quintil == 3:
                if not tiene_aporte:
                    monto_beca = 150000
                else:
                    monto_beca = 70000
            else:
                monto_beca = 0  # Para quintil 4 o 5

            # Mostrar resultado
            print(f"\nResultado:")
            print(f"Quintil: {quintil}")
            print(f"Tiene aporte: {'Sí' if tiene_aporte else 'No'}")
            print(f"Beca asignada: ${monto_beca}")

except ValueError:
    print("Error: Entrada no válida. Asegúrese de ingresar números enteros para el quintil.")

#tercero
while True:
    print("\n--- Sistema de Postulación a Becas ---")
    
    try:
        quintil = int(input("Ingrese su quintil (1 a 5): "))
        
        if quintil < 1 or quintil > 5:
            print("Error: El quintil debe estar entre 1 y 5.")
            continue

        aporte_input = input("¿Tiene aporte económico? (si/no): ").strip().lower()
        
        if aporte_input not in ["si", "no"]:
            print("Error: Debe ingresar 'si' o 'no'.")
            continue

        tiene_aporte = True if aporte_input == "si" else False

        # Calcular monto de beca según condiciones
        if quintil in [1, 2]:
            if not tiene_aporte:
                monto_beca = 250000
            else:
                monto_beca = 80000
        elif quintil == 3:
            if not tiene_aporte:
                monto_beca = 150000
            else:
                monto_beca = 70000
        else:
            monto_beca = 0  # Quintil 4 y 5 no tienen beca asignada

        # Mostrar resultado
        print("\n--- Resultado de Evaluación ---")
        print(f"Quintil: {quintil}")
        print(f"Tiene aporte: {'Sí' if tiene_aporte else 'No'}")
        print(f"Beca asignada: ${monto_beca}")

    except ValueError:
        print("Error: Entrada no válida. Asegúrese de ingresar un número entero para el quintil.")
        continue

    # Preguntar si desea evaluar a otro estudiante
    seguir = input("\n¿Desea evaluar otro estudiante? (si/no): ").strip().lower()
    if seguir != "si":
        print("\nGracias por usar el sistema de becas. ¡Hasta luego!")
        break
