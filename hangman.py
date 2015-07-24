
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for ch in lettersGuessed:
        if ch in secretWord:
            count += 1
    
    if (count == len(secretWord)):
        return True
    else:
        return False
    

            
            
def getGuessedWord(secretWord, lettersGuessed):
    work = []
    for ch in secretWord:
        work.append('_')

    for ch in lettersGuessed:
        for i,vl in enumerate(secretWord):
            if ch == vl:
                work[i] = ch
    return ' '.join(work)    
    
def getAvailableLetters(lettersGuessed):
    all = 'abcdefghijklmnopqrstuvwxyz'
    for ch in lettersGuessed:
        s1= all.replace(ch, '')
        all = s1
    return all

def hangman(secretWord):
    print "The word contains {} letters ".format(len(secretWord))
    print "-----------------------------"
    print "You have 3 guesses left"
   
    lettersGuessed = []
  
    no_of_guesses = 3
    while (no_of_guesses != 0):
        print "Available letters", getAvailableLetters(lettersGuessed)
        print "Please guess a letter:"
        guess_i = str(raw_input()) 
        guess = guess_i.lower()
        if guess in lettersGuessed:
            print "This letter is already guessed"
            continue
        else:
            lettersGuessed.append(guess)        
        if guess not in secretWord  :
            no_of_guesses -= 1
            print "Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed) 
            print  "------------------"
            print "You have {} guesses left".format(no_of_guesses)      
        else:
            print "Good Guess",getGuessedWord(secretWord, lettersGuessed)
            print  "------------------"
            print "You have {} guesses left".format(no_of_guesses) 
        
        if isWordGuessed(secretWord, lettersGuessed) ==True:
            print "Congratulations! You win"   
            break
     
    #print "lettrs guessed final", lettersGuessed
    
    if no_of_guesses == 0:
        print "Sorry, you lose"    
    print "Word is", secretWord
    
        
        
        
def main():
    #secretWord = 'brick' 
    #hangman(secretWord)
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)    
    
if __name__ == "__main__":
    main()