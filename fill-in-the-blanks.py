#FILL-IN-THE-BLANKS

from random import randint

#print 'ana are mere'

practice_sentences = ["_1_ test _____2__. --__3__??? + == .._____4_!?_?___5___."]

easy_sentences = ["\nIn _1_, function blocks begin with the keyword _2_ and are \
followed by the _3_ name and _4_."]

medium_sentences = ["\n_1_ are the essential _2_ that lets us execute a series \
of _3_ as many _4_ as we want."]

hard_sentences = ["\n_1_ expressions use the _2_ character to indicate special _3_ \
or to allow special characters to be used without _4_ their special meaning."]

insane_sentences = ["_1_ _2_ _3_ _4_ _5_", "_1_ ? _2_ ? _3_ ? _4_ ? _5_"]

practice_answers = [["a", "b", "c", "d", "e"]]

easy_answers = [["a", "b", "c", "d"]]

medium_answers = [["a", "b", "c", "d"]]

hard_answers = [["a", "b", "c", "d"]]

insane_answers = [["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"]]

#print easy_sentence

mySentences = {
             "practice" : 1,
             "easy"     : 2,
             "medium"   : 3,
             "hard"     : 4,
             "insane"   : 5,
            }

myAnswers = {
             "practice" : 1,
             "easy"     : 2,
             "medium"   : 3,
             "hard"     : 4,
             "insane"   : 5,
            }

def keep_playing():
    choice = raw_input("Do you want to start a new game ? (y/n) : ")
    while choice.lower() != 'y' and choice.lower() != 'n':
        print "That's not an optin ! \n", \
              "Type "'y'" to start a new game or "'n'" to exit !"
        choice = raw_input("Try again ? (y/n) : ")
    if choice.lower() == 'y':
        return True   
    return False

def play_game(sentences, answers):
    """ Doctrgings
    """
    print "Welcome to FILL-IN-THE-BLANKS !\n"
    print sentences
    while True:
        print "\nNew game starting .... Good luck !\n"
        #level, variant = choose_level(sentences)
        #score = play(level, variant)
        #if score == -1:
            #print "You lost !"
        #else:
            #print score
        if not keep_playing():
            break
    print "\nGoodbye !"

play_game(mySentences, myAnswers)
        
        
    
    
