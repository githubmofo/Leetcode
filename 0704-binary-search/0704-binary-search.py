class Solution(object):
    def search(self, nums, target):
        for i, val in enumerate(nums):
            if val == target:
                return i
        return -1