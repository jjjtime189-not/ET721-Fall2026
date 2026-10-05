def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
#exercise 2
def validate_password(password):
    if len(password) < 8:
        return False
    return any(char.isdigit() for char in password)
#exercise 3
def is_even(n):
    return n % 2 == 0 and n!=0