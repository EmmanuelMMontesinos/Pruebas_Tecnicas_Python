# Prueba de FreeCodeCamp (Par o Impar)
"""
Lo primero que vamos a realizar es dar la bienvenida preguntando
un número entre 1 y 1000.

Cuando el usuario proporciona el número, comprobaremos si es par o impar
y después imprimimos el mensaje con el resultado.

Ejemplo:

    Mensaje que se muestra: ¿En qué número estás pensando?
    Entrada: 25
    Salida: ¡Es un número impar! ¿Puedes añadir otro?
"""

# Funcion que comprueba si el numero es Par o Impar


def es_Par(num):
    try:
        num = int(num)
        if num % 2 == 0:
            resultado = "Par"
        else:
            resultado = "Impar"

        return f"Python dice: {num} es {resultado}"
    # Si el dato no puede convertirse a entero
    except ValueError:
        return f"Error: {num} no es un numero"


# Controlador de Salida
salir = False
print("Bienvenido/a/e al comprobador de Numeros Par/Impar")
consulta = input("Ponga un numero para saber si es Par o Impar: ")
# Inicio del Bucle
while salir == False:
    resultado = es_Par(consulta)
    print(resultado)
    consulta = input("¿Quieres comprobar otro numero?(S para salir): ")
    if consulta.lower() == "s":
        salir = True
