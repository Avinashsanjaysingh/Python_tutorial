'''
    Can you change the values inside a list which is contained in set S 
        S = {8,7,12,"Avinash", [1,2]}

'''

#   No, we cannot directly change the values inside a list that is part of a set in Python. Sets are designed to contain only hashable and immutable elements. Lists, being mutable, cannot be added to a set.

#   If we try to create a set with a list element, we'll encounter a TypeError because lists are unhashable:
