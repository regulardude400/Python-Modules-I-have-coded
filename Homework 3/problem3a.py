'''
Container objects
Alvin Williams
'''

class Container():
    def __init__(self):
        '''
        Simply creates an empty list as an attribute of the object.
        '''
        self.contents = []
        
    def insert(self, item):
        '''
        Inserts things into places... i.e self.contents
        '''
        self.contents.append(item)
        
    
    def erase_one(self, item):
        '''
        Erases one item from self.contents
        '''
        self.contents.remove(item)
        
    def erase_all(self, item):
        '''
        Erases all occurences of item from self.contents
        '''
        for i in self.contents:
            if i == item:
                self.contents.remove(i)
    def count(self, item):
        '''
        Counts all the occurences of an object
        in self.contents and returns the number.
        '''
        count = 0
        for i in self.contents:
            if i == item:
                count += 1
        return count
    def items(self):
        '''
        Shows a list of distinct items in
        the container.
        '''
        L = []
        A = []
        for items in self.contents:
            k = self.count(items)
            if k == 1:
                L.append(items)
            elif k>1:
                A.append(items)
        L = sorted(A)+L
        return L
                
    def __str__(self):
        '''
        Shows a string of the items in self.contents.
        '''
        L = []
        A = []
        for items in self.contents:
            k = self.count(items)
            if k == 1:
                L.append(str(items))
            elif k>1:
                A = []
                A.append(str(items))
        L = sorted(A)+ L
                    
        return ', '.join(L)
    def __repr__(self):
        '''
        Uses self.__str__ to show a representation
        of all the items in self.contents.
        '''
        return self.__str__()

    def __add__(self, other):
        '''
        Adds two content-attributes together
        to form a new object with contents.
        '''
        S = Container()
        for k in self.contents:
            S.insert(k)
        for p in other.contents:
            S.insert(p)
        return S.contents
    def __sub__(self, other):
        '''
        Subtracts two content-attributes together
        to form a new object with contents with the left-
        over items.
        '''
        S = Container()
        for k in self.contents:
            S.insert(k)
        for p in other.contents:
            S.insert(p)
        for a in self.contents:
            for b in other.contents:
                if a == b:
                    try:
                        S.erase_one(a)
                    except ValueError:
                        pass
        return S.contents
    def __mul__(self, other):
       '''
        Multiplies two content-attributes together
        to form a new object with contents of the intersection
        of two objects.
       '''
       S = Container()
       
       for k in self.contents:
           if k in other.contents:
               S.insert(k)
               p = S.count(k)
               if p > 1:
                   try:
                       S.erase_one(k)
                   except ValueError:
                        pass
       return S.contents
    

    
