def fibonacci(num):
    fibonici = [0, 1, 1, 2]
    for number in range(4, num):
        num1 = number
        num2 = number
        num3 = fibonici[num1 - 1] + fibonici[num2 - 2]
        fibonici.append(num3)
    return fibonici


num = int(input('enter how many numbers needed in Fibonacci series- '))
print(fibonacci(num))

num=[]
def recur_fibo(n):
   if n <= 1:
       return n
   if n in num:
       return num[n]
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterm = 100
if nterm <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for term in range(nterm):
       print(recur_fibo(term))
