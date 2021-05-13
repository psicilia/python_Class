import random

salir = "si"

while salir == "si":
    userChoise = input("elige, piedra papel o tijeras: ")
    posibilidades = ["piedra", "papel", "tijeras"]

    computadora = random.choice(posibilidades)

    print(f"El usuario eligio {userChoise} \n la computadora eligio {computadora}")

    if userChoise == computadora:
        print("es un empate!!!")

    elif userChoise == "piedra":

        if computadora == "papel":
            print(f"{computadora} gana a {userChoise} gano la computadora")
        else:
            print(f"{userChoise} gana a {computadora} ganaste!")

    elif userChoise == "papel":

        if computadora == "tijeras":
            print(f"{computadora} gana a {userChoise} gano la computadora")
        else:
            print(f"{userChoise} gana a {computadora} ganaste!")
    elif userChoise == "tijeras":

        if computadora == "piedra":
            print(f"{computadora} gana a {userChoise} gano la computadora")
        else:
            print(f"{userChoise} gana a {computadora} ganaste!")
    salir = input("quieres jugar de nuevo? si, no: ")