# classmethod 類方法
# staticmethod 靜態方法

# Python面向對象編程中，類中定義的方法可以是 @classmethod 裝飾的 類方法
# 也可以是 @staticmethod 裝飾的 靜態方法
# 用的最多的還是不帶裝飾器的 實體方法

class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        print(n)

# m1 是實體方法，第一個參數必須是 self（約定俗成的）
# m2 是類方法，第一個參數必須是cls（同樣是約定俗成）
# m3 是靜態方法，參數根據業務需求定，可有可無。

a = A()

# 「實體方法」
print(A.m1) # <function A.m1 at 0x7f9b081da4c0>
print(a.m1) # <bound method A.m1 of <__main__.A object at 0x7f8ea0149f10>>

A.m1(a, 1)  # self: <__main__.A object at 0x000001E596E41A90>
a.m1(1)     # self: <__main__.A object at 0x000001E596E41A90>
# A.m1(1)   # TypeError: m1() missing 1 required positional argument: 'n'

# A.m1是一個還沒有綁定實體對象的方法，對於未綁定方法，調用 A.m1 時必須顯示地傳入一個實體對象進去
# a.m1是已經綁定了實體的方法，python隱式地把對像傳遞給了self參數，所以不再手動傳遞參數，這是調用實體方法的過程

# 「類方法」
A.m2(1)     # cls: <class '__main__.A'>
a.m2(1)     # cls: <class '__main__.A'>

print(A.m2) # <bound method A.m2 of <class '__main__.A'>>
print(a.m2) # <bound method A.m2 of <class '__main__.A'>>

# m2是類方法，不管是A.m2 還是a.m2，都是已經自動綁定了類對象A的方法，對於後者，因為python可以通過實體對象a找到它所屬的類是A，找到A之後自動綁定到cls。

# 「靜態方法」
# m3是裡面的一個實體方法，跟普通函數沒有什麼區別
# 類和實體都沒有關聯的關係，它確實是碰巧類中的一個真實存在的方法。
A.m3(1)
# 1
a.m3(1)
# 1
A.m3("apple")
# apple
a.m3("apple")
# apple


