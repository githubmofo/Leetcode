class Solution(object):

    def lowerBound(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low

    def upperBound(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return low

    def searchRange(self, nums, target):
        first = self.lowerBound(nums, target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = self.upperBound(nums, target) - 1

        return [first, last]