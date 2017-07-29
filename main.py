import numpy as np
import datetime
import random
import math

import test # Run tests

def findFactorials(num):
    if num < 2: raise ValueError('`num` must be greater than 1')

    tmp = num
    factorials = []
    while tmp != 1:
        divisor = 2
        while tmp % divisor != 0:
            divisor += 1
        tmp /= divisor
        factorials.append(divisor)
    return factorials

def findFirstValueWithDivisorAboveValue(value, divisor):
    if value % 1 != 0: raise ValueError('`value` must not have decimals')
    if divisor % 1 != 0: raise ValueError('`divisor` must not have decimals')
    if divisor == 0: raise ValueError('`divisor` must not be 0')
    if divisor == 0: raise ValueError('`divisor` must not be 0')

    while value % divisor != 0:
        value += 1
    return value

def findFirstValueWithDivisorBelowValue(value, divisor):
    if value % 1 != 0: raise ValueError('`value` must not have decimals')
    if divisor % 1 != 0: raise ValueError('`divisor` must not have decimals')
    if divisor == 0: raise ValueError('`divisor` must not be 0')

    value -= 1 # for non inclusive
    while value % divisor != 0:
        value += 1
    return value


def getRandomIntDivisibleByNum(minVal, maxVal, divisor):
    if minVal >= maxVal: raise ValueError('`minVal` must be less than `maxVal`')
    startValue = findFirstValueWithDivisorAboveValue(minVal, divisor)
    endValue = maxVal
    return random.choice(np.arange(startValue, endValue, divisor))

def getRandomIntDivisibleBy5(minVal, maxVal):
    return getRandomIntDivisibleByNum(minVal, maxVal, 5)

def getRandomIntDivisibleBy10(minVal, maxVal):
    return getRandomIntDivisibleByNum(minVal, maxVal, 10)

def getRandomIntEndsIn5(minVal,maxVal):
    return getRandomIntDivisibleBy10(minVal, maxVal)+5

def makeDictForPractice(valArray, ans, question, wrongAnsHint):
    return {"value" : valArray, 
            "answer" : ans,
            "question" : question,
            "wrong answer hint": wrongAnsHint}

def practiceSquare10s(minVal, maxVal):
    val = getRandomIntDivisibleBy10(minVal, maxVal)
    ans = val**2
    question = "What is %s^2?" % val
    wrongAnsHint = "Square nonzero numbers then add the zeros"
    return makeDictForPractice([val], ans, question, wrongAnsHint)

def practiceMultiplying2Nums(minVal1, maxVal1, minVal2, maxVal2):
    val1 = np.random.randint(minVal1, maxVal1)
    val2 = np.random.randint(minVal2, maxVal2)
    ans = val1*val2
    question = "What is %s*%s?" % (val1, val2)
    wrongAnsHint = ""
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceCombinations(maxVal):
    assert(maxVal > 4)
    n = np.random.randint(4, maxVal)
    k = np.random.randint(2, n-1)
    ans = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    question = "What is %s choose %s?" % (n, k)
    wrongAnsHint = "n! / (k!*(n-k)!)"
    return makeDictForPractice([n, k], ans, question, wrongAnsHint)
    
def practiceFactorials(minVal, maxVal):
    val = np.random.randint(minVal, maxVal)
    ans = findFactorials(val)
    question = "What are the factorials of %s? Input as a list." % val
    wrongAnsHint = ""
    return makeDictForPractice([val], ans, question, wrongAnsHint)



def runTimeAndGiveMetricsOnQuestions(questions, numQuestionsToAsk):

    print "\nGRE MATH PRACTICE\n=================\n"

    isCorrectForEachQuestion = []
    timeForEachQuestion = []
    for i in range(0,numQuestionsToAsk):

        startTime =  datetime.datetime.now()

        print "Question %s:" % (i+1)
        question = random.choice(questions)
        isCorrect = askUserForAnswer(question)

        endTime = datetime.datetime.now() 
        timeForEachQuestion.append((endTime-startTime).seconds)
        isCorrectForEachQuestion.append(isCorrect)

    printFeedback(isCorrectForEachQuestion, timeForEachQuestion)

def askUserForAnswer(problem):
    problemDesc = problem()
    vals = problemDesc["value"]
    ans = problemDesc["answer"]
    question = problemDesc["question"]
    wrongAnsHint = problemDesc["wrong answer hint"]

    isNotValidEntry = True
    while isNotValidEntry:
        userInput = raw_input("\t" + question + "\n\t")
        if set('/*+-^').intersection(userInput):
            print "\nAre you trying to cheat?\n"
            continue
        try:
            userAns = float(userInput)
            isNotValidEntry = False
        except:
            try:
                userAns = list(eval(userInput))
                isNotValidEntry = False
            except:
                print "\n***Must enter a digit or list\n"
                isNotValidEntry = True

    if userAns == ans:
        print "\tCorrect!\n"
        return True
    elif wrongAnsHint != "":
        print "\tIncorrect! Answer is " + str(ans) + "\n\t\t" + wrongAnsHint + "\n"
    else:
        print "\tIncorrect! Answer is " + str(ans) + "\n"
    return False

def printFeedback(isCorrectList, solveTimeList):
    numQuestions = len(isCorrectList)

    correctAnswers = sum(isCorrectList)

    totalTime = sum(solveTimeList)
    avgTime = totalTime/numQuestions
    longestTimeIdx = solveTimeList.index( max(solveTimeList) )

    print "\nSUMMARY\n======="
    print "\tCorrect:       \t%s / %s " % (correctAnswers, numQuestions)
    print "\tTotal time:   \t%s seconds\t" % (totalTime)
    print "\tAverage time: \t%s seconds\t" % (avgTime)
    print "\tSlowest question was question %s (%s seconds) \t" % (longestTimeIdx, solveTimeList[longestTimeIdx])
   
# TODO 
# - Press q to quit
# - Add relative frequency to functions
# - Add sexy intro and summary
# - Add the following
#       - Square value ending in 5
#       - Square value + or - known value
#       - Double and halve multiply
#       - Divide by 2 and multiply by 10 for multiply by 5

if __name__ == "__main__":

    multiplyNumsLessThan21 = lambda: practiceMultiplying2Nums(3, 21, 3, 21)
    combinationsLessThan8 = lambda: practiceCombinations(8)
    factorialsLessThan50 = lambda: practiceFactorials(10, 100)

    questions = [multiplyNumsLessThan21, 
                 combinationsLessThan8,
                 factorialsLessThan50]
    runTimeAndGiveMetricsOnQuestions(questions, 2)
