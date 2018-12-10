# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def tree_hb(root):
            if not root:
                return [True, 0]
            else:
                lef = tree_hb(root.left)
                rig = tree_hb(root.right)
                height = max(lef[1], rig[1]) + 1
                if abs(lef[1] - rig[1]) <= 1 and lef[0] and rig[0]:
                    return [True, height]
                else:
                    return [False, height]

        return tree_hb(root)[0]


"""
Runtime: 68 ms, faster than 71.25% of Python3 online submissions for Balanced Binary Tree.
use a label to decide whether the tree(subtree) is balanced and its height
"""

# a revised version because we don't need to save the height of subtree which is not balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def tree_hb(root):
            if not root:
                return 0
            else:
                lef=tree_hb(root.left)
                rig=tree_hb(root.right)
                if lef<0 or rig<0 or abs(lef-rig)>1:
                    return -1
                else:
                    return max(lef,rig)+1
        return tree_hb(root)!=-1

    """
Runtime: 64 ms, faster than 92.25% of Python3 online submissions for Balanced Binary Tree.
here we use a negative number to indicate that tree from this node is not balanced.
    """