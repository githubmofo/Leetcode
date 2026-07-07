class Solution(object):
    def isPalindrome(self, s):
        chars = []

        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())

        return chars == chars[::-1]