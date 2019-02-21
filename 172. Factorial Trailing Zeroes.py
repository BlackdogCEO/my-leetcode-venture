class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count


"""
Runtime: 24 ms, faster than 98.87% of Python online submissions for Factorial Trailing Zeroes.
the reason we only need to care 5, 5*5, 5*5*5 is that in factorial computation there is always much 2 to make
2*5 to contribute a trailing 0. so we use n/5 to count 5, n/5*5 to count 25....
"""