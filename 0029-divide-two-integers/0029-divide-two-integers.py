class Solution(object):
    def divide(self, dividend, divisor):

        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            count = 1

            while dividend >= temp + temp:
                temp += temp
                count += count

            dividend -= temp
            quotient += count

        return sign * quotient