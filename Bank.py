from Account import Account
import json

class Bank(Account):
    def __init__(self):
        self.accounts = []
        self.load_from_file()

    def create_account(self):
        print('Open an account ')
        name = input("Enter your full name: ")
        balance = float(input("Enter your initial balance: "))
        account = Account(self.next_id,name, balance)
        account.name = name
        account.balance = balance

        self.accounts.append(account)
        self.save_to_file()
        print(f"Account created:\nID: {account.id}\nName: {account.name}\nBalance: {account.balance}")



    def deposit(self):
        id = input("Enter your id: ")
        amount = (input("Enter amount for deposit: "))
        account = self.find_account(id)
        if account:
            account.balance += float(amount)
            self.save_to_file()
            return True
        else:
            return False

    def withdraw(self):
        id = (input("Enter your id: "))
        amount = input("Enter amount for withdraw: ")
        account = self.find_account(id)
        if account and account.balance >= float(amount):
            account.balance -= float(amount)
            self.save_to_file()
            return True
        else:
            return False


    def transfer(self,):
        id_from = input("Enter your id: ")
        amount= (input("Enter amount for transfer "))
        id_to = input("Enter id to transfer ")
        account_from = self.find_account(id_from)
        account_to = self.find_account(id_to)
        if account_from and account_to and account_from.balance >= float(amount):
            account_from.balance -= float(amount)
            account_to.balance += float(amount)
            self.save_to_file()
            return True
        else:
            print('Υour balance is not enough')
            return False


    def get_balance(self):
        id = input("Enter your id: ")
        account = self.find_account(id)
        if account:
             bal = (account.balance)
             print(bal)
        else:
            return None
    def find_account(self,id):
        for account in self.accounts:
            if account.id == int(id):
                return account
        return print('lathos')

    def save_to_file(self):
        accounts_data = []
        for account in self.accounts:
            accounts_data.append(account.to_dict())

        with open("accounts.json", "w") as f:
            json.dump(accounts_data, f)

    def load_from_file(self):
        try:
            with open('accounts.json','r') as f:
                data = json.load(f)
                self.accounts = [Account(account['id'], account['name'], account['balance']) for account in data]
        except:
            pass