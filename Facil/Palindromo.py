# Prueba de FreeCodeCamp (Acronimo)
"""
Es palíndromo

Animamos a los usuarios a introducir cinco palabras.
Después comprobamos cuáles son palabras palíndromas o no.

¿Qué es un palíndromo? Es una palabra que podemos leer
de la misma manera desde la izquierda a la derecha y viceversa.

Ejemplo:

    madam es palíndromo.
    También lo es malayalam.
    En el caso de  geeks no lo es.
"""


def main():
    texto = input("¿Que palabra quiere comprobar?: ")
    index = -1
    texto_reves = ""
    for t in texto:
        texto_reves += texto[index]
        index -= 1
    check = True
    for a in range(len(texto)):
        if texto[a] != texto_reves[a]:
            check = False
            break
    if not check:
        print(f"{texto} NO es un Palindromo")
    else:
        print(f"{texto} ES Palindromo!!!")


if __name__ == "__main__":
    main()
