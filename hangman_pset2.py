# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
global wordlist 
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True





def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    string = ""
    for index in range(len(secret_word)):
      if secret_word[index] in letters_guessed:
        string = string + secret_word[index] + ' '
      else:
        string += '_ '
    return string



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    avail = ""
    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        avail += letter
    return avail
    
def number_of_unique_letters(secret_word):
  reduced_word = ""
  for letter in secret_word:
    if letter not in reduced_word:
      reduced_word += letter
  return len(reduced_word)


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
    
    print("Wellcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("-------------")

    letters_guessed = ""   
    number_of_warnings_left= 3
    number_of_guesses_left = 6

    def plural_warning(number_of_warnings_left):
      if number_of_warnings_left > 1:
        return "warnings"
      else:
        return "warning"

    def plural_guess(number_of_guesses_left):
      if number_of_guesses_left > 1:
        return "guesses"
      else:
        return "guess"
    print("you have", number_of_warnings_left, plural_warning(number_of_warnings_left), "left.")

    while not is_word_guessed(secret_word, letters_guessed) and number_of_guesses_left > 0:
      print("You have", number_of_guesses_left, plural_guess(number_of_guesses_left), "left.")
      print("Available letters:", get_available_letters(letters_guessed))

      guess_letter = (input("Please guess a letter:")).lower()
      
      if guess_letter in letters_guessed:
        print("You have already guessed that letter.")

        if number_of_warnings_left== 0:
          print("You have no warning left. You will lose 1 guess")
          number_of_guesses_left -= 1
        else:
          number_of_warnings_left -= 1
          print("You now have", number_of_warnings_left, plural_warning(number_of_warnings_left),"left.")

      elif guess_letter in secret_word:
        print("Good guess!")

      elif guess_letter in string.ascii_lowercase:
        print("Oops! That letter is not in my word.")
        
        if guess_letter in "aeio":
          print("You lose 2 guesses because you have guessed a wrong vowel.")
          number_of_guesses_left -= 2
        else:
          number_of_guesses_left -= 1

      else:
        print("Oops! That is not a valid letter.")
        if number_of_warnings_left == 0:
          print("You have already had 3 warnings. You will lose 1 guess")
          number_of_guesses_left -= 1
        else:
          number_of_warnings_left -= 1
          print("You now have", number_of_warnings_left, plural_warning(number_of_warnings_left),"left.")

      letters_guessed += guess_letter
      print(get_guessed_word(secret_word, letters_guessed))
      print("-----------")
    
    if is_word_guessed(secret_word, letters_guessed):

      total_score = number_of_guesses_left * number_of_unique_letters(secret_word)
      print("Congratulations, you won!")
      print("Your total score for this game is:", total_score)
    
    else:
      print("Sorry, you ran out of guesses. The word was", secret_word + ".")





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(other_word) != len(my_word)/2:
      return False
    else:
      for index in range(len(other_word)):
        if my_word[2*index] != '_':
          if other_word[index] != my_word[2*index]:
            return False
        elif other_word[index] in my_word:
          return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_list = []
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):
        matched_list.append(other_word)
    if len(matched_list) == 0:
      print("No matches found.")
    else:
      print(" ".join(matched_list))
    return matched_list

def show_less_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_list = []
    for other_word in wordlist:
      if match_with_gaps(my_word, other_word):        
        def is_match(other_word):
          for letter in letters_guessed:
            if letter not in my_word and letter in other_word:
              return False
          return True

        if is_match(other_word):
          matched_list.append(other_word)

    if len(matched_list) == 0:
      print("No matches found.")
    else:
      print(" ".join(matched_list))
    return matched_list




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Wellcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    

    letters_guessed = ""   
    number_of_warnings_left = 3
    number_of_guesses_left = 6


    def plural_warning(number_of_warnings_left):
      if number_of_warnings_left > 1:
        return "warnings"
      else:
        return "warning"

    def plural_guess(number_of_guesses_left):
      if number_of_guesses_left > 1:
        return "guesses"
      else:
        return "guess"
    print("you have", number_of_warnings_left, plural_warning(number_of_warnings_left), "left.")
    print("You can enter the asterisk symbol * for hint.")
    print("-------------")
    while not is_word_guessed(secret_word, letters_guessed) and number_of_guesses_left > 0:
      print("You have", number_of_guesses_left, plural_guess(number_of_guesses_left), "left.")
      print("Available letters:", get_available_letters(letters_guessed))

      guess_letter = (input("Please guess a letter:")).lower()
      
      if guess_letter in letters_guessed:
        print("You have already guessed that letter.")

        if number_of_warnings_left == 0:
          print("You have already had 3 warnings. You will lose 1 guess")
          number_of_guesses_left -= 1
        else:
          number_of_warnings_left -= 1
          print("You now have", number_of_warnings_left, plural_warning(number_of_warnings_left),"left.")

      elif guess_letter in secret_word:
        print("Good guess!")

      elif guess_letter in string.ascii_lowercase:
        print("Oops! That letter is not in my word.")
        
        if guess_letter in "aeio":
          print("You lose 2 guesses because you have guessed a wrong vowel.")
          number_of_guesses_left -= 2
        else:
          number_of_guesses_left -= 1

      else:
        global wordlist 
        if guess_letter == '*':
          
          wordlist = show_possible_matches(get_guessed_word(secret_word, letters_guessed))
          
        elif guess_letter == '**':
          
          wordlist = show_less_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)

        elif guess_letter == '***':
          print(secret_word)
        else:
          print("Oops! That is not a valid letter.")
          if number_of_warnings_left == 0:
            print("You have already had 3 warnings. You will lose 1 guess")
            number_of_guesses_left -= 1
          else:
            number_of_warnings_left -= 1
            print("You now have", number_of_warnings_left, plural_warning(number_of_warnings_left),"left.")

      if guess_letter not in ['*', '**', '***']:
        letters_guessed += guess_letter
      print(get_guessed_word(secret_word, letters_guessed))
      print("-----------")
    
    if is_word_guessed(secret_word, letters_guessed):

      total_score = number_of_guesses_left * number_of_unique_letters(secret_word)
      print("Congratulations, you won!")
      print("Your total score for this game is:", total_score)
    
    else:
      print("Sorry, you ran out of guesses. The word was", secret_word + ".")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# secret_word = choose_word(wordlist)
# hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
secret_word = choose_word(wordlist)

hangman_with_hints(secret_word)
