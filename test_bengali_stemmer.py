import unittest
from bengali_stemmer import *

class TestBengaliStemmer(unittest.TestCase):
    
    def test_isBnCommonSuffix(self):
        self.assertEqual(isBnCommonSuffix('\u09cc'), True)
        self.assertEqual(isBnCommonSuffix('\u0986'), True)
        self.assertEqual(isBnCommonSuffix('\u0995'), False)
    
    def test_stripPluralSuffixes(self):
        self.assertEqual(stripPluralSuffixes('মানুষগুলি'), 'মানুষ')
        self.assertEqual(stripPluralSuffixes('মানুষগুলো'), 'মানুষ')
        self.assertEqual(stripPluralSuffixes('মানুষ'), 'মানুষ')
        self.assertEqual(stripPluralSuffixes('মানুষগুলোতে'), 'মানুষ')
        self.assertEqual(stripPluralSuffixes('মানুষগুলিতে'), 'মানুষ')

if __name__ == '__main__':
    unittest.main()