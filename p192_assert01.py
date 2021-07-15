# assert assertion assertionerror

# 當 assert 後面的條件是 False 時執行

# 語法格式：
# assert expression
# 等價於：
# if not expression:
#     raise AssertionError

# 語法格式：
# assert expression [, arguments]
# 等價於：
# if not expression:
#     raise AssertionError(arguments)

# 範例測試

assert True 

# assert False
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p192_assert.py", line 15, in <module>
#     assert False
# AssertionError

assert 1==1

# assert 1==2
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p192_assert.py", line 27, in <module>
#     assert 1==2
# AssertionError

# assert 1==2, "大家都知道一不等於二"
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p192_assert.py", line 35, in <module>
#     assert 1==2, "大家都知道一不等於二"
# AssertionError: 大家都知道一不等於二