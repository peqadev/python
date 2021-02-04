# Modificadores de cadenas

a =" Hello, World! "
print(a.upper())  # HELLO, WORLD!
print(a.lower())  # hello, world!
print(a.strip())  # Hello, World! (Elimina todos los espacios en blanco)
print(a.lstrip())  # Hello, World!  (Elimina los espacios en blanco a la izquierda) 
print(a.rstrip())  #  Hello, World! (Elimina los espacios en blanco a la derecha).
print(a.replace("H", "J"))  #  Jello, World! (Reemplaza todas las letras que encuentre)
print(a.strip().split(" "))  # ['Hello,', 'World!'] (Retorna una lista)
