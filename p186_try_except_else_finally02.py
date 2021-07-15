# try except else finally 實務

# 在實務上開發時，不論是資料庫的連線或是檔案處理
# 最後運算完成都要把資源釋放，否則資源將耗盡或無法開啟檔案
# 在一般情況下，我們都會把釋放資源的程式碼放在運算的最後，如下範例：

names = ["swift", "python", "java", "flask", "django"]
try:
    file = open("p182_Error.py")
    seq = names.index("seiftUI") # 開啟檔案後，會在這裡出現錯誤，程式會跳到 except
    seq += 1
except:
    print("You got an error.")
finally:
    file.close()
# 運用 finally，這樣無論程式是否出錯，都一定會執行 file.close()

# 『不理想寫法一』
# names = ["swift", "python", "java", "flask", "django"]
# try:
#     file = open("p182_Error.py")
#     seq = names.index("seiftUI") # 開啟檔案後，會在這裡出現錯誤，程式會跳到 except
#     seq += 1 # 不執行
#     file.close() # 不執行，無法釋放資源
# except:
#     print("You got an error.")

# 『不理想寫法二』
# names = ["swift", "python", "java", "flask", "django"]
# try:
#     file = open("p182_Error.py")
#     seq = names.index("seiftUI") # 開啟檔案後，會在這裡出現錯誤，程式會跳到 except
#     seq += 1 # 不執行
# except:
#     print("You got an error.")
#     file.close()
#
# 此寫法有個問題就是
# 如果 seq = names.index() 沒有出錯，就又無法釋放資源了

# 『不理想寫法三』
# names = ["swift", "python", "java", "flask", "django"]
# try:
#     file = open("p182_Error.py")
#     seq = names.index("seiftUI") # 開啟檔案後，會在這裡出現錯誤，程式會跳到 except
#     seq += 1 # 不執行
# except:
#     print("You got an error.")
#     file.close()
# file.close()
#
# 雖然可以達到不論是否有例外錯誤，都能夠釋放資源
# 不過同樣的程式碼重複出現在應用程式中是不好的
# 除了容易出現 Bug 外，也不易維護


