class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low=int(0)
        high=x
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid<=x:
                low=mid+1
            else:
                high=mid-1
        return high

"""
first i use (low+high)//2
Runtime: 64 ms,faster than 67.46% of Python3 online submissions for Sqrt(x).
also binary search
but when i change (high+low)//2 to low+(high-low)//2, suddenly
Runtime: 56 ms, faster than 91.95% of Python3 online submissions for Sqrt(x).
this is because plus result much bigger number and more time for division calculation.
keep it in mind!
"""
