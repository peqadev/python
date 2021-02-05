# Como agregar valores a una lista
a = ["manzana", "banana", "arándano", ]
print(a)  # ['manzana', 'banana', 'arándano', ]

a.append("melón")
print(a)  # ['manzana', 'banana', 'arándano', 'melón']

a.insert(0, "piña")
print(a)  # ['piña', 'manzana', 'banana', 'arándano', 'melón']

b = [1, 2]
a.extend(b)
print(a)  # ['piña', 'manzana', 'banana', 'arándano', 'melón', 1, 2]

c = (3, 4)
a.extend(c)
print(a)  # ['piña', 'manzana', 'banana', 'arándano', 'melón', 1, 2, 3, 4]
