# 在 set 中使用 for 和 in 從 list 生成 set
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set1 = {i + 10 for i in list1}
print(set1)
# {11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
print(type(set1))
# <class 'set'>

# 在 set 中使用 for 和 in 從 set 生成新 set
set2 = {i - 5 for i in set1}
print(set2)
# {6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(type(set2))
# <class 'set'>

set3 = {i for i in set1 if i % 2 == 1}
print(set3)
# {11, 13, 15, 17, 19}
