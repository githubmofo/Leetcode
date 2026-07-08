class Solution(object):
    def convertToTitle(self, columnNumber):
        letters = ''
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber-1, 26)
            letters = chr(65 + remainder) + letters
        return letters    
       