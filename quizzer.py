import numpy as np
import datetime
import random
import math

def sampleArray(array, frequencies):
    if len(array) != len(frequencies):
        raise ValueError('`array` and `frequencies` must be the same length')
    if len([x for x in frequencies if x < 0]):
        raise ValueError('`array` and `frequencies` must be positive or zero')
    if sum(frequencies) == 0:
        raise ValueError('`frequencies` must have at least one positive value')

    probabilities = [1.0*x/sum(frequencies) for x in frequencies]
    randomValue = np.random.rand(1)
    probabilitiesSum = 0.0
    for idx, prob in enumerate(probabilities):
        probabilitiesSum += prob
        if randomValue < probabilitiesSum:
            return (array[idx], idx)

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


def practiceSquareInts(minVal, maxVal):
    val = np.random.randint(minVal, maxVal)
    ans = val**2
    question = "What is %s^2?" % val
    wrongAnsHint = ""
    return makeDictForPractice([val], ans, question, wrongAnsHint)

def practiceSquare10s(minVal, maxVal):
    val = getRandomIntDivisibleBy10(minVal, maxVal)
    ans = val**2
    question = "What is %s^2?" % val
    wrongAnsHint = "Square nonzero numbers then add the zeros"
    return makeDictForPractice([val], ans, question, wrongAnsHint)

def practiceSquareEndsIn5(minVal, maxVal):
    val = getRandomIntEndsIn5(minVal, maxVal)
    ans = val**2
    question = "What is %s^2?" % val
    wrongAnsHint = "Take number infront of 5, take product with it plus one, prepend to 25"
    return makeDictForPractice([val], ans, question, wrongAnsHint)

def practiceSquareAdjacentToKnown(minVal, maxVal):
    isAdd5 = np.random.randint(0,2)

    addOrSubtract = 0
    if np.random.randint(0,2):
        addOrSubtract = 1
    else:
        addOrSubtract = -1

    val = getRandomIntDivisibleBy10(minVal, maxVal) + isAdd5*5 + addOrSubtract
    ans = val**2
    question = "What is %s^2?" % val
    wrongAnsHint = "n^2 + n + (n+1) = (n+1)^2"
    return makeDictForPractice([val], ans, question, wrongAnsHint)

def practiceAdding2Nums(minVal1, maxVal1, minVal2, maxVal2):
    val1 = np.random.randint(minVal1, maxVal1)
    val2 = np.random.randint(minVal2, maxVal2)
    ans = val1+val2
    question = "What is %s+%s?" % (val1, val2)
    wrongAnsHint = ""
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceSubtracting2Nums(minVal1, maxVal1, minVal2, maxVal2):
    val1 = np.random.randint(minVal1, maxVal1)
    val2 = np.random.randint(minVal2, maxVal2)
    ans = val1-val2
    question = "What is %s-%s?" % (val1, val2)
    wrongAnsHint = "Add single value to both terms to get nice number: a-b = (a+k) - (b+k)"
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceSub2NumsOnesIn2ndNumAreGreater(minVal1, maxVal1, minVal2, maxVal2):
    tens1 = getRandomIntDivisibleBy10(minVal1, maxVal1)
    tens2 = getRandomIntDivisibleBy10(minVal2, maxVal2)
    ones1 = np.random.randint(0,9)
    ones2 = np.random.randint(ones1,10)
    val1 = tens1+ones1
    val2 = tens2+ones2
    ans = val1-val2
    question = "What is %s-%s?" % (val1, val2)
    wrongAnsHint = "Add single value to both terms to get nice number: a-b = (a+k) - (b+k)"
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceSub2NumsOnesIn2ndNumAreGreaterPos(minVal, maxVal):
    tens1 = getRandomIntDivisibleBy10(minVal+10, maxVal)
    tens2 = getRandomIntDivisibleBy10(minVal, tens1)
    ones1 = np.random.randint(0,9)
    ones2 = np.random.randint(ones1+1,10)
    val1 = tens1+ones1
    val2 = tens2+ones2
    ans = val1-val2
    question = "What is %s-%s?" % (val1, val2)
    wrongAnsHint = "Add single value to both terms to get nice number: a-b = (a+k) - (b+k)"
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceMultiplying2Nums(minVal1, maxVal1, minVal2, maxVal2):
    val1 = np.random.randint(minVal1, maxVal1)
    val2 = np.random.randint(minVal2, maxVal2)
    ans = val1*val2
    question = "What is %s*%s?" % (val1, val2)
    wrongAnsHint = ""
    return makeDictForPractice([val1, val2], ans, question, wrongAnsHint)

def practiceMultiplyingNumBy5(minVal, maxVal):
    problemDict = practiceMultiplying2Nums(minVal, maxVal, 5, 6)
    problemDict["wrong answer hint"] = "Divide by 2, then multiply by 10"
    return problemDict

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
    question = "What are the factorials - smallest to largest - of %s? Input as a list ([x,y,...])." % val
    wrongAnsHint = ""
    return makeDictForPractice([val], ans, question, wrongAnsHint)


def runTimeAndGiveMetricsOnQuestions(questionsAndFrequency, numQuestionsToAsk):
    if numQuestionsToAsk == 0: return

    npQuestionsAndFrequencies = np.array(questionsAndFrequency)
    questions = list(npQuestionsAndFrequencies[:,0])
    frequencies = list(npQuestionsAndFrequencies[:,1])

    print("\nGRE MATH PRACTICE\n=================\n")

    isCorrectForEachQuestion = []
    timeForEachQuestion = []
    for i in range(0,numQuestionsToAsk):

        startTime =  datetime.datetime.now()

        print("Question %s:" % (i+1) + "\n")
        (question, _) = sampleArray(questions, frequencies)
        isCorrect = askUserForAnswerAndPrintResults(question)

        endTime = datetime.datetime.now()
        timeForEachQuestion.append((endTime-startTime).seconds)
        isCorrectForEachQuestion.append(isCorrect)

    printFeedback(isCorrectForEachQuestion, timeForEachQuestion)

def askUserForAnswerAndPrintResults(problem):
    problemDesc = problem()
    vals = problemDesc["value"]
    ans = problemDesc["answer"]
    question = problemDesc["question"]
    wrongAnsHint = problemDesc["wrong answer hint"]

    isNotValidEntry = True
    while isNotValidEntry:
        userInput = input("\t" + question + "\n\n\t>>> ")
        if set('/*+^').intersection(userInput):
            print("\tAre you trying to cheat?\n\n")
            continue
        try:
            userAns = float(userInput)
            isNotValidEntry = False
        except:
            try:
                userAns = list(eval(userInput))
                isNotValidEntry = False
            except:
                print("\t***Must enter a digit or list\n\n")
                isNotValidEntry = True

    if userAns == ans:
        print("\n\tCorrect!\n")
        return True
    elif wrongAnsHint != "":
        print("\n\tIncorrect! Answer is " + str(ans) + "\n\t***Hint: " + wrongAnsHint + "\n")
    else:
        print("\n\tIncorrect! Answer is " + str(ans) + "\n")
    return False

def printFeedback(isCorrectList, solveTimeList):
    numQuestions = len(isCorrectList)

    correctAnswers = sum(isCorrectList)

    totalTime = sum(solveTimeList)
    avgTime = totalTime/numQuestions
    longestTimeIdx = solveTimeList.index( max(solveTimeList) )

    print("\nSUMMARY\n=======")
    print("\tCorrect:       \t%s / %s " % (correctAnswers, numQuestions))
    print("\tTotal time:   \t%s seconds\t" % (totalTime))
    print("\tAverage time: \t%s seconds\t" % (avgTime))
    print("\tSlowest question was question %s (%s seconds) \t"
          % (longestTimeIdx+1, solveTimeList[longestTimeIdx]))
