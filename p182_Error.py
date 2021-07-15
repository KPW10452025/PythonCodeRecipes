# https://www.runoob.com/python/python-exceptions.html

# 常見 Error 簡介

# AttrubuteError 對像沒有這個屬性
str1 = "apple"
# x = str1.a
# AttributeError: 'str' object has no attribute 'a'
# 當把 ｘ 另為 str1.a 時，系統會出錯。因為 str1 並沒有 a 這個屬性。

# IndexError 序列中沒有此索引(index)
list1 = [1, 2, 3]
# x = list1[5]
# IndexError: list index out of range
# 當把 ｘ 另為 list1[5] 時，系統會出錯。因為 list1[5] 超出 list1 故有序列。

# KeyError 映射中沒有這個鍵
dict1 = {1 : "swift", 2 : "python"}
# x = dict1[6]
# KeyError: 6
# 當把 ｘ 另為 dict1[6] 時，系統會出錯。因為 dict1 並沒有 6 這個鍵位。

# TypeError 對類型無效的操作
# x = len(300)
# TypeError: object of type 'int' has no len()
# 當把 ｘ 另為 len(300) 時，系統會出錯。因為 int 類型無法使用 len()。

# ValueError 傳入無效的參數
# x = int("python")
# ValueError: invalid literal for int() with base 10: 'python'
# 當把 ｘ 另為 int("python") 時，系統會出錯。因為 "python" 無法變成 int。

# ZeroDivisionError
# x = 3 / 0
# ZeroDivisionError: division by zero
# 除法錯誤。

