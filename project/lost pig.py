def main():
    board=create_board()
    for i in board:
        print(i)
    pig_coorodinate=input("pig,please enter you cooroniate use commer to sprate them ")
    farmer_coorodinate= input("farmer,please enter you cooroniate ")
    pig_xcoorodinate=finding_xcoorodinate(pig_coorodinate)
    pig_ycoorodinate=ycoordinate(pig_coorodinate)
    farmer_x =finding_xcoorodinate(farmer_coorodinate)
    farmer_ycorodniate=ycoordinate(farmer_coorodinate)
    pig=Point(pig_xcoorodinate,pig_ycoorodinate)
    farmer=Point(farmer_x,farmer_ycorodniate)
    action=input("")



def create_board():
    board = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
    newboard = []
    for i in range(10):
        board1 = [[".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]
        newboard = board + newboard
    return newboard

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
def  finding_xcoorodinate(coordinates):
    global count
    count=1
    farmer_xccoordinates=""
    if count>1:
        count=1
    for i in coordinates:
        if i==",":
            break
        farmer_xccoordinates+=i
        count+=1
    return farmer_xccoordinates
def ycoordinate(corodinates):
    return corodinates[count:]
if __name__=="__main__":
    main()