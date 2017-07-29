import unittest
import main

class testThings(unittest.TestCase):

    def testFindFactorials(self):
        self.assertEqual(main.findFactorials(2), [2]) # simple repeated
        self.assertEqual(main.findFactorials(4), [2, 2]) # simple repeated
        self.assertEqual(main.findFactorials(6), [2, 3]) # two different factorials

        # exceptions 
        with self.assertRaises(ValueError): # check 0
            main.findFactorials(0)
        with self.assertRaises(ValueError): # check 1
            main.findFactorials(1) 
        with self.assertRaises(ValueError): # check negative
            main.findFactorials(-5) 

    def testFindDivisorNearBounds(self):
        self.assertEqual(main.findFirstValueWithDivisorAboveValue(0, 10), 0) # inclusive
        self.assertEqual(main.findFirstValueWithDivisorAboveValue(1, 10), 10) # goes up
        self.assertEqual(main.findFirstValueWithDivisorAboveValue(-19, 10), -10) # with negative

        self.assertEqual(main.findFirstValueWithDivisorBelowValue(0, 10), 0) # inclusive
        self.assertEqual(main.findFirstValueWithDivisorBelowValue(1, 10), 0) # goes down
        self.assertEqual(main.findFirstValueWithDivisorBelowValue(-9, 10), -10) # with negative

        # exceptions
        # check 0 exception
        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorAboveValue(1, 0)
        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorBelowValue(1, 0)

        # # check not decimal
        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorAboveValue(.5, 2)
        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorAboveValue(1, 2.5)

        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorBelowValue(.5, 2)
        with self.assertRaises(ValueError):
            main.findFirstValueWithDivisorBelowValue(1, 2.5)

    def testGetRandomIntDivisibleByNum(self):
        minVal = 0
        maxVal  = 10 
        divisor = 2

        for i in range(0,100):
            val = main.getRandomIntDivisibleByNum(minVal,maxVal,divisor)
            self.assertGreaterEqual(val, minVal) # inclusive of minVal
            self.assertLess(val, maxVal) # not inclusive of maxVal
            self.assertTrue(isinstance(val,int))

        # exceptions
        with self.assertRaises(ValueError): # if minVal > maxVal
            main.getRandomIntDivisibleByNum(1,0,2)
        with self.assertRaises(ValueError): # if minVal = maxVal
            main.getRandomIntDivisibleByNum(1,1,2)

    # Note uses function that uses the above function, so redundant tests
    # are left outomited
    def testGetRandomIntDivisibleBySpecificNum(self):
        minVal = 0
        maxVal  = 10 

        for i in range(0,100):
            valDiv5 = main.getRandomIntDivisibleBy5(minVal,maxVal)
            valDiv10 = main.getRandomIntDivisibleBy10(minVal,maxVal)
            valDiv10EndIn5 = main.getRandomIntEndsIn5(minVal,maxVal)

            self.assertTrue(valDiv5 % 5 == 0)
            self.assertTrue(valDiv10 % 10 == 0)
            self.assertTrue( (valDiv10EndIn5-5) % 10 == 0)

    def testSampleArrayProbabilities(self):
        vals = [1, 2, 3] 

        # check integer frequencies
        freq = [3, 2, 1] 
        allSelectedIdxs = []
        for _ in range(100):
            (val, idxSelected) = main.sampleArray(vals, freq)
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
            (val, idxSelected) = main.sampleArray(vals, freq)
            self.assertGreaterEqual(idxSelected,0)
            self.assertLess(idxSelected, len(freq))

        # exceptions
        with self.assertRaises(ValueError): # check equal lengths
            main.sampleArray([1],[1,4])
        with self.assertRaises(ValueError): # check negative frequencies
            main.sampleArray([1,2],[-1,4])
        with self.assertRaises(ValueError): # check all zero frequencies
            main.sampleArray([1,2],[0,0])

if __name__ == '__main__':
    unittest.main()
