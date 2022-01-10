import random
import json
from functions import *

words = json.loads(open("words.json").read())
alphabet = json.loads(open("abc.json").read())
abc = json.loads(open("abc.json").read())
word_num = random.randint(0, 212)

num_right = 0
num_wrong = 0
max_guesses = 10

chosen_word = words[word_num]
underscores = []
word_length = len(chosen_word)

for i in range(word_length):
    print("_", end="", flush=True)
    underscores.append("_")

print("\n")
run = True
while run:
    guess = input("what letter would you like to guess?  ")
    if guess in abc:
        if guess in chosen_word:
            i = 0
            for letter in chosen_word:
                i += 1
                if letter == guess:
                    underscores[i - 1] = guess

        else:
            num_wrong += 1
            guesses_left = 10 - num_wrong
            print("You have " + str(guesses_left) + " guesses left")


        let_in_alpha_num = -1
        for let in abc:
            let_in_alpha_num += 1
            if let == guess:
                abc.pop(let_in_alpha_num)

        # Display the correct letters they have
        for lett in underscores:
            print(lett, end="", flush=True)
        print("")

        # Check to see if the player has won
        num_right = 0
        for letter in underscores:
            if letter in alphabet:
                num_right += 1
        if num_right == word_length:
            print("You won!")
            run = False

        # Check to see if the player has run out of guesses
        if num_wrong >= max_guesses:
            print("You Lost")
            print("The word was: " + chosen_word)
            run = False
            break

        # Give them a hint after 5 wrong guesses
        if num_wrong == 5 and (underscores[0] == '_' or underscores[1] == '_' or underscores[2] == '_'):
            i = 0
            hint = input("would you like a hint?(y/n)  ")
            if hint == 'y':
                for i in range(3):
                    underscores[i] = chosen_word[i]
                for lett in underscores:
                    print(lett, end="", flush=True)
                print("\n you got a hint!")



        # Show how much of the alphabet they have left
        for a in abc:
            print(a + ", ", end="", flush=True)
        print("")
    else:
        print("invalid input")
        for a in abc:
            print(a + ", ", end="", flush=True)
        print("")


input("press enter to finish:  ")