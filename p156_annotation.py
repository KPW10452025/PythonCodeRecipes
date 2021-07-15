# Annotation
# アノテーション
# 註解

a1 : int = 100
print(a1)
# 100

# 真的是“註解”，而非型別宣告，所以不依照註解設定變數，也不會怎樣。
a2 : int = "apple"
print(a2)
# apple

def AddTwoNumber(num1 : int, num2 : int) -> int :
    return num1 + num2
answer1 = AddTwoNumber(10, 35)
print(answer1)
# 45
