class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in str(int("".join(list(map(lambda x:str(x), digits))))+1):
            a.append(int(i))
        return a




"""
Runtime: 56 ms, faster than 18.42% of Python3 online submissions for Plus One.
this solution transform list(int) to list(str), then to a single str, then to single int, then plus 1, then to
str ,then to list(int)
"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]+=1
        i=1
        while digits[-i]==10:
            digits[-i]=0
            i+=1
            try:
                digits[-i]+=1
            except IndexError:
                digits.insert(0,1)
        return digits

"""
Runtime: 40 ms, faster than 71.34% of Python3 online submissions for Plus One.
this is a very straight solution, one by one ,just check if it's 10, then we need to send the carry to the
next number, and if the first number gets to 10, change it to 0 and add number 1 at the head  of list.

"""