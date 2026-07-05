class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for i in range(len(numbers)):
            need = target - numbers[i]

            if need in seen:
                return [seen[need] + 1,i+1]
            seen[numbers[i]] = i
        return []             
        