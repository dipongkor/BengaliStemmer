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
    
    def test_stripCommonSuffixes(self):
        self.assertEqual(stripCommonSuffixes('মানুষগুলি', False), ('মানুষগুলি', False))
        self.assertEqual(stripCommonSuffixes('মানুষটি', False), ('মানুষ', True))
        self.assertEqual(stripCommonSuffixes('মানুষের', False), ('মানুষ', True))
        self.assertEqual(stripCommonSuffixes('মানুষকে', False), ('মানুষ', True))
        self.assertEqual(stripCommonSuffixes('মানুষদের', False), ('মানুষ', True))
        self.assertEqual(stripCommonSuffixes('মানুষরা', False), ('মানুষরা', False))
        self.assertEqual(stripCommonSuffixes('মরণশীল', False), ('মরণ', True))


    def test_stemWord(self):
        self.assertEqual(stemWord('মানুষগুলি'), 'মানুষ')
        self.assertEqual(stemWord('পাখিরা'), 'পাখি')


if __name__ == '__main__':
    unittest.main()