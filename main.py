MAX_LINES = 3


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():


def main():
    balance = deposit()


main( )
