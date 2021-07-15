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