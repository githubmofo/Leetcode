class Solution(object):
    def moveZeroes(self, nums):
        non_zero = [x for x in nums if x != 0]
        zeros = [0] * (len(nums) - len(non_zero))

        nums[:] = non_zero + zeros