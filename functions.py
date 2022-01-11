def check_win_condition(underscores, alphabet, word_length, num_wrong, max_guesses, chosen_word, run):
    num_right = 0
    for letter in underscores:
        if letter in alphabet:
            num_right += 1
    if num_right == word_length:
        print("You won!")
        return False

    # Check to see if the player has run out of guesses
    if num_wrong >= max_guesses:
        print("You Lost")
        print("The word was: " + chosen_word)
        return False
    else:
        return True

def give_hint(num_wrong, underscores, chosen_word):
    if num_wrong == 5 and (underscores[0] == '_' or underscores[1] == '_' or underscores[2] == '_'):
        i = 0
        hint = input("would you like a hint?(y/n)  ")
        if hint == 'y':
            for i in range(3):
                underscores[i] = chosen_word[i]
            for lett in underscores:
                print(lett, end="", flush=True)
            print("\n you got a hint!")

def print_options(abc):
    for a in abc:
        print(a + ", ", end="", flush=True)
    print("")