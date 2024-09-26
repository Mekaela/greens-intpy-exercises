# ask user for number plate combination
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # maximum of 6 characters and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    # The first number used cannot be a ‘0’
    i = 0
    while i < len(s):
        if s[i].isnumeric():
            if s[i] == '0':
                return False
            else:
                break
        i+=1

    # “No periods, spaces, or punctuation marks are allowed.”
    for char in s:
        if char in ['.',' ','!']:
            return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    j = 0
    while j < len(s)-1:
        if s[j].isnumeric():
            if s[j+1].isalpha():
                return False
        j+=1

    return True

main()