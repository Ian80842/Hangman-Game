def check_letter(guess, chosen_word, num_wrong, underscores, abc):
    if guess in chosen_word:
        i = 0
        for letter in chosen_word:
            i += 1
            if letter == guess:
                underscores[i - 1] = guess

    else:
        num_wrong += 1
        guesses_left = 10 - num_wrong
        print("\nYou have " + str(guesses_left) + " guesses left\n")

    let_in_alpha_num = -1
    for let in abc:
        let_in_alpha_num += 1
        if let == guess:
            abc.pop(let_in_alpha_num)

    return [num_wrong, underscores, abc]

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
        print("\nkeep up the good work!\n")
        return True

def give_hint(num_wrong, underscores, chosen_word, run):    
    if num_wrong == 5 and (underscores[0] == '_' or underscores[1] == '_' or underscores[2] == '_'):
        i = 0
        hint = input("would you like a hint?(y/n)  ")
        if hint == 'y':
            for i in range(3):
                underscores[i] = chosen_word[i]
            for lett in underscores:
                print(lett, end="", flush=True)
            print("\n you got a hint!")
    elif num_wrong < 5:
        print("You may recieve a hint after 5 inccorect guesses\n")
