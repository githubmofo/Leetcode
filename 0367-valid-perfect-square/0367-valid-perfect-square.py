class Solution(object):
    def isPerfectSquare(self, num):
        if num == 0:
            return True

        y = int(num ** 0.5)

        if y * y == num:
            return True
        else:
            return False