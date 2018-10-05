def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    num = int(num)
    if num == 1:
        return 0
    elif num == base:
        return 1
    else:
        exponent = 1
        while base**exponent < num:
            exponent += 1
        if (base**exponent - num) < (num - base**(exponent - 1)):
            return exponent
        else:
            return (exponent - 1)
'''
print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
print(closest_power(2,192.0))
print(closest_power(5,375.0))
print(closest_power(20,210.0))
print(closest_power(4,160.0))
print(closest_power(15,8.0))
'''

def lessThan4(aList):
    '''
    aList: a list of strings
    Returns a sublist of strings in aList that contain fewer than 4 characters
    '''
    sList = []
    for word in aList:
        if len(word) < 4:
            sList.append(word)
    return sList
'''
aList = ["apple", "cat", "dog", "banana"]
print(lessThan4(aList))
'''

'''
Write a function called dict_invert that takes in a dictionary with immutable 
values and returns the inverse of the dictionary. The inverse of a dictionary 
d is another dictionary whose keys are the unique dictionary values in d. The 
value for a key in the inverse dictionary is a sorted list of all keys in d 
that have the same value in d.

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
'''
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # create an empty list; place unique values from the dictionary into the list
    vList = []
    for key in d:
        if d[key] in vList:
            pass
        else:
            vList.append(d[key])
    # create an empty dictionary
    # place each unique value into the dictionary with a blank list
    inv_d = {}
    for value in vList:
        inv_d[value] = []
    # iterate through each key:value pair in the dictionary 
    # append empty lists of the keys as values in dictionary = values in vList
    for key, value in d.items():
        inv_d[value].append(key)
    # sort each list and return
    for key, value in d.items():
        inv_d[value].sort()
    return inv_d
''' 
print(dict_invert({1:10, 2:20, 3:30}))
print(dict_invert({1:10, 2:20, 3:30, 4:30}))
print(dict_invert({4:True, 2:True, 0:True}))
print(dict_invert({2: 3, 3: 20, 4: 10}))
'''

'''
Write a recursive procedure, called laceStringsRecur(s1, s2), which also laces 
together two strings. Your procedure should not use any explicit loop mechanism, 
such as a for or while loop. We have provided a template of the code; your job 
is to insert a single line of code in each of the indicated places.

For this problem, you must add exactly one line of code in each of the three 
places where we specify to write a line of code. If you add more lines, your 
code will not count as correct.
'''
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')
'''
print(laceStringsRecur('hello','goodbye'))
'''

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    cloneL = L[:]
    for string in cloneL:
        if not f(string):
            L.remove(string)
    return len(L)
    

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
L = ['f', 'b', 'c']
L = ['a', 'a', 'a']
L = []
print(satisfiesF(L))
            
    


    
