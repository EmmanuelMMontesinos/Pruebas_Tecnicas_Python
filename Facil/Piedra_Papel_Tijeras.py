# Prueba de FreeCodeCamp (Acronimo)
"""
Rock, Paper, Tijeras

Es un popular juego para dos jugadores. Cualquier jugador puede ejecutar una
jugada con sus manos con estas opciones que tenemos disponible  a continuación:

    piedra (puño cerrado)
    papel (mano plana)
    tijeras (un puño con el dedo índice y el dedo medio extendidos, formando una V)
"""
from random import choice


def main():
    piedra = "🗿"
    papel = "📃"
    tijera = "✂️"
    elementos = [piedra, papel, tijera]
    salir = False
    while salir == False:
        jugada = input(
            f"\nElije tirada (PIEDRA{piedra}, PAPEL{papel}, TIJERA{tijera} )\nSalir para cerrar\n")
        if jugada.lower() == "piedra":
            jugada = piedra
        elif jugada.lower() == "papel":
            jugada = papel
        elif jugada.lower() == "tijera":
            jugada = tijera
        if jugada.lower() == "salir":
            salir = True
            break

        cpu = choice(elementos)
        if jugada != cpu:
            if jugada == piedra:
                if cpu == tijera:
                    print(f"Has GANADO! Tu - {jugada} vence a CPU - {cpu}")
                else:
                    print(f"Has PERDIDO! CPU - {cpu} vence a Tu - {jugada}")
            elif jugada == papel:
                if cpu == piedra:
                    print(f"Has GANADO! Tu - {jugada} vence a CPU - {cpu}")
                else:
                    print(f"Has PERDIDO! CPU - {cpu} vence a Tu - {jugada}")
            else:
                if cpu == papel:
                    print(f"Has GANADO! Tu - {jugada} vence a CPU - {cpu}")
                else:
                    print(f"Has PERDIDO! CPU - {cpu} vence a Tu - {jugada}")
        elif jugada == cpu:
            print(f"Habeis Empatado!! {jugada} es igual que {cpu}")


if __name__ == "__main__":
    main()
