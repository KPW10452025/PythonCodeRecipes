try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
#================================================
# An exception flew by!
# Traceback (most recent call last):
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p189_raise02.py", line 2, in <module>
#     raise NameError('HiThere')
# NameError: HiThere
#================================================
# 『編碼進行過程』
# 直接 try 一個人工錯誤：NameError('HiThere')
# 因為 try 後出錯，所以進入 except 
# except 會執行 print('An exception flew by!') 得到第一行
# 再執行 raise 得到第二、三、四行

# （報錯時，系統默認第一句）
# Traceback (most recent call last):

# （第二句為檔案位置，錯誤的位置，第幾行）
#   File "/Users/kuopowei/Developer/Python/PythonCodeRecipes/p189_raise02.py", line 2, in <module>

# （第三句為錯誤該行的編碼）
#     raise NameError('HiThere')

# （錯誤內容）
# NameError('HiThere')