import os

for a in os.environ.items():
    print(a)

print(type(os.environ))
# <class 'os._Environ'>

# 可以用 os.environ["鍵"] 尋找相對的值
print(os.environ["USER"])
# kuopowei

# 但是 os.environ["鍵"] 的"鍵"不存在時，系統會出錯
# print(os.environ["apple"])
# KeyError: 'apple'

# 為避免此問題，os.environ 可以使用 get() 介面從物件讀取
# 如果尚未定義查詢的環境變數，則 get() 返回 None。
print(os.environ.get('USER'))
# kuopowei

print(os.environ.get('apple'))
# None

# 替代 os.environ.get() 的方法是使用 os.getenv() 功能
# 這兩個函式的工作原理相同，你可以將後者視為便捷的 API。
print(os.getenv('USER'))
# kuopowei

print(os.getenv('apple'))
# None

