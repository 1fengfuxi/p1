def happy_numbers(n):
    past = set()
    while n != 1:
        for i in str(n):
            n=sum(int(i)**2)
        if n in past:
            return False
        past.add(n)
    return True
print([x for x in range(500) if happy_numbers(x)][:20])
s