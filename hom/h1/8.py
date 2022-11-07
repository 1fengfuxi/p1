board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]
yellowpoint=0
redpoint=0
for row in range(5):
    for column in range(6):
        if board[column][row]== "Y":
            yellowpoint+=1
        elif  board[column][row]== "R":
            redpoint+=1
    if yellowpoint==4:
        print("yellow")
    elif redpoint==4:
        print("red you win ")
    else:
        yellowpoint=0
        redpoint=0


for column in range(6):
    for row in range(5):
        if board[column][row] == "Y":
            yellowpoint += 1
        elif board[column][row] == "R":
            redpoint += 1
        else:
            pass
    if yellowpoint == 4:
        print("yellow")
    elif redpoint == 4:
        print("red you win ")
    else:
        yellowpoint = 0
        redpoint = 0



