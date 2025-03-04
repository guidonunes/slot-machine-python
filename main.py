import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

# Check the winnings for the slot machine spin
def check_winnings(columns,lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Generates a random spin for the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Prints the slot machine spin
def print_slot_machine_spin(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

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

# Handle's the user's input for the amount to bet on each line
def get_bet_amount():
    while True:
        amount = input("What would you like to bet o each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

# The main game loop
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough funds to place this bet, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}!")
    print(f"You win on lines:", *winning_lines)
    return winnings - total_bet

# Main function
def main():
    balance = deposit()
    while True:
        print(f"Your current balance is: ${balance}")
        answer = input("Would you like to spin? (y/n) ")
        if answer.lower() == "y":
            balance += spin(balance)
        else:
            break

    print(f"Your final balance is: ${balance}")


main( )
