import random
import math


def jugar():
    frases_perder = [
        "Perdiste, para la próxima bb",
        "Perdiste, sigue participando",
        "Ya nada, para otra será",
        "¿Qué pashó papu? perdiste"
    ]

    frases_ganar = [
        "Ganaste. ¡Qué pro, sigue así!",
        "Ganaste, eres el admin, no un NPC",
        "Ganaste, eres la mera verdura",
        "Levanta la cabeza, princese, acabas de ganar"
    ]

    frases_empate = [
        "Empate… parece que compartimos la misma neurona",
        "Empate. Claramente nacimos del mismo meme",
        "Empate bestie, el algoritmo no estaba preparado para esto"
    ]

    print("\nIngresa tu opción: piedra, papel o tijera")
    jugador = input().lower()

    opciones = ["piedra", "papel", "tijera"]

    if jugador not in opciones:
        print("Opción inválida, escribe piedra, papel o tijera.")
        return "invalido"

    pc = random.choice(opciones)
    print(f"La computadora eligió: {pc}")

    if jugador == pc:
        print(random.choice(frases_empate))
        return "empate"
    elif (jugador == "piedra" and pc == "tijera") or \
         (jugador == "papel" and pc == "piedra") or \
         (jugador == "tijera" and pc == "papel"):
        print(random.choice(frases_ganar))
        return "gano"
    else:
        print(random.choice(frases_perder))
        return "perdio"

def main():
    while True:
        resultado = jugar()

        # Si gana, sigue jugando automáticamente
        if resultado == "gano":
            continue

        # Si empata o pierde, pregunta si desea seguir
        if resultado in ["empate", "perdio"]:
            print("\n¿Quieres jugar de nuevo? (sí/no)")
            respuesta = input().lower()
            if respuesta not in ["si", "sí"]:
                print("Gracias por jugar. ¡Hasta luego!")
                break

        # Si puso una opción inválida, también pregunta si seguir
        if resultado == "invalido":
            print("\n¿Quieres intentar de nuevo? (sí/no)")
            respuesta = input().lower()
            if respuesta not in ["si", "sí"]:
                print("Gracias por jugar. ¡Hasta luego!")
                break

# Iniciar el juego
main()
