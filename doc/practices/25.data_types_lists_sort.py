# Ordenamiento
frutas_a = ["Manzana", "banana", "arándano", ]
frutas_a.sort()  # Ordena de menor a mayor (A-Z)
print(frutas_a)  # ['Manzana', 'arándano', 'banana']

numeros = [1, 2, 4, 100, 3, 5]
numeros.sort()  # Ordena de menora  mayor (1-N)
print(numeros)  # [1, 2, 3, 4, 5, 100]

frutas_a.sort(reverse=True)  # Ordena de mayor a menor (Z-A)
print(frutas_a)  # ['banana', 'arándano', 'Manzana']
numeros.sort(reverse=True)  # Ordena de mayor a menor (N-1)
print(numeros)  # [100, 5, 4, 3, 2, 1]

arr = [10, 20, 30, 100, 10]
arr.reverse()  # Voltea la lista sin tomar en cuenta el orden.
print(arr)  # [10, 100, 30, 20, 10]
