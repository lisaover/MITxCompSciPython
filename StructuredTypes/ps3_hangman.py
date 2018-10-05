# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
    if len(secretWord) == count:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word = word + ' ' + letter + ' '
        else:
            word = word + ' _ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters = 'abcdefghijklmnopqrstuvwxyz'
    availableLetters = ''
    for letter in letters:
        if letter in lettersGuessed:
            pass
        else:
            availableLetters = availableLetters + letter
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # welcome message
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------')
    # initialize variables
    guessesLeft = 8
    lettersGuessed = ''
    # take guesses and check them until the player wins or until they use all guesses
    while guessesLeft > 0:
        print('You have ' + str(guessesLeft) + ' guesses left')
        # end = '' causes the newline created by the input statement 
        # to be placed on the same line as this print statement
        # for some reason this was not necessary in the course simulator
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)), end = '')
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        else:
            lettersGuessed = lettersGuessed + letter
            if letter in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
                guessesLeft -= 1
        # if they guess the word, they win
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
    # if they use all guesses without guessing the correct word, they lose
    if not isWordGuessed(secretWord, lettersGuessed):
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
                
    
#hangman('hello')


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
