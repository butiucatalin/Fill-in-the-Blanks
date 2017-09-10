#FILL-IN-THE-BLANKS
"""Simple console Python Fill-in-the-Blanks Game.

This game has up to five levels and asks the player to answer in the
Python and general computer science related language trivia.

Immediately after running the program, user is prompted to select a
difficulty level from the available difficulty levels .
Once a level is selected, game displays a fill-in-the-blank and a
prompt to fill in the first blank.

It is not required to have a single right answer for each of the blanks .
We may have a list of correct answers the player can guess from .

When player guesses correctly, new prompt shows with correct answer
in the previous blank and a new prompt for the next blank .
When players guess incorrectly, they are prompted to try again .
The players can also decide at the beginning how many wrong guesses
they can make before they love . The game has a scoring system too .

"""

from random import randint
from collections import OrderedDict #to use the ordered dictionay
NUMBER_OF_GUESSES = STANDARD_NUMBER_OF_GUESSES = 5
# NUMBER_OF_GUESSES represents the number of guesses players can make
# before they lose and initially is set at its default value
# STANDARD_NUMBER_OF_GUESSES . Value of NUMBER_OF_GUESSES cand be
# modified throughout the game , but STANDARD_NUMBER_OF_GUESSES
# remains a constant 

MAX_GUESSES = 100
# NUMBER_OF_GUESSES stores the maximum number of guesses a player is
# allowed to choose

MAX_POINTS = 5
# maximum number of points a player can get after a right answer

BLANKS_LIMIT = 1000
# the number of blanks in a sentence is limited to this value
#
#          ~ DATA STRUCTURES ~
# 
# Data structures were designed in such a way that new functionality could
# easily be added in the future .
# For each level there is a list of sentences with blanks ( eg:
# practice_sentences , easy_sentences , medium_sentences , hard_sentences ,
# insane_sentences ) . Each of these lists has several sentences the game
# can randomly chose from , every time a new game or level starts . New
# sentences could be added in ( or removed from ) the lists .

practice_sentences = ["The _____1_____ is the program that manages the " \
                    "___2___ of the computer system, including the CPU, " \
                    "memory, storage devices, and input/output devices. " \
                    "A __3_____ gathers data, processes it, outputs the " \
                    "data or information, and _4_ the data or information.",
                      "The binary language consists of two digits: " \
                    "_1_ and _2_.  ___3___ __4____ is the science that " \
                    "attempts to create machines that will emulate " \
                    "the human ____5_____ process.",
                      "When you connect to the __1_______, your computer " \
                    "is communicating with a ______2_ at your Internet " \
                    "service provider (_3_). Next, name 3 diferent " \
                    "network protocols: __4_,_5__ and __6__.",
                      "Let's have some fun ! Name an operating system " \
                    "composed of three leters : _1_2_3_ . _4__5_____ " \
                    "are using that operating system !"]

easy_sentences = ["A common first thing to do in a __6__ is display "\
                "'Hello __1__!'  In __2__ this is particularly easy; all " \
                "you have to do is type in: __3__ \"Hello __1__!\" " \
                "Of course, that isn't a very useful thing to do. However, " \
                "it is an example of how to output to the user using the " \
                "__3__ command, and produces a program which does something, " \
                "so it is useful in that capacity. It may seem a bit odd " \
                "to do something in a __5__ complete __6__ that can be " \
                "done even more easily with an __4__ file in a browser, but " \
                "it's a step in learning __2__ syntax, and that's really its " \
                "purpose.",
                  "Python is a high __1__ , interpreted and object-oriented " \
                "language . __2__ are for programmers for better " \
                "understanding of the program . In Python , a __3__ name can " \
                "start with an underscore. The statement using \'and\' " \
                "operator results true if both operands are __4__."]

medium_sentences = ["Python has full support for object-__1__ programming " \
                  "including user-defined __2__, inheritance, and " \
                  "run-time binding of __3__. Python has an extensive " \
                  "standard __4__, which is one of the main reasons for " \
                  "its popularity. Python was first created in __5__ 1989",
                    "A __1__ is created with the def keyword . You specify " \
                  "the inputs a __1__ takes by adding __2__ separated by " \
                  "commas between the parantheses. __1__s by default " \
                  "returns __3__ if you don't specity the vale to return. "\
                  "The __2__ can be standard data types such as string, " \
                  "integer, dictionary, tuple, and __4__ or cand be more " \
                  "complicated such as objects and lambda functions."]

hard_sentences = ["__1__ is an __2__ __3__. That means that, unlike " \
                "__3__s like C and its variants, __1__ does not need to be " \
                "compiled before it is run. Other __2__ languages include PHP" \
                " and __4__.__1__ is dynamically __5__d, this means that you " \
                "don't need to state the __5__s of __6__ when you declare " \
                "them or anything tike that. __1__ is well suited to object " \
                "__7__ programming in that it allows the __8__ of classes " \
                "along with composition and __9__ . __1__ does not have " \
                "__10__ specifiers(like __11__'s piblic , private) .",
                  "In __1__, __2__ are first-__3__ objects. This mean that " \
                "they can be assigned to __4__, returned from other __2__ " \
                "and passed into __2__; __3__es are also first __3__ " \
                "objects. Writing __1__ code is __5__ but __6__ it is often " \
                "slower than __7__ languages . Fortunately, __1__ allows the "
                "inclusion of __8__ based __9__ so bottlenecks can be " \
                "__10__ away and often are . The numpy __11__ is a good " \
                "example of this. It's really quite __5__ because a lot of " \
                "number __12__ it does isn't actualy done by __1__!"]

insane_sentences = ["Use _1_2____ when you aren't sure how many __3__ are " \
                  "going to be passed to a __4__, or if we want to pass a " \
                  "sorted list or __5__ of __3__ to a __4__. _1_1_6____ is " \
                  "used when we don't know how many __7__ __3__ will be " \
                  "passed to a __4__, or it can be used to pass values of a " \
                  "__8__ as __7__ __3__. The identifiers ____2_ and ____6_ " \
                  "are a convention, you could also use _1_9____ and " \
                  "_1_1_10_____ but that would not be wise."]

# Answers are also grouped like sentences .
# For each level there is a list of answers .
# The following lists are all nested lists , each of them containing a list of
# answers for the corresponding sentence . Than , each of these inner lists has
# a list of solutions for every blank of the sentence . Finally , a solution
# ( the innermost list ) is a list of strings whose elements a specific blank
# can be replaced with . A list of strings it's been used instead of a single
# solution , because synonyms and multiple choices are allowed .
# A general structure of these lists :
#   [[[s1,s2,...,sn],[s1,s2,...,sm], .... ], [[...],[...],... ] , ... ]
#   |||__________|                        |                           |
#   |||     |                             |                           |
#   ||  solutions for a blank ( strings ) |                           |
#   ||____________________________________|                           |
#   |                |                                                |
#   |       answers for a sentence ( covering all the blanks )        |
#   |_________________________________________________________________|
#                                   |
#     answers for a specific level ( for all sentences in that level )

practice_answers = [[["operating system", "OS"],
                     ["hardware"],
                     ["computer"],
                     ["stores", "keeps", "deposits", "saves", "hoards"]],
                    [["0"],
                     ["1"],
                     ["Artificial"],
                     ["intelligence"],
                     ["thought"]],
                    [["internet"],
                     ["server"],
                     ["ISP"],
                     ["FTP","HTTP","HTTPS","TCP","UDP","POP","SSL","SSH"],
                     ["FTP","HTTP","HTTPS","TCP","UDP","POP","SSL","SSH"],
                     ["FTP","HTTP","HTTPS","TCP","UDP","POP","SSL","SSH"]],
                    [["i"],
                     ["O"],
                     ["S"],
                     ["i"],
                     ["Phones"]]]

easy_answers = [[["world"],
                 ["Python"],
                 ["print"],
                 ["html"],
                 ["Turing"],
                 ["language"]],
                [["level"],
                 ["Comments"],
                 ["function", "variable"],
                 ["true"]]]
                 
medium_answers = [[["oriented"],
                   ["classes"],
                   ["methods"],
                   ["library"],
                   ["December"]],
                  [["function"],
                   ["arguments", "operands"],
                   ["None"],
                   ["list"]]]

hard_answers = [[["Python"],
                 ["interpreted"],
                 ["language"],
                 ["Java", "JavaScript", "Ruby" ,"Forth", "Perl", "R", "J", \
                  "Lisp", "Maple", "Haskell", "DM", "Ant", "Groovy", "REXX" , \
                  "Tcl", "Spin", "Oriel", "PostScript", "S-Lang", "Lua", \
                  "VBScript", "Tea", "LPC", "MUMPS", "Mathematica"],
                 ["type"],
                 ["variables"],
                 ["oriented"],
                 ["definition", "definitions" , "declaration" , "declarations"],
                 ["inheritance"],
                 ["access"],
                 ["C++", "C#", "Java", "PHP"]],
                [["Python"],
                 ["functions"],
                 ["class"],
                 ["variables"],
                 ["quick"],
                 ["running"],
                 ["compiled"],
                 ["C"],
                 ["extensions"],
                 ["optimised"],
                 ["package"],
                 ["crunching"]]]
                 

insane_answers = [[["*"],
                   ["args"],
                   ["arguments"],
                   ["function"],
                   ["tuple"],
                   ["kwargs"],
                   ["keyword"],
                   ["dictionary"],
                   ["bob"],
                   ["billy"]]]

# Dictionaries are used to map levels ( each level its own key eg: level
# name ) to their corrensponding lists of sentences and answers . Thus a
# link is also created between sentences and answers .
#      mySentences[level][i]    => ....... myAnswers[level][i]
# So : the i-th element of myAnswers[level] stores the answers for the
# corrensponding i-th element of mySentences[level] , where "level" in
# the name( also the key ) of the underlying level .
# Requirements :
#      len(myAnswers[level]) >= len(mySentences[level])
# In other words , there must be a list of answers for each of the sentences
# in one particular level .

mySentences = OrderedDict([
             ("practice" , practice_sentences),
             ("easy"     , easy_sentences),
             ("medium"   , medium_sentences),
             ("hard"     , hard_sentences),
             ("insane"   , insane_sentences)
            ])
# An ordered dictionary is used in this case because it's better to list the
# level names ( dictionary's keys ) to the user in a desired way , not in the
# way the keys are sorted by the hashing algorithm .

myAnswers = {
             "practice" : practice_answers,
             "easy"     : easy_answers,
             "medium"   : medium_answers,
             "hard"     : hard_answers,
             "insane"   : insane_answers,
            }

lifeVariations = {
                  "hard"   : -1,
                  "insane" : -2,
                  }
# NUMBER_OF_GUESSES can be altered with various amounts , based on levels

def keep_playing():
    """This function prompts the user to chose if he wants to start a new
game , after a previous game has finished .
    Inputs : (-)
    Outputs : True or False
    Postconditions :
        Function returns True if the player wants to start another game
    and False otherwise .
"""
    choice = raw_input("Do you want to start a new game ? (y/n) : ")
    while choice.lower() != 'y' and choice.lower() != 'n':
        # reprompts until the user enters 'y' or 'n'
        print "That's not an optin !\n", \
              "Type \'y\' to start a new game or \'n\' to exit !"
        choice = raw_input("Try again ? (y/n) : ")
    if choice.lower() == 'y':
        return True   
    return False

def choice_message(sentences):
    """Returns a formatted string representing the names of the game's levels
stored as keys in our ordered dictionary . This gives flexibility to the
program . Levels can be added or removed , without changing other functions .
    Inputs : sentences
    Preconditions :
        sentences is an ordered dictionary and has at least one key
    Outputs : message
    Postconditions :
        message is a string with proper formatting
"""
    myKeys = sentences.keys()
    # get the list of dictionary's keys
    message = myKeys[0]
    index = 1
    while index < len(myKeys) - 1:
        message = message + ", " + myKeys[index]
        index += 1
    message = message + " and " + myKeys[index] + ".\n"
    # construncting the message
    return message
        
def choose_level(sentences):
    """Prompts the user to choose a level , and returns that chosen level
along with a random index pointing to a specific sentence from that level's
list of sentences
    Inputs : sentences
    Preconditions :
        sentences is an ordered dictionary and has at least one key
    Outputs : tuple (level, index)
    Postconditions :
        level is one of the dictionary's keys
        0 <= index < len(sentences[level])
"""
    while True:
        level = raw_input("Please select a game difficulty by typing it in !" \
              + "\nPossible choices include " + choice_message(sentences))
        if level in sentences:
            # prompts until the chosen level is a key in the dictionary
            break
        else:
            print "That's not an option !"
    print "You've chosen " + level + " !\n"
    return level, randint(0, len(sentences[level]) - 1)

def valid_data(sentences, answers):
    """Checks the consistency of our data structures and returns False if
inconsistend data is found : a key is found only in the ordered dictionary or
there is an empty value ( no data ) in one of the dictionaries
    Inputs : sentences , answers
    Preconditions :
        sentences is an ordered dictionary and has at least one key
        answers is a dictionary
    Outputs : True or False
"""
    for key in sentences:
        if ( (not key in answers) or
             (len(sentences[key]) == 0) or
             (len(answers[key]) == 0)):
            print "Inconsistent data found ! Can't start a new game !"
            return False
    return True                            

def exist_answers(answerList, number):
    """Verifies if there are any answers available for the chosen level and
randomly selected sentence
    Inputs : answerList, number
    Preconditions :
        answerList is a list
        answerList = [[[s1,s2,...,sn],[s1,s2,...,sm], .... ],
        [[...],[...],... ] , ... ]
        len(answerList) > number
    Outputs : True or False
    Postconditions :
        True , if len(answerList[number]) > 0
"""    
    try:
        assert (len(answerList) > number and len(answerList[number]) > 0)
        return True
    except AssertionError:
        print "Oups ! Something went wrong !\nList of answers not found !"
    return False

def print_paragraph(paragraph, current = True):
    """As the game progresses , this function prints the parapraph with blanks
replaced by the player's inputs. Finally , it prints the final solution .
    Inputs : paragraph , current(boolean)
    Preconditions :
        paragraph is a string
    Outputs : (-)
"""
    if current == True:
        print "The current paragraph reads as such :\n"
    else:
        print"The final paragraph :\n"
    print 30*"-" + "\n" + paragraph + "\n" + 30*"-" + "\n"

def get_player_input(number):
    """Reads an input from the player as he tries to guess the answer for the
blank number 'number + 1' . In the list , blanks are indexed starting from 0 ,
that's why we have to use 'number + 1' when we refer to the current blank
    Inputs : number
    Outputs : (-)
"""
    response = raw_input("What should be substituted in for _" \
                         + str(number + 1) + "_ ?  ")
    return response

def print_current_score(score, points):
    """Shows player's current score and the latest number of points won
    Inputs : score, points
    Outputs : (-)
"""
    current = "Your current score is : %d\n" %(score + points)
    if points == 1:
        print "Correct ! \nYou won 1 point ! " + current
    else:
        print "Correct ! \nYou won %d points ! " % (points) + current

def choose_guesses_number():
    """Lets the users decide how many wrong guesses they can make before
they lose . Variable 'number' will store that inormation
    Inputs : (-)
    Outputs : number or None
    Postconditions :
        'number' is returned if the user wants to choose , otherwise None is
returned
        1 <= number <= MAX_GUESSES
"""
    choice = raw_input("Do you want to choose how many wrong gusses " \
                       "you can make ? (y/n) : ")
    while choice.lower() != 'y' and choice.lower() != 'n':
        print "That's not an optin !\nType \'y\' if you want to choose " \
              "that or \'n\' to use the game defaults !"
        choice = raw_input("Try again ? (y/n) : ")
    if choice.lower() == 'y':
        while True:
            number = raw_input("Select the number of lives : ")
            try:
                assert (number != None and number.isdigit() == True and \
                        int(number) > 0 and int(number) <= MAX_GUESSES )
                # checks if the input is number ( and a valid one ! )
                return int(number)
            except AssertionError:
                print "Please enter a valid number between 1 and %d !" \
                    % (MAX_GUESSES)
    return None     

def init_player_stats(level):
    """Initialise some of the game stats ( is used when a new game starts )
like : initial score , number of lives , numer of point / right answer ,
according to user's preferences in some cases ( eg: umber of guesses )
    Inputs : level
    Outputs : tuple (score, points, lives)
    Postconditions :
        score = 0
        points = MAX_POINTS
        lives is set according to user's preferences or game's default for
    this particular 'level'
"""
    global NUMBER_OF_GUESSES
    # global is used because we want to change the value of a global variable
    # inside a defined function
    chosen_number = choose_guesses_number()
    if chosen_number != None:
        NUMBER_OF_GUESSES = chosen_number
    elif level in lifeVariations:
        NUMBER_OF_GUESSES = STANDARD_NUMBER_OF_GUESSES + lifeVariations[level]
    else:
        NUMBER_OF_GUESSES = STANDARD_NUMBER_OF_GUESSES
    print "You will get %d guesses per problem .\n" % (NUMBER_OF_GUESSES)
    return 0, MAX_POINTS, NUMBER_OF_GUESSES

def update_player_stats(lives, score, points, isCorrect):
    """Updates the player stats(lives, score, points) during the game , based
on the correctness of the player's answers
    Inputs : lives, score, points, isCOrrect(bolean)
        lives => stores the player's remaining lives ( number of guesses )
        score => keeps track of the player's score
        points => number of points to be added to the score in case of a
                    right answer
    Outputs : tuple(lives, score, points)
    Postconditions :
        if isCorrect = True =>
            lives = NUMBER_OF_GUESSES
            score = score + points
            points = MAX_POINTS
        else =>
            lives = lives - 1
            points = points - 1 ( if points > 0 )
"""
    if isCorrect == True:
        print_current_score(score, points)
        lives = NUMBER_OF_GUESSES
        score += points
        points = MAX_POINTS
    else:
        lives -= 1
        if lives > 0:
            print "That isn't the correct answer!  Let's try again; " \
                  + "You have %d tries left!" % (lives)
            # prompts the player if there are any lives left
        if points > 0:
            points -= 1
    return lives, score, points

def nearby_blank(word, start, maxBlank, toRight):
    """Checks if another blank can be found inside the string 'word' , starting
right at the 'start' position and moving towards the specified direction ( to
the right or to the left ).
    A blank is defined as a substring consisting of a number followed by
underscores ( minimum 1 undescore and only underscores ! ) on each side of
the number . Examples :
            _1_ ; __5__ ; _7_______ ; _____9__ ; ___10____ ; __11___________
    Inputs : word, start, maxBlank, toRight(boolean)
    Preconditions :
        word is a string
        0 <= start < len(word)
    Outputs : True or False ( whether or not a nerby blank is found )
    Postconditions :
        If found , the blank have to be a valid one : its number must be
        lower than maximum number of blanks in the current sentence
    This function solves the case where blanks ar enot properly separated
one from another .
"""
    number = 0
    prod = 1
    if(toRight):
        # searching to the right
        while start < len(word) and word[start].isdigit() and number<maxBlank:
            number = 10 * number + (int)(word[start])
            start += 1
        if start < len(word) and number <= maxBlank and word[start] == '_':
            return True
    else:
        # searching to the left
        while start >= 0 and word[start].isdigit() and number<maxBlank:
            number += prod * int(word[start])
            prod *= 10
            start -= 1
        if start >=0 and number <= maxBlank and word[start] == '_':
            return True
    return False
    
def left_blank_edge(word, start, maxBlank):
    """Finds the left edge of the current blank ( blanks doesn't have a fixed
number of underscores ! ) starting from 'start' position
    Inputs : word, start, maxBlank
    Preconditions :
        word is a string
        0 <= start < len(word)
    Outputs :
        leftEdge
    Postconditions :
        leftEdge = position of the blank's left edge
"""
    while start >= 0 and word[start] == '_':
        # search until there's no more undescors or the string is over
        start -= 1
    if start < 0:
        return 0
    if nearby_blank(word, start, maxBlank, False):
        # if there's a blank to the left , than in this case it should have
        # only one undescore to the right , so that undescore has to be kept
        # and not overwritten by the user inputs => start = start + 2
        return start + 2
    return start + 1

def right_blank_edge(word, start, maxBlank):
    """Finds the right edge of the current blank ( blanks doesn't have a fixed
number of underscores ! ) starting from 'start' position
    Inputs : word, start, maxBlank
    Preconditions :
        word is a string
        0 <= start < len(word)
    Outputs :
        rightEdge
    Postconditions :
        rightEdge = position of the blank's right edge
"""
    while start < len(word) and word[start] == '_':
        # search until there's no more undescors or the string is over
        start += 1
    if start >= len(word):
        return len(word) - 1
    if nearby_blank(word, start, maxBlank, True):
        # if there's a blank to the right , than in this case it should have
        # only one undescore to the left , so that undescore has to be kept
        # and not overwritten by the user inputs => start = start - 2
        return start -2
    return start - 1

def replace_blank(word, target, newString, maxBlank):
    """Replaces with 'newString' all the occurrences of the 'target'
blank within the 'word' string . Edges of the 'target' are to be found later
and that larger substring ( from left edge to right edge ) will be replaced
by 'newString' substring given as user input .
    Inputs : word, target, newString, maxBlank
    Preconditions :
        word is a string
        target is a valid blank ( a string also )
        newString is a string
    Outputs : word
    Postconditions :
        word is modified as mentioned in the description
"""
    startIndex = 0
    #start at the beginning
    findPosition = 0
    while True:
        findPosition = word.find(target, startIndex)
        #search for the target string ( from position startIndex )
        if findPosition == -1:
            # exit when the target cannot be found anymore
            break
        leftIndex = left_blank_edge(word, findPosition, maxBlank)
        rightIndex = right_blank_edge(word, \
                                      findPosition + len(target) -1 , maxBlank)
        # finding the extent of the blank ( the replacement area )
        word = word[:leftIndex] + newString + word[(rightIndex + 1):]
        # replace
        startIndex = leftIndex + len(newString)
        # jump to the right side of the replacement and continue searching
    return word

def found_in(words, target):
    """Checks if there is a sequence(substring) 'target' within the strings of 
the list 'words'
    Inputs : words , target
    Preconditions :
        words is a list of strings
        target is a string
    Outputs : True or False
    Postconditions :
        True , if at teast one of the strings in 'words' contains the
        substring 'target'
        False , otherwise
"""
    for word in words:
        if word.find(target) != -1:
            return True
    return False

def update_game(words, target, answer, theAnswer, index):
    """Replaces with 'theAnswer' al the occurrences of blank 'target' within
the words list( the list of words in the current parapraph ) , updates the
'words' list and moves on to the next blank( increments the index )
    Inputs : words, target, answer, theAnswer, index
    Preconditions :
        words is a list of strings
        target is a blank
        theAnswer is a string
        0 <= index < len(answer)
        index = number of the current blank
    Outputs :
        words ; index
    Postconditions :
        index = number of the next blank
"""
    for i in range(0, len(words)):
        words[i] = replace_blank(words[i], target, \
                                 theAnswer, min(BLANKS_LIMIT, len(answer)))
    return index + 1

def game_result(words, score, lives):
    """Returns the game results and prints a message accordingly . If the
player lost ( used all guesses available ) than game is over , otherwise prints
the final corret paragraph with all of the blanks filled .
    Inputs : words, score, lives
    Outputs : score or None
    Postconditions :
        return None if lives = 0 , else returns the score
"""
    if lives == 0:
        print "You've failed too many straight guesses!  Game over!\n"
        return None
    else:
        print_paragraph(" ".join(words), False)
        return score

def check_answer(answer, index):
    """Asks for a solution and checks if the user's input cand be found
in the list of solutions for the current blank ( represented by 'index' )
    Inputs : answer , index
    Preconditions :
        0 <= index < len(asnwer)
    Outputs : tuple(True or False , anAnswer , None )
    Postconditions :
        if the response is right ( is found in the list ) , than return True
        and anAnswer ; anAnswer = solution written with proper capitalisation
"""
    response = get_player_input(index).lower()
    for anAnswer in answer[index]:
        if response in [ anAnswer.lower() ]:
            return True, anAnswer
    return False, None

def play(sentence, answer, level):
    """Let the user play the game after the level have been chosed
    Inputs : sentence, answer, level
    Preconditions :
        there is a number 0 <= i < len(mySentences) such that :
        sentence = mySentences[level][i] and
        answer = myAnswers[level][i]
    Outputs : score or None
    Postconditions :
        returns the score if the player have won , else returns None
"""        
    index = 0
    score, points, lives = init_player_stats(level)
    words = sentence.split()
    # split the sentence into words
    while index < len(answer) and lives > 0:
        target = "_" + str(index + 1) + "_"
        # creating the blueprint of the balnk ( number index + 1 )
        if found_in(words, target):
            # if the blank is found , the user is prompted
            print_paragraph(" ".join(words))
            answerIsGood, theAnswer = check_answer(answer, index)
            lives, score, points = update_player_stats( \
                               lives, score, points, answerIsGood)
            if answerIsGood == True:
                # update the game if answer is good
                index = update_game(words, target, answer, theAnswer, index)
        else:
            index += 1
    return game_result(words, score, lives)

def print_final_score(score):
    """Prints the final score in a preformatted way .
    Inputs : score
    Outputs : (-)
"""
    if score == 1:
        print "Congratulations ! You won ! \n" \
                  + "Your final score is : 1 point . \n"
    else:
        print "Congratulations ! You won ! \n" \
                  + "Your final score is : %d points . \n" % (score)

def play_game(sentences, answers):
    """The main function ! Starts new games and asks the user to chose a
different level and other options for each of them until the player
decides to quit the game .
    Inputs : sentences, answers
    Preconditions :
        sentences, answers are dictionaries
        valid_data(sentences, answers) must return True
    Outputs : (-)
    """
    print "Welcome to FILL-IN-THE-BLANKS !\n"
    if not valid_data(sentences, answers):
        return
    while True:
        print "\nNew game starting .... Good luck !\n"
        level, variant = choose_level(sentences)
        # selects the level and the random variant
        if not exist_answers(answers[level], variant):
            break
        score = play(sentences[level][variant], answers[level][variant], level)
        if score != None:
            print_final_score(score) 
        if not keep_playing():
            break
    print "\nGoodbye !"

play_game(mySentences, myAnswers)
    
    
