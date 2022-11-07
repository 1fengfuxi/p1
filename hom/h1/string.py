def LetterChanges(str):
    # create lists of vowels, letters, blank letter var, and convert str to list
    vowels = list('aoieu')
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZA')
    letter = ''
    str_list = list(str)
    x = 0

    # while our var x is less than length of str
    # check if index is in alphabet list, if it is, take the letter next to it
    # if it's a vowel, capitalise, otherwise move to next index
    while x < len(str):
        if str_list[x] in alphabet:
            letter = alphabet[alphabet.index(str_list[x]) + 1]
            if letter in vowels:
                letter = letter.upper()
            str_list[x] = letter
            x += 1
        else:
            x += 1

    # create new var str_new which joins up the elements in the list to make a string
    str_new = "".join(str_list)
    return str_new


# keep this function call here
print(LetterChanges("tr"))