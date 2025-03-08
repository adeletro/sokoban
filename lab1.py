play_board = open("level1.txt", "r").read().strip().splitlines()
print(play_board)



def getPlayerPosition(play_board):
    for i in range(len(play_board)):
        for j in range(len(play_board[i])):
            if play_board[i][j]=="@":
                position_x = j
                position_y = i 
                print("La position du joueur est donc la suivante:")
                return(position_x,position_y)

print(getPlayerPosition(play_board))



def isEmpty(play_board, x, y):
    if play_board[y][x] == "-":
        return True 
    elif play_board[y][x] == "#":
        return True 
    else:
        return False 
    
print(isEmpty(play_board, 5, 0))
print(isEmpty(play_board, 5, 2))

