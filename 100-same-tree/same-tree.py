# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(p, q):
            if not p and not q:
                return True
            elif (not p and  q)  or (p and not q):
                return False
            if p.val != q.val:
                return False
            if (p.left and not q.left) or (not p.left and q.left):
                return False
            
            if (p.right and not q.right) or (not p.right and q.right):
                return False
            
            left = dfs(p.left, q.left) 
            right = dfs(p.right, q.right)
            if not (left and right):
                return False
            return True
        return dfs(p,q)
            