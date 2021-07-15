# os._exit()會直接將python程序終止，之後的所有代碼都不會繼續執行。
import os

try:
    os._exit(0)
except:
    print("over")
finally:
    print("finally over")
# 沒有任何輸出
