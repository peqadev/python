# Dado un cadena, calcular la cantidad de cada letra que hay en la cadena.
# cadena: aabbbaabb
# a: 4
# b: 5

# estudiante = {
#     "nombre": {
#         "primer_nombre": "Erick",
#         "apellido": "Agrazal"
#     },
#     "edad": 29,
#     "materias": ["matematicas", "español", ]
# }
# print(estudiante.get("nombre"))
# print(estudiante["edad"])
# print(estudiante["materias"])
# try:
#     print(estudiante["no_existe"])
# except Exception:
#     print("Hubo un error")
# print(estudiante.get("no_existe"))


def get_character_count(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


if __name__ == "__main__":
    s = input("Introduzca la cadena: ")
    character_count = get_character_count(s)
    keys = character_count.keys()
    values = character_count.values()
    print(f"Las llaves del diccionario son: {keys}")
    print(f"Los valores del diccionario son: {values}")
    for k, v in character_count.items():
        print(f"El caracter {k} apareció {v} veces.")
