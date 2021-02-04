import random
# Tipos de datos relacionados con números:
# - int
# - float
# - complex*

# Ejemplos de enteros
x = 100
print(type(x))
x = -100
print(type(x))
x = 0
print(type(x))

# Ejemplos de flotantes
x = 1.10
print(type(x))
x = -1.0
print(type(x))
x = 0.0
print(type(x))
x = 12e5
print(type(x))
x = -89.123e100
print(type(x))

# Ejemplos de complejos
x = 5j
print(type(x))
x = -100j
print(type(x))

# Ejemplos de casting de numeros
x = 1
y = 2.8
z = 100j

# convertir de entero a flotante
a = float(x)

# convertir de flotante a entero
b = int(y)

# convertir de entero a complejo
c = complex(x)

# Ejemplos de número pseudo-aleatorios
print(random.randrange(1, 20))
