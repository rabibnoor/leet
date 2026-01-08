# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        if root.left == None and root.right == None:
            return root
        left = None
        right = None

        if root.left:
            left = self.invertTree(root.left)
        
        if root.right:
            right = self.invertTree(root.right)
        
        newroot = TreeNode(val=root.val, left=right, right=left)

        return newroot
