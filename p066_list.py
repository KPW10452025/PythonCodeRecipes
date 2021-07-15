list1 = list("AppleAndWsift")
print(list1)
# ['A', 'p', 'p', 'l', 'e', 'A', 'n', 'd', 'W', 's', 'i', 'f', 't']

list2 = list(range(10))
print(list2)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list3 = list(range(1,11))
print(list3)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list4 = list(range(len("apple")))
print(list4)
# [0, 1, 2, 3, 4]

list5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list5[0:11:2]) # [0, 2, 4, 6, 8, 10]
print(list5[:11:2])  # [0, 2, 4, 6, 8, 10]
print(list5[0::2])   # [0, 2, 4, 6, 8, 10]
print(list5[::2])    # [0, 2, 4, 6, 8, 10]

# list [1,2,3,4,5]
# tuple (1,2,3,4,5)
# set {1,2,3,4,5}