list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = ["A", "B", "C", "D", "E"]

for x, y in zip(list1, list2):
    print(x, y)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e

for x, y, z in zip(list1, list2, list3):
    print(x, y, z)
# 1 a A
# 2 b B
# 3 c C
# 4 d D
# 5 e E

list4 = [1, 2, 3, 4, 5]
list5 = ["a", "b", "c"]
list6 = ["Apple", "Bootstrap", "C++", "Django"]

for x, y, z in zip(list4, list5, list6):
    print(x, y, z)
# 1 a Apple
# 2 b Bootstrap
# 3 c C++