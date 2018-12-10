class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        lis=[[1]]
        j=2
        while j<=numRows:
            a=[]
            a.append(1)
            for i in range(1,j-1):
                a.append(lis[j-2][i-1]+lis[j-2][i])
            a.append(1)
            lis.append(a)
            j+=1
        return lis

    """
Runtime: 36 ms, faster than 88.87% of Python3 online submissions for Pascal's Triangle.
    """