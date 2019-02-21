class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            elif s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True

"""
Runtime: 68 ms, faster than 72.70% of Python3 online submissions for Valid Palindrome.
just 2 pointers to judge, skip characters which is not alphanumeric,and change uppercase to lowercase
"""