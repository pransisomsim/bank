import random
import json
import os

class Account:
    def __init__(self, name, account_number, password, balance):
        self.__name = name
        self.__account_number = account_number
        self.__password = password
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__account_number

    def get_password(self):
        return self.__password

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount


class BankAccount:
    def __init__(self):
        self.__acount = None

    def set_account(self, account):
        self.__acount = account

    def withdraw(self, amount):
        if self.__acount is None:
            print("No account is logged in.")
            return

        if amount > self.__acount.get_balance():
            print(f"Insufficient balance to withdraw ₱{amount}.")
        elif amount <= 0:
            print("Invalid amount to withdraw.")
        else:
            print(f"Withdrawn: ₱{amount}")
            self.__acount.set_balance(self.__acount.get_balance() - amount)

    def deposit(self, amount):
        if self.__acount is None:
            print("No account is logged in.")
            return

        if amount <= 0:
            print("Invalid amount to deposit.")
        else:
            print(f"Deposited: ₱{amount}")
            self.__acount.set_balance(self.__acount.get_balance() + amount)

    def show_balance(self):
        if self.__acount is None:
            print("No account is logged in.")
        else:
            print(f"Balance: ₱{self.__acount.get_balance()}")


class BankInterface:
    def __init__(self):
        self.__bank = BankAccount()
        self.home()

    def home(self):
        while True:
            print('-' * 70)
            print("[1]. Create Account\n[2]. Login\n[3]. Exit\n")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                password = input("Enter your password: ")
                self.create_account(name, password)

            elif choice == '2':
                account_number = input("Enter your account number: ")
                password = input("Enter your password: ")
                self.login(account_number, password)

            elif choice == '3':
                print("Thank you! Bye.")
                break

            else:
                print("Invalid choice. Please try again.")

    def create_account(self, name, password):
        account_number = str(random.randint(1111, 9999))
        path = f'users/{account_number}'
        filename = f'{path}/data.json'

        if not os.path.exists(path):
            os.makedirs(path)

        data = {
            'name': name,
            'account_number': account_number,
            'password': password,
            'balance': 0
        }

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
                print(f"Account `{account_number}` successfully created.")

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error saving account data: {e}")

    def save_data(self):
        if self.__bank._BankAccount__acount is None:
            print("No account is logged in.")
            return

        account = self.__bank._BankAccount__acount
        path = f'users/{account.get_account_number()}'
        filename = f'{path}/data.json'

        if not os.path.exists(path):
            os.makedirs(path)

        data = {
            'name': account.get_name(),
            'account_number': account.get_account_number(),
            'password': account.get_password(),
            'balance': account.get_balance()
        }

        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error saving account data: {e}")

    def login(self, account_number, password):
        filename = 'users'

        if not os.path.exists(filename):
            print("No accounts found.")
            return

        for folder in os.listdir(filename):
            path = os.path.join(filename, folder)
            file = os.path.join(path, 'data.json')

            try:
                with open(file, 'r') as f:
                    data = json.load(f)

                if account_number == str(data['account_number']) and password == data['password']:
                    self.__bank.set_account(Account(
                        data['name'],
                        data['account_number'],
                        data['password'],
                        data['balance']
                    ))
                    print(f"Welcome, {data['name']}! Login successful.")
                    self.account_menu()
                    return
            except (FileNotFoundError, json.JSONDecodeError):
                continue

        print("Account not found or incorrect credentials.")

    def account_menu(self):
        while True:
            print("\n[1]. Withdraw\n[2]. Deposit\n[3]. Show Balance\n[4]. Logout\n")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = int(input("Enter amount to withdraw: "))
                self.__bank.withdraw(amount)
                self.save_data()

            elif choice == '2':
                amount = int(input("Enter amount to deposit: "))
                self.__bank.deposit(amount)
                self.save_data()

            elif choice == '3':
                self.__bank.show_balance()

            elif choice == '4':
                print("Logged out successfully.")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    BankInterface()

