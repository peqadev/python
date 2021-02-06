# Verificar un número N es primo o no.
def is_prime(n):
    """
    Calcula si un número es primo o no.
    """
    if n > 1:
        for i in range(2, int(n / 2)):
            if n % i == 0:
                return False
        return True
    return False


if __name__ == "__main__":
    n = int(input("Introduzca el valor de N: "))
    print(f"El número {n} {'es' if is_prime(n) else 'no es'} primo.")
