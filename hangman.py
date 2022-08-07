import random
WON=1
LOST=2
CONTINUE=3
ALREADY_GUESSED = 4
def get_random_word(path="/usr/share/dict/words"):
    file=open(path,'r')
    words=list(file)
    updated_words =[]
    for word in words:
            word = word.strip()
            if len(word) < 6:
                continue
            if not word.isalpha():
                continue
            if word[0].isupper():
                continue
            updated_words.append(word)

    return random.choice(updated_words)

def mask_word(secret_word, guessed_letters):
    masked_word = ""
    for c in secret_word:
        if c in guessed_letters:
            masked_word += c
        else:
            masked_word += "-"
    return masked_word




def get_status(secret_word,guessed_letters,turn_left):
    # if result == WON:
    #     return  f"you won\nsecret word is {secret_word}"
    # if result == LOST:
    #     return f"you lost\nsecret word is {secret_word}"
    # already_guessed = f"""your turns left: {turn_left}
    # Guessed Letters: {" ".join(guessed_letters)}
    # {mask_word(secret_word, guessed_letters)}
    # """

    # if result == ALREADY_GUESSED:
    #     already_guessed = "You already guessed that letter\n" + already_guessed
    #     return already_guessed
    return f"""{mask_word(secret_word, guessed_letters)}
    Guessed Letters: {" ".join(guessed_letters)}
    Turns Left: {turn_left}"""



def process_turn(current_guess,secret_word,guessed_letters,turn_left):
    if current_guess in guessed_letters:
        return guessed_letters,turn_left,ALREADY_GUESSED
    if secret_word == mask_word(secret_word,guessed_letters +[current_guess]):
        return guessed_letters,turn_left,WON
    if turn_left == 1:
        return guessed_letters,turn_left,LOST
    guessed_letters = guessed_letters + [current_guess]
    if current_guess not in guessed_letters:
        turn_left -= 1
        return guessed_letters,turn_left,CONTINUE
    else:
        return guessed_letters,turn_left,CONTINUE





def main():
    secret_word = get_random_word()
    guessed_letters = []
    turn_left = 7
    print(secret_word)
    while True:
        print(get_status(secret_word, guessed_letters, turn_left))
        current_guess = input("guess the letter:")
        guessed_letters,turn_left, result = process_turn(
            current_guess, secret_word, guessed_letters, turn_left
        )
        if result == WON:
            print(get_status(secret_word, guessed_letters, turn_left, result))
            break
        if result == LOST:
            print(get_status(secret_word, guessed_letters, turn_left, result))
            break
        

if __name__ == "__main__":
    main()



