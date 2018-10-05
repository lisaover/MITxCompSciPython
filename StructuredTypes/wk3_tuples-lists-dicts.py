#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a procedure called oddTuples, which takes a tuple 
as input, and returns a new tuple as output, where every 
other element of the input tuple is copied, starting with 
the first one. So if test is the tuple 
('I', 'am', 'a', 'test', 'tuple'), then evaluating 
oddTuples on this input would return the tuple 
('I', 'a', 'tuple'). 

    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
"""
aTup = (('I', 'am', 'a', 'test', 'tuple'))

def oddTuples(aTup):
    nTup = ()
    for t in range(0, len(aTup), 2):
        nTup = nTup + aTup[t:t+1]
    return nTup
oddTup = oddTuples(aTup)
print(oddTup)
###############

def applyToEach(L, f):
    '''
    Assumes L is a list, f is a function
    Mutates L by replacing each element, e, of L by f(e)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])
'''
For each of the following questions (which you may 
assume is evaluated independently of the previous 
questions, so that testList has the value indicated 
above), provide an expression using applyToEach, 
so that after evaluation testList has the indicated 
value. You may need to write a simple procedure in 
each question to help with this process. 
'''
testList = [1, -4, 8, -9]
def timesFive(a):
    return a * 5
applyToEach(testList, timesFive)
print(testList)
#[5, -20, 40, -45]

testList = [1, -4, 8, -9]
applyToEach(testList, abs)
print(testList)
#[1, 4, 8, 9]

testList = [1, -4, 8, -9]
def addOne(a):
    return a + 1
applyToEach(testList, addOne)
print(testList)
#[2, -3, 9, -8]

testList = [1, -4, 8, -9]
def sqrNum(a):
    return a * a
applyToEach(testList, sqrNum)
print(testList)
#[1, 16, 64, 81]
###############

def applyEachTo(L, x):
    '''
    Assumes L is a list of functions, x is an integer
    Applies each function to x and prints the result
    '''
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
###############

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    length = 0
    values = aDict.values()
    for value in values:
        length = length + len(value)
    return length

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
###############

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if len(aDict) == 0:
        return None
    else:
        length = []
        values = aDict.values()
        for value in values:
            length.append(len(value))
        for key, value in aDict.items():
            if len(value) == max(length):
                return key


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))