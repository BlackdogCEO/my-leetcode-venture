# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 :
            return l2
        if not l2:
            return l1
        if l1.val>l2.val:  # confirm now l1.val<=l2.val,if not, exchange l1 and l2, so the later operation can be done on l1
            inter=l2
            l2=l1
            l1=inter
        head=l1
        while l1 and l2: #do this circle until l2 or l2 is None
            if  not l1.next: #if l1.next is None,than concatenate l2 to l1
                l1.next=l2
                break
            elif l2.val<=l1.next.val: #now that l2 is between l1 and l1.next, we insert this l2 node to l1
                inter=ListNode(l2.val)
                inter.next=l1.next
                l1.next=inter
                l1=l1.next
                l2=l2.next
            else: #now l1 and l1.next is all smaller than l2
                l1=l1.next
        return head

"""
Runtime: 44 ms, faster than 99.21% of Python3 online submissions for Merge Two Sorted Lists.
pay attention:
when giving value like string and numbers,if a=1,b=a,b+=1,then b=2,a still equals 1.
but for list and some thing else,a=[1,2,3],b=a,b.append(4),then a=[1,2,3,4],for the listnode it's the same.
bear in mind that when writing b=a for list,it's just giving the parameter b the same address as a,when we change it
,we in fact change where the pointer points.

one more thing, for such python program, using if a(a can be anything) rather than if a==None is faster.
"""
