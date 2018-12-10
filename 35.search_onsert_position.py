class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        head=0
        tail=len(nums)
        while head!=tail:
            i=(head+tail)//2
            if nums[i]==target:
                return i
            elif nums[i]<target:
                head=i+1
            else:
                tail=i
        return head

"""
48 ms, faster than 27.14% of Python3 online submissions for Search Insert Position.
i use binary search to accomplish this task, because the test case is short so its
advantage doesn't show up, but its time complexity is O(log2n), and search one by one
cost n times search.
note:we should pay extremely attention to the index of list, whether plus one, minus 1,
whether it's out of the range of a list blabla....
"""