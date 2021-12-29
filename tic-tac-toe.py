def buildboard(x,y):
    board = ' ---'*x + '\n'
    for block in range(y):
        board += '|   ' * (x + 1) + '\n'
        board += ' ---'*x + '\n'
    return board

board = buildboard(3,3)

def display_board(x,y,board,player,start_index):
    index = start_index + (start_index *2 *x + 4 * y)
    board = board[:index] + player + board[index+1:]
    return board

def find_winner(matrix):
    winner = None
    for b in range(3): #check columns
        if matrix[0][b] == matrix[1][b] == matrix[2][b]:
            winner = matrix[0][b]
            #print(f'winner is {winner}')
            if winner != 0:
                break
    for a in range(3): #check rows
        if matrix[a][0] == matrix[a][1] == matrix[a][2]:
            winner = matrix[a][0]
            #print(f'winner is {winner} a is {a}')
            if winner != 0:
                break
    for a in range(1): #check diagonals
        if matrix[a][a] == matrix[a+1][a+1] == matrix[a+2][a+2]:
            winner = matrix[a][a]
            #print(f'winner is {winner} a is {a}')
        elif matrix[a][a+2] == matrix[a+1][a+1] == matrix[a+2][a]:
            winner = matrix[a][a+2]
            #print(f'winner is {winner} a is {a}')

    return winner

print(find_winner([['X', 0, 'X'],
                   ['X', 'O', 0],
                   ['O', 0, 0]]))


def input_format(move):
    #clean up string
    move_index = move.split(",")
    move_index = [e.strip() for e in move_index]
    #convert user index to programming index by -1
    x = int(move_index[0])-1
    y = int(move_index[1])-1
    return x, y

def move():
    board = buildboard(3, 3)

    mat = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

    i = 1
    while i <= 9:
        #i range indicate the total turns
        #check whose turn
        if i%2 == 1:
            player = 'X'
            move = input('player1 input rows,column here:')
        else:
            player = 'O'
            move = input('player2 input rows,column here:')

        # clean up string
        x, y = input_format(move)
        if x < 0 or y < 0 or x > 2 or y > 2:
            print('your value is out of range')
            continue

        # if the square is taken player re-input the move. Else sq is empty, allow player to secure their move.
        if mat[x][y] != 0:
            print('please input new value')
            continue
        else:
            mat[x][y] = player
            print(mat)
            i += 1

        # display board to player
        board = display_board(x,y,board,player,15)
        print(board)

        # check for winner
        winner = find_winner(mat)

        # stop the loop once we have a winner.
        if winner != 0 and winner != None:
            print(f'winner is {winner} yay')
            print('----◎[▪‿▪]◎----')
            break
    
    if winner == 0 or winner == None:
        print('There is no Winner')

    return mat


move()

###29/12/21
###For code review and will check out other ppls codes
