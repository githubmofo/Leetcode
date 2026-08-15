class Solution(object):
    def findMissingElements(self, nums):
        mn = min(nums)
        mx = max(nums)

        seen = set(nums)
        ans = []

        for num in range(mn + 1, mx):
            if num not in seen:
                ans.append(num)
        return ans        