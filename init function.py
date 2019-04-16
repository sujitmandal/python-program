#This programe is create by SUjit Mandal

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getname(self):
        print('yor bane is:' + self.name)
    def getage(self):
        print("your age is:" + self.age)

p = person("sujit", "25")

p.getname()
p.getage()