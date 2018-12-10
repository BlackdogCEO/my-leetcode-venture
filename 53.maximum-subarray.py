class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lisnow=0
        import sys
        ans=-sys.maxsize
        for i in nums:
            lisnow=max(lisnow+i,i)
            ans=max(ans,lisnow)
        return ans
"""
Runtime: 40 ms, faster than 84.82%of Python3 online submissions for Count and Say.
the intuition here is that the left sum of max sub-array will be negative, lisnow is
used to sum them, so when it's negative, we reset the start of it to the next number
in this array. another thing is that we use ans to always save the more larger sum,
so when iteration is over, we get the largest sum of sub-array.
"""

