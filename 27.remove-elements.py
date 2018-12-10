class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        j=0
        for ele in nums:
            if ele!=val:
                nums[j]=ele
                j+=1
        return j

"""
Runtime: 36 ms, faster than 99.59% of Python3 online submissions for Remove Element.
this is nearly the same with question 26, but here we use a iteration and a pointer,
the basic idea is to go through the list, and replace the elements which not equal the
val to head of the list.
we should know that list is rather inefficient, like delete and append will cost n times
read and write, so we avoid frequently using that.


 """