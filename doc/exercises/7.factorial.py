# Calcular el factorial de un número N.
# 5! = 1 x 2 x 3 x 4 x 5 = 120
n = int(input("Introduzca el valor de N: "))

factorial = 1
if n < 0:
    print(f"No existe factorial para el valor {n}.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es {factorial}.")
