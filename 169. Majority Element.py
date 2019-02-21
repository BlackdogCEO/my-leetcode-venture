class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        count = 0

        for i in range(len(nums)):
            if 0 == count:
                res = nums[i]
                count += 1
            else:
                if res == nums[i]:
                    count += 1
                else:
                    count -= 1
        return res

"""
Runtime: 32 ms, faster than 86.27% of Python online submissions for Majority Element.
sorry i can't figure this out by myself, after 10 minutes thought, i turned to other's idea
this solution use a counter, it increase 1 when the examined number equals target, decrease 1
when not, and if it changes to 0,this means the showed up target times equal to when it's not,so the next
number will be target.
because the real answer will show up more than n/2 times, it will always be the only one that makes count positive.
"""
