# Prueba de FreeCodeCamp (Contador de Palabras)
"""
Contador de palabras

Preguntamos al usuario en que está pensando.
Cuando se introduce la respuesta, realizará el conteo de palabras
en la sentencia e imprimimos en la salida el resultado.

Ejemplo:

    Pregunta: ¿En qué estás pensando?
    Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
    Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!

Para llevar esto a cabo, vamos a crear un fichero de texto y añadimos una unas frases, y
contamos cuántas palabras tiene y lo imprimimos.
"""

from pathlib import Path


def main():
    texto = input("¿En que esta pensando?\n")
    with open(f"{Path()}/Resultado_Contador.txt", "w+", encoding="utf-8") as archivo:
        # Abro/Creo el archivo txt con el nombre de "Resultado_Contador.txt" y simultaneamente imprimo por terminal
        letras = {}
        for l in texto.lower():
            # Contando los caracteres(Letras,Caracteres especiales y numeros)
            if l not in letras:
                letras[l] = 1
            else:
                letras[l] += 1
            # Guardamos en el archivo la cadena original
            archivo.write(l)
        archivo.write("\n")
        letras_total = 0
        caracteres = 0
        numeros_totales = 0
        for let, numero in letras.items():
            dato = let.isalnum()
            if dato:
                try:
                    if int(let):
                        numeros_totales += numero
                        print(f"{let} es un numero, ha aparecido: {numero}")
                        archivo.write(
                            f"{let} es un numero, ha aparecido: {numero}\n")
                except ValueError:
                    letras_total += numero
                    print(f"{let} es una letra, ha aparecido: {numero}")
                    archivo.write(
                        f"{let} es una letra, ha aparecido: {numero}\n")
            else:
                caracteres += numero
                print(f"{let} es un caracter, ha aparecido: {numero}")
                archivo.write(
                    f"{let} es un caracter, ha aparecido: {numero}\n")
        archivo.write(
            f"\nTotal {letras_total+caracteres+numeros_totales}\nLetras: {letras_total} Caracteres: {caracteres} Numeros: {numeros_totales}")
        print(
            f"\nTotal {letras_total+caracteres+numeros_totales}\nLetras: {letras_total} Caracteres: {caracteres} Numeros: {numeros_totales}")


if __name__ == "__main__":
    main()
