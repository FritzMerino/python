import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def test__init__(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 100
        assert self.a1.deposit(-100) is False
        assert self.a1.get_balance() == 100

    def test_withdraw(self):
        self.a1.deposit(150)
        assert self.a1.withdraw(100) is True
        assert self.a1.get_balance() == 50
        assert self.a1.withdraw(-50) is False
        assert self.a1.get_balance() == 50
        assert self.a1.withdraw(51) is False
        assert self.a1.get_balance() == 50
