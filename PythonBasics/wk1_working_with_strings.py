#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 14:49:09 2018

@author: lisaover
"""
"""
print('hello world')
print('I like 6.00.1x!')
"""
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
s = 'hawaii'
count = 0
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print("Number of vowels: " + str(count))

"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
s = 'botxboizrbrbobzboboobooubobbbob'
count = 0
for i in range(len(s)-2):
    if s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
        count += 1
print("Number of times bob occurs is: " + str(count))

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc
"""
s = 'abcdefghijbotxboizkrbrbobzbak'
longest = ''
temp = ''
for i in range(len(s)):
    # set temp variable and longest variable equal to the first character in s
    if i == 0:
        temp = s[i]
        longest = s[i]
    else:
        # if the last letter in temp is less than or equal to the current 
        # letter in s...add the current letter in s to temp
        if temp[-1] <= s[i]:
            temp = temp + s[i]
        # if the last letter in temp is greater than the current letter in s...
        # set temp equal to the current letter in s
        else:
            temp = s[i]
    # check if temp variable is longer than longest variable
    # copy temp to longest if temp is longer
    if len(temp) > len(longest):
        longest = temp            
print("Longest substring in alphabetical order is: " + longest)
            