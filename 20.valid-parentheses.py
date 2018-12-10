class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b = {"(": ")", "{": "}", "[": "]"}
        a = []
        for i in s:
            if i in b.keys():  # if it's a left parentheses,push it into stack
                a.append(i)
            elif not a:  # if it's a right parentheses and a is empty, return wrong
                return False
            elif b[a[-1]] == i:
                del a[-1]
                """if it's a right parentheses and a is not empty and it
                 match the last pushed left parentheses,pop the last parentheses,
                """
            else:
                return False  # now that they don't match each other, so return false

        return not a


"""
Runtime: 36 ms, faster than 98.91% of Python3 online submissions for Valid Parentheses.
something need to care about:
when judging whether a list is empty, simply use if list or if not list is enough, and it's quicker than
compare this list with [] or use len(list).
"""
