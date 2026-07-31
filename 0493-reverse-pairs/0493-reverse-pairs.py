class Solution(object):
    def reversePairs(self, nums):

        def mergeSort(low, high):
            if low >= high:
                return 0

            mid = (low + high) // 2

            cnt = mergeSort(low, mid)
            cnt += mergeSort(mid + 1, high)

            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - (mid + 1)

            temp = []
            left = low
            right = mid + 1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1

            while left <= mid:
                temp.append(nums[left])
                left += 1

            while right <= high:
                temp.append(nums[right])
                right += 1

            nums[low:high + 1] = temp

            return cnt

        return mergeSort(0, len(nums) - 1)