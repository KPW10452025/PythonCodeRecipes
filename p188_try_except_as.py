def div_number(a, b):
    try:
        val = a / b
        print(val)
    except Exception as e:
        print(e)

div_number(10, 3)
# 3.3333333333333335

div_number("apple", 10)
# unsupported operand type(s) for /: 'str' and 'int'

div_number(3, 0)
# division by zero
