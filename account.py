class Account:
    """
    A class object representing details of a person's name and account balance.
    """
    def __init__(self, name: str) -> None:
        """
        Method to set default values of a new Account object.
        :param name: The person's name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> bool:
        """
        Method to deposit a given amount into the person's account.
        :param amount: The amount to deposit.
        :return: True if the deposit was successful, False otherwise.
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: int) -> bool:
        """
        Method to withdraw a given amount from the person's account.
        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> int:
        """
        Method to get the person's balance account.
        :return: It returns an integer.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to get the person's name.
        :return: It returns a string.
        """
        return self.__account_name
