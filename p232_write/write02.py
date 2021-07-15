text = """這是一篇練練習使用 with open 的短文練習
with open("被寫入檔案名稱", "w" ,encoding="utf-8") as 隨意名稱01
    隨意名稱01.write(寫入內容)
"""

with open("sample02.txt", "w", encoding="utf-8") as open_sample02_txt_and_write:
    open_sample02_txt_and_write.write(text)
