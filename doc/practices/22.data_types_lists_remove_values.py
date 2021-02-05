# Como agregar valores a una lista
a = ["manzana", "banana", "arándano",
     "manzana", "melón", "aguacate", "melocotón"]
# ['manzana', 'banana', 'arándano', 'manzana', 'melón', 'aguacate', 'melocotón']
print(a)

a.remove("manzana")
print(a)  # ['banana', 'arándano', 'manzana', 'melón', 'aguacate', 'melocotón']

a.pop()
print(a)  # ['banana', 'arándano', 'manzana', 'melón', 'aguacate']

a.pop(2)
print(a)  # ['banana', 'arándano', 'melón', 'aguacate']

index_to_delete = 3
a.pop(index_to_delete)
print(a)  # ['banana', 'arándano', 'melón']

# Hace lo mismo que: a.pop(0). El del también funciona con otros elementos.
del a[0]
print(a)  # ['arándano', 'melón']

a.clear()
print(a)  # [], límpia la lista.
