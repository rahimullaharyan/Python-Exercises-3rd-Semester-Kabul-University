class InvalidAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class InvalidOptionError(Exception):
    pass


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        self.balance += amount
        self.save_transaction(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientFundsError("Insufficient account balance.")

        self.balance -= amount
        self.save_transaction(f"Withdrawn: ${amount}")

    def save_transaction(self, record):
        with open("transactions.txt", "a", encoding="utf-8") as file:
            file.write(record + "\n")

    def show_history(self):
        try:
            with open("transactions.txt", "r", encoding="utf-8") as file:
                history = file.read()

        except FileNotFoundError:
            print("No transaction history found.")

        except PermissionError:
            print("Permission denied. Cannot read transaction history.")

        except OSError as e:
            print("File error:", e)

        else:
            print("\nTransaction History:")
            print(history)

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")


account = Account()

while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice == 1:
            account.show_balance()

        elif choice == 2:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
            print("Deposit successful!")

        elif choice == 3:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
            print("Withdrawal successful!")

        elif choice == 4:
            account.show_history()

        elif choice == 5:
            print("Thank you for using our banking system!")
            break

        else:
            raise InvalidOptionError("Please select an option from 1 to 5.")

    except ValueError:
        print("Error: Please enter a valid numeric value.")

    except InvalidAmountError as e:
        print("Error:", e)

    except InsufficientFundsError as e:
        print("Error:", e)

    except InvalidOptionError as e:
        print("Error:", e)

    except OSError as e:
        print("File error: Unable to save transaction.", e)

    else:
        print("Operation completed successfully.")

    finally:
        print("Transaction attempt completed.")