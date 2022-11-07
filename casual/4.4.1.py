li=[2,4,3,4,4,5,4,3,3,3,3,2]

def insertion(lists):
    for i in range(1,len(lists)):
        previous=i-1
        while lists[i]>lists[previous] and previous >=0:
            lists[i],lists[previous]=lists[previous],lists[i]
            i-=1
            previous-=1

    return lists

def bubble(lists):
    for i in range(len(lists)-1):
        for j in range(len(list)-1-i):


