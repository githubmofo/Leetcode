class Solution(object):
    def camelMatch(self, queries, pattern):
        ans = []
        for s in queries:
            i = 0
            valid = True

            for ch in s:
                if i < len(pattern) and ch == pattern[i]:
                    i +=1
                elif ch.isupper():
                    valid = False
                    break
            ans.append(valid and i == len(pattern))

        return ans