# Concatenación
a = "Erick"
b = "Agrazal"

# Todas estas salidas generan el mismo resultado: Erick Agrazal
print(a + " " + b)
print(f"{a} {b}") # String interpolation
print("%s %s" % (a, b))
print("{} {}".format(a, b))
print("{1} {0}".format(a, b))