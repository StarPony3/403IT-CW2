import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

secret_word = choose_word(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string the player is guessing.
    letters_guessed: list of letters that the player has guessed so far.

    Checks whether all the letters in the secret word have been guessed or not.
    
    Once all the letters in the secret word have been appended to letters_guessed,
    the function returns True.

    '''
    for letter in secret_word:
          if letter not in letters_guessed:
              return False                                  
    return True                                                 
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string the player is guessing.
    letters_guessed: list of letters that the player has guessed so far.
    
    Returns a string after each guess with letters guessed correctly filled in, 
    and the unguessed letters remaining as underscores.

    '''

    # List containing underscores to represent each letter in the secret word.
    # Strings are immutable, so a mutable list is used instead.
    length = ['_ '] * len(secret_word)

    # Iterates through each letter in the secret word, checking it against letters guessed. 
    # Replaces the corresponding underscore with the letter if there is a match.
    for x in range(len(secret_word)):
      for letter in letters_guessed:        
        if secret_word[x] == letter:
          length[x] = letter

    # Concatenates the list items into a string.
    return ''.join(length)



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list that the player has guessed so far.

    Checks letters guessed by the player against a list of lowercase letters.
    Returns a string of letters after each guess that the player has not guessed yet.
    '''
    # Iterates through all the letters and removes the ones that have been guessed.
    letters = string.ascii_lowercase
    for letter in letters:
      if letter in letters_guessed:
        letters = letters.replace (letter, "")
    return letters  

# plays hangman
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
      
    Starts up an interactive game of Hangman.
      
    * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
        
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
      
    * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
      
    * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
    partially guessed word so far.
      
    Follows the other limitations detailed in the problem write-up.
    '''
      
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # defines variables used in game
    letters_guessed = []
    duplicate_guesses = []
    letters = string.ascii_lowercase
    vowels = set('aeiou')
    consonants = set ('bcdfghjklmnpqrstvwxyz')
    number_of_guesses = 6
    warnings = 3


    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is {} letters long.".format(len(secret_word))) 
    print ("You have {} warnings left.".format(warnings))  


    # current game ends if guesses reach less than zero
    while number_of_guesses > 0:                                                     
        print ("-------------")
        print ("You have {} guesses left.".format(number_of_guesses)) 
        print ("Available letters:",get_available_letters(letters_guessed))

        # asks player to input letter
        letter_guess = input("Please guess a letter: ").lower()

                   
        # checks if input is valid
        # decreases warnings or guesses left if input invalid
        if letter_guess not in letters:
          warnings = warnings - 1
          if warnings >= 0:
            print ("Oops! That is not a valid letter. You have {} warnings left: {}".format(warnings, get_guessed_word(secret_word, letters_guessed)))
          else:
            number_of_guesses = number_of_guesses - 1
            print ("Oops! That is not a valid letter. You have no warnings left so you lose one guess: {}".format(get_guessed_word(secret_word, letters_guessed))) 


        # checks whether letter already guessed or not
        # decreases warnings or guesses left if already guessed
        if letter_guess in letters_guessed:
          duplicate_guesses.append(letter_guess)
          warnings = warnings - 1
          if warnings >= 0:
            print ("Oops! You've already guessed that letter. You have {} warnings left: {}".format(warnings, get_guessed_word(secret_word, letters_guessed)))
          else:
            number_of_guesses = number_of_guesses - 1
            print ("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {}".format(get_guessed_word(secret_word, letters_guessed)))

        
        # if player input valid, appends it to 'letters guessed' list.
        if letter_guess in letters:
          if letter_guess not in letters_guessed:
            letters_guessed.append(letter_guess)   
            # checks if letter in secret word
            # decreases guesses accordingly if not                      
            if letter_guess not in secret_word:
              if letter_guess in vowels:
                number_of_guesses = number_of_guesses - 2
              if letter_guess in consonants:
                number_of_guesses = number_of_guesses - 1

        # if letter not already guessed, checks if in secret word or not
        if letter_guess not in duplicate_guesses:
          if letter_guess in secret_word:
            print ("Good guess: {}".format(get_guessed_word(secret_word, letters_guessed)))          
          else:
            if letter_guess in letters:
              print ("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letters_guessed))) 
            
        # checks whether all letters in secret word have been guessed and returns total score
        # ends current game  
        if is_word_guessed(secret_word, letters_guessed) == True:
          print ("Congratulations, you've won! The word was {}".format(secret_word))
          print ("Your total score for this game is {}".format (number_of_guesses * len(set(secret_word))))  
          print ("-------------")
          break
          
             
      
    else:
        print ("Sorry, you ran out of guesses. The word was {}".format(secret_word)) 
        print ("-------------")

while True:
  if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
      secret_word = choose_word(wordlist)
      hangman(secret_word)
                                                                                  
