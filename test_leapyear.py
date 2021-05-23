import unittest
import leapyear

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(leapyear.is_leapyear(2004),1)

    def test_2(self):
        self.assertEqual(leapyear.is_leapyear("ten"),0)

    def test_3(self):
        self.assertEqual(leapyear.is_leapyear(2003),-1)

if __name__ == '__main__': 
    unittest.main(verbosity=2) 

