# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        que = [root]
        depth = 1
        while que:
            for i in range(len(que)):
                node = que.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth += 1

    """
Runtime: 52 ms, faster than 89.67% of Python3 online submissions for Minimum Depth of Binary Tree.
using BFS search, easy
    """