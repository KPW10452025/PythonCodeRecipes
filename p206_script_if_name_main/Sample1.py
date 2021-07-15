import mod1

print("執行 Sample1.py")

# 「「「執行 print("執行 Sample1.py") 後，輸出的結果：」」」

# 執行 mod1
# 執行 Sample1.py

# 因為此時的 mod1.py 並沒有加入 if __name__ == "__main__":
# 所以當 main.py 中使用 import mod1 會把 mod1.py 的輸出結果一並都 import 過來

# mod1.py 檔案內容如下：
# =========================================
# def main():
#     print("執行 mod1")
#
# main()
# # 執行 mod1
# =========================================