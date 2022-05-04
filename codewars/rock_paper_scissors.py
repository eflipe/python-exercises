import random, sys
print("Bienvenidos al juego 'Piedra, Papel y Tijera'")

wins = 0
losses = 0
ties = 0

while True: # The main game loop
    forma_table = ('{} Wins, {} Losses, {} Ties').format(wins, losses, ties)
    print(forma_table)
    while True: # The player input loop
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # Break out of the player input loop
        print("Type one of r, p, s or q.")
    # Display what the player chose
    if player_move == 'r':
        print("ROCK versus...")
    elif player_move == 'p':
        print("PAPER versus...")
    elif player_move == 's':
        print("SCISSORS versus...")
    # Display what the computer chose:
    random_numer = random.randint(1, 3)
    if random_numer == 1:
        computer_move = 'r'
        print('ROCK')
    if random_numer == 2:
        computer_move = 'p'
        print('PAPER')
    if random_numer == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/ties
    if player_move == computer_move:
        print("It is a tie!")
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print("You win!")
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print("You win!")
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print("You win!")
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
