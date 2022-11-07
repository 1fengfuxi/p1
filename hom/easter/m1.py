import random
import re
def generate_random_question():
    n1=random.randint(0,10)
    n2=random.randint(0,10)
    key_value= random.randint(1,4)
    symobols = {1: "+" , 2:"-", 3: "*",4:"/"}
    symbol = symobols.get(key_value)
    question = str(n1) + "  "+symbol + "  " +str(n2)
    return question

def check_answer(question):
    numbers_d=re.findall(r"\d" ,question)
    pattern = re.compile(r'[+*/ -]')
    string=pattern.findall(question)
    for i in string:
        if i=="+":
            return int(numbers_d[0])+int(numbers_d[1])
        elif i=="-":
            return int(numbers_d[0]) - int(numbers_d[1])
        elif i=="*":
            return int(numbers_d[0]) * int(numbers_d[1])
        elif i=="/":
            try:
                return  int(numbers_d[0]) / int(numbers_d[1])
            except ZeroDivisionError:
                return "not defined"

def main()
    result=0
    x=20
    while x>10 :
        question=generate_random_question()
        question_format = "please caculate the value of "+ question
        answer=float(input(question_format))
        if check_answer(question)==answer:
            result+=1
        print("correct")
        x-=1






