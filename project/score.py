
def initialise():
    global round
    for index in range(5):
        if index==0:
            for i in point:
                result=point[index]+i
                r0.append(result)
        if index==1:
            for i in point:
                result=point[index]+i
                r1.append(result)
        if index==2:
            for i in point:
                result=point[index]+i
                r2.append(result)
        if index==3:
            for i in point:
                result=point[index]+i
                r3.append(result)
        if index==4:
            for i in point:
                result=point[index]+i
                r4.append(result)
    round=[r0,r1,r2,r3,r4]

def updateresult():
    count=0
    for i in range(0,5):
        for k in range(0,5):
            round[k][i]=round[k][i]+point[count]

    return round
def check(input1):
    for i in range(0,5):
        for k in range(0,5):
            if round[i][k]==input1:
                return True

if __name__=="__main__":

    point=[1,3,9,27,81]
    r0=[]##star with index 0
    r1=[]
    r2=[]
    r3=[]
    r4=[]
    initialise()
    print(round)
    time = 1
    input1 = 24
    while check(input1) != True:
        updateresult()
        print(round)
        time += 1
        if time >= 10:
            print("nmd")
            break

    print("minium time is " + str(time))

