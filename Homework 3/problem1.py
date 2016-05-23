'''
Recursive Functions
Alvin Williams
'''

def replace_element(L, oldel, newel):
    '''
    Takes a list of size n and recursively looks for the element
    to be replaced by a new element.  Returns replaced element +
    concantentated list until it reaches the end of the list.
    '''
    if L == []:
        return []
    elif len(L) == 1:
        if L[0] == oldel:
            return [newel]
        else:
            return L
    else:
        if L[0] == oldel:
            return [newel] + replace_element(L[1:], oldel, newel)
        else:
            return [L[0]] + replace_element(L[1:], oldel, newel)
            
    
def inverse_pair(L):
    '''
    Takes a list and checks to see if any element
    in the list + another element == 0.  The or statement
    is useful because it allows the program to get an inclusive
    answer. One recursive call checks from the back list and the other
    checks from the front of the list. It will return True when it finds
    a pair if it exists.
    '''
    print(L)
    if len(L) == 2:
        return L[0] + L[-1] == 0
    else:
        if L[0] + L[-1] ==0:
            return True
        else:
            return inverse_pair(L[:-1]) or inverse_pair(L[1:])
        
def occurrences(astr, substr):
    '''
    Takes a string and compares it to substr
    to see if an element is found.  Once the element
    is found it adds one and calls the function recursively
    and adding +1 or calling the function recursively and adding
    + 0.
    '''
    if len(astr) == 0:
        return 0
    elif astr[0:len(substr)] == substr:
        astr = astr[len(substr):]
        return occurrences(astr, substr) + 1
    else:
        return occurrences(astr[1:], substr)
    
