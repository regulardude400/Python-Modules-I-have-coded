from problem1 import Date
'''
Calendar Dates
Alvin Williams
'''

def weekend_dates(m,y):
        '''
        Prints out all of the weekend dates within a specified month
        and year.
        '''
        C = Date(m, 1, y)
        d = C.daycount()
        k = C.__add__(d)
        a = C.nextday()
        for days in range(1,d+2):
                C.__day += 1
                C.nextday()
                if C.nextday() == "Saturday" or C.nextday() == "Sunday":
                        print(C)
                        
                
	
def first_mondays(y):
        '''
        Prints out all of the first mondays of the month.
        '''
	C = Date(1, 1, y)
        d = C.daycount()
        k = C.__add__(d)
        a = C.nextday()
        for months in range(1,13):
                C.__day += 1
                C.nextday()
                if C.nextday() == "Monday":
                        print(C)
	
def interval_schedule(start_date, end_date, interval):
        '''
        Prints the days in the range of start and end date
        with the interval being printed out if it falls within
        the range.
        '''
	for k in range(start_date, end_date, interval):
                start_date.daycount()
                end_date.daycount()
                if start_date.daycount() % interval == 0:
                        print(k)
                

        
    
        
