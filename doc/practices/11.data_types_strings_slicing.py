# String Slicing
b = "Hello World"
#    012345...
print(b[2:5])  # llo
print(b[:5])  # hello
print(b[2:])  # llo World
print(b[-1])  # d
print(b[-5:-2])  # Wor
print(b[::-1])  # dlroW olleH
c = "oso"
print(c == c[::-1])  # True (Palindromo)