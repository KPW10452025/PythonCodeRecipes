# traceback
# traceback.format_exc()

# 使用 traceback 和 traceback.format_exc()
# 將錯誤詳細內容打印出來
# 並且系統不會出錯

import traceback

try:
    x = 1 / 0
except Exception as e:
    print("錯誤情報：\n" + traceback.format_exc())

# 錯誤情報：
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p191_traceback.py", line 4, in <module>
#     x = 1 / 0
# ZeroDivisionError: division by zero

try:
    x = 1 / 0
except Exception as e:
    print("錯誤情報：\n", e)

# 錯誤情報：
#  division by zero
