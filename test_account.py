import pytest
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def test__init__(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.deposit(0) is False
        assert self.a1.deposit(1) is True
        assert self.a1.get_balance() == pytest.approx(1)

    def test_withdraw(self):
        assert self.a1.withdraw(-2) is False
        assert self.a1.withdraw(0) is False
        self.a1.deposit(2)
        assert self.a1.withdraw(3) is False
        assert self.a1.withdraw(1) is True
        assert self.a1.get_balance() == pytest.approx(1)
