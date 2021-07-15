import package

result1 = package.mod1.SampleFunc(10, 20)
print(result1)
# 900

user001 = package.mod2.User("Tom", "Tom@gamil.com")
user002 = package.mod2.VIP("Cathy", "Cathy@gamil.com", "20210709", "20230709")

print(user001.name)
# Tom
print(user001.email)
# Tom@gamil.com
user001.UserInfo()
# name:  Tom
# email:  Tom@gamil.com

print(user002.name)
# Cathy
print(user002.email)
# Cathy@gamil.com
user002.UserInfo()
# name:  Cathy
# email:  Cathy@gamil.com

print(user002.startdate)
# 20210709
print(user002.overdate)
# 20230709
user002.VIPInfo()
# stardate:  20210709
# overdate:  20230709
