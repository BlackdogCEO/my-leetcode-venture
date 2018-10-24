class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = None
        a = len(nums)
        b = {}
        for i in range(a):
            b[nums[i]] = i

        for i in range(a):
            if target - nums[i] in b.keys():
                c = b[target - nums[i]]
                if c != i:
                    answer = [c, i]
                    if c > i:
                        answer = [i, c]
        return answer

    """
    Runtime: 40ms, faster than 81.75 % of Python3 online submissions for Two Sum.
    """
    """"

    note:
    the initial question is that i used double loop, so time complexity is O(n^2). Then i use the dict in
    python, which in fact is a hash-map, the search for the second number is transformed to be the search with key
    in a dictionary, its time complexity is in fact O(constant), so the total time complexity is O(n),with the cost of
    space complexity.
    """