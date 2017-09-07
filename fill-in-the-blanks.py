#FILL-IN-THE-BLANKS

from random import randint
from collections import OrderedDict

#print 'ana are mere'

practice_sentences = ["_1_ test _____2__. --__3__??? + == .._____4_!?_?___5___."]

easy_sentences = ["\nIn _1_, function blocks begin with the keyword _2_ and are \
followed by the _3_ name and _4_."]

medium_sentences = ["\n_1_ are the essential _2_ that lets us execute a series \
of _3_ as many _4_ as we want."]

hard_sentences = ["\n_1_ expressions use the _2_ character to indicate special _3_ \
or to allow special characters to be used without _4_ their special meaning."]

insane_sentences = ["_1_ _2_ _3_ _4_ _5_", \
                    "_1_ ? _2_ ? _3_ ? _4_ ? _5_", \
                    "_1_?_2_?_3_?_4_?_5_", \
                    "?_1_?_2_?_3_?_4_?_5_?" ]

practice_answers = [["a", "b", "c", "d", "e"]]

easy_answers = [["a", "b", "c", "d"]]

medium_answers = [["a", "b", "c", "d"]]

hard_answers = [["a", "b", "c", "d"]]

insane_answers = [["a", "b", "c", "d", "e"], \
                  ["a", "b", "c", "d", "e"], \
                  ["a", "b", "c", "d", "e"], \
                  ["a", "b", "c", "d", "e"]]

#print easy_sentence

mySentences = OrderedDict([
             ("practice" , practice_sentences),
             ("easy"     , easy_sentences),
             ("medium"   , medium_sentences),
             ("hard"     , hard_sentences),
             ("insane"   , insane_sentences)
            ])

myAnswers = {
             "practice" : practice_answers,
             "easy"     : easy_answers,
             "medium"   : medium_answers,
             "hard"     : hard_answers,
             "insane"   : insane_answers,
            }

def keep_playing():
    choice = raw_input("Do you want to start a new game ? (y/n) : ")
    while choice.lower() != 'y' and choice.lower() != 'n':
        print "That's not an optin !\n", \
              "Type "'y'" to start a new game or "'n'" to exit !"
        choice = raw_input("Try again ? (y/n) : ")
    if choice.lower() == 'y':
        return True   
    return False

def generate_choice_message(sentences):
    myKeys = sentences.keys()
    message = myKeys[0]
    index = 1
    while index < len(myKeys) - 1:
        message = message + ", " + myKeys[index]
        index += 1
    message = message + " and " + myKeys[index] + ".\n"
    return message
        

def choose_level(sentences):
    while True:
        level = raw_input("Please select a game difficulty by typing it in !\n" \
              + "Possible choices include " + generate_choice_message(sentences))
        if level in sentences:
            break
        else:
            print "That's not an option !"
    return level, randint(0, len(sentences[level]) - 1)

def valid_data(sentences, answers):
    for key in sentences:
        if ( (not key in answers) or
             (len(sentences[key]) == 0) or
             (len(answers[key]) == 0)):
            print "Inconsistent data found ! Game over !"
            return False
    return True                            

def exist_answers(answer, number):
    try:
        #print len(answer)
        #print number
        assert len(answer) > number
        return True
    except AssertionError:
        print "Oups ! Something went wrong !\nList of answers not found !"
    return False

def play_game(sentences, answers):
    """ Doctrgings
    """
    print "Welcome to FILL-IN-THE-BLANKS !\n"
    while True:
        print "\nNew game starting .... Good luck !\n"
        if not valid_data(sentences, answers):
            break
        level, variant = choose_level(sentences)
        #print variant
        if not exist_answers(answers[level], variant):
            break
        #score = play(level, variant)
        #if score == -1:
            #print "You lost !"
        #else:
            #print score
        if not keep_playing():
            break
    print "\nGoodbye !"

#try:
    #assert "birthday cake" == "ice cream cake"
#except AssertionError:
    #print 'Houston, we have a problem.'
    #raise

#x = 'aaaa'
#y = 'bbb'

# assert(x==y)

play_game(mySentences, myAnswers)
        
        
    
    
