# Copiar listas

# Si hacemos asignación directa, se asocian las referencias
# de memoria, y si cambia uno, el otro también cambia.
a = [1, 2]
b = a
a.append(3)
b.append(4)
print(a)  # [1, 2, 3, 4], ambos cambiaron...
print(b)  # [1, 2, 3, 4], ambos cambiaron...

# Para evitar ese comportamiento, lo que hacemos es
# copiar los valores del arreglo original. Para eso
# podemos hacer una de las siguientes técnicas.
c = [1, 2, ]
d = c.copy()
e = [num for num in c]
f = list(c)
c.append(3)
# [1, 2, 3], Sólo este arreglo cambió. Los demás quedaron con los valores originales.
print(c)
print(d)  # [1, 2]
print(e)  # [1, 2]
print(f)  # [1, 2]
