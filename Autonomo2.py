import random
import math

def main():
    print("Ingresa tu opción: piedra, papel o tijera")
    jugador = input().lower()  # lee la opción del jugador

    # Genera un número aleatorio entre 1 y 3
    pc = math.floor(random.random() * 3) + 1

    # Traducción de número a opción
    if pc == 1:
        pc_opcion = "piedra"
    elif pc == 2:
        pc_opcion = "papel"
    else:
        pc_opcion = "tijera"

    print(f"La computadora eligió: {pc_opcion}")

    # Comparaciones
    if jugador == "piedra":
        if pc == 1:
            print("Empate")
        elif pc == 2:
            print("Perdiste")
        elif pc == 3:
            print("Ganaste")

    elif jugador == "papel":
        if pc == 1:
            print("Ganaste")
        elif pc == 2:
            print("Empate")
        elif pc == 3:
            print("Perdiste")

    elif jugador == "tijera":
        if pc == 1:
            print("Perdiste")
        elif pc == 2:
            print("Ganaste")
        elif pc == 3:
            print("Empate")

    else:
        print("Opción inválida, escribe piedra, papel o tijera.")

# Llamamos a la función principal
main()
