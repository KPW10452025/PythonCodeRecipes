list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dict1 = {i : "taiwan" for i in list1}
print(dict1)
# {1: 'taiwan', 2: 'taiwan', 3: 'taiwan', 4: 'taiwan', 5: 'taiwan', 6: 'taiwan', 7: 'taiwan', 8: 'taiwan', 9: 'taiwan', 10: 'taiwan'}

list2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
dict2 = {i : j for i, j in zip(list1, list2)}
print(dict2)
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

dict3 = {i+10 : j+"+ten" for i, j in zip(dict2.keys(), dict2.values())}
print(dict3)
# {11: 'one+ten', 12: 'two+ten', 13: 'three+ten', 14: 'four+ten', 15: 'five+ten', 16: 'six+ten', 17: 'seven+ten', 18: 'eight+ten', 19: 'nine+ten', 20: 'ten+ten'}
