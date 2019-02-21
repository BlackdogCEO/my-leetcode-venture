# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        stack=[[root,str(root.val)]]
        res=[]
        while stack:
            node,ls=stack.pop()
            if node.right:
                stack.append([node.right,ls+"->"+str(node.right.val)])
            if node.left:
                stack.append([node.left,ls+"->"+str(node.left.val)])
            if not node.right and not node.left:
                res.append(ls)
        return res
"""
Runtime: 28 ms, faster than 44.62% of Python online submissions for Binary Tree Paths.
dfs search,just use list of list to contain the path. if using bfs,just change pop() to pop(0)
the following i use recursive way to solve it, the idea is that if we got the list of path of node.left and
node.right, we only need to add node to each of the head of this path and combine this two
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        def path(node):
            left,right=[],[]
            if node.left:
                left=path(node.left)
                for i in range(len(left)):
                    left[i]=str(node.val)+"->"+left[i]
            if node.right:
                right=path(node.right)
                for i in range(len(right)):
                    right[i]=str(node.val)+"->"+right[i]
            if not node.left and not node.right:
                return [str(node.val)]
            return left+right
        return path(root)

"""
Runtime: 24 ms, faster than 100.00% of Python online submissions for Binary Tree Paths.
"""