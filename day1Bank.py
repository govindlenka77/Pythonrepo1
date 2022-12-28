class NegativeValueError(Exception):
    pass


class bank:
    def __init__(self,bal):
        self.bal=bal


    def Withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount
        try:
            if(self.bal-self.withdraw_amount<0):
                raise NegativeValueError
            else:
                self.bal-=self.withdraw_amount
                print("{} is withdrawn from your account".format(self.withdraw_amount))
        #except ZeroDivisionError:
        #    print("Balance is insufficient")
        except TypeError:
            print("Wrong format of input")
        except NegativeValueError:
            print("Balance is insufficient")
        self.complete()

    def complete(self):
        print("Transaction completed")

    def deposit(self,deposit_amount):
        self.deposit_amount=deposit_amount
        self.bal+=self.deposit_amount
        print("{} is deposited ".format(self.deposit_amount))
        self.complete()

    def Balance(self):
        print("Your balance is {}".format(self.bal))

govi=bank(200)
govi.Withdraw(200)
govi.deposit(2000)
govi.Balance()