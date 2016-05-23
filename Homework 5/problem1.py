'''
Polygons
Alvin Williams
'''
from math import cos, sin, sqrt
class Point():
    def __init__(self,x=0,y=0):
        '''
        An x coordinate and y coordinate are the two given attributes.
        '''
        self.x = x
        self.y = y
    def translate(self,s,t):
        '''
        The x coordinate is increased by s and the y coordinate is increased by t.
        '''
        self.x = self.x + s
        self.y = self.y + t
        return self.x, self.y
    def rotate(self, theta):
        '''
        Rotates the coordinates by theta.
        '''
        self.x = cos(theta)*self.x
        self.y = sin(theta)*self.y
        return self.x, self.y
    def distance(self, p):
        '''
        Subtracts the x and y coordinates of self from the p point object.
        Returns the difference vector.
        '''
        return abs(self.x - p.x), abs(self.y - p.y)
    def left_of(self, q,r):
        '''
        If the x and y coordinates are less than q and r.
        return True; else False
        '''
        line1 =(r.x*self.y - self.x*r.y)
        line2 =(q.x*r.y - q.x*p.y)
        line3 =(q.y*p.x - q.y*r.x)
        if line1+line2+line3 > 0:
            return True
        else:
            return False
        
    def right_of(self, q,r):
        '''
        If the x and y coordinates are greater than q and r.
        return True; else False
        '''
        line1 =(r.x*self.y - self.x*r.y)
        line2 =(q.x*r.y - q.x*p.y)
        line3 =(q.y*p.x - q.y*r.x)
        if line1+line2+line3 < 0:
            return True
        else:
            return False
    def __str__(self):
        '''
        A string representation of the two coordinates as a point.
        '''
        return str("(" + str(self.x) + "," + str(self.y) + ")")
    def __repr__(self):
        '''
        Returns self.__str__()
        '''
        return self.__str__()

class SimplePoly():
    def __init__(self, *vertices):
        '''
        A simple polygon with a collection of point 
        '''
        self.vertices = []
        for i in vertices:
            self.vertices.append(i)
    def translate(self, s,t):
        '''
        Translates every x coordinate by s and
        every y coordinates by t in the vertices list.
        '''
        O = self.__iter__()
        for k in O:
            k.x += k.x + s
            k.y += k.y + t
        return self.vertices
    def rotate(self, theta):
        '''
        Rotates every x coordinate by theta and
        every y coordinates by theta in the vertices list.
        '''
        O = self.__iter__()
        for k in O:
            k.x += k.x*cos(theta)
            k.y = k.y*sin(theta)
        return self.vertices
    def __iter__(self):
        '''
        Returns an iterable object of the list.
        '''
        return iter(self.vertices)
    def __next__(self):
        '''
        Returns the next object in the list.
        '''
        O = self.__iter__()
        if len(O) == 0:
            raise StopIteration
        else:
            for i in O:
                return i
    def __len__(self):
        '''
        Returns the number of vertices in the polygon.
        '''
        count = 0
        a = self.__iter__()
        for points in a:
            count += 1
        return count
    def __getitem__(self, i):
        '''
        Returns the object at index i.
        '''
        for points in self.__iter__():
            if len(self) == 0:
                raise IndexError
            elif i > len(self):
                raise IndexError
            else:
                 return self.vertices[i]
    def __str__(self):
        '''
        Shows the vertices as a polygon.
        '''
        astr = ""
        for points in self.vertices:
            astr += str(points) + " "
        return astr
                    
    def perimeter(self):
        '''
        Adds up the x's and y's in the list and
        returns the perimeter.
        '''
        perimeter = 0
        O = self.__iter__()
        for k in O:
            perimeter += k.x
            perimeter += k.y
        return perimeter
                
class ConvPoly(SimplePoly):
    
    def __init__(self, *vertices):
        '''
        This is a convex polygon with a list of points in a list.
        '''
        self.vertices = []
        for i in vertices:
            self.vertices.append(i)
        
        
class EquiTriangle(ConvPoly):
    
    def __init__(self, length, *vertices):
        '''
        Equilaterial triangle with length attributes.
        '''
        self.vertices = []
        for i in vertices:
            self.vertices.append(i)
        self.length = length
    def area(self):
        '''
        Returns the length and width of the equalaterial triangle.
        '''
        return ((sqrt(3)/4)*self.length**2)
class Rectangle(ConvPoly):
    
    def __init__(self, length, width, *vertices):
        '''
        Rectangle class that has length and strength attributes.
        '''
        self.vertices = []
        for i in vertices:
            self.vertices.append(i)
        self.length = length
        self.width = width
    def area(self):
        '''
        Returns the length and width of the rectangle object.
        '''
        return self.length* self.width 
        
class Square(Rectangle):
    
    def __init__(self, length):
        '''
        Subclass square of the Rectangle class.
        '''
        self.length = length
        
r = Point(10, 5)
q = Point(5,5)
p = Point(2,3)
S = SimplePoly(p,q,r)
