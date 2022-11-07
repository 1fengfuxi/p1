
def primein100(number):
    oddnumber=[]
    for new in range(2,number):

        if new%2!=0 and new%3!=0 and new%5!=0 and new%7!=0:
            oddnumber.append(new)
        elif new==2 or new==3 or new==5 or new==7:
            oddnumber.append(new)
    return oddnumber

odd=odd(100)
print(odd)

