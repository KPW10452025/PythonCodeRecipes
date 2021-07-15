print(dir())
# 獲得當前模塊的屬性列表
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

class Sample():
    def __init__(self, x, y):
        self.x = x
        self.y = y

s = Sample(10, 20)
print(s.x) # 10
print(s.y) # 20
print(dir(s))
"""
 ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
 , '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__'
 , '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
 , '__weakref__', 'x', 'y']
"""

# hasattr() 函數用於判斷對像是否包含對應的屬性。
print(hasattr(s, "x")) # True
print(hasattr(s, "__class__")) # True
print(hasattr(s, "__Hello__")) # False