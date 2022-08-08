import random
import hangman


def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["ambulances", "cat", "car", "dog", "hen"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"


def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["elephants", "hospital's", "policeman's"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"


def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["firehouse", "Abraham", "Mercury"]:
            f.write(i + "\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"


def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ["ambulances", "hospitalized", "car", "Abraham", "mercury's"]:
            f.write(i + "\n")
    words = set()
    for _ in range(10):
        word = hangman.get_random_word(my_dict)
        print(word)
        words.add(word)
    assert words == {"hospitalized", "ambulances"}


def test_mask_word():
    assert hangman.mask_word("elephant", ["e", "l"]) == "ele-----"
    assert hangman.mask_word("elephant", []) == "--------"
    assert hangman.mask_word("elephant", ["a"]) == "-----a--"
    assert hangman.mask_word("elephant", ["p", "h", "n", "t"]) == "---ph-nt"
    assert (
        hangman.mask_word("elephant", ["e", "l", "p", "h", "a", "n", "t"]) == "elephant"
    )


def test_not_mask_word():
    assert hangman.mask_word("elephant", ["s", "z", "w"]) == "--------"
    assert hangman.mask_word("elephant", ["m"]) == "--------"
def test_mask_word_single_guess():
    assert hangman.mask_word("elephant",["e"]) == "e-e-----"


def test_get_status():
    secret_word = "pencils"
    guessed_letters = ["p", "e","c"]
    turn_left = 6
    result = f'''{hangman.mask_word(secret_word, guessed_letters)}
    Guessed Letters: {" ".join(guessed_letters)}
    Turns Left: {turn_left}'''
    assert hangman.get_status(secret_word, guessed_letters, turn_left) == result


def test_process_turn_already_guessed():
    current_guess = "p"
    secret_word = "pencils"
    guessed_letters = ["p"]
    turn_left = 6
    assert hangman.process_turn(current_guess, secret_word, guessed_letters, turn_left) ==(guessed_letters, turn_left,hangman.ALREADY_GUESSED)

def test_process_turn_won():
    current_guess = "l"
    secret_word = "pencils"
    guessed_letters = ["p","e","n","c","i","s"]
    turn_left = 6
    assert hangman.process_turn(current_guess,secret_word,guessed_letters,turn_left) == (guessed_letters,turn_left,hangman.WON)


def test_process_turn_lost():
    current_guess = "z"
    secret_word = "pencils"
    guessed_letters = ["p","r","t","o","q"]
    turn_left = 1
    assert hangman.process_turn(current_guess,secret_word,guessed_letters,turn_left) == (guessed_letters,turn_left,hangman.LOST)

def test_process_turn_incorrect_guess():
    current_guess = "z"
    secret_word = "pencils"
    guessed_letters = ["p","r","t","o","q"]
    turn_left = 6
    assert hangman.process_turn(current_guess,secret_word,guessed_letters,turn_left) == (guessed_letters + [current_guess],turn_left - 1,hangman.CONTINUE)

def test_process_turn_correct_guess():
    current_guess = "s"
    secret_word = "pencils"
    guessed_letters = ["p","e","n","c","i"]
    turn_left = 6
    assert hangman.process_turn(current_guess,secret_word,guessed_letters,turn_left) == (guessed_letters + [current_guess],turn_left,hangman.CONTINUE)
