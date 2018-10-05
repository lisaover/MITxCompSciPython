#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    power = 1
    if exp == 0:
        return 1
    else:
        for i in range(exp):
            power *= base
        return power

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base*recurPower(base, exp-1)
    
base = 2
exp = 0
#print(iterPower(base, exp))
#print(recurPower(base, exp))

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
    elif a < b:
        test = a
    else:
        test = b
    
    while test > 0:
            if a%test == 0 and b%test == 0:
                return test
            else:
                test -= 1
            
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    
    The Euclidean algorithm is based on the principle that the greatest common 
    divisor of two numbers does not change if the larger number is replaced by 
    its difference with the smaller number.
    https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
    '''
    if a < b:
        pass
    else:
        temp = a
        a = b
        b = temp
        
    if b%a == 0:
        return a
    else:
        return gcdRecur(b%a, a)

a = 462
b = 1071
#print(gcdIter(a, b))
#print(gcdRecur(a, b))

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    
    First, test the middle character of a string against the character you're 
    looking for (the "test character"). If they are the same, we are done.
    If they're not the same, check if the test character is "smaller" than the 
    middle character. If so, we need only consider the lower half of the 
    string; otherwise, we only consider the upper half of the string.
    Implement the function isIn(char, aStr) which implements the above idea 
    recursively to test if char is in aStr. char will be a single character 
    and aStr will be a string that is in alphabetical order. The function 
    should return a boolean value.
    '''
    if len(aStr) <= 1:
        if char == aStr:
            return True
        else:
            return False
    i = len(aStr)//2
    if char == aStr[i]:
        return True
    else:
        if char < aStr[i]:
            aStr = aStr[:i]
            return isIn(char, aStr)
        else:
            aStr = aStr[i:]
            return isIn(char, aStr)
            
print(isIn('z', ''))