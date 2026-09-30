import unittest
from employee import Employee # import class 'Employee'
class TestEmployee(unittest.TestCase):
    # test template
    def setUp(self):
        self.emp1 = Employee('Peter', 'Pan', 90000)
    # Test if email format is working properly
    def test_emailemployee(self):
        # Check if the email format is correct
        self.assertEqual(self.emp1.emailemployee, "ppan@email.com")
    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, "Peter Pan")
# test raise
    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.salary, 94500)
if __name__ == '__main__':
    unittest.main()