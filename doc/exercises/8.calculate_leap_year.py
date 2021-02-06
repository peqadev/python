# Calcular si un año N es bisiesto o no.
# Año bisiesto: es el divisible entre 4,
# salvo que sea año secular -último de cada
# siglo, terminado en «00»-, en cuyo caso
# también ha de ser divisible entre 400.

def validate_leap_year(year):
    """
    Ejemplo de docstring:
    Esta es una función que calcula si un 
    año es bisiesto o no.
    """
    if (year % 4) == 0:
        if (year % 100) == 0:
            # if (year % 400) == 0:
            #     return True
            # else:
            #     return False
            return (year % 400) == 0
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    year = int(input("Introduzca el año: "))
    is_leap_year = validate_leap_year(year)
    print(f"El año {year} {'es' if is_leap_year else 'no es'} bisiesto.")
