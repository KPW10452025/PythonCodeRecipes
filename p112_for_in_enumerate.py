# enumerate
list1 = ["a", "b", "c", "d", "e", "f", "g"]
print(enumerate(list1))
print(list(enumerate(list1)))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')]
print(list(enumerate(list1, start=1)))
# [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g')]

for i in enumerate(list1):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')

for i in enumerate(list1, start=1):
    print(i)
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')
# (5, 'e')
# (6, 'f')
# (7, 'g')

for i, j in enumerate(list1, start=1):
    print(i, j)
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f
# 7 g

# 運用
list2 = [23, 3, 2, 34, 86, 89]
num2 = 1000
for i, j in enumerate(list2):
    list2[i] = num2 + j
print(list2)
# [1023, 1003, 1002, 1034, 1086, 1089]

list3 = ["白羅波", "高麗菜", "番茄", "大蔥"]
title3 = "台灣生鮮超市"
for i, j in enumerate(list3):
    list3[i] = title3 + j
print(list3)
# ['台灣生鮮超市白羅波', '台灣生鮮超市高麗菜', '台灣生鮮超市番茄', '台灣生鮮超市大蔥']
