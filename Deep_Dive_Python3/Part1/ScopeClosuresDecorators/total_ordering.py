from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    def __abs__(self):# call built absoulte function on a point obje
        return sqrt(self.x **2 + self.y **2)
    
    def __repr__(self):
        return 'Point({0}, {1})'.format(self.x, self.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False 
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented