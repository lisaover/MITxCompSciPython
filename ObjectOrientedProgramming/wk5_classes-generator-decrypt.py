class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, other):
        '''
        Add an __eq__ method that returns True if coordinates refer to same 
        point in the plane (i.e., have the same x and y coordinate).
        '''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''
        Define __repr__, a special method that returns a string that looks 
        like a valid Python expression that could be used to recreate an object 
        with the same value. In other words, eval(repr(c)) == c given the 
        definition of __eq__ from part 1.
        See: https://stackoverflow.com/questions/452300/python-object-repr-self-should-be-an-expression
        '''
        return "Coordinate(%d,%d)" % (self.x, self.y)
    

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self, other):
        '''
        Define an intersect method that returns a new intSet containing 
        elements that appear in both sets. In other words, s1.intersect(s2)
        would return a new intSet of integers that appear in both s1 and s2. 
        Think carefully - what should happen if s1 and s2 have no elements 
        in common?
        '''
        newSet = intSet()
        for value in self.vals:
            if value in other.vals:
                newSet.insert(value)
        return newSet
    
    def __len__(self):
        '''
        Add the appropriate method(s) so that len(s) returns the number of 
        elements in s.
        '''
        return len(self.vals)
'''
test = intSet()
test.insert(5)
test.insert(7)
test.insert(9)
test2 = intSet()
test2.insert(1)
test2.insert(3)
#test2.insert(5)
print(test.intersect(test2))
print(test.__len__())
'''

def genPrimes():
    '''
    Write a generator, genPrimes, that returns the sequence of prime numbers 
    on successive calls to its next() method: 2, 3, 5, 7, 11, ...
    '''
    primes = []
    n = 2
    while True:
        prime = True
        for p in primes:
            if n % p == 0:
                prime = False
                n = n + 1
                break
            
        if prime == True:
            primes.append(n)
            next = n
            yield next
            n = n + 1
# run the following in the concole         
# genP = genPrimes()
# genP.__next__()

def build_shift_dict(shift):
    import string
    shift_dict = {}
    for char in string.ascii_lowercase:
        if string.ascii_lowercase.index(char) <= (25 - shift):
            shift_dict[char] = string.ascii_lowercase[string.ascii_lowercase.index(char) + shift]
        else:
            shift_dict[char] = string.ascii_lowercase[string.ascii_lowercase.index(char) - (26 - shift)]
    for char in string.ascii_uppercase:
        if string.ascii_uppercase.index(char) <= (25 - shift):
            shift_dict[char] = string.ascii_uppercase[string.ascii_uppercase.index(char) + shift]
        else:
            shift_dict[char] = string.ascii_uppercase[string.ascii_uppercase.index(char) - (26 - shift)]
    return shift_dict

import string

def apply_shift(shift, text):
    sd = build_shift_dict(shift)
    shifted_text = ''
    for char in text:
        if char in string.ascii_letters:
            shifted_text = shifted_text + sd.get(char, '')
        else:
            shifted_text = shifted_text + char
    return shifted_text

#print(build_shift_dict(5))
#text = 'hello'
#print(apply_shift(4, text))

def decrypt_message(text):
    for shift in range(1,27):
        # decrypt message
        temp = apply_shift(26 - shift, text)
        count = 0
        final = 0
        valid_words = ['lisa','my','name','is','hello','pig','cow','horse','a']
        words = temp.split(' ')
        for i in range(len(words)):
            for c in string.punctuation:
                words[i] = words[i].replace(c,"")
            if words[i] in valid_words:
                count += 1
        if count > final:
            final = count
            decrypted = temp
    return decrypted

shift = 5             
text = "Hello! My name is Lisa"
encrypted_text = apply_shift(shift, text)
#print(encrypted_text)
print(decrypt_message(encrypted_text))