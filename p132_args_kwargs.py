def say_hello1():
    print("Hello!1!")

say_hello1()
# Hello!1!

# 隨意放入變數到 formula 裡面會報錯
# say_hello1("apple")
# TypeError: say_hello() takes 0 positional arguments but 1 was given

# 使用 *args 解決這問題 arg = arguement
def say_hello2(*args):
    print("Hello!2!")

say_hello2()
# Hello!2!
say_hello2("123")
# Hello!2!
say_hello2(9934)
# Hello!2!

# 放入 x4 = 100 會報錯
# say_hello2(x4 = 100)
# TypeError: say_hello2() got an unexpected keyword argument 'x4'

def say_hello3(*args):
    print("Hello!2!", args) 

say_hello3()
# Hello!2! ()
say_hello3(777)
# Hello!2! (777,)
say_hello3("apple")
# Hello!2! ('apple',)

# 放入 x4 = 100 會報錯
# say_hello3(x4 = 100)
# TypeError: say_hello3() got an unexpected keyword argument 'x4'

# 使用 **kwargs
def say_hello4(*args, **kwargs):
    print("Hello!4!")
say_hello4()
# Hello!4!
say_hello4(777)
# Hello!4!
say_hello4("apple")
# Hello!4!
say_hello4(x4 = 100)
# Hello!4!

def say_hello5(*args, **kwargs):
    print("Hello!5!", args, kwargs)
say_hello5()
# Hello!5! () {}
say_hello5(777)
# Hello!5! (777,) {}
say_hello5("apple")
# Hello!5! ('apple',) {}
say_hello5(x4 = 100)
# Hello!5! () {'x4': 100}
say_hello5("x4", x4 = 100)
# Hello!5! ('x4',) {'x4': 100}

def RectangleAreaFormula1(x, y):
    return x * y

def RectangleAreaFormula2(x, y, *args, **kwargs):
    return x * y

# print(RectangleAreaFormula1(4, 5, 6))
# TypeError: RectangleAreaFormula1() takes 2 positional arguments but 3 were given

print(RectangleAreaFormula2(4, 5, 6))
# 20
