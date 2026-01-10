# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, float("-inf")
                
            leftp, lefts = dfs(root.left)
            
            rightp, rights = dfs(root.right)

            maxs = max(leftp + rightp + root.val, root.val, leftp + root.val, rightp+root.val, lefts, rights)

            path_up = max(root.val, root.val + leftp, root.val + rightp)
          
            return path_up, maxs
        _, maxs = dfs(root)

        return maxs
