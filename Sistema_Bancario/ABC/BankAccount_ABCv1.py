import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime 

class Client:
        def __init__(self, address):
                self.address = address
                self.accounts = []
        
        def do_transaction(self, account, transaction):
                transaction.register(account)
        
        def new_account(self, account):
                self.accounts.append(account)
        

class Personal(Client):
        def __init__(self, name, birth_date, id, address):
                super().__init__(address)
                self.name = name
                self.birth_date = birth_date
                self.id = id

class Account:
        def __init__(self, accnumber, client):
                self._wallet = 0
                self._accnumber = accnumber
                self._agency = "0001"
                self._client = client
                self._history = History()
        
        @classmethod
        def new_account(cls, client, accnumber):
                return cls(accnumber, client)

        @property
        def wallet(self):
                return self._wallet

        @property
        def accnumber(self):
                return self._accnumber
        
        @property
        def agency(self):
                return self._agency
        
        @property
        def client(self):
                return self._client
        
        @property
        def history(self):
                return self._history
        
        def withdraw(self, value):
                wallet = self.wallet
                ex_wallet = value > wallet 

                if ex_wallet:
                        print("\n Insuficient balance")
                        return True
                
                elif value > 0:
                    self._wallet -= value
                    print("\n Successful Transaction  ")
                    return True
                
                else:
                    print("\n Invalid Value")

                return False
        
        def deposit(self, value):
                if value > 0:
                    self._wallet += value
                    print("\n Successful Transaction")
                else:
                    print("\nTransaction Failed: Invalid Value")
                    return False
                
                return True

class Bankaccount(Account):
        def __init__(self, accnumber, client, limit=500,transaction_limit=3):
              super().__init__(accnumber, client)
              self._limit = limit
              self._transaction_limit = transaction_limit

        def withdraw(self, value):
            withdraw_number = len([transaction for transaction in self.history.transactions  if transaction["Type"] == Withdraw.__name__])

            exceded_limit = value > self._limit
            exceded_transactions = withdraw_number >= self._transaction_limit

            if  exceded_limit:
                    print("\n Operation failed, Not eought balance")
            elif exceded_transactions:
                    print("\n Operation Failed, Number of withdraws exceded daily limit")

            else:
                    return super().withdraw(value)
            return False

        
        def __str__(self):
              return f"""\
                Agency:\t{self.agency}
                Account:\t\t{self.accnumber}
                Owner:\t{self.client.name}
                """
        
class History:
        def __init__(self):
              self._transactions = []
        
        @property
        def transactions(self):
              return self._transactions
       
        def add_transaction(self, transaction):
              self._transactions.append(
                     {
                            "Type": transaction.__class__.__name__,
                            "Value": transaction.value,
                            "Data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                     }
              )


class Transaction(ABC):
       @property
       @abstractproperty
       def value(self):
              pass
       @abstractclassmethod
       def register(self, account):
              pass

class Withdraw(Transaction):
        def __init__ (self, value):
               self._value = value
        
        @property
        def value(self):
               return self._value

        def register(self, account):
            successiful_transaction = account.withdraw(self.value)

            if successiful_transaction:
                account.history.add_transaction(self)              
        

class Deposit(Transaction):
       def __init__(self, value):
              self._value = value
        
       @property
       def value(self):
              return self._value

       def register(self, account):
              successiful_transaction = account.deposit(self.value)

              if successiful_transaction:
                     account.history.add_transaction(self)



def menu():
        menu = """\n
        ====================MENU====================
        [d]\tDeposit
        [w]\tWithdraw
        [l]\tList Transactions
        [na]\tNew Account
        [al]\tAccount List
        [nu]\tNew User
        [q]\tQuit
        """
        return input(textwrap.dedent(menu))

def filter_client(id, clients):
       filtered_clients = [client for client in clients if client.id == id]
       return filtered_clients[0] if filtered_clients else None

def recover_account(client):
        if not client.accounts:
              print("\n ###This client does not have an account registered!!!")
              return
        return client.accounts[0]

def deposit(clients):
        id = input("Insert client ID: ")
        client = filter_client(id, clients)

        if not client:
               print("### Client not found! ###")
               return 
        value = float(input("Insert deposit value: "))
        transaction = Deposit(value)


        account = recover_account(client)
        if not account:
               return
        
        client.do_transaction(account, transaction)   

        
def withdraw(clients):
       id = input("Insert client ID: ")
       client = filter_client(id, clients)      

       if not client:
               print("### Client not found! ###")
               return
       value = float(input("Insert withdraw value: "))
       transaction = Withdraw(value)

       account = recover_account(client)
       if not account:
            return
       
       client.do_transaction(account, transaction)


def list_transactions(clients):
        id = input("Insert client ID: ")
        client = filter_client(id, clients)      

        if not client:
               print("### Client not found! ###")
               return
        
        account = recover_account(client)
        if not account:
               return

        print("\n========================= Balance =========================")    
        transactions = account.history.transactions

        history = ""
        if not transactions:
               history = "No transactions registred"
        else:
               for transaction in transactions:
                    history += f"\n{transaction['Type']}:\n\$ {transaction['Value']:.2f}"
        
        print(history)
        print(f"Total:\n\t$ {account.wallet:.2f}")
        print("\n============================================================")

def register(clients):
        id = input("Insert client ID: ")
        client = filter_client(id, clients)      

        if client:
               print("### This client already has an account! ###")
               return
        
        name = input("Full Name: ")
        birth_date = input("Birth date: ")
        address = input("Address: ")

        client = Personal(name = name, birth_date = birth_date, id = id, address = address)
        clients.append(client)

        print("\n### Registered! ###")


def create_account(accnumber, clients, accounts):
        id = input("Insert client ID: ")
        client = filter_client(id, clients)      

        if not client:
               print("### Client not found! ###")
               return
        account = Bankaccount.new_account(client=client, accnumber = accnumber ) 
        accounts.append(account)
        client.accounts.append(account)

        print("\n### Account Created ###")

def  list_accounts(accounts):
       for account in accounts:
              print("=" * 100)
              print(textwrap.dedent(str(account)))


def main():
       clients = []
       accounts = []

       while True:
            option = menu()
            if option == "d":
                    deposit(clients)
            elif option == "w":
                   withdraw(clients)
            elif option == "l":
                    list_transactions(clients)
            elif option == "na":
                    accounts_num = len(accounts) + 1
                    create_account(accounts_num, clients, accounts)
            elif option == "al":
                    list_accounts(accounts)
            elif option == "nu":
                    register(clients)
            elif option == "q":
                    break
            else:
                   print("##### Invalid Operation #####")

main()