class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        i = 1
        res = 0
        while i <= len(s):
            res = res + 26 ** j * (ord(s[-i]) - 64)
            j += 1
            i += 1
        return res


"""
Runtime: 28 ms, faster than 78.42% of Python online submissions for Excel Sheet Column Number.
still the runtime is quiet unstable
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, [ord(i) - 64 for i in s])
"""
this is other's version with only one line code, using reduce function
notice in python 3 reduce is no longer a global function, it is now in functools module
"""