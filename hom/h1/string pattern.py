result=input("words?")
def frame(words):
    print('*' *5)
    for word in words:
        print('* {a:<3} *'.format(a=word, ))
    print('*' * 5)
result=result.split(" ")
frame(result)