import unittest
class DivTest(unittest.TestCase):

    def test_div_001(self):
        self.assertEqual(1, 1)

    def test_div_002(self):
        self.assertEqual(2, 2)

    def test_div_003(self):
        self.assertEqual(3, 3)
        
    def test_div_004(self):
        self.assertEqual(4, 4)
        
    def test_div_005(self):
        self.assertEqual(5, 3)
		
if __name__=='__main__':
	unittest.main()
