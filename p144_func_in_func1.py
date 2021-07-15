def func1():
    print("this is print by func1.")
    def func2():
        print("this is print by func2.")
    func2()

func1()
# this is print by func1.
# this is print by func2.
