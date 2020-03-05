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

if __name__ == '__main__':
    unittest.main()