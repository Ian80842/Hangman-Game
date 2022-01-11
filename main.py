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
        
        # Check to see if the player's guess is in the chosen word
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
        run = check_win_condition(underscores, alphabet, word_length, num_wrong, max_guesses, chosen_word, run)
        
        # Give them a hint after 5 wrong guesses
        give_hint(num_wrong, underscores, chosen_word)

        # Show how much of the alphabet they have left
        print_options(abc)
        
    else:
        print("invalid input")
        for a in abc:
            print(a + ", ", end="", flush=True)
        print("")
