# what is .ini ?

# An INI file is a configuration file for computer software that consists of a text-based
# content with a structure and syntax comprising key–value pairs for properties
# , and sections that organize the properties.

# INI 檔案格式是應用在電腦軟體上的設定檔，是以一種以文字所組成的特殊結構語法。
# 其內容可能有多個 section 區段，且每個 section 區段都有各自的多個屬性，每個屬性都是 key-value 為一組所構成。
# 起初 ini 檔被廣泛應用在 Windows 作業系統中，這個格式後來變成了一種非正式的標準並且被其他作業系統與應用程式當設定檔儲存使用。
# 另外有些應用程式可能改用 .conf 或 .cfg 這種副檔名。

# 簡單的 .ini 設定檔內容如下所示：(sample01.ini)
# [http]
# host = https://www.google.com
# port = 80

# 要寫一個可以讀取這個 ini 設定檔的 python 程式
# 必須要能解析 ini 檔的內容結構
# 而 python 內建已經提供了 configparser 模組替我們完成這件事

# get()
# getint()
# getfloat()
# getbollean()

import configparser # import configparser 以用來分析 ini 檔案

config = configparser.ConfigParser()
config.read("sample01.ini")

host = config["http"]["host"]
port = config["http"]["port"]

print(host)
# https://www.google.com
print(port)
# 80
print(type(port))
# <class 'str'>     # 會發現這裡輸出的 port 是 80 但 type 是 str 字串，而非 int

# configparser 也有提供直接轉成 int 的函式叫 getint() 實際用法如下所示，這樣使用後就直接可以取得 int 整數
port02 = config["http"].getint("port")
print(port02)
# 80
print(type(port02))
# <class 'int'>


