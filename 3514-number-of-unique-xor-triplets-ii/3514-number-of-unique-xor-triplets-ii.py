class Solution(object):
    def uniqueXorTriplets(self, nums):
        nums = list(set(nums))

        m = 2048

        pair = [False] * m

        for x in nums:
            for y in nums:
                pair[x ^ y] = True

        ans = [False] * m

        for i in range(m):
            if pair[i]:
                for x in nums:
                    ans[i ^ x] = True

        return sum(ans)