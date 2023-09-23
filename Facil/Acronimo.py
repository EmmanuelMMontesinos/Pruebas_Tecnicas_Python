# Prueba de FreeCodeCamp (Acronimo)
"""
¿Cuál es mi acrónimo?

Vamos a pedir al usuario que ingrese el significado completo de una organización
o concepto y con ello como resultado obtendremos el acrónimo. Por ejemplo:

    Entrada -> As Soon As Possible. Salida -> ASAP.
    Entrada -> World Health Organization. Salida -> WHO.
    Entrada -> Absent Without Leave. Salida -> AWOL.
"""


def main():
    texto = input("Pon un nombre para sacar su acronimo: ")
    final = ""
    acronimo = [l[0] for l in texto.title().split() if l.lower()]
    for l in acronimo:
        final += l
    print(f"Tu acronimo para {texto.title()} es: {final}")


if __name__ == "__main__":
    main()
