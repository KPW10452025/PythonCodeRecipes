# use "for" and "in" in list 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [i + 10 for i in list1]
print(list2)
# [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# use "if" in list
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4 = [i for i in list3 if i % 2 == 0]
list5 = [i for i in list3 if i >= 6]
print(list4)
# [2, 4, 6, 8, 10]
print(list5)
# [6, 7, 8, 9, 10]

tuple1 = tuple(i + 2 for i in list1)
print(tuple1)
# (3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
