class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res=""
        while n:
            b=n%26
            n=n//26
            if 0==b:
                res="Z"+res
                n-=1
            else:
                res=chr(64+b)+res
        return res
"""
Runtime: 20 ms, faster than 89.93% of Python online submissions for Excel Sheet Column Title.
this need special judgement for b==0 because this question is in fact 26 format but it does not have zero
in it, in other word, it generate a carry when it's 27 rather than 26,but every 26 numbers. that's because A to Z
is used to express 1 to 26 rather than 0 to 25
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            b = (n - 1) % 26
            n = (n - 1) // 26
            res = chr(65 + b) + res
        return res

"""
this is another way, here using n-1 to make 0 to 25 match A to Z
"""
