class Employee:
    raise_amt = 1.05
    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary
    # The @property decorator indicates that the emailemployee method will behave like an attribute
    @property
    def emailemployee(self):
        return f"{self.first[0].lower()}.{self.last}@email.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

e= Employee("Peter", "Pan", 90000)
print(e.emailemployee)
print(f'Current salary = {e.salary}')
e.apply_raise()
print(f'After raising the salary = {e.salary}')
