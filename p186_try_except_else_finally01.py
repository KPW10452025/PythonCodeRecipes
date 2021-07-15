# How to use try except else finally

def DivNumber(a, b):
    try:
        val = a / b
        print("The result of {} / {} is {}".format(a, b, val))
    except:
        print("Please input correctly.")
    else:
        print("Processing ended normally.")
    finally:
        print("Processing is finished.")

print("DivNumber(10, 3)")
DivNumber(10, 3)
# DivNumber(10, 3)
# The result of 10 / 3 is 3.3333333333333335
# Processing ended normally.
# Processing is finished.

print("DivNumber(10, 0)")
DivNumber(10, 0)
# DivNumber(10, 0)
# Please input correctly.
# Processing is finished.

# try:
#     進行 try 程序
# except:
#     進行例外
# else:
#     當 try 正常進行完程序後，進行 else 程序
# finally:
#     無論是進行完 except 或是 else，最後都會進行 finally 程序