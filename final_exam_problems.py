def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    
    Numbers in Mandarin follow 3 simple rules.

    -There are words for each of the digits from 0 to 10.
    -For numbers 11-19, the number is pronounced as "ten digit", so for example, 
    16 would be pronounced (using Mandarin) as "ten six".
    -For numbers between 20 and 99, the number is pronounced as “digit ten 
    digit”, so for example, 37 would be pronounced (using Mandarin) as "three 
    ten seven". 
    -If the digit is a zero, it is not included.
    '''
    # convert number to a string and then to a list of digits
    digits = [int(digit) for digit in str(us_num)]
    # create mandarin dictionary
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    
    if len(digits) == 1:
        return trans.get(str(digits[0]), 'None')
    elif digits[0] == 1:
        if digits[1] == 0:
            return trans.get('10', 'None')
        else:
            return trans.get('10', 'None') + ' ' + trans.get(str(digits[1]), 'None')
    else:
        if digits[1] == 0:
            return trans.get(str(digits[0]), 'None') + ' ' + trans.get('10', 'None')
        else:
            return trans.get(str(digits[0]), 'None') + ' ' + trans.get('10', 'None')  + ' ' + trans.get(str(digits[1]), 'None') 
    
    
#print(convert_to_mandarin(10))
            
def longestRun(L):
    '''
    L, a list of integers
    returns the length of the longest run of monotonically increasing numbers 
    occurring in L
    
    A run of monotonically increasing numbers means that a number at position 
    k+1 in the sequence is either greater than or equal to the number at 
    position k in the sequence.

    For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function 
    should return the value 5 because the longest run of monotonically 
    increasing integers in L is [3, 4, 5, 7, 7].
    '''
    longestRun = []
    tempRun = []
    if len(L) == 1:
        return len(L)
    for i in range(len(L)):
        if i == 0:
            tempRun.append(L[i])
        else:
            if L[i] >= L[i-1]:
                tempRun.append(L[i])
            else:
                if len(tempRun) >= len(longestRun):
                    longestRun = tempRun[:]
                tempRun = [L[i]]
            if i == len(L)-1:
                if len(tempRun) >= len(longestRun):
                    longestRun = tempRun[:]
    return len(longestRun)

#print(longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 9]))
    
def f(a, b):
    return a+b
def f(a, b):
    return a>b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions:
        
        Write a function called dict_interdiff that takes in two dictionaries 
        (d1 and d2). The function will return a tuple of two dictionaries: a 
        dictionary of the intersect of d1 and d2 and a dictionary of the 
        difference of d1 and d2, calculated as follows:

        intersect: The keys to the intersect dictionary are keys that are 
        common in both d1 and d2. To get the values of the intersect 
        dictionary, look at the common keys in d1 and d2 and apply the function 
        f to these keys' values -- the value of the common key in d1 is the 
        first parameter to the function and the value of the common key in d2 
        is the second parameter to the function. Do not implement f inside your 
        dict_interdiff code -- assume it is defined outside.
        
        difference: a key-value pair in the difference dictionary is (a) every 
        key-value pair in d1 whose key appears only in d1 and not in d2 and (b) 
        every key-value pair in d2 whose key appears only in d2 and not in d1.

    EXAMPLES
    
    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns 
    ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    
    If f(a, b) returns a > b
    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}
    then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
    '''
        
    intersect = {}
    difference = {}
    
    for k in d1.keys():
        if k in d2.keys():
            intersect[k] = f(d1.get(k, 0), d2.get(k, 0))
        else:
            difference[k] = d1.get(k, 0)
    for k in d2.keys():
        if k not in d1.keys():
            difference[k] = d2.get(k, 0)
            
    return (intersect, difference)

d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90} 
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}            
#print(dict_interdiff(d1, d2))

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)
    
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return self.name + ' says: It is obvious that ' + Person.say(self, stuff)
    def lecture(self, stuff):
        return 'It is obvious that ' + Person.say(self, stuff)
'''
class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return 'It is obvious that ' + self.say(stuff)
'''

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')

'''
print(e.say('the sky is blue'))
print(le.say('the sky is blue'))
print(le.lecture('the sky is blue'))
print(pe.say('the sky is blue'))
print(pe.lecture('the sky is blue'))
print(ae.say('the sky is blue'))
print(ae.lecture('the sky is blue'))
'''

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if self.vals.get(e, 0) != 0:
            del self.vals[e]

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals.keys():
            return True
        else: 
            return False
        
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)
