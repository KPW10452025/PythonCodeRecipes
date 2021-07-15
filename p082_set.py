# list [1,2,3,4,5]
# tuple (1,2,3,4,5)
# set {1,2,3,4,5}

tuple2 = (1,2,3)
tuple3 = (1,3,2)

print(tuple2 == tuple3) # False

set2 = {1,2,3}
set3 = {1,3,2}

print(set2 == set3) # True 由此可知 set 無順序性

# add
set2.add(4)
print(set2) # {1, 2, 3, 4}
set2.add(4)
print(set2) # {1, 2, 3, 4} 由此可知 set 無重複性

# remove
set2.remove(2)
print(set2) # {1, 3, 4}

# clear
set2.clear()
print(set2) # set()

# 判斷元素數否在 set 裡面
set3 = {1,2,3,4,5,6,7}
print(2 in set3) # True
print(99 in set3) # False

set4 = {2,4,6,8,11,22,33}
set5 = {1,3,5,7,9,11,22,33}

# union 聯集
print(set4.union(set5)) # {1,2,3,4,5,6,7,8,9,11,22,33}
print(set4 | set5)      # {1,2,3,4,5,6,7,8,9,11,22,33}

# intersection 交集
print(set4.intersection(set5)) # {11,22,33}
print(set4 & set5)             # {11,22,33}

# difference 差集
print(set4.difference(set5)) # {2,4,6,8}
print(set4 - set5)           # {2,4,6,8}
print(set5.difference(set4)) # {1,3,5,7,9}
print(set5 - set4)           # {1,3,5,7,9}

# issubset 子集合
set6 = {1,3}
set7 = {1,2,3,4,5,6,7,8,9,11,22,33,44,55,66}
print(set4.issubset(set7)) # True
print(set6.issubset(set5)) # True

# issuperset 超集合
print(set4.issubset(set7)) # True
print(set6.issubset(set5)) # True

# len() sum() max() min()
print(len(set7)) # 15
print(sum(set7)) # 276
print(max(set7)) # 66
print(min(set7)) # 1