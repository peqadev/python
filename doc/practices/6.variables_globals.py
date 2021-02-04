# Uso básico de las variables globales
x = "El COVID-19"


def mi_funcion():
    print("El valor de x es: " + x)


mi_funcion()


# Modificación de variable global
x = "El COVID-19"


def mi_funcion():
    x = "123"
    print("El valor de x es: " + x)


mi_funcion()
print("El valor de x es: " + x)


# Uso de globals, para modificar la variable global
x = "El COVID-19"


def mi_funcion():
    global x
    x = "123"
    print("El valor de x es: " + x)


mi_funcion()
print("El valor de x es: " + x)
