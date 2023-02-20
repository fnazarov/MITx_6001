'This is the solution of the PS3 '
import random

#Wordlist is given in .txt format
WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ( "Loading word list from file..." )
    # inFile: file
    inFile = open ( WORDLIST_FILENAME,'r' )
    # line: string
    line = inFile.readline ()
    # wordlist: list of strings
    wordlist = line.split ()
    print ( "  ",len ( wordlist ),"words loaded." )
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice ( wordlist )


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i=0
    while i<len(secretWord):
        if secretWord[i] in lettersGuessed:
            i=i+1
        else:
            return False
    return True


def getGuessedWord(secretWord,lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = ''
    for w in secretWord:
        if w in lettersGuessed:
            ans = ans + w
        else:
            ans = ans + "_"
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_new = ''
    lg = ''
    for j in lettersGuessed:
        lg = lg + j.lower ()

    for w in alphabet:
        if w not in lg:
            alphabet_new = alphabet_new + w
    return alphabet_new


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

    word_lens = len ( secretWord )
    print ( "Welcome to the game Hangman! \n" )
    print ( 'I am thinking of a word that is ',word_lens,'letters long. \n' )
    print ( "-----------" )
    nr_of_guess = 8
    lettersGuessed = ""
    while nr_of_guess > 0 and not isWordGuessed ( secretWord,lettersGuessed ):
        print ( "You have ",nr_of_guess,"guesses left. \n" )

        print ( "Available Letters: ",getAvailableLetters ( lettersGuessed ),"\n" )
        ask_letter = input ( "Please guess a letter: " )
        if ask_letter in lettersGuessed:
            print ( "Oops! You've already guessed that letter: ",getGuessedWord ( secretWord,lettersGuessed ) )
            print ( '------------ \n' )
        else:
            lettersGuessed = lettersGuessed + ask_letter
            if ask_letter in secretWord:
                print ( "Good guess: ",getGuessedWord ( secretWord,lettersGuessed ) )
                print ( '------------ \n' )

            else:
                print ( "Oops! That letter is not in my word: ",getGuessedWord ( secretWord,lettersGuessed ),'\n' )
                print ( "-----------" )
                nr_of_guess = nr_of_guess - 1

    if nr_of_guess == 0 and not isWordGuessed ( secretWord,lettersGuessed ):
        print ( "Sorry, you ran out of guesses. The word was ",secretWord )
    if isWordGuessed ( secretWord,lettersGuessed ):
        print ( "Congratulations, you won!" )
    else:
        print ( "Game over" )
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)