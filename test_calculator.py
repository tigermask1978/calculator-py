from calculator import multi
import unittest



class TestStringMethods(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(multi(2, 3),  6)

    

if __name__ == '__main__':
    unittest.main()