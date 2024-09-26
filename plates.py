# ask user for number plate combination
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # maximum of 6 characters and a minimum of 2 characters.
    if len(plate) < 2 or len(plate) > 6:
        return False

    # must start with at least two letters
    if plate[0].isalpha() == False or plate[1].isalpha() == False:
        return False

    # The first number used cannot be a ‘0’
    i = 0
    while i < len(plate):
        if plate[i].isnumeric():
            if plate[i] == '0':
                return False
            else:
                break
        i+=1

    # “No periods, spaces, or punctuation marks are allowed.”
    for char in plate:
        if char in ['.',' ','!']:
            return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    j = 0
    while j < len(plate)-1:
        if plate[j].isnumeric():
            if plate[j+1].isalpha():
                return False
        j+=1

    return True

main()