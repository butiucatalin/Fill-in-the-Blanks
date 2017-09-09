#FILL-IN-THE-BLANKS

from random import randint
from collections import OrderedDict

#print 'ana are mere'

NUMBER_OF_GUESSES = 5

BLANKS_LIMIT = 1000

practice_sentences = ["_1_ test _____2__. --__3__??? + == .._____4_\n!?_?___5___6_"]

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

practice_answers = [[["yes1" , "yes2"], ["b"], ["c"], ["d","dd","ddd"], ["e"] ,["pula"]]]

easy_answers = [[["a"], ["b"], ["c"], ["d"]]]

medium_answers = [[["a"], ["b"], ["c"], ["d"]]]

hard_answers = [[["a"], ["b"], ["c"], ["d"]]]

insane_answers = [[["a1"], ["b"], ["c"], ["d"], ["e"]], \
                  [["a"], ["b2"], ["c"], ["d"], ["e"]], \
                  [["a"], ["b"], ["c3"], ["d"], ["e"]], \
                  [["a"], ["b"], ["c"], ["d4"], ["e"]]]

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

def print_current_score(score, points):
    current = "Your current score is : %d\n" %(score + points)
    if points == 1:
        print "Correct ! \nYou won 1 point ! " + current
    else:
        print "Correct ! \nYou won %d points ! " % (points) + current

def update_player_status(lives, score, points, isCorrect):
    if isCorrect == True:
        print_current_score(score, points)
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

def nearby_blank(word, start, maxBlank, toRight):
    number = 0
    prod = 1
    if(toRight):
        while start < len(word) and word[start].isdigit() and number<maxBlank:
            number = 10 * number + (int)(word[start])
            start += 1
        #print "unum " + str(number)
        if start < len(word) and number <= maxBlank and word[start] == '_':
            return True
    else:
        while start >= 0 and word[start].isdigit() and number<maxBlank:
            number += prod * int(word[start])
            prod *= 10
            start -= 1
        #print "unum " + str(number)
        if start >=0 and number <= maxBlank and word[start] == '_':
            return True
    return False
    
def left_blank_edge(word, start, maxBlank):
    while start >= 0 and word[start] == '_':
        start -= 1
    if start < 0:
        return 0
    if nearby_blank(word, start, maxBlank, False):
        return start + 2
    return start + 1

def right_blank_edge(word, start, maxBlank):
    while start < len(word) and word[start] == '_':
        start += 1
    if start >= len(word):
        return len(word) - 1
    if nearby_blank(word, start, maxBlank, True):
        return start -2
    return start - 1

def replace_blank(word, target, newString, maxBlank):
    startIndex = 0
    findPosition = 0
    while True:
        findPosition = word.find(target, startIndex)
        if findPosition == -1:
            break
        #print "word = " + word[startIndex:]
        #print "target = " + target
        leftIndex = left_blank_edge(word, findPosition, maxBlank)
        #print "leftIndex = " + str(leftIndex)
        rightIndex = right_blank_edge(word, \
                                      findPosition + len(target) -1 , maxBlank)
        #print "rightIndex = " + str(rightIndex)
        word = word[:leftIndex] + newString + word[(rightIndex + 1):]
        startIndex = leftIndex + len(newString)
        #print word + " start = " + str(startIndex)
    return word
        #startIndex = findPosition + len(target)
        #print findPosition

def found_in(words, target):
    for word in words:
        if word.find(target) != -1:
            return True
    return False

def update_game(words, target, answer, theAnswer, index):
    #print target
    #print "WORDS = \n"
    #print words
    for i in range(0, len(words)):
        #print words[i]
        #print 'gasit'
        words[i] = replace_blank(words[i], target, \
                                 theAnswer, min(BLANKS_LIMIT, len(answer)))
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

def check_answer(answer, index):
    response = get_player_input(index).lower()
    if response in answer[index]:
        return True, response
    return False, None

def play(sentence, answer):
    index = 0
    score = 0 
    points = lives = NUMBER_OF_GUESSES
    words = sentence.split()
    #print words
    while index < len(answer) and lives > 0:
        target = "_" + str(index + 1) + "_"
        if found_in(words, target):
            print_paragraph(" ".join(words))
            answerIsGood, theAnswer = check_answer(answer, index)
            lives, score, points = update_player_status( \
                               lives, score, points, answerIsGood)
            if answerIsGood == True:
                index = update_game(words, target, answer, theAnswer, index)
        else:
            index += 1
    return game_result(words, score, lives)

def print_final_score(score):
    if score == 1:
        print "Congratulations ! You won ! \n" \
                  + "Your final score is : 1 point . \n"
    else:
        print "Congratulations ! You won ! \n" \
                  + "Your final score is : %d points . \n" % (score)

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
            print_final_score(score) 
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

#c="12k"
#print c[2].isdigit()
#print left_blank_edge("_7_______1__",8,100)
#print right_blank_edge("__1__25_",3,100)
#print "_1_2_1___ma_1____pula1_1___________"
#ss=["abc","aka","pula"]
#cc="pula"
#print cc in ss
#print replace_blank("_1_2_1___ma_1____pula1_1___________","_1_","piciu",14)
play_game(mySentences, myAnswers)
        

    
    
