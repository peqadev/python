# List Comprehension
frutas_a = ["manzana", "banana", "arándano"]
frutas_b = []

for fruta in frutas_a:
    if "b" in fruta:
        frutas_b.append(fruta)

print(frutas_b)  # ['banana']

# [expression for item in iterable if condition == True]
# Mismo comportamiento que el for anterior pero con
# list comprehension.
frutas_c = [fruta for fruta in frutas_a if "b" in fruta]
print(frutas_c)  # ['banana']
frutas_d = [fruta for fruta in frutas_a if "arándano" == fruta]
print(frutas_d)  # ['arándano']
frutas_e = [fruta for fruta in frutas_a if "b" not in fruta]
print(frutas_e)  # ['manzana', 'arándano']

arr = [x for x in range(10)]
print(arr)

# Arreglo que tenga los números pares del 0-99
arr = [x for x in range(100) if x % 2 == 0]
print(arr)

# Todos los elementos del arreglo en mayúsculas
arr = [fruta.upper() for fruta in frutas_a]
print(arr)

# Crear arreglo nuevo del mismo tamaño de frutas_a
# con todos los valores como 1
arr = [1 for fruta in frutas_a]
print(arr)

# List comprehension con if y else al mismo tiempo.
arr = [True if "b" in fruta else False for fruta in frutas_a]
# ^^^^^^^^ El list comprehension de arriba, hace lo mismo
# que el siguiente "for":
# for fruta in frutas_a:
#     if b in frutas_a:
#         arr.append(True)
#     else:
#         arr.append(False)
print(arr)
