class Value:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value * (1 - instance.commission)

class Account:

    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(.05)
    new_account.amount = 100

    print(new_account.amount)