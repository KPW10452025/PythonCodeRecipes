import math

class Sample():
    class_valt = math.pi

    def __init__(self, valt):
        self.instance_valt = valt

    def instance_method(self):
        print(self.class_valt) # math.pi
        print(self.instance_valt)
        print((self.instance_valt**2)*self.class_valt)

    @classmethod
    def class_method(cls):
        local_val = 100
        print(local_val)

    @staticmethod
    def static_method():
        local_val = 200
        print(local_val)

# 類方法：沒有實體方法仍然可以使用
Sample.class_method()
# 100

# 靜態方法：視為純公式
Sample.static_method()
# 200

print(Sample.class_valt)
# 3.141592653589793

print(Sample(10))
# <__main__.Sample object at 0x7fd8480b6f10>

print(Sample(10).instance_valt)
# 10

Sample(10).instance_method()
