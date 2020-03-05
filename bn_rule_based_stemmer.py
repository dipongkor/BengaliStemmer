from bn_letters import BengaliLetter
first_rule_of_verb = [BengaliLetter.bn_i, BengaliLetter.bn_chh, 
                      BengaliLetter.bn_t, BengaliLetter.bn_b,
                      BengaliLetter.bn_l, BengaliLetter.bn_dn,
                      BengaliLetter.bn_k, BengaliLetter.bn_s, 
                      BengaliLetter.bn_m]

second_rule_of_verb = [BengaliLetter.bn_l + BengaliLetter.bn_AA,
                       BengaliLetter.bn_t + BengaliLetter.bn_AA,
                       BengaliLetter.bn_chh + BengaliLetter.bn_I,
                       BengaliLetter.bn_b + BengaliLetter.bn_E,
                       BengaliLetter.bn_t + BengaliLetter.bn_E,
                       BengaliLetter.bn_chh + BengaliLetter.bn_E,
                       BengaliLetter.bn_l + BengaliLetter.bn_E]
diacritic_marks = [BengaliLetter.bn_AA, BengaliLetter.bn_I,
                   BengaliLetter.bn_II, BengaliLetter.bn_E,
                   BengaliLetter.bn_O, BengaliLetter.bn_AI,
                   BengaliLetter.bn_AU, BengaliLetter.bn_U,
                   BengaliLetter.bn_UU]
third_rule_of_verb = [BengaliLetter.bn_chh + BengaliLetter.bn_I,
                      BengaliLetter.bn_chh + BengaliLetter.bn_E]

first_rule_of_noun = [BengaliLetter.bn_t + BengaliLetter.bn_E,
                      BengaliLetter.bn_k + BengaliLetter.bn_E]
second_rule_of_noun = [BengaliLetter.bn_r, BengaliLetter.bn_y, 
                       BengaliLetter.bn_E, BengaliLetter.bn_r + BengaliLetter.bn_AA,
                       BengaliLetter.bn_e + BengaliLetter.bn_r + BengaliLetter.bn_AA]
third_rule_of_noun = [BengaliLetter.bn_d + BengaliLetter.bn_E,
                      BengaliLetter.bn_k + BengaliLetter.bn_E, 
                      BengaliLetter.bn_k + BengaliLetter.bn_AA,
                      BengaliLetter.bn_tt + BengaliLetter.bn_AA,
                      BengaliLetter.bn_tt + BengaliLetter.bn_I]
fourth_rule_of_noun = [BengaliLetter.bn_j + BengaliLetter.bn_dn,
                       BengaliLetter.bn_g + BengaliLetter.bn_U + BengaliLetter.bn_l + BengaliLetter.bn_O,
                       BengaliLetter.bn_g + BengaliLetter.bn_U + BengaliLetter.bn_l + BengaliLetter.bn_I,
                       BengaliLetter.bn_kh + BengaliLetter.bn_AA + BengaliLetter.bn_dn + BengaliLetter.bn_AA 
                       ]
class BengaliStemmer:
    
    def applyFirstRuleOfVerb(self, word):
        if word[-1] in first_rule_of_verb:
            word = word[0:-1]
        return word
    
    def applySecondRuleOfVerb(self, word):
        if len(word) <= 3 and word[-1] in diacritic_marks:
            word = word[0:-1]
            return word
        if word[-2:] in second_rule_of_verb:
            word = word[:-2]
        return word
    
    def applyThirdRuleOfVerb(self, word):
        return word[:-2] if word[-2:] in third_rule_of_verb else word
    
    def applyFourthRuleOfVerb(self, word):
        is_chord_needed = False
        
        if len(word) > 1 and word[-1] \
            not in [BengaliLetter.bn_i, BengaliLetter.bn_o] \
            and word[-2:] != BengaliLetter.bn_y + BengaliLetter.bn_E:
                if word[-1] in [BengaliLetter.bn_AA, BengaliLetter.bn_E, BengaliLetter.bn_I]:
                    word = word[0:-1]
                    return word
        elif word[-1] == BengaliLetter.bn_i or word[-1] == BengaliLetter.bn_o:
            word = word[0:-1]
            is_chord_needed = True
        elif word[-2:] == BengaliLetter.bn_y + BengaliLetter.bn_E:
            word = word[:-2]
            is_chord_needed = True
        
        if is_chord_needed == True: 
            if word[1] == BengaliLetter.bn_E:
                word = word.replace(BengaliLetter.bn_E, BengaliLetter.bn_AA, 1)
            if word[1] == BengaliLetter.bn_I:
                word = word.replace(BengaliLetter.bn_I, BengaliLetter.bn_E, 1)
            if word[1] == BengaliLetter.bn_U:
                word = word.replace(BengaliLetter.bn_U, BengaliLetter.bn_O, 1)
            word = word + BengaliLetter.bn_o + BengaliLetter.bn_y + BengaliLetter.bn_AA
        return word
    
    def findStemOfVerb(self, word):
        afterFirstRule = self.applyFirstRuleOfVerb(word)
        afterSecondRule = self.applySecondRuleOfVerb(afterFirstRule)
        afterThirdRule = self.applyThirdRuleOfVerb(afterSecondRule)
        afterFourthRule = self.applyFourthRuleOfVerb(afterThirdRule)
        return afterFourthRule
    
    def applyFirstRuleOfNoun(self, word):
        for inflection in first_rule_of_noun:
            if word.endswith(inflection):
                word = word.replace(inflection, "")
                break
        return word
    
    def applySecondRuleOfNoun(self, word):
        for inflection in second_rule_of_noun:
            if word.endswith(inflection):
                word = word.replace(inflection, "")
                break
        return word
    
    def applyThirdRuleOfNoun(self, word):
        for inflection in third_rule_of_noun:
            if word.endswith(inflection):
                word = word.replace(inflection, "")
                break
        return word
    
    def applyFourthRuleOfNoun(self, word):
        for inflection in fourth_rule_of_noun:
            if word.endswith(inflection):
                word = word.replace(inflection, "")
                break
        return word
    
    def findStemOfNoun(self, word):
        afterFirstRule = self.applyFirstRuleOfNoun(word)
        afterSecondRule = self.applySecondRuleOfNoun(afterFirstRule)
        afterThirdRule = self.applyThirdRuleOfNoun(afterSecondRule)
        root = self.applyFourthRuleOfNoun(afterThirdRule)
        return root
        
            