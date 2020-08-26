from sys import exit

def gold_room():
    print("Aquí hay mucho oro: ")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Algo misterioso sobre números.")

    if how_much < 50:
        print("Nice, ganaste algo!")
        exit(0)
    else:
        dead("Màs funcione smisteriosas.")

def bear_room():
    print("Texto + texto")
    print("Opcion 1 o 2.")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "1":
            dead("Moriste.")
        elif choice == "2" and not bear_moved:
            print("Zafaste.")
            bear_moved = True
        elif choice == "2" and bear_moved:
            dead("Moriste de alguna forma")
        elif choice == "3" and bear_moved:
            gold_room()
        else:
            print("No te entiendo.")


def cthulhu_room():
    print("Otra habitación.")
    print("Más opciones. 3 o 4")

    choice = input("> ")

    if "3" in choice:
        start()
    elif "4" in choice:
        dead("Dead.")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("Vas a la left o right?")
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("Moriste.")


start()