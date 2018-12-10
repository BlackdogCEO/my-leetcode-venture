# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack=[[root,root.val]]
        while stack:
            node,val=stack.pop()
            if val==sum and not node.left and not node.right:
                return True
            stack.append([node.left,node.left.val+val]) if node.left else None
            stack.append([node.right,node.right.val+val]) if node.right else None
        return False

    """
Runtime: 52 ms, faster than 98.68% of Python3 online submissions for Path Sum.
    """