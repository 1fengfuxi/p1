def sumcaculator(sum):
        value=0
        for i in range(1,sum):
                value+=i
        return value

def productcaculatoe(product):
        value=1
        for i in range(1,product):
                value=value*i
        return value

def sum2(chosen_time):
        value=0
        for i in range(1, chosen_time):
            if i%3==0 or i%5==0:
                value+=i
        return(value)


def timetable(time_table_numbeer):
        for i in range(1, 12):
                print(time_table_numbeer * i)



timetable(3)

choice=input("chose 1 for sum chose 2 for product ")
if choice=="1":
        sum=int(input("the sum of 1 to n ,please enter n "))
        sum=sumcaculator(sum)
        sum=str(sum)
        print(sum)
elif choice=="2":
        product=int(input(" the product of 1 to n please enter n "))
        product=productcaculatoe(product)
        print(str(product))
else:
        print(" please enter a valid information ")