class Solution(object):
    def detectCapitalUse(self, word):
        if word.islower():
            return True
        elif word.isupper():
            return True
        elif len(word)> 0 and word[0].isupper() and word[1:].islower():
            return True
        else:
            return False        
