import unittest
import numpy as np
import quizzer as qz

class testThings(unittest.TestCase):

    def testFindFactorials(self):
        self.assertEqual(qz.findFactorials(2), [2]) # simple repeated
        self.assertEqual(qz.findFactorials(4), [2, 2]) # simple repeated
        self.assertEqual(qz.findFactorials(6), [2, 3]) # two different factorials

        # exceptions 
        with self.assertRaises(ValueError): # check 0
            qz.findFactorials(0)
        with self.assertRaises(ValueError): # check 1
            qz.findFactorials(1)
        with self.assertRaises(ValueError): # check negative
            qz.findFactorials(-5)

    def testFindDivisorNearBounds(self):
        self.assertEqual(qz.findFirstValueWithDivisorAboveValue(0, 10), 0) # inclusive
        self.assertEqual(qz.findFirstValueWithDivisorAboveValue(1, 10), 10) # goes up
        self.assertEqual(qz.findFirstValueWithDivisorAboveValue(-19, 10), -10) # with negative

        self.assertEqual(qz.findFirstValueWithDivisorBelowValue(0, 10), 0) # inclusive
        self.assertEqual(qz.findFirstValueWithDivisorBelowValue(1, 10), 0) # goes down
        self.assertEqual(qz.findFirstValueWithDivisorBelowValue(-9, 10), -10) # with negative

        # exceptions
        # check 0 exception
        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorAboveValue(1, 0)
        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorBelowValue(1, 0)

        # # check not decimal
        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorAboveValue(.5, 2)
        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorAboveValue(1, 2.5)

        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorBelowValue(.5, 2)
        with self.assertRaises(ValueError):
            qz.findFirstValueWithDivisorBelowValue(1, 2.5)

    def testGetRandomIntDivisibleByNum(self):
        minVal = 0
        maxVal  = 10 
        divisor = 2

        for i in range(0,100):
            val = qz.getRandomIntDivisibleByNum(minVal, maxVal, divisor)
            self.assertGreaterEqual(val, minVal) # inclusive of minVal
            self.assertLess(val, maxVal) # not inclusive of maxVal
            self.assertTrue(isinstance(val, np.integer))

        # exceptions
        with self.assertRaises(ValueError): # if minVal > maxVal
            qz.getRandomIntDivisibleByNum(1,0,2)
        with self.assertRaises(ValueError): # if minVal = maxVal
            qz.getRandomIntDivisibleByNum(1,1,2)

    # Note uses function that uses the above function, so redundant tests
    # are left outomited
    def testGetRandomIntDivisibleBySpecificNum(self):
        minVal = 0
        maxVal  = 10 

        for i in range(0,100):
            valDiv5 = qz.getRandomIntDivisibleBy5(minVal,maxVal)
            valDiv10 = qz.getRandomIntDivisibleBy10(minVal,maxVal)
            valDiv10EndIn5 = qz.getRandomIntEndsIn5(minVal,maxVal)

            self.assertTrue(valDiv5 % 5 == 0)
            self.assertTrue(valDiv10 % 10 == 0)
            self.assertTrue( (valDiv10EndIn5-5) % 10 == 0)

    def testSampleArrayProbabilities(self):
        vals = [1, 2, 3] 

        # check integer frequencies
        freq = [3, 2, 1] 
        allSelectedIdxs = []
        for _ in range(100):
            (val, idxSelected) = qz.sampleArray(vals, freq)
            # check valid index return
            self.assertGreaterEqual(idxSelected,0)
            self.assertLess(idxSelected, len(freq))

            allSelectedIdxs.append(idxSelected)

        # check all indexes are being returned
        allSelectedIdxSet = set(allSelectedIdxs)
        self.assertEqual(len(allSelectedIdxSet),len(freq))

        # check float frequencies
        freq = [.3, .2, .1] 
        for _ in range(100):
            (val, idxSelected) = qz.sampleArray(vals, freq)
            self.assertGreaterEqual(idxSelected,0)
            self.assertLess(idxSelected, len(freq))

        # exceptions
        with self.assertRaises(ValueError): # check equal lengths
            qz.sampleArray([1],[1,4])
        with self.assertRaises(ValueError): # check negative frequencies
            qz.sampleArray([1,2],[-1,4])
        with self.assertRaises(ValueError): # check all zero frequencies
            qz.sampleArray([1,2],[0,0])

if __name__ == '__main__':
    unittest.main()
