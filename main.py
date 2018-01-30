import quizzer as qz
import sys

if __name__ == "__main__":

    # Set number of questions, by command line or default
    defaultNumOfQuestionsToAsk = 5
    numQuestions = 0
    if len(sys.argv) == 2:
        userInput = sys.argv[1]
        try:
            numQuestions = int(userInput)
        except:
            print("\nSecond argument must be an integer. Quiting...")
            exit()
    else:
        numQuestions = defaultNumOfQuestionsToAsk

    # Questions
    add2DigitNums = lambda: qz.practiceAdding2Nums(11, 100, 11, 100)
    subtract2DigitNums = lambda: qz.practiceSubtracting2Nums(11, 100, 11, 100)
    sub2DigNums2ndOnesAreGreater = lambda: qz.practiceSub2NumsOnesIn2ndNumAreGreater(11, 100, 11, 100)
    sub2DigNums2ndOnesAreGreaterPos = lambda: qz.practiceSub2NumsOnesIn2ndNumAreGreaterPos(11, 100)
    multiplyNumsLessThan21 = lambda: qz.practiceMultiplying2Nums(3, 21, 3, 21)
    multiplyNumsLessThan21 = lambda: qz.practiceMultiplying2Nums(3, 21, 3, 21)
    multiplyNumsLessThan50By5 = lambda: qz.practiceMultiplyingNumBy5(10, 51)
    combinationsLessThan10 = lambda: qz.practiceCombinations(10)

    factorialsLessThan200 = lambda: qz.practiceFactorials(10, 201)

    squareIntsBetween13And20 = lambda: qz.practiceSquareInts(13, 21)
    square10sLessThan200 = lambda: qz.practiceSquare10s(20, 201)
    squareEndsIn5LessThan200 = lambda: qz.practiceSquareEndsIn5(20, 201)
    squareSumOfSquaresLessThan100 = lambda: qz.practiceSquareAdjacentToKnown(20, 101)

    questionsAndFrequencies = [
            # function,                 frequency ]
            [ add2DigitNums,                    8 ],
            [ subtract2DigitNums,               5 ],
            [ sub2DigNums2ndOnesAreGreater,     5 ],
            [ sub2DigNums2ndOnesAreGreaterPos, 10 ],
            [ multiplyNumsLessThan21,          20 ],
            [ multiplyNumsLessThan50By5,        8 ],
            [ combinationsLessThan10,           3 ],
            [ factorialsLessThan200,           10 ],
            [ squareIntsBetween13And20,        10 ],
            [ square10sLessThan200,             1 ],
            [ squareEndsIn5LessThan200,         5 ],
            [ squareSumOfSquaresLessThan100,    1 ]
          ]

    qz.runTimeAndGiveMetricsOnQuestions(questionsAndFrequencies, numQuestions)

