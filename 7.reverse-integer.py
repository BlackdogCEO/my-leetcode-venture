class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        b = 0
        a = 0
        c = 1
        if x < 0:
            x = -x
            c = -1
        while x != 0:
            if (2147483647 - a) / 10 < b:
                a = b = 0
                break
            b = b * 10 + a
            a = x % 10
            x = x // 10
        if (2147483647 - a) / 10 < b:
            a = b = 0
        b = b * 10 + a
        return c * b


"""
Runtime: 56 ms, faster than 83.34% of Python3 online submissions for Reverse Integer.
the point is to examine overflow of multiple and sum
i use mod and round to get each number
"""
