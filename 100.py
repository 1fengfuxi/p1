import tkinter
names=["Bob","Mary","Ismail","Nuringa"]
class player():
    clist=[]
    pNum=0

    def __init__(self,pNum):
        self.clist=[]
        self.pNum=pNum

    def check(self, given_name):
        tempName=given_name
        if len(tempName) > 0:
            self.name = tempName
        else:
            import random
            if len(names) > 0:
                self.name = names.pop(random.randint(0, len(names) - 1))
            else:
                self.name = "Player " + str(self.pNum)

    def draw(self):
        import random
        temp=random.randint(2,11)
        self.clist.append(temp)

    def getTotal(self):
        #return self.clist
        return sum(self.clist)

def overdrawn(pl):
    return pl.getTotal()>21

def whoWins(pl1,pl2):
    if overdrawn(pl1) and not(overdrawn(pl2)):
        return pl2.name
    elif (overdrawn(pl1) and (overdrawn(pl2))) or (pl1.getTotal()==pl2.getTotal()):
        return "draw"
    elif overdrawn(pl2) and not(overdrawn(pl1)):
        return pl1.name
    elif pl1.getTotal()> pl2.getTotal():
        return pl1.name
    else:
        return pl2.name
#main program
def fun_pressed():
    global var_pressed
    global var_e
    global var_e2
    var_pressed=True
    var_e= e1.get()
    var_e2=e2.get()



var_pressed=False
plagain='y'
root = tkinter.Tk()
root.geometry("500x500")
while plagain=='y':
    p1=player(1)
    p2=player(2)
    p1_text= "Enter player" + str(p1.pNum )+ "'s name, or hit <Enter> for default names: "
    p2_text="Enter player" + str(p2.pNum )+ "'s name, or hit <Enter> for default names: "

    l1 = tkinter.Label(root, text=p1_text)
    l2 = tkinter.Label(root, text=p2_text)
    e1=tkinter.Entry(root)
    e2=tkinter.Entry(root)
    l1.grid(row=0,column=0,pady=10)
    l2.grid(row=1, column=0)
    e1.grid(row=0,column=1)
    e2.grid(row=1, column=1)
    b1=tkinter.Button(root,text="submit",width=10,height=1,command=fun_pressed)
    b1.grid(row=2,column=0)
    if var_pressed==True:
        p1.check(str(var_e))
        p2.check(var_e2)
        for i in range(3):
            p1.draw()
            p2.draw()

        print(p1.name,"played:",p1.clist,"vs: ", p2.name,"played:", p2.clist)
        print(p1.name,p1.getTotal(),"vs: ",p2.name,p2.getTotal())
        if whoWins(p1,p2)!="draw":
            print(whoWins(p1,p2), " won")
        else:
            print("It's a draw")
        plagain=input("Play again: type 'y'? ")
root.mainloop()
print("bye!")
