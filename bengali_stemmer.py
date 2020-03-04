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

def stripCommonSuffixes(word, i_removed):
    new_len = len(word)
    old_len = len(word)
    while True:
        if old_len <= 4:
            break   
        #Remove 'tta' or 'ta' (only if it is not preceeded with a m or g)
        if word[old_len - 1] == bn_suffixes["bn_AA"] and \
            word[old_len - 2] == bn_suffixes["bn_tt"] or \
            word[old_len - 2] == bn_suffixes["bn_t"] and \
            word[old_len - 3] != bn_suffixes["bn_m"] and \
            word[old_len - 3] != bn_suffixes["bn_g"]:
            word = word[0: old_len - 2]
            old_len = len(word)

            if old_len <= 4:
                break

        #Remove 'ti' or 'tti'
        if word[old_len - 1] == bn_suffixes["bn_I"] and word[old_len - 2] == bn_suffixes["bn_tt"]:
            word = word[0: old_len - 2]
            old_len = len(word)

            if old_len <= 4:
                break
        
        #Remove "ra"  ("rai" has alreday been stemmed to "ra")
        if word[old_len - 1] == bn_suffixes["bn_r"]:
            word = word[0: old_len - 1]
            old_len = len(word)

            if old_len <= 4:
                break

            #Remove "-er"
            if word[old_len - 1] == bn_suffixes["bn_E"]:
                position = 2 if word[old_len - 2] == bn_suffixes["bn_d"] else 1
                word = word[0: old_len - position]
                old_len = len(word)
        
        if old_len <= 5:
            break

        #Remove ttai tai ttar or tar
        if word[old_len - 1] == bn_suffixes["bn_y"] or \
            word[old_len - 1] == bn_suffixes["bn_r"] and \
            word[old_len - 2] == bn_suffixes["bn_AA"] and \
            word[old_len - 3] == bn_suffixes["bn_tt"] or \
            word[old_len - 3] == bn_suffixes["bn_t"]:
            word = word[0: old_len - 3]
            old_len = len(word)
        elif word[old_len - 1] == bn_suffixes["bn_r"] and word[old_len - 2] == bn_suffixes["bn_I"] and \
            word[len - 3] == bn_suffixes["bn_tt"]:
            word = word[0: old_len - 3]
            old_len = len(word)

        if old_len <= 5:
            break

        if word[old_len - 1] == bn_suffixes["bn_E"] and \
            word[old_len - 2] == bn_suffixes["bn_k"]:
            word = word[0: old_len - 2]
            old_len = len(word)
        
        if old_len <= 5:
            break

        #Remove 'shil'
        if word[old_len - 1] == bn_suffixes["bn_l"] and \
            word[old_len - 2] == bn_suffixes["bn_II"] and \
            word[old_len - 3] == bn_suffixes["bn_sh"]:
            word = word[0: old_len - 3]
            old_len = len(word)
        
        if old_len <= 6:
            break

        #Remove 'tuku'
        if word[old_len - 1] == bn_suffixes["bn_U"] and \
            word[old_len - 2] == bn_suffixes["bn_k"] and \
            word[old_len - 3] == bn_suffixes["bn_U"] and \
            word[old_len - 4] == bn_suffixes["bn_tt"]:
            word = word[0: old_len - 4]
            old_len = len(word)
        
        if old_len <= 6:
            break

        #Remove 'debi'
        if word[old_len - 1] == bn_suffixes["bn_II"] and \
            word[old_len - 2] == bn_suffixes["bn_b"] and \
            word[old_len - 3] == bn_suffixes["bn_E"] and \
            word[old_len - 4] == bn_suffixes["bn_d"]:
            word = word[0: old_len - 4]
            old_len = len(word)
        
        if old_len <= 6:
            break

        #Remove 'babu'
        if word[old_len - 1] == bn_suffixes["bn_U"] and \
            word[old_len - 2] == bn_suffixes["bn_b"] and \
            word[old_len - 3] == bn_suffixes["bn_AA"] and \
            word[old_len - 4] == bn_suffixes["bn_b"]:
            word = word[0: old_len - 4]
            old_len = len(word)
        
        if old_len <= 6 or not i_removed:
            break

        #Remove 'bhai'
        if word[old_len - 1] == bn_suffixes["bn_AA"] and \
            word[old_len - 2] == bn_suffixes["bn_bh"]:
            word = word[0: old_len - 2]
            old_len = len(word)
        
        if old_len <= 6:
            break

        #Remove 'bhabe'
        if word[old_len - 1] == bn_suffixes["bn_b"] and \
            word[old_len - 2] == bn_suffixes["bn_E"] and \
            word[old_len - 3] == bn_suffixes["bn_AA"] and \
            word[old_len - 4] == bn_suffixes["bn_bh"]:
            word = word[0: old_len - 4]
            old_len = len(word)
    return word, new_len != old_len

def stemWord(word):
    new_len = len(word)
    old_len = len(word)
    i_removed = False
    is_aggressive = False

    buff = word

    if not is_aggressive and old_len <= 3:
        return buff
    
    if buff[old_len -1] == bn_suffixes["bn_i"] or \
        buff[old_len -1] == bn_suffixes["bn_o"]:
        buff = buff[0: old_len -1]
        old_len = old_len -1
    
    buff, changed_length = stripCommonSuffixes(buff, i_removed)

    while changed_length:
        buff, changed_length = stripCommonSuffixes(buff, i_removed)
        i_removed = False
    
    buff = stripPluralSuffixes(buff)

    if is_aggressive:
        current_length = len(buff) - 1
        while isBnCommonSuffix(buff[current_length]):
            current_length = current_length - 1
        if current_length - new_len + 1 >= 2:
            buff = buff[0: current_length + 1]
    
    if buff[len(buff) - 1] == bn_suffixes["bn_E"]:
        buff = buff[0: len(buff) - 1]
    
    return buff


