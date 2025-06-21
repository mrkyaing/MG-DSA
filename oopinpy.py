from math import *

class Point:
    x= 0
    y= 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def set_location(self, x, y):
        self.x = x
        self.y = y
    def get_location(self):
        return (self.x, self.y)
    def distance_from_origin(self):
        return sqrt(self.x*self.x + self.y*self.y)
    def distance_from(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx*dx + dy*dy)
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy
p=Point()
p.set_location(3, 4)
print('Location:',p.get_location())
print('Distance from origin:',p.distance_from_origin())
p2=Point()
p2.set_location(6, 8)
print('Distance from p to p2:',p.distance_from(p2))
p.translate(1, 1)
print('New location of p:',p.get_location())
