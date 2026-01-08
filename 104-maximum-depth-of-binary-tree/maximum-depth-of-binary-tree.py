# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        left = 0
        right = 0
        if not root:
            return 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        if left > right:
            return left + 1
        return right + 1
        