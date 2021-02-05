# Practica

# 1. Imprime el segundo elemento de la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
print(frutas[1])  # banana

# 2. Cambia el valor de "manzana" a "kiwi", en la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
frutas[0] = "kiwi"
print(frutas)  # ['kiwi', 'banana', 'arándano']

# 3. Utiliza el método append para añadir "naranja" a la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
frutas.append("naranjas")
print(frutas)  # ['manzana', 'banana', 'arándano', 'naranjas']

# 4. Utiliza el método insert para añadir "limón" como segundo elemento de la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
frutas.insert(1, "limón")
print(frutas)  # ['manzana', 'limón', 'banana', 'arándano']

# 5. Utiliza el método remove para eliminar "banana" de la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
frutas.remove("banana")
print(frutas)  # ['manzana', 'arándano']

# 6. Utiliza la indexación negativa para imprimir el último elemento de la lista de frutas.
frutas = ["manzana", "banana", "arándano", ]
print(frutas[-1])  # arándano

# 7. Utilice un rango de índices para imprimir el tercer, cuarto y quinto elemento de la lista.
num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(num[2:5])  # [2, 3, 4]

# 8. Imprima la lista usando "list comprehension"
num = [0, 1, 2, 3, 4, 5]
[print(x) for x in num]
# 0
# 1
# 2
# 3
# 4
# 5
