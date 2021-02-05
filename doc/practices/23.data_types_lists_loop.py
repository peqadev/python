# Iterar sobre listas
a = ["manzana", "banana", "arándano"]

for fruta in a:
    print(fruta)

for i in range(len(a)):
    # Impresión leyendo índices
    print(a[i])

i = 0
while(i < len(a)):
    # Impresión leyendo índices
    print(a[i])
    i += 1

# List comprehension
[print(fruta) for fruta in a]  # Mismos resultados que los de arriba
[print(a[i]) for i in range(len(a))]  # Mismos resultados que los de arriba
