class Solution(object):
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        str = s.split()

        if not str:
            return 0
        return len(str[-1])        
        
        