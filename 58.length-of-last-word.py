class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 1
        j = 0
        while i <= len(s):
            if s[-i] == " ":
                i += 1
            else:
                break
        while i <= len(s):
            if s[-i] != " ":
                j += 1
                i += 1
            else:
                break
        return j


"""
Runtime: 40 ms, faster than 54.95% of Python3 online submissions for Length of Last Word.
i use 2 continuous count to complete it, the first while iteration to find the first character which is not " "
in the reverse order, the second while iteration to find the first word's length in reverse order.
simply we can also use python's string.split() to split the string and return the last word's length in the split list.
also: learn to use try... except...IndexError to avoid judging len(None)
"""

