import random, json, os
#from window_generator import WindowGenerator
#from tkinter import messagebox

class Account():
    def __init__(self,account_number, password, balance) -> None:
        self.__account_number = account_number
        self.__password = password
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_password(self):
        return self.__password

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

class BankAccount():
    __registeredAccount = []

    def __init__(self) -> None:
        #self.__generator = WindowGenerator()
        self.__acount = Account(
            random.randint(1111, 9999),
            random.randint(1111, 9999),
            random.randint(1111, 9999),
        )
        self.home()

    def home(self):
        BankAccount.create_account(123, 4567)

    def withdraw(self, data):
        try:
            if data > self.__acount.get_balance():
                print(f"Insufficient balance to withdrawn ₱{data}.")

            elif data <=0:
                print("Invalid amount to withdrawn.")

            else:
                print(f"withdrawn: ₱{data}")
                data = self.__acount.get_balance() - data
                self.__acount.set_balance(data)

        except ValueError:
            print("Enter integer inputs")

    def deposit(self, data):
        if data <=0:
            print("Invalid amount to deposit.")

        else:
            print(f"deposited: ₱{data}")
            data = self.__acount.get_balance() + data
            self.__acount.set_balance(data)

    def showBalance(self):
        print(f"Balance: ₱{self.__acount.get_balance()}")

    def saveData(self):
        path = f"users/{self.__acount.get_account_number()}"
        filename = f'{path}/data.json'

        if not os.path.exists(path):
            os.makedirs(path)

        data = {
            'account_number' : self.__acount.get_account_number(),
            'password' : self.__acount.get_password(),
            'balance' : self.__acount.get_balance()
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(e)

    def loadData(self, user: str, filename='users'):
        if os.path.exists(filename):
            for folder in os.listdir(filename):
                BankAccount.__registeredAccount.append(folder)
                path = os.path.join(filename, folder)

                if folder == user:
                    file = os.path.join(path, 'data.json')
                    with open(file, 'r') as f:
                        data = json.load(f)

                    self.__acount = Account(
                        data['account_number'],
                        data['password'],
                        data['balance']
                    )
    @staticmethod
    def create_account(id, password):
        path = f'users/{id}'
        filename = f'{path}/data.json'

        if not os.path.exists(path):
            os.makedirs(path)

        data = {
            'account_number' : id,
            'password' : password,
            'balance' : 0,
        }
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(e)


if __name__ == "__main__":
    BankAccount()
