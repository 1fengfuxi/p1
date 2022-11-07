list=[3,4,5,7,5,6]
target=9
def lin(list,target):
    x=0;
    while x<len(list):
        if list[x]==target:
            return x
        else:
            x+=1
    if x>=len(list):
        return "element in not in the iist"

list2=[ 1,3 ,4 ,6 ,7 ,9 ]
def b_s(list,targrt):
    low=0
