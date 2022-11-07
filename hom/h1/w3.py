def validator(digit):
    newdigit=list(digit)
    del(newdigit[-1])#ensure validate number is not count in
    digit1=newdigit[::-2]
    digit2 = newdigit[1::2]
    number1=[]
    for i in digit1:
        number=int(i)*2
        if number>=10:
            number=list(str(i))#seprate into each element
            result=0
            for i in number:
                result=result+int(i)
            number1.append(result)
        else:
            number1.append(number)

    number2=list(map(int,digit2))
    sum1=sum(number1)
    sum2=sum(number2)
    total=sum1+sum2
    tota2=10-(total%10)
    if total==digit[:-1]:
        return("valid")
    else:
        return("invalid")

digit=input("please enter your card number")
print(validator(digit))