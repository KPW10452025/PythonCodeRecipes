# "Private 變數" and "Private method"

# 未使用 Private
class Sample1():
    def __init__(self, val1):
        self.instance_val1 = val1

    def private_method(self):
        print(self.instance_val1)

s1 = Sample1(777)
print(s1.instance_val1)
# 777
s1.private_method()
# 777

# 使用 Private
class Sample2():
    def __init__(self, val1):
        self.__instance_val1 = val1 # 加上雙底線

    def __private_method(self): # 加上雙底線
        print(self.__instance_val1)

s2 = Sample2(888)
# print(s2.__instance_val1)
# 我們會得到錯誤資訊如下
# AttributeError: 'Sample2' object has no attribute '__instance_val1'

# s2.__private_method()
# 我們會得到錯誤資訊如下
# AttributeError: 'Sample2' object has no attribute '__private_method'

# 破解方法
print(s2._Sample2__instance_val1) # 加上 _Sample2
# 888
s2._Sample2__private_method() # 加上 _Sample2
# 888
