# Dada un número, imprimir la tabla de multiplicación de ese número.
# Ejemplo:
# N = 10
# 10 x 1 = 10
# 10 x 2 = 20
# ...
# 10 x 10 = 100
n = int(input("Introduzca el valor de N: "))

# Primera solución
print('Primera solución')
for i in range(1, 10 + 1):
    print(f"{n} X {i} = {n * i}")

# Segunda solución
print('Segunda solución')
[print(f"{n} X {i} = {n * i}") for i in range(1, 10 + 1)]
