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
        if not root:
            return None
        
        v = root.val
        pv = p.val
        qv = q.val
        if pv < v and qv < v:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if pv > v and qv > v:
            return self.lowestCommonAncestor(root.right, p, q)

        return root  