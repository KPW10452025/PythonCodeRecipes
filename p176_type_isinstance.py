# type() and isinstance()
 
val1 = 100
val2 = "apple"
val3 = (1, 2, 3)
val4 = [1, 2, 3]
val5 = {1, 2, 3}
val6 = {1 : "apple", 2 : "banana"}
val7 = False

print(type(val1))
# <class 'int'>
print(type(val2))
# <class 'str'>
print(type(val3))
# <class 'tuple'>
print(type(val4))
# <class 'list'>
print(type(val5))
# <class 'set'>
print(type(val6))
# <class 'dict'>
print(type(val7))
# <class 'bool'>

print(isinstance(val1, int)) # True
print(isinstance(val1, str)) # False

#============================================

class Sample():
    pass

s = Sample()
print(isinstance(s, Sample)) # True

#============================================

class Sample1():
    pass
class Sample2(Sample1):
    pass
s1 = Sample1()
s2 = Sample2()

print(isinstance(s1, Sample1)) # True
print(isinstance(s1, Sample2)) # False
print(isinstance(s2, Sample1)) # True
print(isinstance(s2, Sample2)) # True

print(type(s1)) # <class '__main__.Sample1'>
print(type(s2)) # <class '__main__.Sample2'>
