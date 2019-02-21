# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val==val:
                head=head.next
            else:
                break
        if not head:
            return None   
        now=head
        while now.next:
            if now.next.val==val:
                now.next=now.next.next
            else:
                now=now.next
        return head

    """
Runtime: 68 ms, faster than 59.39% of Python online submissions for Remove Linked List Elements.
    """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        else:
            head.next = Solution.removeElements(self, head.next, val)
            if head.val == val:
                return head.next
            else:
                return head
"""
this is other's recursive solution but because python doesn't optimize it, so it runs quirt slow.
"""
