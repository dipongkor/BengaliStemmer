import unittest
from bn_rule_based_stemmer import *

class TestBengaliStemmer(unittest.TestCase):
    
    def test_first_rule_of_verb(self):
        stemmer = BengaliStemmer()
        root = stemmer.applyFirstRuleOfVerb("চলেন")
        self.assertEqual(root, "চলে")
    
    def test_second_rule_of_verb(self):
        stemmer = BengaliStemmer()
        root = stemmer.applySecondRuleOfVerb("চলে")
        self.assertEqual(root, "চল")
        root = stemmer.applySecondRuleOfVerb("গাইতা")
        self.assertEqual(root, "গাই")
    
    def test_third_rule_of_verb(self):
        stemmer = BengaliStemmer()
        root = stemmer.applyThirdRuleOfVerb("করেছি")
        self.assertEqual(root, "করে")
    
    def test_verb(self):
        stemmer = BengaliStemmer()
        afterFirstRule = stemmer.applyFirstRuleOfVerb("করেছিলাম")
        afterSecondRule = stemmer.applySecondRuleOfVerb(afterFirstRule)
        afterThirdRule = stemmer.applyThirdRuleOfVerb(afterSecondRule)
        afterFourthRule = stemmer.applyFourthRuleOfVerb(afterThirdRule)
        self.assertEqual(afterFourthRule, "কর")
        root = stemmer.findStemOfVerb("করছে")
        self.assertEqual(root, "কর")
    
    def test_verb_chord(self):
        stemmer = BengaliStemmer()
        root = stemmer.findStemOfVerb("গাইতে")
        self.assertEqual(root, "গাওয়া")
        root = stemmer.findStemOfVerb("পেয়েছেন")
        self.assertEqual(root, "পাওয়া")
        root = stemmer.findStemOfVerb("দিয়েছিলাম")
        self.assertEqual(root, "দেওয়া")
        root = stemmer.findStemOfVerb("নিয়েছিলাম")
        self.assertEqual(root, "নেওয়া")
        
    def test_first_rule_of_noun(self):
        stemmer = BengaliStemmer()
        root = stemmer.applyFirstRuleOfNoun("বাসাতে")
        self.assertEqual(root, "বাসা")
    
    def test_noun_stem(self):
        stemmer = BengaliStemmer()
        root = stemmer.findStemOfNoun("মানুষগুলোতে")
        self.assertEqual(root, "মানুষ")
    
    def test_stem(self):
        stemmer = BengaliStemmer()
        root = stemmer.findStem("মানুষগুলোতে")
        self.assertEqual(root, "মানুষ")
        root = stemmer.findStem("নিয়েছিলাম")
        self.assertEqual(root, "নেওয়া")
        root = stemmer.findStem("বিবদমান")
        self.assertEqual(root, "বিবদমান")
    
    def test_ex(self):
        stemmer = BengaliStemmer()
        #root = stemmer.findStemOfVerb("রয়েছেন")
        root = stemmer.findStem("পাপিয়ার")
        self.assertEqual(root, "পাপিয়া")   
        root = stemmer.findStemOfNoun("পাপিয়া")
        self.assertEqual(root, "পাপিয়া")
        root = stemmer.findStemOfNoun("ছাত্রলীগের")
        self.assertEqual(root, "ছাত্রলীগ") 
if __name__ == '__main__':
    unittest.main()