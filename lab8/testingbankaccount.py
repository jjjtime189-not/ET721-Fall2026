import unittest
from bankaccount import BankAccount # import class
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.emp1 = BankAccount('Owner', 90)
    def test_balance(self):
        self.assertEqual(self.emp1.balance, 90)
    def test_deposit(self):
        self.emp1.deposit(10)
        self.assertEqual(self.emp1.balance, 100)
    def test_withdraw(self):
            self.emp1.withdraw(10)
            self.assertEqual(self.emp1.balance, 80)
    def test_withdraw_failed(self):
            self.emp1.withdraw(100)
            self.assertEqual(self.emp1.balance, -10)
    def test_sequence(self):
                self.emp1.deposit(10)
                self.assertEqual(self.emp1.balance, 100)
                self.emp1.withdraw(20)
                self.assertEqual(self.emp1.balance, 80)
                self.emp1.deposit(30)
                self.assertEqual(self.emp1.balance, 110)
                self.emp1.withdraw(40)
                self.assertEqual(self.emp1.balance, 70)
if __name__ == '__main__':
    unittest.main()