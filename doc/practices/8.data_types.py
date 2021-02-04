# Data types

x = "Hello World"
print(type(x))  # str

x = 20
print(type(x))  # int

x = 20.5
print(type(x))  # float

x = 1j
print(type(x))  # complex

x = ["manzana", "banana", "arándano"]
print(type(x))  # list (Mutable)

x = ("manzana", "banana", "arándano")
print(type(x))  # tuple (Inmutable)

x = range(6)  # [0, 1, 2, 3, 4, 5]
print(type(x))  # range

x = {
    "nombre": "Erick",
    "apellido": "Agrazal"
}
print(type(x))  # dict (Keyword: Value)

x = {"manzana", "banana", "arándona"}
print(type(x))  # set (No se repite)

x = True
print(type(x))  # bool (True / False)
