'''
Straight Lines
Alvin Williams
'''

class StraightLine():
    def __init__(self, a=0, b=0 ,c=0):
        '''
        Init parameter sets 3 attributes == to the paramenters.
        '''
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        '''
        Returns a string representation of the appropiate object.
        The output varies depending if it has met certain conditions.
        '''
        if self.a == 0 and  self.b != 0:
            return str(self.b) + "y" + " = " + str(self.c)
        elif self.b == 0 and self.a != 0:
            return str(self.a) + "x" + " = " + str(self.c)
        elif self.a < 0 and self.b > 0:
            return "-"+str(abs(self.a)) +"x " + "+ "+ str(self.b) + "y " + " = " + str(self.c)
        elif self.a > 0 and self.b > 0:
            return str(abs(self.a)) +"x " + "+ "+ str(self.b) + "y " + " = " + str(self.c)
        elif self.b < 0 and self.a > 0:
            return str(self.a) +"x" + " - " + str(abs(self.b)) + "y" + " = " + str(self.c)
        else:
            return str(self.a) +"x" + " + " + str(self.b) + "y" + " = " + str(self.c)
    def __repr__(self):
        '''
        Reusues the str method because there is no extra information
        that would be of use here for developing purposes.
        '''
        return self.__str__()
    def slope(self):
        '''
        Calculates the slope via rise/run.
        Returns the slope.
        '''
        try:
            s = float(-self.a/self.b)
        except ZeroDivisionError:
            return None
        else:
            return s
    
    def yintercept(self):
        '''
        Calculates the yintercept by setting  x = 0
        and dividing y by the constant.
        '''
        k = self.slope()
        if k == None:
            return None
        else:
            if k == 0:
                return None
            else:
                yint = float(self.c/self.b)
                return yint
    def xintercept(self):
        '''
        Calculates the yintercept by setting  y = 0
        and dividing x by the constant.
        '''
        k = self.slope()
        if k == None:
            return None
        else:
            if k == 0:
                return None
            else:
                xint = float(self.c/self.a)
                return xint
    def parallel(self, L):
        '''
        If the first object's slope is equal to the slope
        of the other object.
        '''
        q = self.slope()
        p = L.slope()
        if q == p:
            return True
        else:
            return False
    def perpendicular(self, L):
        '''
        Reutrn True if slope is a line.
        Also returns True if the reciprical
        of the other slope is equal to the first
        line object.
        '''
        q = self.slope()
        p = L.slope()
        if p == 0:
            return True
        elif q == float(-1/p):
            return True
        else:
            return False
    def intersection(self, L):
        '''
        First checks if the object is parallel to see if it should
        return None.  Then calculates the intersections of the x and
        the y.
        '''
        w = self.parallel(L)
        if w == "Lines are Parallel":
            return None
        else:
           
            if L.yintercept() != None and self.yintercept != None:
                try:
                    interx = ((L.yintercept() - self.yintercept()) / (self.slope() - L.slope()))
                    intery = self.slope()*(interx + self.yintercept())
                    return (interx, intery)
                except ZeroDivisionError:
                    return "Do not intersect"
            else:
                return "Do not intersect"
    def __eq__(self, other):
        '''
        Two lines are equal if the slope and the y intercept are
        equal to each other.  This function simply makes variables
        for this and compares the two to return
        the two equal objects.
        '''
        ss = self.slope()
        sy = self.yintercept()
        os = other.slope()
        oy = other.yintercept()
        if ss == os and sy == oy:
            return type(self) == type(other)
        return False
        
        
    def __ne__(self, other):
        '''
        Uses the eq method to return if it is equal to the other object.
        '''
        return not self.__eq__(other)
            
    
