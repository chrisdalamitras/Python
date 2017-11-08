#Draw the game board
def drawboard(board):
    print ('    |   |    ')
    print (' ' +board[0][0]+ '  | ' +board[0][1]+ ' |  ' +board[0][2] )
    print ('    |   |    ')
    print ('---------------')
    print ('    |   |   ')
    print (' ' +board[1][0]+ '  | ' +board[1][1]+ ' |  ' +board[1][2] )
    print ('    |   |    ')
    print ('---------------')
    print ('    |   |    ')
    print (' ' +board[2][0]+ '  | ' +board[2][1]+ ' |  ' +board[2][2] )
    print ('    |   |    ')

#Read the players move
def input_move(player_id , board):
    
    player_move = input("Player " +str(player_id)+ " make your move: ")
    
    while (not check_input(player_move , board)):
        player_move = input("Player " +str(player_id)+ " please give again: ")

    row , col = player_move.split(",")
    return  int(row) , int(col)   

#Check if the players move is acceptable
def check_input(player_move , board):
        
    try:
        row , col = player_move.split(",")
    except ValueError:
        print("Input must be two integers in format row,col between 1-3 e.g. 1,2")
        return False
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("Input must be two integers in format row,col between 1-3 e.g. 1,2")
        return False
    
    if ((row > 3 or row <=0) or (col > 3 or col <=0)):
        print("Input must be two integers in format row,col between 1-3 e.g. 1,2")
        return False
    elif (board[row-1][col-1] != " "):
        print("Cell already occupied")
        return False
    else:
        return True

#Update the board according to players moves
def update_board(board , row , col , player_id):

    if (player_id == 1):
        board[row-1][col-1] = "X"
    else:
        board[row-1][col-1] = "O"
    return board

#Check if a player has won
def win_condition(board , row , col):

    if (board[row-1][0] == board[row-1][1] == board[row-1][2]):
        return True
    if (board[0][col-1] == board[1][col-1] == board[2][col-1]):
        return True
    if (row-1 == col-1 == 1):
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            return True
    elif (row-1 == col-1 == 0 or row-1 == col-1 == 2):
        if (board[0][0] == board[1][1] == board[2][2]):
            return True
    elif ((row-1 == 0 and col-1 == 2) or (row-1 == 2 and col-1 == 0)):
        if (board[0][2] == board[1][1] == board[2][0]):
            return True
    else:
        return False
    
    return False

#Check if the game ends in a draw
def draw_condition(board):

    for i in range(3):
        for j in range(3):
            if (board[i][j] == " "):
                return False
    return True
        
#Procedure that calls the above functions and makes the game playable
def Tic_Tac_Toe(board , player_id):
    
    row , col = input_move(player_id , board)
    board = update_board(board , row , col , player_id)
    drawboard(board)

    if (win_condition(board , row , col)):
        print("Congratulation player " +str(player_id)+" you're winner!!!")
        return
    if (draw_condition(board)):
        print("The game ends in draw")
        return
        
    if (player_id == 1):
        Tic_Tac_Toe(board , 2)
    else:
        Tic_Tac_Toe(board , 1)

    return

#Main programm
print("Welcome to the Tic Tac Toe game")
play = "y"

while (play == "y"):
    
    player_id = 1
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    drawboard(board)
    Tic_Tac_Toe(board , player_id)

    play = input("If you would like to play another game press y : ")
