class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s={}
        dic_t={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dic_s:
                dic_s[s[i]]+=1
            else:
                dic_s[s[i]]=1
            if t[i] in dic_t:
                dic_t[t[i]]+=1
            else:
                dic_t[t[i]]=1
        return dic_s==dic_t
"""
Runtime: 84 ms, faster than 12.83% of Python online submissions for Valid Anagram.
this is my original version using 2 dictionary, other people use like sort, or predetermined dict(26 for 26 char)
or 1 dictionary so char showed in s increase its value and char in t decrease its value ,then use all to determine
whether it's all zero.
note that sort in fact is O(n*logn),but because the test case is small, the difference is not that big
"""
