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
            not in [BengaliLetter.bn_i, BengaliLetter.bn_y + BengaliLetter.bn_E, BengaliLetter.bn_o]:
                if word[-1] in [BengaliLetter.bn_AA, BengaliLetter.bn_E, BengaliLetter.bn_I]:
                    word = word[0:-1]
                    return word
        elif word[-1] == BengaliLetter.bn_i or word[-1] == BengaliLetter.bn_o:
            word = word[0:-1]
            is_chord_needed = True
        elif word[-2:] == BengaliLetter.bn_y + BengaliLetter.bn_E:
            word = word[:-2]
            is_chord_need = True
        
        #if is_chord_need:
           
        return word