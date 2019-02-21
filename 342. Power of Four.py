class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num ==1:
            return True
        res=num&3
        while num>1 and res==0:
            res = num&3
            num = num>>2
        if res==0:
            return True
        else:
            return False


"""
Runtime: 24 ms, faster than 100.00% of Python online submissions for Power of Four.
Memory Usage: 10.8 MB, less than 43.59% of Python online submissions for Power of Four.

"""
