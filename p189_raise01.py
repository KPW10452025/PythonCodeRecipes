x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
#================================================
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p189_raise.py", line 3, in <module>
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
# Exception: x 不能大于 5。x 的值为: 10
#================================================
# 『編碼進行過程』
# 令 x 等於 10，若 x 大於 5 則 使用 raise 人工報錯：

# （報錯時，系統默認的第一句）
# Traceback (most recent call last):

# （第二句為檔案位置，錯誤的位置，第幾行）
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p189_raise01.py", line 3, in <module>

# （第三句為錯誤該行的編碼）
    # raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# （錯誤內容）
# Exception: x 不能大于 5。x 的值为: 10

