class Solution(object):
    def toLowerCase(self, s):
        if s.isupper():
            return s.lower()
        elif len(s) > 0 and s[0].isupper() and s[1:].islower():
            return s.lower()   
        else:
            return s.lower()
        
        