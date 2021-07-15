# __repr__ 與 __str__ 效果差異不大
# 未使用__repr__
class Cat2():
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat01 = Cat2("Tommy", 4)
print(cat01.name)
# Tommy
print(cat01.age)
# 4
print(cat01)
# <__main__.Cat2 object at 0x7fd3982fef70>

# 使用__repr__
class Cat1():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "The name of this cat is "+ self.name # return 描述內容

cat001 = Cat1("Tom", 3)
print(cat001.name)
# Tom
print(cat001.age)
# 3
print(cat001)
# The name of this cat is Tom
print(repr(cat001))
# The name of this cat is Tom

