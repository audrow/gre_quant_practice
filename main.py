import numpy as np
import datetime

def displayProblem(operator, values):
    for value in values:
        print value


# def squareNumberD

def getRandomIntDivisibleBy10(minVal, maxVal):
    return np.random.randint(minVal/10.0,maxVal/10.0)*10

def getRandomIntDivisibleBy5(minVal, maxVal):
    include5 = np.random.randint(0,2)
    return getRandomIntDivisibleBy10(minVal, maxVal)+(include5*5)

def getRandomIntEndsIn5(minVal,maxVal):
    return getRandomIntDivisibleBy10(minVal, maxVal)+5


def practiceSquare10s(minVal, maxVal):
    val = getRandomIntDivisibleBy10(minVal, maxVal)
    ans = val**2
    operator = "^2"
    wrongAnsHint = "Square nonzero numbers then add the zeros"
    return {"value" : [val], 
            "answer" : ans,
            "operator" : operator,
            "wrong answer hint": wrongAnsHint}

def practiceMultiplying2Nums(minVal, maxVal):
    val1 = np.random.randint(minVal, maxVal)
    val2 = np.random.randint(minVal, maxVal)
    ans = val1*val2
    operator = "*"
    wrongAnsHint = ""
    return {"value" : [val1, val2], 
            "answer" : ans,
            "operator" : operator,
            "wrong answer hint": wrongAnsHint}

def askUserForAnswer(problem, minVal, maxVal):

    problemDesc = problem(minVal, maxVal)
    vals = problemDesc["value"]
    ans = problemDesc["answer"]
    operator = problemDesc["operator"]
    wrongAnsHint = problemDesc["wrong answer hint"]

    question = ""
    if len(vals) == 1:
        question = "What is " + str(vals[0]) + str(operator) + "?\n\t"
    else:
        question = "What is "
        for idx, val in enumerate(vals):
            if idx < len(vals)-1: # not last element
                question += str(val) + operator 
            else:
                question += str(val)

        question += "?\n\t"

    isNotValidEntry = True
    while isNotValidEntry:
        userInput = raw_input(question)
        if set('/*+-^').intersection(userInput):
            print "\nAre you trying to cheat?\n"
            continue
        try:
            userAns = int(userInput)
            isNotValidEntry = False
        except:
            print "\n***Must enter a digit\n"
            isNotValidEntry = True

    if userAns == ans:
        print "Correct!\n"
        return True
    elif wrongAnsHint != "":
        print "Incorrect: \n\t" + wrongAnsHint + "\n"
    else:
        print "Incorrect!\n"
    return False



askUserForAnswer(practiceSquare10s, 1, 100)
askUserForAnswer(practiceMultiplying2Nums,1,21)

# for i in range(0,100):
    # getRandomIntDivisibleBy5(0, 100)
    # print getRandomIntDivisibleBy5(0,100)

# timeStart =  datetime.datetime.now()
# print  datetime.datetime.now()

# import time 
# time.sleep(.5)

# timeEnd =  datetime.datetime.now()
# print  timeEnd - timeStart
