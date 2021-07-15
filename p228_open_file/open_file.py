# Open file in Python

# open("file path", "mode", encoding="encode")
# open("sample.txt", "r", encoding="utf-8")

# mode
# "r", for reading.
# "w", for writing.
# "a" , for appending.
# "r+", for both reading and writing

# file01 = open("sample.txt", "r", encoding="utf-8")
# file01.close()

with open("sample01.txt", "r") as open_sample01_txt:
    sample01_txt_read = open_sample01_txt.read()
print(sample01_txt_read)
# Hello, this is a file for leaning open file in Python3.
# This is an apple.
# There have several frameworks.
# You can use Flask, Django to build a website.

# How to use .read() .readlines() .readline()

with open("sample02.txt", "r") as open_sample02_txt:
    sample02_txt_read = open_sample02_txt.read()
print(sample02_txt_read)
# aaaa
# bbbb
# cccc

with open("sample02.txt", "r") as open_sample02_txt:
    sample02_txt_readlines = open_sample02_txt.readlines()
print(sample02_txt_readlines)
# ['aaaa\n', 'bbbb\n', 'cccc']

with open("sample02.txt", "r") as open_sample02_txt:
    sample02_txt_readline = open_sample02_txt.readline()
print(sample02_txt_readline)
# aaaa
