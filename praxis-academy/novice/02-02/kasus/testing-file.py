import unittest

#from my_test import addAll

class Test(unittest.TestCase):

    def add(self):
        data = [3, 5]
        result = sum(data)
        self.assertEqual(result, 999, "should be 999")

if __name__ == '__main__':
    unittest.main()