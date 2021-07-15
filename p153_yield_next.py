# https://www.runoob.com/python3/python3-iterator-generator.html

def func1():
    print("start 1")
    yield "apple"
    print("start 2")
    yield "banana"
    print("start 3")
    yield "orange"

func1()
# 無反應
gen1 = func1()
print(gen1)
# <generator object func1 at 0x7fb9781af7b0>
print(next(gen1)) # 第一次迭代
# start 1
# apple
print(next(gen1)) # 第二次迭代
# start 2
# banana
print(next(gen1)) # 第三次迭代
# start 3
# orange
# print(next(gen1)) # 第四次迭代會報錯 StopIteration

#=============================================================
def func2():
    print("start 1")
    yield "apple"
    print("start 2")
    yield "banana"
    print("start 3")
    yield "orange"
gen2 = func2()
for x in gen2:
    print(x)
# start 1
# apple
# start 2
# banana
# start 3
# orange
#=============================================================

def fab1(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        print(b)
        a, b = b, a + b 
        n = n + 1
fab1(5)
# 1
# 1
# 2
# 3
# 5

def fab2(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        a, b = b, a + b 
        n = n + 1
print(list(fab2(5)))
# [1, 1, 2, 3, 5]
for n in fab2(5): 
    print(n)
# 1
# 1
# 2
# 3
# 5
