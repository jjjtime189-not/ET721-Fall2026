def addnumbers(a=0, b=0):
    return a + b
def subtractingnumbers(a=0, b=0):
    return a - b
def multiplynumbers(a=1, b=1):
    return a * b
def dividenumbers(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error! Can't divide by zero")
    except ValueError:
        print("ERROR! not a numerical value")
    except:
        print("ERROR! Can't divide the numbers")