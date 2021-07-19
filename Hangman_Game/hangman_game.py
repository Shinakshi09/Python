"""
What is Hangman Game

Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.

"""

random_word_list = ['Artwork', 'Orbit', 'Rocket', 'Alien']

"""
Step : 1

Randomly select a word and assign a variable to it , variable selected_word

"""
import random

selected_word = random.choice(random_word_list)

""" 

Step 2 :

Asking the user to guess a letter and assign this to a variable called guess

"""
guess = input("guess a letter").lower()

"""
Step 2 :

Checking if the letter the user guessed is one of the  letters in the selected_word

"""

 for letter in selected_word:

     if letter == guess:
         print("Correct")

     else:
         print("Incorrect")


"""

Step 3 :

 Create an empty list  called show. For each letter in selected_Word, add  a "_" to the list 'show'


 So if the selected_Word was orbit. show should be [" _ " , "_ " , "_ ", "_", "__"] with 5  "_"  representing each letter to guess

"""

show= []

for _ in  range(len(selected_word)):
    
    show += " _ "

print(show)





