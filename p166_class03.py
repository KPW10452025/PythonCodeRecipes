class apple1():
    class01 = 100
    class02 = "banana"
    def __init__(self):
        pass

print(apple1.class01)
# 100
print(apple1.class02)
# banana

apple1.class01 = 200
print(apple1.class01)
# 200

A = apple1()
print(A.class01, apple1.class01)
# 200 200
A.class01 = 300
print(A.class01, apple1.class01)
# 300 200