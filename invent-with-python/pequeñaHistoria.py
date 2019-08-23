import random
import time

def displayIntro():
    print('''Lagos, montañas, bosques, diferentes opciones para diferentes fines.
Tenés que elegir entre caminar por el lago o ir directo a la montaña.
La desición no es fácil.''')


print()


def choosePlace():
    place = ''
    while place != '1' and place != '2':
        print('Quieres ir a recorrer el lago o caminar hasta la montaña? (1 o 2)')
        place = input()
    return place


def checkPlace(placeNumber):
    print('Empezás a caminar...')
    time.sleep(2)
    print('Muy despacito, disfrutando el paisaje...')
    time.sleep(2)
    print('Sintiendo el viento..')
    time.sleep(2)
    print('Una nube negra y gigante se acerca...')
    time.sleep(2)

    climaRandom = random.randint(1, 2)

    if placeNumber == str(climaRandom):
        print('La nube pasa y nada sucede.')
    else:
        print('Llueve y te arruina la caminata.')


playAgain = 'si'
while playAgain == 'si' or playAgain == 'sí' or playAgain == 's':
    displayIntro()
    placeNumber = choosePlace()
    checkPlace(placeNumber)

    print('Querés jugar otra vez? (sí o no)')
    playAgain = input()
