class Solution(object):
    def longestSubsequence(self, nums):
        n = len(nums)
        total_xor = 0

        for num in nums:
            total_xor ^= num

        if total_xor != 0:
            return n

        for num in nums:
            if num != 0:
                return n - 1

        return 0