class Solution:
    def subarraySum(self, arr, k):
        n = len(arr)
        prefixSumCount = {}

        prefixSum = 0
        count = 0
        prefixSumCount[0] = 1

        for i in range(n):
            prefixSum += arr[i]
            remove = prefixSum - k

            if remove in prefixSumCount:
                count += prefixSumCount[remove]

            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1

        return count



