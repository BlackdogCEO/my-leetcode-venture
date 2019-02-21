# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
"""
Runtime: 28 ms, faster than 98.01% of Python online submissions for Delete Node in a Linked List.
this one is quiet easy, just copy the node.next val to this node and delete node.next in the list node.
don't focus ont deleting the node under consideration because you don't know the one linked to it
"""
