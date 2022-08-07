import random
import hangman
def test_get_random_word_min_length_6():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'cat', 'car', 'dog', "hen"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "ambulances"
def test_get_random_word_no_non_alphanum():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['elephants', "hospital's", "policeman's"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "elephants"

def test_get_random_word_no_proper_noun():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['firehouse', "Abraham", "Mercury"]:
            f.write(i+"\n")
    word = hangman.get_random_word(my_dict)
    assert word == "firehouse"
def test_get_random_word():
    my_dict = "/tmp/my_dict.txt"
    with open(my_dict, "w") as f:
        for i in ['ambulances', 'hospitalized', 'car', 'Abraham', "mercury's"]:
            f.write(i+"\n")
    words = set()
    for _ in range(10):
        word = hangman.get_random_word(my_dict)
        print (word)
        words.add(word)
    assert words == {"hospitalized", 'ambulances'}
def test_mask_word():
    assert hangman.mask_word('elephant',['e','l']) == 'ele-----'
    assert hangman.mask_word('elephant',[]) == '--------' 
    assert hangman.mask_word('elephant',['a']) == '-----a--'
    assert hangman.mask_word('elephant',['p','h','n','t']) == '---ph-nt' 
    assert hangman.mask_word('elephant',['e','l','p','h','a','n','t']) == 'elephant' 
def test_not_mask_word():
    assert hangman.mask_word('elephant',['s','z','w']) == '--------'
    assert hangman.mask_word('elephant',['m']) == '--------'


def test_process_turn():
    


    
