# __str__ 可以用來描述實體對象
# 當未使用 __str__ 時，print(實體對象)，非視覺化，會出現實體對象的記憶體位置 <__main__.實體對象 object at 記憶體座標>
# 使用 __str__ 後，print(實體對象)，可以 return 對實體對象的描述
# __str__功能：將實例對象按照自定義的格式用字符串的形式顯示出來，提高可讀性。

# 未使用__str__
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

# 使用__str__
class Cat1():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "The name of this cat is "+ self.name # return 描述內容

cat001 = Cat1("Tom", 3)
print(cat001.name)
# Tom
print(cat001.age)
# 3
print(cat001)
# The name of this cat is Tom
print(str(cat001))
# The name of this cat is Tom
