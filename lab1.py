play_board = open("level1.txt", "r").read().strip().splitlines()
#print(play_board)



def getPlayerPosition(play_board):
    for i in range(len(play_board)):
        for j in range(len(play_board[i])):
            if play_board[i][j]=="@":
                position_x = j
                position_y = i 
                print("La position du joueur est donc la suivante:")
                return(position_x,position_y)

#print(getPlayerPosition(play_board))



def isEmpty(x, y):
    if play_board[y][x] == "-":
        return True 
    elif play_board[y][x] == "#":
        return True 
    else:
        return False 
    
#print(isEmpty(5, 0))
#print(isEmpty(5, 2))



def isBox(x,y):
    if play_board[y][x] == "$" or play_board[y][x] == "*" :
        return True 
    else:
        return False 

#print(isBox(5, 0))
#print(isBox(5, 2))



def printBoard(play_board):
    for i in range(len(play_board)):
        print(play_board[i])
        print()  # passe a la ligne suviante 

#printBoard(play_board)
