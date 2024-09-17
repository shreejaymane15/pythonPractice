balance = 0


def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)


def deposit(amount):
    global balance
    balance += amount
    print("Deposited Successfully")


def withdraw(amount):
    global balance
    balance -= amount
    print("Withdrawn Successfully")


if __name__ == "__main__":
    main()