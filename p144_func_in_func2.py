def func1(f):
    def new_func():
        print("start func1")
        f()
        print("over func1")
    return new_func()
def func2():
    print("doing something func2")

func1(func2)
# start func1
# doing something func2
# over func1

def func3(f):
    def new_func():
        print("start func3")
        f()
        print("over func3")
    return new_func
def func4():
    print("doing something func4")

func5 = func3(func4)
func5()
# start func3
# doing something func4
# over func3


def add_message(f):
    def new_func():
        print('start add_message')
        f()
        print('over add_message')
    return new_func
@add_message
def sample_func():
    print("doing something sample_func")

sample_func()
# start add_message
# doing something sample_func
# over add_message