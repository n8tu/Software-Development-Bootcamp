import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        if(nums):
            for i in nums:
                self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        if(nums):
            for i in nums:
                self.result -= i
        return self

class addTest(unittest.TestCase):
    
    def testOne(self):
        self.assertEqual(MathDojo().add(1,2,3,4,5,6,7).result,28)

    def testTwo(self):
        self.assertEqual(MathDojo().add(1,2,3,4).result,10)

    def setUp(self):
        print("Running add Test")

    def tearDown(self):
        print("Test over")

class substractTest(unittest.TestCase):
    
    def testOne(self):
        self.assertEqual(MathDojo().subtract(12).result,-12)

    def testTwo(self):
        self.assertEqual(MathDojo().subtract(1,2,3,4).result,-10)

    def setUp(self):
        print("Running Substract Test")

    def tearDown(self):
        print("Test over")



if __name__ == '__main__':
    unittest.main()
