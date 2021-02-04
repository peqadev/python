# Cadenas / strings
print("Hello \" world")
print('Hello \' world')

# Asignación de cadena de una línea
a = "Hello"
print(a)

# Asignación de cadena multilinea
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Cadenas como arreglos
a = "hello world"
print(a[0])  # h
print(a[1])  # e
print(a[2])  # l

# Iterar sobre cadena
for x in "banana":
    print(x)

# Tamaño de una cadena
a = "Hello World"
print(len(a))  # 11


# Verificar cadenas
txt = "El nombre del profesor es: Erick Agrazal"
print("Erick" in txt)  # True
print("Lopez" in txt)  # False
print("Lopez" not in txt)  # True
profesor = "Erick"
if profesor in txt:
    print(f"{profesor} es el profesor.")
else:
    print(f"{profesor} no es el profesor.")
