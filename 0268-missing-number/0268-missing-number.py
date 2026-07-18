class Solution(object):
    def missingNumber(self, nums):
        xor = len(nums)

        for i in range(len(nums)):
            xor ^= i
            xor ^= nums[i]

        return xor