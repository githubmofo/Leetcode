class Solution(object):
    def hasAlternatingBits(self, n):
        if n <= 0:
            return False
        bits = bin(n)[2:]

        for i in range(len(bits)-1):
            if bits[i] == bits[i+1]:
                return False
        return True            
        