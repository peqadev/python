# Acceso a listas
a = ["manzana", "banana", "arándano", "mango", "melon", "kiwi"]

# "manzana", acceder usando índices
print(a[0])

# "kiwi", si es negativo, empieza a contar en el final. El -1 es el último elemento.
print(a[-1])

# ['banana', 'arándano'], para leer un segmento, se lee usando
# arreglo[inicio:fin]. La posición "inicio", es considerada en la
# lista de salida, la de "fin", no.
print(a[1:3])

# ['manzana', 'banana', 'arándano'], para leer desde el inicio
# hasta la posición 3.
print(a[:3])

# ['melon', 'kiwi'], para leer desde la posición 4 hasta el
# final de la lista
print(a[4:])

# Buscar "bananas" en el arreglo "a".
if "bananas" in a:
    print("Existen bananas en a")
else:
    print("No existen bananas en a")
