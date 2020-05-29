class Point:
    def __init__(self, *pnt):
        self.__pnt = pnt
    def set_pnt(self, *pnt):
        self.__pnt = pnt
    def get_pnt(self):
        return self.__pnt
    def __add__(self, other):
        return Point(self.__pnt[0] + other.__pnt[0],\
            self.__pnt[1] + other.__pnt[1])
    def __sub__(self, other1):
        return Point(self.__pnt[0] - other1.__pnt[0],\
            self.__pnt[1] - other1.__pnt[1])
    def __mul__(self, other1):
        return Point(self.__pnt[0] * other1.__pnt[0],\
            self.__pnt[1] * other1.__pnt[1])
    def distance(self, other2):
        return (((self.__pnt[0] - other2.__pnt[0])**2 \
            + (self.__pnt[1] - other2.__pnt[1])**2)**0.5)
    
    def __str__(self):
        return str(self.get_pnt())
        
    

a = Point(1, 5)
b = Point(3, 5)

c = a + b
d = a - b
e = a * b


print(str(c))
print(str(d))
print(str(e))
print(a.distance(b))
