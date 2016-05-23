'''
Calendar Dates
Alvin Williams
'''

class Date():
    
    def __init__(self, month=1, day=1, year=1800):
        '''
        Creates a date object with a month day and year.
        The if statements below are the conditions necessary
        to keep the date object valid.
        '''

        self.__min_year = 1800
        self.__dow_jan1 = "Wednesday"
        self.__month = month
        self.__day = day
        self.__year = year
        
        if self.__year < self.__min_year:
            raise ValueError("Year value is less than 1800")
        if self.__month not in range(1,13):
            raise ValueError("Month is not in the range of 1-12")
        elif self.__month == 2:
            if self.year_is_leap():
                if self.__day > 29:
                    raise ValueError("Invalid day for this month and year")
            else:
                if self.__day > 28:
                    raise ValueError("Invalid day for this month and year")
        elif self.__month == 4 or self.__month == 6 or \
             self.__month == 9 or self.__month == 11:
            if self.__day > 30:
                raise ValueError("Invalid day for this month")
                    
        elif self.__month == 1 or self.__month == 3 or self.__month == 5 or self.__month == 7 or \
             self.__month == 8 or self.__month == 10 or self.__month == 12:
            if self.__day > 31:
                raise ValueError("Invalid day for this month")
            
    def month(self):
        '''
        Returns the number of the month
        '''
        return self.__month
    def day(self):
        '''
        Returns the number of the day
        '''
        return self.__day
    def year(self):
        '''
        Returns the number of the year
        '''
        return self.__year
    def year_is_leap(self):
        '''
        Returns T/F depending if year is a leap year.
        '''
        if self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0:
            return True
        else:
            return False
    def daycount(self):
        '''
        Returns the number of days in the respective month and year.
        '''
        k = self.__month
        count = 0
        for i in range(1, k+1):
            if i == 2 and self.year_is_leap():
                count += 29
            elif i == 2:
                count+= 28
            elif i == 4 or i == 6 or i == 9 or i == 11:
                count+= 30
            else:
                count+= 31
        count -= self.__day
        
        for v in range(0, self.__year - self.__min_year):
            if v is self.year_is_leap():
                count += 366
            else:
                 count += 365
        return count
    
    def day_of_week(self):
        '''
        Returns a string based on the index position of the list and daycount().
        '''
        Days = [0, self.__dow_jan1, "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        i = self.daycount()
        return Days[i%7]
    
    def nextday(self):
        '''
        Returns a date, after the current date.
        '''
        p = self.__day + 1
        if self.__month == 2:
            if self.year_is_leap() and p > 29:
                    self.__month = 3
                    p = 1
                    k = self.__month, p, self.__year
                    return k
            else:
                if p > 28:
                    self.__month = 3
                    p = 1
                    k = self.__month, p, self.__year
                    return k
        elif self.__month == 4 and p > 30 or self.__month == 6 and p > 30 or\
             self.__month == 9 and p > 30 or self.__month == 11 and p > 30:
                p = 1
                k = self.__month+1, p, self.__year
                return k  
        elif self.__month == 1 and p > 31 or self.__month == 3 and p > 31 or self.__month == 5 and p > 31 \
             or self.__month == 7 and p > 31 or  self.__month == 8 and p > 31 \
             or self.__month == 10 and p > 31:
                 p = 1
                 k = self.__month+1, p, self.__year
                 return k
        elif self.__month == 12 and p > 31:
                p = 1
                self.__month = 1
                k = self.__month, p, self.__year+1
                return k
        else:
            k = self.__month, p, self.__year
            return k
    
    def prevday(self):
        '''
        Returns a date, before the current date.
        '''
        p = self.__day - 1
        if self.__year == self.__min_year and self.__day == 1 and self.__month == 1:
            raise Exception("There are no valid dates before 1/1/1800")

        elif self.__month == 1 and p == 0:
            self.__month = 12
            p = 31
            k = self.__month, p, self.__year-1
            return k
        elif self.__month == 2 and p == 0:
            self.__month = 1
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 3 and p == 0:
                if p == 0 and self.year_is_leap():
                    self.__month = 2
                    p = 29
                    k = self.__month, p, self.__year
                    return k
                elif p == 0:
                    self.__month = 2
                    p = 28
                    k = self.__month, p, self.__year
                    return k
        elif self.__month == 4 and p == 0:
            self.__month = 3
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 5 and p == 0:
            self.__month = 4
            p = 30
            k = self.__month, p, self.__year
            return k
        elif self.__month == 6 and p == 0:
            self.__month = 5
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 7 and p == 0:
            self.__month = 6
            p = 30
            k = self.__month, p, self.__year
            return k
        elif self.__month == 8 and p == 0:
            self.__month = 1
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 9 and p == 0:
            self.__month = 8
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 10 and p == 0:
            self.__month = 9
            p = 30
            k = self.__month, p, self.__year
            return k
        elif self.__month == 11 and p == 0:
            self.__month = 10
            p = 31
            k = self.__month, p, self.__year
            return k
        elif self.__month == 12 and p == 0:
            self.__month = 11
            p = 30
            k = self.__month, p, self.__year
            return k
        else:
            k = self.__month, p, self.__year
            return k
        
    def __add__(self, n):
        '''
        Returns a date, n + days after the current date.
        '''
        D = Date(self.__month, self.__day, self.__year)
        for i in range(0, n):
            D.__day += 1
            D.nextday()
        return D
        
    def __sub__(self, n):
        '''
        Returns a date, n - days after the current date.
        '''
        D = Date(self.__month, self.__day, self.__year)
        for i in range(0, n):
            D.__day -= 1
            D.prevday()
        return D
    
    def __lt__(self, other):
        '''
        Returns True is object is less than other object.
        '''
        if self.__year < other.__year:
            return True
        elif self.__year == other.__year:
            if self.__month < other.__month:
                return True
            elif self.__month == other.__month:
                if self.__day < other.__day:
                    return True
                else:
                    return False
        else:
            if self.__year > other.__year:
                return False
    def __eq__(self, other):
        '''
        Returns True is object is equal to other object.
        '''
        a = self.__year
        b = self.__month
        c = self.__day
        d = other.__year
        e = other.__month
        f = other.__day

        if a == d and b == e and c == f:
            return True
        else:
            return False
        
    def __le_(self, other):
        '''
        Returns True is object is equal to or less than other object.
        '''
        k = self.__lt__(other)
        m = self.__eq__(other)

        if k == True or m == True:
            return True
        elif k == True and m != False:
            return True
        elif k == False and m == True:
            return True
        else:
            return False
        
    def __gt__(self, other):
        '''
        Returns True is object is greater than other object.
        '''
        if self.__year == other.__year:
            return False
        else:
            return not self.__lt__(other)
        
    def __ge__(self, other):
        '''
        Returns True is object is equal to or greater than other object.
        '''
        k = self.__gt__(other)
        m = self.__eq__(other)

        if k == True or m == True:
            return True
        elif k == True and m != False:
            return True
        elif k == False and m == True:
            return True
        else:
            return False
    
    def __ne__(self, other):
        '''
        Returns True is object is not equal to other object.
        '''
        return not self.__eq__(other)
    
    def __str__(self):
        '''
        Returns string representation of the object.
        '''
        monthy = ""
        k = self.__month
        d = self.__day
        y = self.__year
        if k == 1:
            monthy = "January "
        elif k == 2:
            monthy = "February "
        elif k == 3:
            monthy = "March "
        elif k == 4:
            monthy = "April "
        elif k == 5:
            monthy = "May "
        elif k == 6:
            monthy = "June "
        elif k == 7:
            monthy = "July "
        elif k == 8:
            monthy = "August "
        elif k == 9:
            monthy = "September "
        elif k == 10:
            monthy = "October "
        elif k == 11:
            monthy = "November "
        else:
            monthy = "December "
        return monthy + str(d) + "," + " " + str(y) 
        
    def __repr__(self):
        '''
        Returns the same thing as __str__ method.
        '''
        return self.__str__()
    
        
