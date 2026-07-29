class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)

        SN = n * (n + 1) // 2
        S2N = n * (n + 1) * (2 * n + 1) // 6

        S = 0
        S2 = 0

        for num in nums:
            S += num
            S2 += num * num

        val1 = S - SN
        val2 = (S2 - S2N) // val1

        repeating = (val1 + val2) // 2
        missing = val2 - repeating

        return [repeating, missing]