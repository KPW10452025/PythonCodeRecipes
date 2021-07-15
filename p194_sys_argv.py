# 命令行參數
# import sys
# sys.argv

# 平時在 terminal 會輸入 python3 p194_sys_argv.py 以執行本檔案
# 但因為今天這個檔案有 import sys
# 所以可以在 python3 p194_sys_argv.py 後面放入一些參數
# 這些參數稱為「命令行參數」

# 在 terminal 輸入 python3 p194_sys_argv.py 12345678 apple 3.14
# 12345678 和 apple 和 3.14 就是「命令行參數」

from sys import argv

print(argv)
# ['p194_sys_argv.py', '12345678', 'apple', '3.14']

print(str(argv))
# ['p194_sys_argv.py', '12345678', 'apple', '3.14']

print(argv[0])
# p194_sys_argv.py

print(argv[1])
# 12345678

print(argv[2])
# apple

print(argv[3])
# 3.14

print(len(argv))
# 4
