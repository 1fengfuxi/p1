import random
score=0
word=["apple","banana","orange", "lemon"]


def random_genrator():
    global number
    number = [0, 0, 0, 0]
    for i in range(len(number)):
        number[i] = random.randint(1, 4)

def fruit_printer():
    for n in number:
        if n==1:
            print(word[0])
        elif n==2:
            print(word[1])
        elif n==3:
            print(word[2])
        else :
            print(word[3])

def checker():
    global score
    if number[0]==number[1]==number[2]:
        print("you won")
        score+=10
    else:
        print("good luck for you")

while True:
    random_genrator()
    fruit_printer()
    checker()
    print("you score is "+str(score))
    answer=input("enter q to quit")
    if answer=="q":
        break

print("you final score is "+score)