# defined menu options as global, so it's cleaner to use anywhere
MENU_OPTIONS = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
}

def main():
    print_menu(MENU_OPTIONS)
    get_order(MENU_OPTIONS)

# prints menu options
def print_menu(MENU_OPTIONS):
    print('Menu Options: ')
    print('\n'.join({f'{key} {value}' for key, value in MENU_OPTIONS.items()}))

# gets the input from the user, adds it to total, prints the total, and reprompts until exited
def get_order(MENU_OPTIONS):
    order_total = 0
    try:
        while True:
            item = input("Item: ").title()
            if item in MENU_OPTIONS.keys():
                order_total += MENU_OPTIONS[item]
                print("Order total: $" + str("%.2f" % order_total))
    # to exit when user exits with control-d
    except EOFError as e:
        print(e)

main()