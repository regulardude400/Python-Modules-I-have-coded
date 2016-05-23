'''
Calendar
'''


def is_leap(yr):
    if yr % 4 ==0 and yr % 100 != 0 or yr % 400 == 0:
        return True
    else:
        return False
def monthdays(yr, mon):
    days_of_month = {1:31, 2:28, 3:31, 4:30, 5:31,
                     6:30, 7:31, 8:31, 9:30, 10:31,
                     11:30, 12:31}
    check = is_leap(yr)
    if is_leap(yr) == True and mon == 2:
        return 29
    else:
        for k in days_of_month:
            if mon == k:
                return days_of_month.get(k)

def yeardays(yr):
    check = is_leap(yr)
    if check == True:
        return 366
    else:
        return 365

def wkday_on_first(yr, mon):
    Day_name = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if mon == 1 or mon ==2:
        mon=mon+12
        yr=yr-1
    day = (((13*mon+3)/5+1+yr+(yr/4)-(yr//100)+(yr//400))%7)
    return Day_name[(int(day))]
    
            
def print_calendar(yr, mon):
    name_of_month = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                     6:"June", 7:"July", 8:"August", 9:"September", 10:"October",
                     11:"November", 12:"December"}
    

    for k in name_of_month:
        if mon == k:
            e = name_of_month.get(k)
    w = "\n"

    print('{:^30}'.format(str(yr)) + " " + w + '{:^30}'.format(e))
    print('{:^5}'.format("Mon") + '{:^5}'.format("Tue") + '{:^5}'.format("Wed") + '{:^5}'.format("Thu") + '{:^5}'.format("Fri") + '{:^5}'.format("Sat") + '{:^5}'.format("Sun"))
    days = [str(i) for i in range(1,32)]
    k = wkday_on_first(yr, mon)
    f = is_leap(yr)
    
    if k == "Mon":
        print('{:^5}'.format("Mon") + '{:^5}'.format("Tue") + '{:^5}'.format("Wed") + '{:^5}'.format("Thu") + '{:^5}'.format("Fri") + '{:^5}'.format("Sat")
    elif k == "Tue":
        print(' '.join(days).center(15))
    elif k == "Wed":
        print(' '.join(days).center(15))
    elif k == "Thu":
        print(' '.join(days).center(15))
    elif k == "Fri":
        print(' '.join(days).center(15))
    elif k == "Sat":
        print(' '.join(days).center(15))
    elif k == "Sun":
        print(' '.join(days).center(15))
    
