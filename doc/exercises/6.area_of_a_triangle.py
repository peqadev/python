# Dados los lados de un triángulo, conseguir el área del mismo.
# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))
c = int(input("Introduzca el valor de c: "))

s = (a + b + c)/2  # Semiperímetro
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"El área del triángulo es: {area}")
