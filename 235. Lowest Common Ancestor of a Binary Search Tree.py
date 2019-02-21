# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p=p.val
        q=q.val
        if p>q:
            p,q=q,p
        def getcom(node):
            if not node:
                return None
            if p<=node.val and q>=node.val:
                return node
            elif p>node.val:
                return getcom(node.right)
            elif q<node.val:
                return getcom(node.left)
        return getcom(root)
"""
Runtime: 72 ms, faster than 77.87% of Python online submissions for Lowest Common Ancestor of a Binary Search Tree.
this is the recursive way, but with tail recursive, so it's quiet easy to transform it to iterative version
the basic idea is to search from root , and the lowest common ancestor should be where p and q goes to the different side
of the tree.
"""
