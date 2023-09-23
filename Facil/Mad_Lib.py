# Prueba de FreeCodeCamp (Mad Lib)
"""
Juego del Mad Lib

Pedimos al usuario que introduzca varias entradas con varias preguntas.

Puede ser cualquier cosa, como un nombre, un adjetivo, un pronombre o
incluso una acción. Una vez que se obtiene la entrada,
se puede reorganizar para construir su propia historia.
"""


def historia(nombre, adjetivo, pronombre, accion, objeto):
    return f"{nombre} se levanto por la mañana un poco {adjetivo}.\n{pronombre} intento {accion} un {objeto} con catastofricas consecuencias"


def entrada():
    nombre = input("Un Nombre: ")
    adjetivo = input("Un Adjetivo: ")
    pronombre = input("Un pronombre(El,Ella,Elle): ")
    accion = input("Una accion: ")
    objeto = input("Un Objeto: ")
    c_historia = historia(nombre,
                          adjetivo,
                          pronombre,
                          accion,
                          objeto)
    print(c_historia)
    bucle = input("Quiere generar otra (Si/No): ")
    return bucle


def main():
    print("Bienvenido a Mad Lib, customiza tu historia.")
    salir = False
    while salir == False:
        check = entrada()
        if check.lower() == "no":
            salir = True


if __name__ == "__main__":
    main()
