# Prueba de FreeCodeCamp (Adivina numero oculto)
"""
Adivina el número oculto

Debemos de preguntar al usuario un número entre 1 y 50.

Si añaden un número fuera de ese rango, vamos a indicar con un error que anime
a elegir un número dentro del rango adecuado..

Si no acertamos el número oculto, preguntaremos al usuario si queremos seguir jugando,
introduciendo un nuevo número o queremos dejar de jugar.

Finalmente, cuando el usuario acierta correctamente el número oculto,
mostramos un mensaje de enhorabuena y mostramos el número de intentos
que hemos utilizado para llegar a esta situación.
"""
from random import randint


def solucion(num):
    numero = randint(1, num)
    respuesta = input("Que numero crees que es?: ")
    while True:
        try:
            respuesta = int(respuesta)
        except ValueError:
            print(f"{respuesta} no es un numero")
        else:
            if respuesta == numero:
                print(f"Has Acertado el numero era {numero}")
                return True
            else:
                print(
                    f"No, {respuesta} no es el numero. Pulse S para salir u otro numero para continuar")
                salir = input("")
                if salir.lower() == "s":
                    print(f"El numero era {numero}")
                    return False
                if salir.isnumeric():
                    respuesta = salir


def main():
    print("Bienvenido a Adivina el Numero, indica la dificultad (A-10 Nº,B-25 Nº,C-50 Nº)\nS para salir")
    salir = False
    while salir == False:
        dificultad = input("")
        if dificultad.lower() == "a":
            salir = solucion(10)
        elif dificultad.lower() == "b":
            salir = solucion(25)
        elif dificultad.lower() == "c":
            salir = solucion(50)
        if salir:
            break
        if dificultad.lower() == "s":
            salir = True
        else:
            print(f"{dificultad} no es una opcion valida (A, B o C) o S para cerrar")


if __name__ == "__main__":
    main()
