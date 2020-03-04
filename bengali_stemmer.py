bn_suffixes = {
"bn_aa" : '\u0986',
"bn_i" : '\u0987',
"bn_o" : '\u0993',
"bn_au" : '\u0994',
"bn_k" : '\u0995',
"bn_g" : '\u0997',
"bn_tt" : '\u099f',
"bn_t" : '\u09a4',
"bn_d" : '\u09a6',
"bn_b" : '\u09ac',
"bn_bh" : '\u09ad',
"bn_m" : '\u09ae',
"bn_y" : '\u09df',
"bn_r" : '\u09b0',
"bn_l" : '\u09b2',
"bn_sh" : '\u09b6',
"bn_AA" : '\u09be',
"bn_I" : '\u09bf',
"bn_II": '\u09c0',
"bn_U" :'\u09c1',
"bn_UU" : '\u09c2',
"bn_E" : '\u09c7',
"bn_O" : '\u09cb',
"bn_AU" : '\u09cc'
}
swaraBarnas = ["bn_AA", "bn_E", "bn_I", "bn_II", "bn_U", "bn_UU"]

def isBnCommonSuffix(char):
    if char >= bn_suffixes["bn_AA"] and char <= bn_suffixes["bn_AU"]:
        return True            
    if char >= bn_suffixes["bn_aa"] and char <= bn_suffixes["bn_au"]:
        return True
    return True if char == bn_suffixes["bn_y"] else False

def stripPluralSuffixes(word):
    word_length = len(word)
    if word_length <= 6:
        return word
    if word[word_length - 1] == bn_suffixes["bn_E"] and \
        word[word_length - 2] == bn_suffixes["bn_t"]:
        word = word[0:word_length-2]
        word_length = len(word)
        if word_length <= 6:
            return word
    if word[word_length - 4] == bn_suffixes["bn_g"] and \
        word[word_length - 3] == bn_suffixes["bn_U"] and \
        word[word_length - 2] == bn_suffixes["bn_l"] and \
        word[word_length - 1] == bn_suffixes["bn_O"] or \
        word[word_length - 1] == bn_suffixes["bn_I"]:
        word = word[0: word_length - 4]
    return word
        
    
    
   