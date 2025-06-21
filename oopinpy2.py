from math import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other):
        dx= self.x - other.x
        dy = self.y - other.y
        return sqrt(dx*dx + dy*dy)
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p1= Point(3, 4)
p2= Point(6, 8)
print("Point p1:", p1)
print("Point p2:", p2)
print("Distance from origin for p1:", p1.distance_from_origin())
print("Distance from origin for p2:", p2.distance_from_origin())
print("Distance from p1 to p2:", p1.distance(p2))
p1.translate(2, 3)
print("After translating p1 by (2, 3):", p1)
p2.translate(-1, -1)
print("After translating p2 by (-1, -1):", p2)
print("Distance from p1 to p2 after translation:", p1.distance(p2))
print("Distance from origin for p1 after translation:", p1.distance_from_origin())
print("Distance from origin for p2 after translation:", p2.distance_from_origin())
print("Final coordinates of p1:", p1)
Point.translate(p1, 1, 1)  # This will not change p1 since translate is an instance method
print("After trying to translate p1 using class method (no change):", p1)