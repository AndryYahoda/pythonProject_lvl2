class Client:
    """
    A class to manage a client's financial account, including operations like withdrawal, deposit, and transfer.
    """
    def __init__(self, name: str, balance: float, checking_account: bool) -> None:
        """
        Initializes a new client with a name, balance, and checking account status.
        :param name: The name of the client.
        :param balance: The initial balance of the client's account.
        :param checking_account: A boolean indicating if the client has a checking account.
        """
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraws_money(self, amount: float) -> str:
        """
        Withdraws a specified amount from the client's balance, if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: A message indicating the remaining balance.
        """
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount
        return f'на рахунку у {self.name} в залишку {self.balance}'

    def transfer(self, other: 'Client', amount: float) -> str:
        """
        Transfers a specified amount to another client's account, if both accounts are validated.
        :param other: The recipient client.
        :param amount: The amount to transfer.
        :return: A message indicating the updated balances for both clients.
        """
        if not other.checking_account:
            raise ValueError("Аккаунт не валідується.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку для переведення.")
        self.balance -= amount
        other.balance += amount
        return f'на рахунку у {self.name} в залишку {self.balance}, а у {other.name} в залишку {other.balance}'

    def replenishes_the_account(self, amount: float) -> str:
        """
        Adds a specified amount to the client's balance.
        :param amount: The amount to deposit.
        :return: A message indicating the new balance.
        """
        self.balance += amount
        return f'на рахунку у {self.name} в залишку {self.balance}'


Taras = Client('Тарас', 120, True)
Stepan = Client('Степан', 95, False)

print(Taras.withdraws_money(2))
Stepan.checking_account = True
print(Stepan.transfer(Taras, 25))
print(Stepan.replenishes_the_account(20))
