import mod2

print("執行 Sample2.py")

# 「「「執行 print("執行 Sample2.py") 後，輸出的結果：」」」

# 執行 Sample2.py

# 因為此時的 mod2.py 已經加入 if __name__ == "__main__":
# mod2.py 的輸出結果不會因為任何檔案 import 而被傳送出去

# mod2.py 檔案內容如下：
# =========================================
# def main():
#     print("執行 mod1")
#
# if __name__ == "__main__":
#     main()
#     print("這是 mod2.py 檔案內部測試")
# # 執行 mod1
# # 這是 mod2.py 檔案內部測試
# =========================================