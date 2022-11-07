from itertools import chain, permutations
from string import digits

def main():
    lines=int(input("enter the line"))
    result=[]
    if lines<=6 and lines>=3 :
        while len(result)<lines:
            letter=input("enter your letter")
            if len(letter) >10:
                print("letter need to be less than 10 ")
                break
            result.append(letter)
        newresult=result[0:len(result)-1]
        print(newresult)
        solve_cryptarithm(newresult,result[-1])
    else:
        print("please enter a number between 3 to 6")


def solve_cryptarithm(addends, result):
    """Print a solution to the cryptarithm, if any exists.
    Arguments are the list of addends and the result of the sum.
    For example:
     solve_cryptarithm(['SEND', 'MORE'], 'MONEY')
    SEND(9567) + MORE(1085) = MONEY(10652)

    """
    letters = ''.join(set(chain(result, *addends)))
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in addends))))
    for perm in permutations(digits, len(letters)):
        decipher_table = str.maketrans(letters, ''.join(perm))
        def decipher(s):
            return s.translate(decipher_table)
        if '0' in decipher(initial_letters):
            continue # leading zeros not allowed
        deciphered_sum = sum(int(decipher(addend)) for addend in addends)
        if deciphered_sum == int(decipher(result)):
            def fmt(s):
                return f"{s}({decipher(s)})"
            print(" + ".join(map(fmt, addends)), "=", fmt(result))
            break
    else:
        print(" + ".join(addends), "=", result, " : no solution")

def create_output_result(result):
    output_result=" "
    for i in result:
        if i ==result[-2]:
            output_result = output_result + i + "="
        elif i==result[-1]:
            output_result = output_result + i
        else:
            output_result= output_result + i + "+"
    return output_result
dice=0

if __name__ == '__main__':
    main()








