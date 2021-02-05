# Como cambiar los valores de una lista
a = ["manzana", "banana", "arándano", "mango", "melon", "kiwi"]
print(a)  # ['manzana', 'banana', 'arándano', 'mango', 'melon', 'kiwi']

a[0] = "melocotón"
# ['melocotón', 'banana', 'arándano', 'mango', 'melon', 'kiwi']
# Cambiamos el valor de 0 a "melocotón"
print(a)

a[1:3] = ["uva", "pera"]
# ['melocotón', 'uva', 'pera', 'mango', 'melon', 'kiwi']
# Cambiamos los valores de banana y arándano, por uva y pera.
print(a)

a[1:4] = ["coco"]
# ['melocotón', 'melón', 'melon', 'kiwi']
# Cambiamos los valores de las posiciones del 1-4 a que sea "coco".
# Se reemplaza las cualquier valor anterior.
print(a)

a.insert(0, "piña")
# ['piña', 'melocotón', 'coco', 'melon', 'kiwi']
# Agregamos "piña" en la primera posición
print(a)
