import unittest

class TestCase1(unittest.TestCase):
    def testCase1(self):
        print("this is one")
    def testCase2(self):
        print("this is two")


class TestCase2(unittest.TestCase):
    def testCase3(self):
        print("this is three")
    def testCase4(self):
        print("this is four")

if __name__ == '__main__':
   suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
   suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
   suit = unittest.TestSuite([suite1,suite2])
   unittest.TextTestRunner(verbosity=2).run(suit)



