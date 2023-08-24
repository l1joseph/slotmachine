"""
Leo Joseph
Simple Slot machine with 3 slots, bets $1-$100.
"""
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLUMNS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}

symbol_values = {"A": 5, "B": 4, "C": 3, "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
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


def print_slot_machine(columns):  # traposing matrix
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        account_balance = input("How much would you like to deposit? $")
        if account_balance.isdigit():
            account_balance = int(account_balance)
            if account_balance > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid amount. Please enter a valid number.")
    return account_balance


def num_lines():
    while True:
        lines = input(
            "How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? "
        )
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:  # lines > 0 and lines <= MAX_LINES:
                break
            else:
                print(f"Amount must be greater than 0 and less than {MAX_LINES+1}.")
        else:
            print("Invalid amount. Please enter a valid number.")
    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Invalid amount. Please enter a valid number.")
    return amount


def spin(balance):
    lines = num_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(
                f"Your balance is ${balance}. You don't have enough money to make that bet. Please lower your bet."
            )
        else:
            break

    print(f"You are betting ${bet} on {lines} lines for a total bet of ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings} on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play or 'q' to quit. ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
