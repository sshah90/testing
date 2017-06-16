class circle:

    def __init__(self,radius,x,y):
        self.radius=radius
        self.x=x
        self.y=y

    def area(self):
        return 3.14*self.radius*self.radius

    def perimeter(self):
        return 2*3.14*self.radius

    def pw(self):
        return self.x**self.y

s=circle(12,2,3)
print(s.area())
print(s.perimeter())
print(s.pw())
