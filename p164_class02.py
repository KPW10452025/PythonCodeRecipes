class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def UserInfo(self):
        print("name: ", self.name)
        print("email: ", self.email)

class VIP(User):
    def __init__(self, name, email, startdate, overdate):
        super().__init__(name, email)
        self.startdate = startdate
        self.overdate = overdate
    def VIPInfo(self):
        print("stardate: ", self.startdate)
        print("overdate: ", self.overdate)

user001 = VIP("Tom", "Tom@gmail.com", "20200123", "20220123")
print(user001.name)
# Tom
print(user001.email)
# Tom@gmail.com
print(user001.startdate)
# 20200123
print(user001.overdate)
# 20220123
user001.UserInfo()
# name:  Tom
# email:  Tom@gmail.com
user001.VIPInfo()
# stardate:  20200123
# overdate:  20220123
