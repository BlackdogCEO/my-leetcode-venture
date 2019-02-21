class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[1]
        for i in range(rowIndex):
            ans=list(map(lambda x,y:x+y,[0]+ans,ans+[0]))
        return ans

    """
Runtime: 52 ms, faster than 19.05% of Python3 online submissions for Pascal's Triangle II.
the pattern of pascal's triangle is the then next line can be built as [0+last line]+[last line +0]
here use map to do this ,the follow codes shows maybe using zip and list generator is faster
    """

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans=[1]
        for i in range(rowIndex):
            ans=[x+y for x,y in zip([0]+ans,ans+[0])]
        return ans

"""
Runtime: 40 ms, faster than 49.76% of Python3 online submissions for Pascal's Triangle II.
zip is also a iterator, list(zip([1,2],[3,4])) will be [(1,3),(2,4)]
"""