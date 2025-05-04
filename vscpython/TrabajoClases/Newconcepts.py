#------Conceptos Resumidos------

# Deciles: Dividen un conjunto de datos ordenados en 10 partes iguales. Cada parte = 10%.

# Percentiles: Dividen los datos en 100 partes iguales. Cada percentil representa 1%.

# Quintiles: Dividen los datos en 5 partes iguales. Cada parte representa el 20%.

# Random: Datos aleatorios (números, listas, elecciones, mezclas, etc.). randint(), randrange() y rand()

import numpy as np # type: ignore #
import random

# Crear datos de ejemplo
# random.randint(a, b) genera un número entero aleatorio entre a y b.
datos = [random.randint(1, 100) for _ in range(20)]
print("Datos:", datos)

# np.percentile es la función que permite calcular cualquier percentil (y por extensión decil y quintil).

# Deciles
d1 = np.percentile(datos, 10)
d9 = np.percentile(datos, 90)
#Los deciles serían percentiles múltiplos de 10 (10, 20, ..., 90).

# Percentiles
p25 = np.percentile(datos, 25)
p50 = np.percentile(datos, 50)  # Mediana
p75 = np.percentile(datos, 75)
#Percentiles: Dividen en 100 partes. | muy preciso.

# Quintiles
q1 = np.percentile(datos, 20)
q2 = np.percentile(datos, 40)
q3 = np.percentile(datos, 60)
q4 = np.percentile(datos, 80)
# Los quintiles serían percentiles múltiplos de 20 (20, 40, 60, 80).

print(f"Decil 1 (10%): {d1}, Decil 9 (90%): {d9}")
print(f"Percentil 25: {p25}, 50 (mediana): {p50}, 75: {p75}")
print(f"Quintil 1 (20%): {q1}, Quintil 2 (40%): {q2}, Quintil 3 (60%): {q3}, Quintil 4 (80%): {q4}")