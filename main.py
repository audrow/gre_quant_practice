import quizzer as qz
import utils

import argparse


def main(numQuestions):

    # Questions
    add2DigitNums                    = lambda: qz.practiceAdding2Nums(11, 100, 11, 100)
    subtract2DigitNums               = lambda: qz.practiceSubtracting2Nums(11, 100, 11, 100)
    sub2DigNums2ndOnesAreGreater     = lambda: qz.practiceSub2NumsOnesIn2ndNumAreGreater(11, 100, 11, 100)
    sub2DigNums2ndOnesAreGreaterPos  = lambda: qz.practiceSub2NumsOnesIn2ndNumAreGreaterPos(11, 100)
    multiplyNumsLessThan21           = lambda: qz.practiceMultiplying2Nums(3, 21, 3, 21)
    multiplyNumsLessThan50By5        = lambda: qz.practiceMultiplyingNumBy5(10, 51)
    combinationsLessThan10           = lambda: qz.practiceCombinations(10)

    factorialsLessThan200            = lambda: qz.practiceFactorials(10, 201)

    squareIntsBetween13And20         = lambda: qz.practiceSquareInts(13, 21)
    square10sLessThan200             = lambda: qz.practiceSquare10s(20, 201)
    squareEndsIn5LessThan200         = lambda: qz.practiceSquareEndsIn5(20, 201)
    squareSumOfSquaresLessThan100    = lambda: qz.practiceSquareAdjacentToKnown(20, 101)


    questionsAndFrequencies = [
       #[ function,        relative frequency ]
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


def checkIsPositiveIntArg(val, lessThan=None):

    if not utils.isPositivInt(val, lessThan=lessThan):
        raise argparse.ArgumentTypeError('Value must be a positive integer')
    else:
        return int(val)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Setup your quiz')
    parser.add_argument('--num_questions', '-n',
                        default=5, type=checkIsPositiveIntArg,
                        help='The number of questions the quizzer will ask you')
    args = parser.parse_args()

    main(args.num_questions)


