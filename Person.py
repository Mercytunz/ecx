class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def addAge(self,n):
        if type(n) is not int:
            print("AssertionError")
        else:
            return f"{self.name} will be {self.age + n} in the next {n} years"
    def printUser(self):
        return f"{self.name} is {self.age} years old"
babs = Person("Babatunde", 20)
print(babs.addAge(10))
print(babs.addAge("a"))
print(babs.printUser())

        
        
        