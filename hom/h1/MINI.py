#####
###   connect 4 game
#### wirteen by
####  last updata 3/12/2021 knownbug;no
def main():
    staredup()
    print("this is the currenly board")
    Show_Board()
    while True:
        selection1 = input(name + "   " + "which colun will you STAR first with A to E ")
        update_board(selection1, colur)
        if winner():
            break
        elif full():
            break
        else:
            pass
        selection2 = input(name2 + "   " + "which colun will you STAR first with A to E ")
        update_board(selection2, colur2)
        if winner():
            break
        elif full():
            break
        else:
            pass





board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]


def staredup():
    global name
    global colur
    global colur2
    global name2
    choice = ["r", "y"]
    print("this is connect 4 ")
    print("this game is for 2 player to play you can chose either red R or yellow Y ")
    name = input("please enter your name ")
    colur = input("plase chose you colur R OR Y")
    if colur == "Y":
        name2 = input("second player please enter your name")
        colur2 = "R"
    elif colur == "R":
        name2 = input("second player please enter your name")
        colur2 = "Y"
    else:
        print("enter the right colur")
        return False


def Show_Board():
    global board
    for row in range(0, 6):
        for column in range(0, 5):
            print(board[row][column], "    ", end='')  # prints Horizontally
        print()  # adds New LinE


def update_board(selection, decision):
    global board
    possible = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
    num = possible.get(selection)
    for remain in range(4, -1, -1):
        if board[remain][num] == "0":
            board[remain][num] = decision
            Show_Board()
            break


def full():
    check = 0
    for row in range(0, 6):
        for column in range(0, 5):
            if board[row][column] == "0":
                pass
            else:
                check += 1
        if check == 30:
            return True
        else:
            return False
def winner():
    yellowpoint=0
    redpoint=0
    for row in range(5):
        for column in range(6):
            if board[column][row]== "Y":
                if yellowpoint>=1:
                    if board[column][row]!=board[column-1][row]:
                        yellowpoint=0
                yellowpoint+=1

            elif  board[column][row]== "R":
                if redpoint>=1:
                    if board[column][row]!=board[column-1][row]:
                        redpoint=0
                redpoint+=1
        if yellowpoint==4:
            print("yellow win")
            return True
        elif redpoint==4:
            print("red you win ")
            return True
        else:
            yellowpoint=0
            redpoint=0
    for column in range(6):
        for row in range(5):
            if board[column][row] == "Y":
                if yellowpoint>=1:
                    if board[column][row]!=board[column][row-1]:
                        yellowpoint=0
                yellowpoint += 1
            elif board[column][row] == "R":
                if redpoint>=1:
                    if board[column][row]!=board[column][row-1]:
                        redpoint+=1
                redpoint+=1
            else:
                pass
        if yellowpoint == 4:
            print("yellow")
            return True
        elif redpoint == 4:
            print("red you win ")
            return True
        else:
            yellowpoint = 0
            redpoint = 0

main()