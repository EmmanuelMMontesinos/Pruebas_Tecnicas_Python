# Prueba de FreeCodeCamp (Info Bio)
"""
Información de la biografía

Pregunte a un usuario su información personal en una sola ronda de preguntas.
Luego hay que verificar que la información que se ha ingresado sea válida.
Finalmente, se imprime un resumen de toda la información que ha sido ingresada.

Por ejemplo: ¿Cuál es su nombre? Si el usuario ingresa *, hay que indicar que la entrada
es incorrecta y se pide que se ingrese correctamente un nombre válido.

Cuando se introduce todo correctamente, se muestra un resumen
"""


def main():
    checks = {"check_nombre": False,
              "check_nacimiento": False}
    nombre = input("Cual es tu nombre: ")
    if nombre.isalpha():
        checks["check_nombre"] = True
    nacimiento = input("Fecha de Nacimiento (dd/mm/yyyy): ")
    try:
        dia, mes, año = nacimiento.split("/")
        if int(dia) < 31 and int(dia) > 0:
            if int(mes) < 12 and int(mes) > 0:
                if int(año) < 2023 and int(año) > 1910:
                    checks["check_nacimiento"] = True
    except:
        pass
    dire = input("Dirirecion: ")
    text = input("Ponga una frase que le represente: ")
    for llave, valor in checks.items():
        if valor == False:
            print(f"Introduzca los elementos adecuados: {llave[6:]}")
            check_general = False
            break
        else:
            check_general = True
    if check_general == True:
        print(
            f"---\n\n\nNombre: {nombre}\nFecha Nacimineto: {dia}/{mes}/{año}\nDirección: {dire}\nFrase: {text}")


if __name__ == "__main__":
    main()
