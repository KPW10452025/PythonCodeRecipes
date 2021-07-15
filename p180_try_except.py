# How to use "try" and "except"

def DivNum1(a, b):
    result = a / b
    print(result)

# It is ok when 2 / 10
DivNum1(2, 10)
# 0.2

# when 2 / 0, it will get error
# DivNum1(2, 0)
# ZeroDivisionError: division by zero

def DivNum2(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("The number of b need to larger than 0.")

DivNum2(2, 0)
# The number of b need to larger than 0.

# DivNum2(2, "apple")
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

def DivNum3(a:int, b:int) -> float :
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("The number of b need to larger than 0.")
    except TypeError:
        print("Variable a and b are numbers.")
    except:
        print("Please input correctly.")

DivNum3(10, 3)
# 3.3333333333333335
DivNum3(10, 0)
# The number of b need to larger than 0.
DivNum3(10, "apple")
# Variable a and b are numbers.

def DivNum4(a:int, b:int) -> float :
    try:
        result = a / b
        print(result)
    except:
        print("Please input correctly.")

DivNum4(100000, 0)
# Please input correctly.
DivNum4("apple", {1,2,3})
# Please input correctly.
