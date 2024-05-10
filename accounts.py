class Account:

    def __init__(self, account_name, account_balance = 0):

        self.__account_name = account_name
        self.__account_balance = account_balance

        self.set_balance(self.__account_balance)

    def deposit(self, amount):

        if amount > 0:

            self.__account_balance += amount
            return True

        else:

            return False

    def withdraw(self, amount):

        if amount > 0 and (self.__account_balance - amount) >= 0:

            self.__account_balance -= amount
            return True

        else:

            return False

    def get_balance(self):

        return self.__account_balance

    def get_name(self):

        return self.__account_name

    def set_balance(self, value):

        if value >= 0:

            self.__account_balance = value

        else:

            self.__account_balance = 0

    def set_name(self, value):

        self.__account_name = value

    def __str__(self):

        return f'Account name = {self.get_name()}, Account Balance = {self.get_balance():.2f}'

class SavingAccount(Account):

    MINIMUM = 100
    RATE = 0.02

    def __init__(self, account_name):

        super().__init__(account_name, SavingAccount.MINIMUM)
        self.__deposit_amount = 0

    def apply_interest(self):

        interest =self.get_balance() * SavingAccount.RATE

        self.set_balance(self.get_balance() + interest)

    def deposit(self, amount):

        if super().deposit(amount):

            self.__deposit_amount += 1

            if self.__deposit_amount % 5 == 0:

                SavingAccount.apply_interest(self)

            return True

        else:

            return False

    def withdraw(self, amount):

        if amount > 0 and (self.get_balance() - amount) >= SavingAccount.MINIMUM:

            self.set_balance(self.get_balance() - amount)
            return True

        else:

            return False

    def set_balance(self, value):

        if value >= SavingAccount.MINIMUM:

            super().set_balance(value)

        else:

            super().set_balance(SavingAccount.MINIMUM)

    def __str__(self):

        return f'SAVING ACCOUNT: {super().__str__()}'


