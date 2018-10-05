#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:05:31 2018

@author: lisaover
"""

"""
In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!

Note: your program should use input to obtain the user's input! Be sure to 
handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to 
the user explaining you did not understand their input. Then, you should 
re-ask the question, and prompt again for input.
"""

# get user to input a number
# change end to 101 so use can choose 100 as their number
print("Please think of a number bewteen 0 and 100!")
print()
start = 0
end = 100
while True:
    guess = (end + start)//2
    print("Is your secret number " + str(guess) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == 'c':
        break
    elif response == 'h':
        end = guess
    elif response == 'l':
        start = guess
    else:
        print("Sorry, I did not understand your input.")
    print()
print("Game over. Your secret number was: " + str(guess))


"""
Solution by MIT
This solution does not work if the user guesses 100.
"""
"""
print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))
"""