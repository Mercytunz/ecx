class circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 22/7
    def computeArea(self):
        return self.pi * self.radius**2
    def computeCircum(self):
        return 2 * self.pi * self.radius
    
a = circle(7)
print(a.computeArea())
print(a.computeCircum())
        