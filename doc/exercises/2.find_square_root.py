# Encontrar la raíz cuadrada de un número
import cmath


a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))

sq = a ** (0.5)
print(f"La raíz cuadrada de {a} es: {sq}")

sq = cmath.sqrt(b)
print(f"La raíz cuadrada de {b} es: {sq}")
