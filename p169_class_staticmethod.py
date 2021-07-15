class Sample():
    class_valt = 1

    def __init__(self, valt):
        self.instance_valt = valt

    def instance_method(self):
        print(self.class_valt, self.instance_valt)

    @classmethod
    def class_method(cls):
        local_val = 100
        print(local_val)

    @staticmethod
    def static_method():
        local_val = 200
        print(local_val)

s= Sample(10)

s.instance_method()
# 1 10

s.class_method()
# 100
Sample.class_method()
# 100

s.static_method()
# 200
Sample.static_method()
# 200
