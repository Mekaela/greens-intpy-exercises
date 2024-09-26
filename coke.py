# prompts the user to pay for coke of value 50
def main():
    total = 0
    while total < 50:
        print("Amount Due: " + str(50 - total))
        change_received = get_input()
        total += change_received
    print('Change Owed: ' + str(total - 50))

# gets user input; only accepts 25, 10, and 5
def get_input():
    user_input = int(input("Insert coin: "))
    if user_input == 5 or user_input == 10 or user_input == 25:
        return user_input
    else:
        return 0

main()