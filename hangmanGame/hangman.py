"""************** The Hangman Code *****************"""

import emoji
import random
from words import word_list


class Hangman():

    #Function that will generate a random word from the wordlist python file
    def getWord(self):
        self.randomWord = random.choice(word_list)
        return self.randomWord


    #Function display the drawing of hangman
    def display_hangman(self,trial):
        self.stages = [  # initial state(empty space): When trial = 0
                    """
                       --------
                       |      |
                       |      
                       |
                       |
                       |
                       -
                    """,
                    #second state (head): When trial = 1
                    """
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    """,
                    # third state (head & torso): When trial = 2
                    """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    """,
                    # fourth state (head, torso, and one arm): When trial = 3
                    """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    """,
                    # fifth state (head, torso, and both arms): When trial = 4
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    """,
                    # sixth state (head,torso,both arms and one leg): When trial = 5
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    """,
                    # final state (head,torso,both arms and both leg): When trial = 6
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """
        ]
        return self.stages[trial]


    #Function that request for user input
    def user_input(self):
        guess = input("\nEnter your guess: ")
        return guess
        

    #Function that sets and executes the game
    def hangman(self,randomWord):

        #lists each character of the word
        self.word = list(randomWord)
        #print(self.word)

        #prints the welcome message for the player
        print(emoji.emojize('\nWelcome to Hangman Game!!:grinning_face_with_big_eyes::grinning_face_with_big_eyes:\n'))
        print("\nLet's play the game...")

        self.hidden = []
        self.char_guessed = []

        #loop will replace every character with '_"
        for character in word:
            self.hidden.append("_")
            
        self.trial = 0
        self.max_trial = 6
        self.gameOver = False
        print(self.display_hangman(self.trial))

        #loop will continue till the gameOver ==True 
        while not self.gameOver:

            self.attempt = self.max_trial - self.trial
            print("You have "+str(self.attempt) + " remaining attempts!!")
            print("\nCurrent word is: " + str(self.hidden))

            #Function called for user input
            guess = self.user_input()
            
            try:
                #if the input is not alphabet, error will be catched
                if guess.isalpha() == False:
                    raise Exception("opps") 
                  
                if len(guess) == 1 and guess.isalpha():
                    if guess in self.word:
                        if guess in self.char_guessed:
                            print("You already guessed the letter " + guess)
                            print(self.display_hangman(self.trial))
                            
                        else:
                            print("Good Job!! " + guess + " is found in the word.")
                            print(self.display_hangman(self.trial))
                            self.char_guessed.append(guess)

                            #this loop will matches the input with each caharcter of word
                            # and replace "_" with the entered character in it's position
                            
                            for i in range(len(self.word)):
                                self.character = self.word[i]
                                if self.character == guess:
                                    self.hidden[i] = self.word[i]
                                    self.word[i] = "_"

                    else:
                        if guess in self.char_guessed:
                            print ("You already guessed the letter " + guess)
                            print(self.display_hangman(self.trial))
                        else:
                            print("Poor Guess!! " + guess + " is not present in the word.")
                            self.trial= self.trial + 1
                            print(self.display_hangman(self.trial))
                            self.char_guessed.append(guess)

                    #checks if player entered all the matching characters of the word
                    if all("_" == char for char in self.word):
                        print(emoji.emojize("Congratulations!! You won the game :grinning_face_with_big_eyes::grinning_face_with_big_eyes:"))
                        self.gameOver = True

                    #player looses the game if no. of trials == maximum trial
                    if (self.trial > self.max_trial or self.trial == self.max_trial):
                        print(emoji.emojize("Sorry!! You lost the game :disappointed_face::disappointed_face:"))
                        print("\nThe word was: " + randomWord.upper())
                        self.gameOver = True

            # error is catched if user input is not an alphabet          
            except Exception:
                print("Oops!  That was no valid character. Try again...")
                print(self.display_hangman(self.trial))



    #Function whether user wants to go for another round of game
    def play_again(self):
        game_again = input("\nDo you want to play Again? (Y/N): ")
        return game_again


if __name__ == "__main__":

    while True:
        game = Hangman()
        word = game.getWord()
        game.hangman(word)
        game_again = game.play_again()

        if game_again == 'Y' or game_again == 'y':
            print("\nAnother round starting.....")
            continue
        
        elif game_again == 'N' or game_again == 'n':
            print("\nSee you next time!! Come back soon..")
            break

        else:
            print("\nOops!! That's an invalid option")
            game.play_again()
            
        
    
    
    
