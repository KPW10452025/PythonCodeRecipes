dict1 = dict()
print(dict1) # {}
print(type(dict1)) # <class 'dict'>

dict2 = {}
print(type(dict2)) # <class 'dict'>
# 由此可以發現 直接令變數 = {} 時，系統是視為 dict 而非 set
set1 = set()
print(type(set1)) # <class 'set'>

dict2 = {"a" : "apple", "b" : "banana", "c" : "car"}
print(dict2) # {'a': 'apple', 'b': 'banana', 'c': 'car'}
print(dict2["a"]) # apple
print(dict2.get("a")) # apple

# get
print(dict2.get("d")) # None
# print(dict2["d"])
# KeyError: 'd'
# 使用 get 的好處就是，即使輸入的鍵無相對應的值，系統也不會報錯，而是回傳一個 None

# .keys() .values() .items()
print(dict2.keys()) # dict_keys(['a', 'b', 'c'])
print(dict2.values()) # dict_values(['apple', 'banana', 'car'])
print(dict2.items()) # dict_items([('a', 'apple'), ('b', 'banana'), ('c', 'car')])
# 我們可以把一個字典裡面的東西取出後做成 list
print(list(dict2.keys())) # ['a', 'b', 'c']
print(list(dict2.values())) # ['apple', 'banana', 'car']
print(list(dict2.items())) # [('a', 'apple'), ('b', 'banana'), ('c', 'car')]

# 確認某元素是否在 dict 裡
# 可以直接用 in 尋找鍵
print("a" in dict2) # True
# 但是尋找值時會找不到
print("apple" in dict2) #False
# 這時可以使用剛剛的技巧 .values()
print("apple" in dict2.values()) # True
print(("a", "apple") in dict2.items()) # True

# 增加新鍵值對
dict2["d"] = "door"
print(dict2) # {'a': 'apple', 'b': 'banana', 'c': 'car', 'd': 'door'}

# 減少、刪除、移除 鍵值對 del .pop()
del dict2["a"]
print(dict2) # {'b': 'banana', 'c': 'car', 'd': 'door'}

dict2.pop("c")
print(dict2) # {'b': 'banana', 'd': 'door'}

# 此時的.pop()不會默認最後一個，一定要指定一個鍵
# dict2.pop()
# print(dict2)
# TypeError: pop expected at least 1 argument, got 0

# .clear() 全刪除
dict2 = {"a" : "apple", "b" : "banana", "c" : "car", "d" : "Django", "e" : "elphant"}
print(dict2) # {'a': 'apple', 'b': 'banana', 'c': 'car', 'd': 'Django', 'e': 'elphant'}
dict2.clear()
print(dict2) # {}