class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        num = ""

        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        if num == "":
            return 0

        num = sign * int(num)

        if num < -2147483648:
            return -2147483648
        if num > 2147483647:
            return 2147483647

        return num