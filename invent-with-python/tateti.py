import random


def drawBoard(board):
    '''Esta función imprime el board.
    'board' es una lista de 10 str que representa
    el board.
    Ej: drawBoard([' ', ' ', ' ', ' ', 'X', 'O', ' ', 'X', ' ', 'O'])
    '''
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    '''
    Devuelve una lista con la elección del jugador en el primer item y
    la de la computadora en el segundo item.
    '''
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Querés jugar como X o O')
        letter = input().upper()
    '''
    El primer elemento en la lista es la elecci'on del jugador.
    El segundo es la letra de la computadora.
    '''
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # randomly choose quien va primero
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    '''
    Dado un board y la letra del jugador, esta función
    devuelve True si el jugador ganó.
    bo = board
    le = letter

    '''
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the righ  side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal


def getBoardCopy(board):
    # hace una copia del board
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board
    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Cuál es tu próximo movimiento? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # devuelve un movimiento valido
    # devuelve None si no hay ningún movimiento válido
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
     # Check if the player could win on their next move and block them.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

     # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
       return move

     # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
       return 5

     # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
     # Return True if every space on the board has been taken. Otherwis      return False.
    for i in range(1, 10):
      if isSpaceFree(board, i):
          return False
    return True
print('Welcome to Tic-Tac-Toe!')
while True:
    # Reset the board.
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
             # Computer's turn
             move = getComputerMove(theBoard, computerLetter)
             makeMove(theBoard, computerLetter, move)

             if isWinner(theBoard, computerLetter):
                 drawBoard(theBoard)
                 print('The computer has beaten you! You lose.')
                 gameIsPlaying = False
             else:
                 if isBoardFull(theBoard):
                     drawBoard(theBoard)
                     print('The game is a tie!')
                     break
                 else:
                     turn = 'player'
    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
