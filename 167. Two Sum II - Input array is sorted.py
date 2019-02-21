class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(numbers):
            dic[numbers[i]]=i+1
        for i in range(numbers):
            if target-numbers[i] in dic.keys():
                if dic[target-numbers[i]] > i+1:
                    return [i+1,dic[target-numbers[i]]]
                if dic[target-numbers[i]] < i+1:
                    return [dic[target-numbers[i]],i+1]
"""
Runtime: 24 ms, faster than 79.10% of Python online submissions for Two Sum II - Input array is sorted.
this is too costly here, because it didn't use the information of ascending arrays.
because the array is ascending, we can search from head(h) and tail(t) of array, if the sum is too large,then use
the number before t, else : use number after h, until they meet...

"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return None
        i=0
        j=len(numbers)-1
        while i!=j:
            if numbers[i]+numbers[j] > target:
                j-=1
            elif numbers[i]+numbers[j] < target:
                i+=1
            else:
                return [i+1,j+1]
        return None

"""
Runtime: 24 ms, faster than 79.10% of Python online submissions for Two Sum II - Input array is sorted.
the runtime is nearly the same but this method takes far more less space. it just simply use 2 pointers(index)
"""