def finding(list):
    max_element = max(list)
    return(max_element)


def Reverse(list):
    new_list = list[::-1]
    return new_list

def target(numbers):
    count=0
    for target in list:
        if target==numbers:
            return True

list = [10, 11, 12, 13, 14, 15]
print(finding(list))
print(Reverse(list))
print(target(15))

