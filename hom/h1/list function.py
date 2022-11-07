def oddposition(list):
    new=[]
    for element in list:
        if list.index(element)%2!=0:
            new.append(element)
    return new
list1=[5,9,0,8,7,6,4]


def total_caculator(list):
    value=0
    for element in list:
        value+=element
    return value

def isPalindrome(s):
    return s == s[::-1]

def sum(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + sum(list1[1:])

def add_caculator(list):
    total = 0
    j = 0
    Number = len(list1)
    while (j < Number):
        total = total + list1[j]
        j = j + 1
    return total