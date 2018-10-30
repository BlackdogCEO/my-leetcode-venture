class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x%10==0 and x!=0):
            return False
        reverse=0
        while x>reverse:
            reverse=10*reverse+x%10
            x=x//10
        if x==reverse or x==reverse//10:
            return True
        else:
            return False

"""
Runtime: 284 ms, faster than 71.74% of Python3 online submissions for Palindrome Number.
point:the reverse algorithm ignores zeros in the end of a number
1700 will be reverse as 71, so 12100 will be cut like 1 and 21, which need to preset an if to exclude such
situation
on the other hand, choosing to just reverse half of the number does not lead to obvious less time.


"""
