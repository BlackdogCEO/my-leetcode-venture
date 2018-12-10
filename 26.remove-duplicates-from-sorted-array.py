class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenth = nums.__len__()
        if lenth == 0:
            return 0
        i = 0
        while i != lenth - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
                lenth -= 1
            else:
                i += 1
        return lenth


"""
Runtime: 80 ms, faster than 46.28% of Python3 online submissions for Remove Duplicates from Sorted Array.
the answer suggested use two pointers, its idea is that we change the list so the first len(nums) is the
required list, i just del the duplicated numbers in this list.

Note!! del ops cost n times read/write for every operation, the next question(27) we will use 2 pointers to 
solve this question. furthermore, the we only need to replace the right element in the list the the head of the
the list. then change the len of the list(if required).
in fact ,pop operation for a list simply change the list.length in its class attribution
"""
