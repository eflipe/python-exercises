import random

intentos = 0
print('Bienvenido!, cuál es tu nombre?')
playerName = input()

secretNum = random.randint(1, 20)
print(secretNum)

print('Hola, ' + playerName + '. Estoy pensado un número entre 1 y 20, intentan adivinarlo')

for intentos in range(6):
    print('Intento #', intentos+1)
    guess = input()
    guess = int(guess)

    if guess < secretNum:
        print('Tu número es muy bajo.')

    if guess > secretNum:
        print('Tu número es muy alto.')

    if guess == secretNum:
        break

if guess == secretNum:
    intentos = str(intentos + 1)
    print('Maravilloso, ' + playerName + ', adivinaste el número en ' + intentos + ' intentos!'
          '. El número era', secretNum)

if guess != secretNum:
    secretNum = str(secretNum)
    print('Lo siento, el número correcto era: ' + secretNum + '.')
