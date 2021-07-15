# python的程序有兩中退出方式：os._exit()   sys.exit()
# sys.exit()會引發一個異常：SystemExit
# 如果這個異常沒有被捕獲，那麼python解釋器將會退出
# 如果有捕獲此異常的代碼，那麼這些代碼還是會執行
# 捕獲這個異常可以做一些額外的清理工作
# 0為正常退出，其他數值（1-127）為不正常，可拋異常事件供捕獲

import sys

try:
    sys.exit(0)
except:
    print("over")
finally:
    print("finally over")
# over
# finally over

# 使用 sys.exit(0) 退出程序
# 因為有用 try 所以會捕獲檔錯誤
# 故會執行 except 以及 finally
