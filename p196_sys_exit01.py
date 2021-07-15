# import sys
# sys.exit(1)

# 當使用 sys.exit(1) 時，會退出程序
# 這也是經常使用的方法，也不需要考慮平台等因素的影響，一般是退出Python程序的首選方法
 
import sys # 執行
print("start!") # 執行
print("finish!") # 執行
sys.exit(1) # 執行並退出程序
print("start again after sys.exit")
if 1==1:
    print("1 = 1")
else:
    print("an apple")


# 得到的結果是
# start!
# finish!

# 只有 sys.exit(1) 以前的程式碼會出現，之後的程式碼都被強制結束了