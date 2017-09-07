#FILL-IN-THE-BLANKS

from random import randint
from collections import OrderedDict

#print 'ana are mere'

NUMBER_OF_GUESSES = 5

practice_sentences = ["_1_ test _____2__. --__3__??? + == .._____4_\n!?_?___5___."]

easy_sentences = ["\nIn ___1_, function blocks begin with the keyword _2_ and are \
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

insane_answers = [["a1", "b", "c", "d", "e"], \
                  ["a", "b2", "c", "d", "e"], \
                  ["a", "b", "c3", "d", "e"], \
                  ["a", "b", "c", "d4", "e"]]

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

def choice_message(sentences):
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
        level = raw_input("Please select a game difficulty by typing it in !" \
              + "\nPossible choices include " + choice_message(sentences))
        if level in sentences:
            break
        else:
            print "That's not an option !"
    print "You've chosen " + level + " !\n"
    print "You will get %d guesses per problem .\n" % (NUMBER_OF_GUESSES)
    return level, randint(0, len(sentences[level]) - 1)

def valid_data(sentences, answers):
    for key in sentences:
        if ( (not key in answers) or
             (len(sentences[key]) == 0) or
             (len(answers[key]) == 0)):
            print "Inconsistent data found ! Can't start a new game !"
            return False
    return True                            

def exist_answers(answerList, number):
    try:
        #print len(answerList)
        #print number
        assert (len(answerList) > number and len(answerList[number]) > 0)
        return True
    except AssertionError:
        print "Oups ! Something went wrong !\nList of answers not found !"
    return False

def print_paragraph(paragraph, current = True):
    if current == True:
        print "The current paragraph reads as such :\n"
    else:
        print"The final paragraph :\n"
    print 30*"-" + "\n" + paragraph + "\n" + 30*"-" + "\n"

def get_player_input(number):
    response = raw_input("What should be substituted in for _" \
                         + str(number + 1) + "_ ?  ")
    return response

def update_player_status(lives, score, points, isCorrect):
    if isCorrect == True:
        if points == 1:
            print "Correct ! \nYou won 1 point !\n"
        else:
            print "Correct ! \nYou won %d points !\n" % (points)
        lives = NUMBER_OF_GUESSES
        score += points
        points = lives
    else:
        lives -= 1
        if lives > 0:
            print "That isn't the correct answer!  Let's try again; " \
                  + "You have %d tries left!" % (lives)
        if points > 0:
            points -= 1
    return lives, score, points

def update_game(words, answer, index):
    target = "_" + str(index + 1) + "_"
    #print target
    #print "WORDS = \n"
    #print words
    for i in range(0, len(words)):
        #print words[i]
        if words[i].find(target) != -1:
            #print 'gasit'
            word = words[i].replace(target, answer[index], 1)
            words[i] = word
            #print word
            #print words[i]
    #print "WORDS = \n"
    #print words
    return index + 1

def game_result(words, score, lives):
    if lives == 0:
        print "You've failed too many straight guesses!  Game over!\n"
        return None
    else:
        print_paragraph(" ".join(words), False)
        return score

def play(sentence, answer):
    index = 0
    score = 0 
    points = lives = NUMBER_OF_GUESSES
    words = sentence.split()
    #print words
    while index < len(answer) and lives > 0:
        print_paragraph(" ".join(words))
        answerIsGood = answer[index].lower() == get_player_input(index).lower()
        lives, score, points = update_player_status( \
                               lives, score, points, answerIsGood)
        if answerIsGood == True:
            index = update_game(words, answer, index)
    return game_result(words, score, lives)

def print_score(score):
    if score == 1:
        print "Congratulations ! You won ! \n" \
                  + "Your score is : 1 point . \n"
    else:
        print "Congratulations ! You won ! \n" \
                  + "Your score is : %d points . \n" % (score)

def play_game(sentences, answers):
    """ Doctrgings
    """
    print "Welcome to FILL-IN-THE-BLANKS !\n"
    if not valid_data(sentences, answers):
        return
    while True:
        print "\nNew game starting .... Good luck !\n"
        level, variant = choose_level(sentences)
        #print variant
        if not exist_answers(answers[level], variant):
            break
        score = play(sentences[level][variant], answers[level][variant])
        if score != None:
            print_score(score) 
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

#print "There are %d births" % (births,)
#print "There are ", births, "births"

play_game(mySentences, myAnswers)
        

    
    
