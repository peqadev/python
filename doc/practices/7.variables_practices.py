# Prácticas de variables

# 1. Crea una variable llamada nombre del carro y asígnale el valor Volvo.
nombre_del_carro = "Volvo"

# 2. Crea una variable llamada x y asígnale el valor 50.
x = 50

# 3. Muestra la suma de 5 + 10, utilizando dos variables: x e y.
x, y = 5, 10
print(x + y)

# 4. Crea una variable llamada z, asígnale x + y y muestra el resultado.
z = x + y
print(z)

# 5. Elimina los caracteres ilegales en el nombre de la variable:
# 2mi-nombre = "Juan"
mi_nombre = "Juan"

# 6. Inserta la palabra clave correcta para que la variable x pertenezca al ámbito global.
# x = ""
# def mi_funcion():
#     x = "Fantástico"
x = ""


def mi_funcion():
    global x
    x = "Fantástico"
    print(x)


print(x)
