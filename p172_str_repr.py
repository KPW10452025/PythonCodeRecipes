class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        print("我是str")
        return "Student from str (%s,%d)"%(self.name,self.age)
    def __repr__(self):
        print("我是repr")
        return "Student form repr(%s,%d)"%(self.name, self.age)

stu1 = Student("Webb", 32)

print(stu1)
# 我是str
# Student from str (Webb,32)

print(str(stu1))
# 我是str
# Student from str (Webb,32)

print(repr(stu1))
# 我是repr
# Student form repr(Webb,32)
