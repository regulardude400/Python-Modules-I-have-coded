'''
Magic Numbers
'''

def magic(n):
    '''
    Takes an integer n and makes n the end of the range.
    If the integer modded by k is equal to 0 then
    it assigns the sum variable to itself + i.
    It returns the corresponding statement.
    '''
    A_sum = 0
    i=1
    if n == 0:
        return False
    for k in range(1, n):
        if n%k == 0:
            A_sum = A_sum + k
    if A_sum == n:
        return True
    else:
        return False
       
def magic_list(num):
    '''
    Takes an integer and makes it the range.
    Any value that returns true is put into the list.
    Returns the list.
    '''
    P = []
    for k in range(2, num):
        if magic(k) == True:
            P.append(k)
        else:
            continue
    return P
