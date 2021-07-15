# https://www.runoob.com/python/python-func-map.html

def func1(x1):
    return "apple " + str(x1) + " apple"

print(func1(123))
# apple 123 apple
print(func1("Tom"))
# apple Tomapple

func2 = lambda x1: "banana " + str(x1) + " banana"

print(func2(123))
# banana 123 banana
print(func2("Tom"))
# banana Tom banana

func3 = lambda *args: sum(args)
print(func3(1, 2, 3, 4, 5))
# 15

fruits_list = ["apple", "banana", "orange"]
for fruit in map(lambda x: "Taiwan " + str(x), fruits_list):
    print(fruit)
# Taiwan apple
# Taiwan banana
# Taiwan orange

# map 用法
# map(function, iterable, ...)
# Python 3.x 返回迭代器

print(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
# <map object at 0x7fb710192fd0>

for answer in  map(lambda x: x ** 2, [1, 2, 3, 4, 5]):
    print(answer)
# 1
# 4
# 9
# 16
# 25

print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
# [1, 4, 9, 16, 25]
