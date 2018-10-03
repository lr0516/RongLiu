from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2

class BankAccount():
    def __init__(self, owner, accountType):
        self.owner = owner
        self.balance = 0
        self.accountType = accountType

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        return True

    def __str__(self):
        return 'This account is owned by {0}, and it is a {1} account'.format(self.owner, self.accountType)

    def __len__(self):
        return self.balance

class BankUser():
    def __init__(self, owner):
        self.owner = owner
        self.accounts = {}

    def addAccount(self, accountType):
        if accountType.name in self.accounts:
            print('Account already exists.')
            return False
        else:
            self.accounts[accountType.name] = BankAccount(self.owner, accountType.name)

    def checkAccount(self, accountType):
        if accountType.name in self.accounts:
            return True
        else:
            return False

    def getBalance(self, accountType):
        if accountType.name not in self.accounts:
            return 'Account does not exist.'
        else:
            return len(self.accounts[accountType.name])
        
    def deposit(self, accountType, amount):
        self.accounts[accountType.name].deposit(amount)

    def withdraw(self, accountType, amount):
        if len(self.accounts[accountType.name]) < amount:
            print('Not enough balance in the account.')
        else:
            self.accounts[accountType.name].withdraw(amount)
            
    def __str__(self):
        result = 'User name: {0}\n'.format(self.owner)
        result += str(self.accounts)
        return result

def PosInt(n):
    try:
        num = float(n)
    except Exception:
        return False
    else:
        if num % 1 != 0 or num < 0:
            return False
    return True

def ATMSession(bankUser):
    def Interface():
        choice = '0'
        #print(choice)
        while (choice != '1'):
            # get input 'choice' as string
            choice = input('1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n')
            print('choice: ', choice)
            while choice not in ['1', '2', '3', '4', '5']:
                print('Invalid Input')
                choice = input('1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw\n')

            if choice == '1':
                return
            else: # choice = '2', '3', '4', or '5'
                # get input for accountType
                Type = input('Enter Option:\n1)Savings\n2)Checking\n')
                while Type not in ['1', '2']:
                    print('Invalid Input')
                    Type = input('Enter Option:\n1)Savings\n2)Checking\n')

                # generate accountType_enum based on input
                if Type == '1':
                    accountType_enum = AccountType.SAVINGS
                else:
                    accountType_enum = AccountType.CHECKING

                # process other choices
                if choice == '2':
                    bankUser.addAccount(accountType_enum)
                elif choice == '3':
                    print(bankUser.getBalance(accountType_enum))
                elif choice == '4':
                    if bankUser.checkAccount(accountType_enum):     
                        amount = input('Enter Integer Amount, Cannot Be Negative:')
                        # get positive integer input
                        while not PosInt(amount):
                            print('Invalid Input')
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                        bankUser.deposit(accountType_enum, int(amount))
                    else:
                        print('Account does not exist.')
                elif choice == '5':
                    if bankUser.checkAccount(accountType_enum): 
                        amount = input('Enter Integer Amount, Cannot Be Negative:')
                        # get positive integer input
                        while not PosInt(amount):
                            print('Invalid Input')
                            amount = input('Enter Integer Amount, Cannot Be Negative:')
                        bankUser.withdraw(accountType_enum, int(amount))
                    else:
                        print('Account does not exist.')
        return
    return Interface()

#l = BankUser('Liu')
#ATMSession(l)
