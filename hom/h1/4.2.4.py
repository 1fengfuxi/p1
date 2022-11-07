def main():
    # ask user for carowner name and contact name
    # owenername = input("please enter your name")
    # contact_number = input("please enter you contact number")
    car_registration = input("do you have a regestriation number enter 1 for true 0 for false")
    registered_year = int(input(" please enter year when car was regeistered"))
    if car_registration == "0" or registered_year < 2001:
        if registered_year < 2001:
            car_regerstration_number = input("please enter you regerstration number")
            store(car_regerstration_number)
            print(" “Registration Completed” ")
        else:
            pass

    elif car_registration == "1":
        car_regerstration_number = input("please enter you regerstration number")
        if len(car_regerstration_number)==8:
            if car_regstration_rule(car_regerstration_number):
                store(car_regerstration_number)
                print(" “Registration Completed” ")
            else:
                print("The following digits are incorrect")
        else:
            print("The following digits are incorrect")

    else:
        print("The following digits are incorrect")


def car_regstration_rule(registered_number):
    right_element = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V",
                     "W", "X", "X", "Y"]
    wrong_elementA = ["I", "Q", "Z"]
    right_elementd = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U",
                      "V", "W", "X", "X", "Y", "Z"]
    numseta = registered_number[0:2]
    numsetb = registered_number[2:4]
    numsetc = registered_number[4]
    numsetd = registered_number[5:8]
    if registered_number[0] in wrong_elementA or registered_number[1] in wrong_elementA:
        pass
    elif registered_number[0] in right_element and registered_number[1] in right_element:
        if numsetb.isdigit():
            if numsetc.isspace():
                for i in numsetd:
                    if i not in right_elementd:
                        return False
                    else:
                        return True
def store(number):
    f=open("python.txt","a")
    f.write("\n"+ number)
    f.close()



main()

