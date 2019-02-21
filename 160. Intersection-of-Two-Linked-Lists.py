# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        A=headA
        B=headB
        i=0
        j=0
        while A.next:
            A=A.next
            i+=1
        while B.next:
            B=B.next
            j+=1
        if A!=B:
            return None
        else:
            if i<j:
                for j in range(j-i):
                    headB=headB.next
            else:
                for i in range(i-j):
                    headA=headA.next
        while True:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next

"""
Runtime: 204 ms, faster than 84.27% of Python online submissions for Intersection of Two Linked Lists.
the basic idea is to go through 2 list and count for there length, if they have the same end, we can get the difference
between the length, so then the longer one goes at first for the different steps, then the 2 keep going to find their
intersection.
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        A=headA
        B=headB
        while(A!=B):
            A= A.next if A else headB
            B= B.next if B else headA
        return A

"""
this is an impressive idea from discussion area, the idea is like 2 different road, if you runs to the end of one, you
go to the start of another, so whichever road you go at first, the time it takes to go through both is the same.
and if 2 roads have intersection, 2 people start from different road will intersect in the second round(or in some special
case the first round)

"""