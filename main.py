MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Handle's the user's deposit
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

# Handle's the user's input for the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet_amount():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount


# Main function
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main( )
