class Solution(object):
    def plusOne(self, digits):
        result = int("".join(map(str, digits)))
        res = [int(i) for i in str(result+1)]
        return res


        