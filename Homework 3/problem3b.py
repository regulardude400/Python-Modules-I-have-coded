'''
Container objects
Alvin Williams
'''
from problem3a import Container

def symmetric_difference(c1, c2):
    '''
    Returns a list of items that are not in both lists but
    unique to a single list.
    '''
    F = []
    for all_items in c1.contents:
        if all_items not in c2.contents:
            F.append(all_items)
    for every_item in c2.contents:
        if every_item not in c1.contents:
            F.append(all_items)
    return F
                
def subcontainer(c1, c2):
    '''
    If every item in A is in B return True
    else return False
    '''
    for all_items in c1.contents:
        k = c1.count(all_items)
        p = c2.count(all_items)
        if all_items in c2 and k <= p:
            return True
        else:
            return False
def remove_repeats(C):
    '''
    Erases all copies until one is only left
    '''
    
    for i in C:
        k = C.count(i)
        if k > 1:
            if i == k:
                C.remove(i)
        else:
            pass
    return C
            
    
def similar(A, B):
    '''
    Checks to see if A and B have the same items
    not depending on the count for each also.
    '''
    for all_items in A.contents:
        k = A.count(all_items)
        b = B.count(all_items)
        if all_items in B.contents and k <= b :
            return True
        else:
            return False

