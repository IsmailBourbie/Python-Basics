# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:22:07 2019

@author: Ismail Bourbie
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    
    def __str__(self):
        """
            this method called when you try ti print an object of this class
        """
        return "<" + str(self.x) + "," + str(self.y) + ">"
        

c = Coordinate(3, 4)

other_c = Coordinate(0, 0)

print(c.x)

print(c.distance(other_c)) ## 1
## 1 equivalent to 2
print(Coordinate.distance(c, other_c)) ## 2

print(c) ## use __str__ to print the object informations