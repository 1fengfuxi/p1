
def caculator(list1):
    total = 0
    j = 0
    Number = len(list1)
    while(j < Number):
        total = total + list1[j]
        j = j + 1
    return total
list1=[5,9,0,8,7,6,4]
print(caculator(list1))